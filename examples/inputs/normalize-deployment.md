Use the loaded self-contained skill to NORMALIZE the following operational procedure. Return the revised procedure, followed by a brief explanation of material changes or unresolved questions. Do not provide a rule-by-rule audit. Preserve the meaning, requirement strength, conditions, numbers, identifiers, sequence, and exact quoted interface text.

Context: This is an original fictional training scenario, not instructions for an actual production system. The audience is a release operator familiar with Dispatch Gateway. The shift lead authorizes the maintenance window. The release owner handles failures. The shift lead disables normal dispatch before this procedure starts. The quoted interface strings cannot be changed. “Routing rule” and “change record” are established terms in this fictional organization.

Draft:

# Dispatch Gateway configuration update — station H-17

This activity moves station H-17 from configuration DG-4.8.1 to DG-4.8.2 during the approved maintenance window, 22:00–22:20 UTC. The station sends dispatch requests to the warehouse system. Requests already in the queue must be retained. Do not cancel or delete requests to make the queue empty.

Before getting started, you should take a screenshot of the current status page for troubleshooting purposes, and you must obtain the shift lead's approval and confirm that the request queue is empty. The screenshot is recommended, not required. If approval has not been given or the queue isn't empty, stop the procedure and tell the shift lead. Do not continue outside the maintenance window. If the current configuration is anything other than DG-4.8.1, stop and contact the release owner.

The existing settings are to be exported by clicking “Export settings”; attach the resulting file to change record CHG-2041 before applying the update. The file name must be H-17-DG-4.8.1.json. NOTE: The exported file must open successfully and contain exactly 12 routing rules. If either check fails, stop and contact the release owner. You must not apply DG-4.8.2 without this verified export.

After selecting package DG-4.8.2, check that the “Colour mapping” field displays “Standard”, and don't click “Apply & restart” unless both the package version and this field are correct. If either value is incorrect, stop and contact the release owner. Once the button is clicked, a “DON'T CLOSE; WAIT” message is shown while the service restarts. Do not close the browser or switch off the station while this message is displayed. Do not click “Apply & restart” a second time.

The station should show “Ready” within 90 seconds after the first click. This is a required acceptance limit. If “Ready” doesn't appear within that time, stop, keep dispatch disabled, and contact the release owner. Do not restore the previous configuration unless the release owner instructs you to do so.

When “Ready” appears within the limit, verify that the active configuration is DG-4.8.2 and send one test request with identifier TEST-0000. The test must show “Accepted” within 30 seconds after it is sent. Normal dispatch may be enabled only when both the active-configuration check and the test pass. If either check fails, keep dispatch disabled and contact the release owner. Finally, record the active configuration, test result, and completion time in CHG-2041. The screenshot remains optional, but this completion record is mandatory.
