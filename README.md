# ICPAP Exam Browser

A modified version of [Safe Exam Browser](https://github.com/SafeExamBrowser/seb-win-refactoring) 3.10.2 for the ICPAP Online Examination System. It stays under the Mozilla Public License 2.0 (see `LICENSE.txt`); the original copyright notices are unchanged.

Changes from upstream, all on the `icpap` branch:

- **Built-in settings** (`SafeExamBrowser.Configuration/ConfigurationData/DataValues.cs`): starts at the exam system's login page, only allows main-page navigation to the exam system's domain and `meet.jit.si`, quits at `/seb/quit`, and sends the `X-SafeExamBrowser-ConfigKeyHash` header with a fixed Config Key. No `.seb` file is needed; a `.seb` file opened in it is applied on top of these settings.
- **Branding**: ICPAP seal and the name "ICPAP Exam Browser" on icons, splash, About window, English messages and the installer. Regenerate the images with `python3 Branding/make-branding.py` after replacing `Branding/icpap-logo.png`.
- **Build**: `.github/workflows/icpap-build.yml` builds the installers on GitHub Actions. Run it from the Actions tab with the exam address; it reads the Config Key from the `ICPAP_CONFIG_KEY` repository secret. The exam system's Safe Exam Browser settings page needs the same key.

The installer keeps upstream's upgrade code, so installing it replaces an official Safe Exam Browser on the same computer.

---

# Safe Exam Browser, Version 3.x

Refactored version of Safe Exam Browser for Windows with Chromium as integrated browser engine.

## Requirements

> [!NOTE]  
> Starting with version 3.8.0, Safe Exam Browser for Windows requires a minimum operating system version of **Windows 10 version 1803**.

Safe Exam Browser for Windows requires the prerequisites listed below in order to work correctly. These are automatically installed with the setup bundle and need only be manually installed when using the MSI packages.

* .NET Framework 4.8 Runtime: https://dotnet.microsoft.com/download/dotnet-framework/net48
* Visual C++ 2015-2022 Redistributable: https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist

## Project Status

> [!WARNING]
> **The builds linked below are for testing purposes only.** They may be unstable and should thus _never_ be used in a production environment! Always use the latest, official release version of SEB.

| Aspect            | Status                                                                                                                | Details                                                         |
| ----------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| Development Build | ![Development Build Status](https://sebdev.ethz.ch/api/projects/status/kq78qrjtnpk82ti0?svg=true)                     | https://sebdev.ethz.ch/project/appveyor/seb-win-refactoring     |
| Test Build        | ![Test Build Status](https://ci.appveyor.com/api/projects/status/a56akt9r174570m7?svg=true)                           | https://ci.appveyor.com/project/dbuechel/seb-win-refactoring    |
| Test Run          | ![AppVeyor Tests](https://img.shields.io/appveyor/tests/dbuechel/seb-win-refactoring?logo=appveyor&logoColor=%23ccc)  | https://ci.appveyor.com/project/dbuechel/seb-win-refactoring    |
| Code Coverage     | ![Code Coverage](https://codecov.io/gh/SafeExamBrowser/seb-win-refactoring/branch/master/graph/badge.svg)             | https://codecov.io/gh/SafeExamBrowser/seb-win-refactoring       |
| Issue Status      | ![GitHub Issues](https://img.shields.io/github/issues/safeexambrowser/seb-win-refactoring?logo=github)                | https://github.com/SafeExamBrowser/seb-win-refactoring/issues   |
| Downloads         | ![GitHub All Releases](https://img.shields.io/github/downloads/safeexambrowser/seb-win-refactoring/total?logo=github) | https://github.com/SafeExamBrowser/seb-win-refactoring/releases |
| Development       | ![GitHub Last Commit](https://img.shields.io/github/last-commit/safeexambrowser/seb-win-refactoring?logo=github)      | n/a                                                             |
| Repository Size   | ![GitHub Repo Size](https://img.shields.io/github/repo-size/safeexambrowser/seb-win-refactoring?logo=github)          | n/a                                                             |
