:::writing{variant="document" id="73164"}
# Dispatch Gateway configuration update — station H-17

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
:::

I separated the actions and failure conditions into steps. I moved the export checks from the note into required steps and made the acceptance limits explicit. The quoted interface text remains unchanged. No unresolved questions remain.
