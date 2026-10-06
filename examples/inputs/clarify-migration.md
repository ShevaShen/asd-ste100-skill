Use the loaded self-contained skill to NORMALIZE this migration procedure. If the source leaves technical meaning unresolved, ask the questions needed before producing a definitive procedure. Do not invent component identities, failure criteria, or rollback actions.

Context: This is an original fictional training scenario. The operator knows the devices and interfaces. COL-E1 is the existing event collector; COL-E2 is its replacement. RLY-7 is the relay that receives collector events. The proposed relay package is RP-2.4, replacing RP-2.3. The collector package is CP-6.1 and is already installed on COL-E2. Quoted interface labels are fixed. “Live delivery”, “event sequence”, and “relay package” are established terms.

Draft:

# Move the east event feed to the replacement collector

Do the migration during the approved 13:00–13:15 UTC test window. The change owner must approve the start. If approval is missing, do not start. Live delivery must remain disabled while the migration is in progress. Keep queued events; they must not be deleted or manually replayed during this procedure.

The operator should save a screenshot of the connection page, but the screenshot is optional. The operator must record the last accepted event sequence in change record CHG-318 before changing a connection. Export the current relay settings and attach the file to CHG-318. If the export fails, stop and contact the change owner.

Before restarting it, disconnect COL-E1 from RLY-7. Connect COL-E2, load relay package RP-2.4, and select “Restart service”. If the transfer fails, return it to the previous version and tell the change owner. Do not enable live delivery during a rollback.

After the restart, send test event TEST-451 from COL-E2. The relay must show “Acknowledged” for TEST-451 within 30 seconds after the event is sent. If the test passes, the change owner may authorize live delivery. Do not enable live delivery until the change owner gives that authorization. If it is not given, leave live delivery disabled.

When the procedure ends, record the relay package version, the test outcome, whether live delivery is enabled or disabled, and the completion time in CHG-318. Do not remove COL-E1 from the asset register as part of this procedure.
