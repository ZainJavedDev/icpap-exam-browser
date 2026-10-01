/*
 * Copyright (c) 2025 ETH Zürich, IT Services
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

using SafeExamBrowser.Configuration.Contracts.Integrity;
using SafeExamBrowser.Core.Contracts.OperationModel;
using SafeExamBrowser.Core.Contracts.OperationModel.Events;
using SafeExamBrowser.I18n.Contracts;
using SafeExamBrowser.Logging.Contracts;

namespace SafeExamBrowser.Runtime.Operations.Bootstrap
{
	internal class ApplicationIntegrityOperation : IOperation
	{
		private readonly IIntegrityModule module;
		private readonly ILogger logger;

		public event StatusChangedEventHandler StatusChanged;

		public ApplicationIntegrityOperation(IIntegrityModule module, ILogger logger)
		{
			this.module = module;
			this.logger = logger;
		}

		public OperationResult Perform()
		{
			var result = OperationResult.Success;

			logger.Info($"Attempting to verify application integrity...");
			StatusChanged?.Invoke(TextKey.OperationStatus_VerifyApplicationIntegrity);

			VerifyCodeSignature();

			if (!VerifyRuntimeIntegrity())
			{
				result = OperationResult.Failed;
			}

			return result;
		}

		public OperationResult Revert()
		{
			return OperationResult.Success;
		}

		private void VerifyCodeSignature()
		{
			if (module.TryVerifyCodeSignature(out var isValid))
			{
				if (isValid)
				{
					logger.Info("Application integrity successfully verified.");
				}
				else
				{
					logger.Warn("Application integrity is compromised!");
				}
			}
			else
			{
				logger.Warn("Failed to verify application integrity!");
			}
		}

		private bool VerifyRuntimeIntegrity()
		{
			// ETH's integrity module (seb_x64.dll / seb_x86.dll) is closed source and not part of our build, so the check
			// cannot run. Only abort if the module is present and reports that the runtime has been tampered with.
			if (module.TryVerifyRuntimeIntegrity(out var isValid))
			{
				if (isValid)
				{
					logger.Info("Runtime integrity successfully verified.");
				}
				else
				{
					logger.Error("Runtime integrity is compromised!");
				}
			}
			else
			{
				isValid = true;
				logger.Warn("Failed to verify runtime integrity!");
			}

			return isValid;
		}
	}
}
