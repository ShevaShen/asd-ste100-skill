Use the loaded self-contained skill to VALIDATE ONLY the following draft. Do not rewrite it and do not supply a corrected procedure. Provide a substantive report that distinguishes clear writing-rule findings from meaning questions and vocabulary uncertainty. Cite specific rule IDs where the skill supports them, quote the relevant text, and explain practical consequences. Avoid inventing missing facts or dictionary approvals.

Context: This is an original fictional support process, not a real data-access policy. The audience is a duty analyst. “Tenant ID”, “data steward”, “service log”, and “request record” are established terms in this fictional organization. The quoted interface strings, including “Don't close; export running”, are exact labels and must not be edited. Assess all text below, including the description and notes.

Draft:

# Weekly service-log export

The service log contains operational events. It does not contain message bodies. Each export covers one tenant. The duty analyst owns the export request. The “Approve & Export” control starts the export. Files remain available for 24 hours. During incident INC-317, an export was deleted. The available evidence does not identify who or what deleted it.

1. Don't start until you have reviewed the request record; compare the Tenant ID with the support ticket and obtain approval from the data steward.
2. Select the last seven complete UTC days, excluding the current day, and start the export by selecting “Approve & Export” if the request record shows “Approved”.
3. While the “Don't close; export running” message is being displayed, you should keep the browser open until the download has completed.
4. If the export doesn't finish within 10 minutes, cancel it and notify the data steward, but do not submit a second export until the data steward authorizes it.
5. Save the downloaded file in the restricted case folder, verify that it opens, and send the folder link to the requester; never attach the file to an email.
6. The request record is to be updated by the duty analyst after the file has been checked, and the ticket can then be closed.

NOTE: You must compare the Tenant ID in the downloaded file with the approved request before sharing the folder link. If they do not match, do not share the link and notify the data steward.

NOTE: The download must be completed within 10 minutes. This time includes preparation, export processing, and the download itself.

NOTE: A file can remain available in the portal after it has been downloaded. The portal removes it 24 hours after export creation.

For the handover, the analyst should record the export creation time and any cancellation in the request record. A screenshot is optional. Requesters may receive the restricted folder link only after data-steward approval. Operators must not change the retention period.
