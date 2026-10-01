"""Regenerates every ICPAP-branded image from Branding/icpap-logo.png.

Run from the repository root: python3 Branding/make-branding.py
Needs Pillow and the Noto Sans / Noto Serif fonts (fonts-noto on Debian/Ubuntu).
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
GREEN = (12, 115, 71, 255)
DARK = (40, 52, 46, 255)
GREY = (120, 128, 124, 255)
FONTS = Path('/usr/share/fonts/truetype/noto')

seal = Image.open(ROOT / 'Branding/icpap-logo.png').convert('RGBA')
seal = seal.crop(seal.getchannel('A').getbbox())


def fit(height: int) -> Image.Image:
    return seal.resize((round(seal.width * height / seal.height), height), Image.LANCZOS)


def square(size: int) -> Image.Image:
    canvas = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    mark = fit(size)
    canvas.alpha_composite(mark, ((size - mark.width) // 2, 0))
    return canvas


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONTS / name), size)


def save_icon(path: str) -> None:
    square(256).save(ROOT / path, sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])


for icon in [
    'SafeExamBrowser.Client/SafeExamBrowser.ico',
    'SafeExamBrowser.Runtime/SafeExamBrowser.ico',
    'SafeExamBrowser.Service/SafeExamBrowser.ico',
    'SafeExamBrowser.UserInterface.Desktop/Images/SafeExamBrowser.ico',
    'SafeExamBrowser.UserInterface.Mobile/Images/SafeExamBrowser.ico',
    'Setup/Resources/Application.ico',
]:
    save_icon(icon)

# Splash, About and runtime windows. SEB draws its version text over the lower right,
# so the name stays above y=120 and right of x=310.
splash = Image.new('RGBA', (550, 300), (255, 255, 255, 255))
mark = fit(270)
splash.alpha_composite(mark, ((310 - mark.width) // 2, 15))
draw = ImageDraw.Draw(splash)
draw.text((318, 14), 'ICPAP', font=font('NotoSerif-Bold.ttf', 62), fill=GREEN)
draw.text((320, 88), 'Exam Browser', font=font('NotoSans-Regular.ttf', 27), fill=DARK)
for path in ['SafeExamBrowser.UserInterface.Desktop/Images/SplashScreen.png', 'SafeExamBrowser.UserInterface.Mobile/Images/SplashScreen.png']:
    splash.save(ROOT / path)

# Installer: bundle logo, MSI banner (top strip) and dialog (welcome and finish pages).
square(64).save(ROOT / 'SetupBundle/Resources/Logo.png')

banner = Image.new('RGBA', (493, 58), (255, 255, 255, 255))
banner.alpha_composite(fit(50), (493 - fit(50).width - 8, 4))
banner.convert('RGB').save(ROOT / 'Setup/Resources/Banner.bmp')

dialog = Image.new('RGBA', (493, 312), (255, 255, 255, 255))
dialog.alpha_composite(fit(124), ((164 - fit(124).width) // 2, 70))
draw = ImageDraw.Draw(dialog)
for text, y, face, size, colour in [('ICPAP', 205, 'NotoSerif-Bold.ttf', 26, GREEN), ('Exam Browser', 238, 'NotoSans-Regular.ttf', 15, DARK), ('Based on Safe Exam Browser', 262, 'NotoSans-Regular.ttf', 10, GREY)]:
    face = font(face, size)
    width = draw.textlength(text, font=face)
    draw.text(((164 - width) / 2, y), text, font=face, fill=colour)
dialog.convert('RGB').save(ROOT / 'Setup/Resources/Dialog.bmp')

print('Branding images written.')
