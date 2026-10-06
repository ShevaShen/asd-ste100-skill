# NORMALIZE: configuration deployment with acceptance checks

This original fictional scenario was run through the actual self-contained skill in a fresh responding-agent context. The response was not hand-written as an ideal answer.

## Reviewer assessment

The response retains the optional screenshot, the mandatory completion record, both export checks, and the joint conditions for enabling dispatch. It preserves the 90-second and 30-second limits and the fixed strings, including “Colour mapping” and “DON'T CLOSE; WAIT”. The required export checks move out of a note into the work steps.

Review limitation: the request context says that the shift lead disables dispatch before this procedure starts. The response relies on that context without repeating the prerequisite. Keep that context with the procedure; this is not a verified standalone production runbook. No full dictionary assessment was performed.

## Original request and draft

Use the loaded self-contained skill to NORMALIZE the following operational procedure. Return the revised procedure, followed by a brief explanation of material changes or unresolved questions. Do not provide a rule-by-rule audit. Preserve the meaning, requirement strength, conditions, numbers, identifiers, sequence, and exact quoted interface text.

Context: This is an original fictional training scenario, not instructions for an actual production system. The audience is a release operator familiar with Dispatch Gateway. The shift lead authorizes the maintenance window. The release owner handles failures. The shift lead disables normal dispatch before this procedure starts. The quoted interface strings cannot be changed. “Routing rule” and “change record” are established terms in this fictional organization.

Draft:

### Dispatch Gateway configuration update — station H-17

This activity moves station H-17 from configuration DG-4.8.1 to DG-4.8.2 during the approved maintenance window, 22:00–22:20 UTC. The station sends dispatch requests to the warehouse system. Requests already in the queue must be retained. Do not cancel or delete requests to make the queue empty.

Before getting started, you should take a screenshot of the current status page for troubleshooting purposes, and you must obtain the shift lead's approval and confirm that the request queue is empty. The screenshot is recommended, not required. If approval has not been given or the queue isn't empty, stop the procedure and tell the shift lead. Do not continue outside the maintenance window. If the current configuration is anything other than DG-4.8.1, stop and contact the release owner.

The existing settings are to be exported by clicking “Export settings”; attach the resulting file to change record CHG-2041 before applying the update. The file name must be H-17-DG-4.8.1.json. NOTE: The exported file must open successfully and contain exactly 12 routing rules. If either check fails, stop and contact the release owner. You must not apply DG-4.8.2 without this verified export.

After selecting package DG-4.8.2, check that the “Colour mapping” field displays “Standard”, and don't click “Apply & restart” unless both the package version and this field are correct. If either value is incorrect, stop and contact the release owner. Once the button is clicked, a “DON'T CLOSE; WAIT” message is shown while the service restarts. Do not close the browser or switch off the station while this message is displayed. Do not click “Apply & restart” a second time.

The station should show “Ready” within 90 seconds after the first click. This is a required acceptance limit. If “Ready” doesn't appear within that time, stop, keep dispatch disabled, and contact the release owner. Do not restore the previous configuration unless the release owner instructs you to do so.

When “Ready” appears within the limit, verify that the active configuration is DG-4.8.2 and send one test request with identifier TEST-0000. The test must show “Accepted” within 30 seconds after it is sent. Normal dispatch may be enabled only when both the active-configuration check and the test pass. If either check fails, keep dispatch disabled and contact the release owner. Finally, record the active configuration, test result, and completion time in CHG-2041. The screenshot remains optional, but this completion record is mandatory.

## Actual first response

### Dispatch Gateway configuration update — station H-17

This procedure changes station H-17 from configuration DG-4.8.1 to DG-4.8.2 during the approved maintenance window, 22:00–22:20 UTC.
The station sends dispatch requests to the warehouse system.

Retain all requests already in the queue. Do not cancel or delete requests to make the queue empty.

1. Before you start, consider a screenshot of the current status page to help investigate problems. The screenshot is recommended, but optional.

2. Obtain the shift lead's approval.

3. Confirm that the request queue is empty. If approval is missing or the queue is not empty, stop the procedure. If either condition applies, tell the shift lead.

4. Do not continue outside the maintenance window, 22:00–22:20 UTC.

5. Check the current configuration. If the current configuration is not DG-4.8.1, stop the procedure. If the current configuration is not DG-4.8.1, contact the release owner.

6. Click “Export settings” to export the existing settings. Make sure that the file name is H-17-DG-4.8.1.json. Attach the exported file to change record CHG-2041 before you apply the update.

7. Verify that the exported file opens successfully. Verify that the exported file contains exactly 12 routing rules. If either check fails, stop the procedure. If either check fails, contact the release owner. Do not apply DG-4.8.2 without this verified export.

8. Select package DG-4.8.2. Check that the package version is DG-4.8.2. Check that the “Colour mapping” field displays “Standard”. If either value is incorrect, stop the procedure. If either value is incorrect, contact the release owner.

9. If both values are correct, click “Apply & restart”. Do not click “Apply & restart” a second time.

   The interface shows “DON'T CLOSE; WAIT” while the service restarts.

   While “DON'T CLOSE; WAIT” is visible, do not close the browser. While “DON'T CLOSE; WAIT” is visible, do not switch off the station.

10. Verify that the station shows “Ready” within 90 seconds after the first click on “Apply & restart”. This acceptance limit is mandatory. If “Ready” does not appear within 90 seconds, stop the procedure. If this failure occurs, keep dispatch disabled. If this failure occurs, contact the release owner.

11. Do not restore the previous configuration unless the release owner instructs you to do so.

12. If “Ready” appears within the limit, verify that the active configuration is DG-4.8.2. Then send one test request with identifier TEST-0000.

13. Verify that the test shows “Accepted” within 30 seconds after you send the test request.

14. If the active-configuration check or the test fails, keep dispatch disabled. If either fails, contact the release owner. You may enable normal dispatch only when both the active-configuration check and the test pass.

15. Finally, record the active configuration, test result, and completion time in CHG-2041. This completion record is mandatory. The screenshot remains optional.

I separated the actions and failure conditions into steps. I moved the export checks from the note into required steps and made the acceptance limits explicit. The quoted interface text remains unchanged. No unresolved questions remain.

## Evidence

See [execution metadata and file hashes](manifest.json). Display headings are nested and application writing-block wrappers are omitted here; the response wording is unchanged. Exact responses are retained in [outputs/](outputs/), and original prompts in [inputs/](inputs/). Reviewer assessments were written by the primary assistant after execution, not by a human expert.
