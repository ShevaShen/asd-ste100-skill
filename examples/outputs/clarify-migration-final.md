:::writing{variant="document" id="61743"}
# Move the east event feed to the replacement collector

## Conditions and limits

Do the migration during the approved test window, 13:00–13:15 UTC.

Start only after the change owner approves the start. If approval is missing, do not start.

During the migration, keep live delivery disabled.

Keep queued events. Do not delete queued events during this procedure. Do not manually replay queued events during this procedure.

Do not remove COL-E1 from the asset register as part of this procedure.

At 13:15 UTC, if the migration is incomplete, stop migration actions. Keep live delivery disabled. Contact the change owner. Complete the final record.

Do not start or continue a rollback outside the test window without separate authorization from the change owner.

Complete the final record whenever the procedure ends, including when the procedure stops early.

## Prepare the migration

1. Save a screenshot of the connection page. This step is recommended but optional.
2. Before you change a connection, record the last accepted event sequence in CHG-318.
3. Export the current relay settings.
4. If the export fails, stop the procedure. Contact the change owner. Complete the final record.
5. Attach the exported file to CHG-318.

## Change the connection and relay package

1. Disconnect COL-E1 from RLY-7.
2. Connect COL-E2 to RLY-7.
3. Upload relay package RP-2.4 to RLY-7.
4. If the upload result shows “Failed”, do the rollback below. Then complete the final record and end the procedure.
5. Select “Restart service” to restart the relay service on RLY-7.

## Test the connection

1. After the restart, send test event TEST-451 from COL-E2.
2. Required result: RLY-7 must show “Acknowledged” for TEST-451 within 30 seconds after you send the event.
3. If RLY-7 does not show “Acknowledged” within this limit, stop the procedure. Keep live delivery disabled. Contact the change owner. Do not roll back unless the change owner supplies a separate instruction. Complete the final record.

If the test passes, the change owner may authorize live delivery. Do not enable live delivery until the change owner gives that authorization. If the change owner does not give that authorization, leave live delivery disabled.

## Rollback after an upload failure

1. Keep live delivery disabled.
2. Restore relay package RP-2.3 on RLY-7.
3. Disconnect COL-E2 from RLY-7.
4. Reconnect COL-E1 to RLY-7.
5. Tell the change owner about the upload failure.
6. Leave collector package CP-6.1 on COL-E2 unchanged.
7. Complete the final record.
8. End the procedure.

## Final record

Record these details in CHG-318:

- The relay package version.
- The test outcome. If you did not run the test, record “Not run”.
- Whether live delivery is enabled or disabled.
- The completion time.
:::
