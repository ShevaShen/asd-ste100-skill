# NORMALIZE: migration with a clarification exchange

This original fictional scenario was run through the actual self-contained skill in a fresh responding-agent context. The response was not hand-written as an ideal answer.

## Reviewer assessment

The first response requests the restart target, the failure definition, rollback scope, test-failure handling, and window-expiry handling. It does not select a meaning for “it” or invent rollback steps. The follow-up supplies those facts as part of the fictional scenario.

The final response preserves the optional screenshot, start approval, disabled delivery, retained events, package identities, acknowledgment limit, and final record. Upload failure triggers the specified rollback; test failure does not automatically trigger it. It also retains the separate authorization needed for rollback outside the window. No claim of full dictionary compliance or operational verification is made.

## Original request and draft

Use the loaded self-contained skill to NORMALIZE this migration procedure. If the source leaves technical meaning unresolved, ask the questions needed before producing a definitive procedure. Do not invent component identities, failure criteria, or rollback actions.

Context: This is an original fictional training scenario. The operator knows the devices and interfaces. COL-E1 is the existing event collector; COL-E2 is its replacement. RLY-7 is the relay that receives collector events. The proposed relay package is RP-2.4, replacing RP-2.3. The collector package is CP-6.1 and is already installed on COL-E2. Quoted interface labels are fixed. “Live delivery”, “event sequence”, and “relay package” are established terms.

Draft:

### Move the east event feed to the replacement collector

Do the migration during the approved 13:00–13:15 UTC test window. The change owner must approve the start. If approval is missing, do not start. Live delivery must remain disabled while the migration is in progress. Keep queued events; they must not be deleted or manually replayed during this procedure.

The operator should save a screenshot of the connection page, but the screenshot is optional. The operator must record the last accepted event sequence in change record CHG-318 before changing a connection. Export the current relay settings and attach the file to CHG-318. If the export fails, stop and contact the change owner.

Before restarting it, disconnect COL-E1 from RLY-7. Connect COL-E2, load relay package RP-2.4, and select “Restart service”. If the transfer fails, return it to the previous version and tell the change owner. Do not enable live delivery during a rollback.

After the restart, send test event TEST-451 from COL-E2. The relay must show “Acknowledged” for TEST-451 within 30 seconds after the event is sent. If the test passes, the change owner may authorize live delivery. Do not enable live delivery until the change owner gives that authorization. If it is not given, leave live delivery disabled.

When the procedure ends, record the relay package version, the test outcome, whether live delivery is enabled or disabled, and the completion time in CHG-318. Do not remove COL-E1 from the asset register as part of this procedure.

## Actual first response

I need these technical details before I can produce a definitive procedure:

1. Which component and service does “Restart service” restart? Does “Before restarting it” refer to the same restart?
2. What does “the transfer” refer to? What conditions indicate that the transfer failed?
3. Which component must return to its previous version? Specify the version and the required rollback actions, including the required collector connections.
4. If RLY-7 does not show “Acknowledged” for TEST-451 within 30 seconds, what must the operator do?
5. If the procedure cannot finish by 13:15 UTC, what must the operator do?

## Supplied clarification

Here are the missing technical details for this fictional training scenario. Use these answers with the original draft to produce the definitive procedure. Preserve the optional screenshot, approvals, limits, identifiers, and final records. Do not invent additional actions.

1. “Restart service” restarts the relay service on RLY-7. “Before restarting it” refers to this same restart. Connect COL-E2 to RLY-7, and load RP-2.4 on RLY-7 before that restart.
2. “Transfer” means uploading RP-2.4 to RLY-7. The upload fails if its result shows “Failed”.
3. If that upload fails, restore relay package RP-2.3 on RLY-7. Disconnect COL-E2 from RLY-7, reconnect COL-E1 to RLY-7, and tell the change owner. Keep live delivery disabled. The operator knows the package-restore control. Do not add a restart or a test to this rollback. Leave CP-6.1 on COL-E2 unchanged. End the procedure with the required record.
4. If RLY-7 does not show “Acknowledged” for TEST-451 within 30 seconds after sending the event, stop and contact the change owner. Keep live delivery disabled. Do not roll back for this test failure unless the change owner supplies a separate instruction. End the procedure with the required record.
5. If the migration is incomplete at 13:15 UTC, stop migration actions, keep live delivery disabled, and contact the change owner. Do not start or continue a rollback outside the window without separate authorization from the change owner. Complete the required record even when the procedure stops early. Mark a test that was not run as “Not run”.

## Actual final response

### Move the east event feed to the replacement collector

#### Conditions and limits

Do the migration during the approved test window, 13:00–13:15 UTC.

Start only after the change owner approves the start. If approval is missing, do not start.

During the migration, keep live delivery disabled.

Keep queued events. Do not delete queued events during this procedure. Do not manually replay queued events during this procedure.

Do not remove COL-E1 from the asset register as part of this procedure.

At 13:15 UTC, if the migration is incomplete, stop migration actions. Keep live delivery disabled. Contact the change owner. Complete the final record.

Do not start or continue a rollback outside the test window without separate authorization from the change owner.

Complete the final record whenever the procedure ends, including when the procedure stops early.

#### Prepare the migration

1. Save a screenshot of the connection page. This step is recommended but optional.
2. Before you change a connection, record the last accepted event sequence in CHG-318.
3. Export the current relay settings.
4. If the export fails, stop the procedure. Contact the change owner. Complete the final record.
5. Attach the exported file to CHG-318.

#### Change the connection and relay package

1. Disconnect COL-E1 from RLY-7.
2. Connect COL-E2 to RLY-7.
3. Upload relay package RP-2.4 to RLY-7.
4. If the upload result shows “Failed”, do the rollback below. Then complete the final record and end the procedure.
5. Select “Restart service” to restart the relay service on RLY-7.

#### Test the connection

1. After the restart, send test event TEST-451 from COL-E2.
2. Required result: RLY-7 must show “Acknowledged” for TEST-451 within 30 seconds after you send the event.
3. If RLY-7 does not show “Acknowledged” within this limit, stop the procedure. Keep live delivery disabled. Contact the change owner. Do not roll back unless the change owner supplies a separate instruction. Complete the final record.

If the test passes, the change owner may authorize live delivery. Do not enable live delivery until the change owner gives that authorization. If the change owner does not give that authorization, leave live delivery disabled.

#### Rollback after an upload failure

1. Keep live delivery disabled.
2. Restore relay package RP-2.3 on RLY-7.
3. Disconnect COL-E2 from RLY-7.
4. Reconnect COL-E1 to RLY-7.
5. Tell the change owner about the upload failure.
6. Leave collector package CP-6.1 on COL-E2 unchanged.
7. Complete the final record.
8. End the procedure.

#### Final record

Record these details in CHG-318:

- The relay package version.
- The test outcome. If you did not run the test, record “Not run”.
- Whether live delivery is enabled or disabled.
- The completion time.

## Evidence

See [execution metadata and file hashes](manifest.json). Display headings are nested and application writing-block wrappers are omitted here; the response wording is unchanged. Exact responses are retained in [outputs/](outputs/), and original prompts in [inputs/](inputs/). Reviewer assessments were written by the primary assistant after execution, not by a human expert.
