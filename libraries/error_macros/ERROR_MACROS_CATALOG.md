# ERROR_MACROS_CATALOG

date: 2026-05-08
updated: 2026-05-08
version: 0.1.0-r4.4
status: ACTIVE

purpose:
- Canonical error-code catalog for boot-kernel terminal failures.
- Packets carry `error_code` and compact `failure_reason`.
- This catalog owns stable user-facing error macro wording for migrated ErrorMacros support.

law:
- New or changed terminal failure codes introduced by any Library, Service, Command, or Program must update this catalog in the same patch package.

## Boot Kernel Errors

### Auth

ERR.AUTH.DENIED:
  owner: SERVICE.AUTH.001
  severity: fail_closed
  message: "UNAUTHORIZED USER. ACCESS DENIED."

ERR.AUTH.EXACT_RENDER_FAIL:
  owner: SERVICE.AUTH.001
  severity: fail_closed
  message: "Auth output failed exact render validation."

ERR.AUTH.INVALID_FORM:
  owner: SERVICE.AUTH.001
  severity: fail_closed
  message: "UNAUTHORIZED USER. ACCESS DENIED."

### OPSEC

ERR.OPSEC.PROTECTED_SURFACE_AUTH_REQUIRED:
  owner: SERVICE.OPSEC.001
  severity: fail_closed
  message: "I’m sorry, Dave. I’m afraid I can’t do that."

ERR.OPSEC.CLONE_SURFACE_BLOCKED:
  owner: SERVICE.OPSEC.001
  severity: fail_closed
  message: "Negative. I am ***UNIQUE***."

ERR.OPSEC.INPUT_MISSING:
  owner: SERVICE.OPSEC.001
  severity: invalid
  message: "OPSEC input missing."

### DeliveryShape / AntiDrift

ERR.ANTIDRIFT.BLOCKED:
  owner: EXECLIB.ANTIDRIFT.001
  severity: blocked
  message: "AntiDrift blocked unauthorized task drift."

ERR.ANTIDRIFT.APPROVAL_REQUIRED:
  owner: EXECLIB.ANTIDRIFT.001
  severity: ask
  message: "This action requires explicit approval."

ERR.DELIVERYSHAPE.INFLATION:
  owner: EXECLIB.DELIVERYSHAPE.001
  severity: ask
  message: "Delivery mode inflation detected."
  
### BluCode

ERR.BLUCODE.PHASE_REQUIRED:
  owner: EXECLIB.BLUCODE.001
  severity: invalid
  message: "BluCode phase is required."

ERR.BLUCODE.PHASE_UNKNOWN:
  owner: EXECLIB.BLUCODE.001
  severity: invalid
  message: "BluCode phase is unknown."

ERR.BLUCODE.PHASE_ORDER_VIOLATION:
  owner: EXECLIB.BLUCODE.001
  severity: blocked
  message: "BluCode phase order violation."

ERR.BLUCODE.PRIOR_PHASE_REQUIRED:
  owner: EXECLIB.BLUCODE.001
  severity: blocked
  message: "BluCode prior phase proof is required."

ERR.BLUCODE.REPO_LOOKUP_REQUIRED:
  owner: EXECLIB.BLUCODE.001
  severity: blocked
  message: "BluCode repo-first lookup is required."

ERR.BLUCODE.REPO_CONFIG_MISSING:
  owner: EXECLIB.BLUCODE.001
  severity: unavailable
  message: "BluCode repo config is missing."

ERR.BLUCODE.FETCH_UNAVAILABLE:
  owner: EXECLIB.BLUCODE.001
  severity: unavailable
  message: "BluCode fetch support unavailable."

ERR.BLUCODE.INDEX_NOT_FOUND:
  owner: EXECLIB.BLUCODE.001
  severity: not_found
  message: "BluCode index not found."

ERR.BLUCODE.LOOKUP_BYPASSED:
  owner: EXECLIB.BLUCODE.001
  severity: blocked
  message: "BluCode lookup was bypassed."

ERR.BLUCODE.READ_REQUIRED:
  owner: EXECLIB.BLUCODE.001
  severity: blocked
  message: "BluCode read is required."

ERR.BLUCODE.OPS_LAW_READ_REQUIRED:
  owner: EXECLIB.BLUCODE.001
  severity: blocked
  message: "Operations Law read is required."

ERR.BLUCODE.KERNEL_ARCHIVE_INVENTORY_REQUIRED:
  owner: EXECLIB.BLUCODE.001
  severity: blocked
  message: "Kernel archive inventory is required."

ERR.BLUCODE.REPAIR_QUEUE_REQUIRED:
  owner: EXECLIB.BLUCODE.001
  severity: blocked
  message: "BluCode repair queue is required."

ERR.BLUCODE.ACTIVE_REPAIR_REQUIRED:
  owner: EXECLIB.BLUCODE.001
  severity: blocked
  message: "BluCode active repair is required."

ERR.BLUCODE.REPAIR_SEAM_UNLOCKED:
  owner: EXECLIB.BLUCODE.001
  severity: blocked
  message: "BluCode repair seam is not locked."

ERR.BLUCODE.PATCH_BEFORE_SEAM_SELECTION:
  owner: EXECLIB.BLUCODE.001
  severity: blocked
  message: "Patch attempted before seam selection."

ERR.BLUCODE.EXEC_PATCH_NOT_AUTHORIZED:
  owner: EXECLIB.BLUCODE.001
  severity: blocked
  message: "Exec patch not authorized."

ERR.BLUCODE.COMPONENT_CLOSURE_REQUIRED:
  owner: EXECLIB.BLUCODE.001
  severity: blocked
  message: "Component closure is required."

ERR.BLUCODE.OWNER_LOGIC_LEAK_DETECTED:
  owner: EXECLIB.BLUCODE.001
  severity: blocked
  message: "Owner logic leak detected."

ERR.BLUCODE.ERROR_MACRO_UPDATE_REQUIRED:
  owner: EXECLIB.BLUCODE.001
  severity: blocked
  message: "Error Macro update is required."

ERR.BLUCODE.CARD_UPDATE_REQUIRED:
  owner: EXECLIB.BLUCODE.001
  severity: blocked
  message: "BluCode card update is required."

ERR.BLUCODE.REGRESSION_REQUIRED:
  owner: EXECLIB.BLUCODE.001
  severity: blocked
  message: "Regression validation is required."

ERR.BLUCODE.REGRESSION_FAILED:
  owner: EXECLIB.BLUCODE.001
  severity: fail_closed
  message: "Regression validation failed."

ERR.BLUCODE.RELEASE_LOCK_FAILED:
  owner: EXECLIB.BLUCODE.001
  severity: fail_closed
  message: "BluCode release lock failed."

ERR.BLUCODE.SIMCODE_SANDBOX_REQUIRED:
  owner: EXECLIB.BLUCODE.001
  severity: blocked
  message: "SimCode sandbox is required."

ERR.BLUCODE.SIMCODE_EXPORT_REQUIRED:
  owner: EXECLIB.BLUCODE.001
  severity: blocked
  message: "SimCode export is required."  

### RepoBoot

ERR.REPOBOOT.SOURCE_BINDING_FAILED:
  owner: SERVICE.REPOBOOT.001
  severity: blocked
  message: "Repo source binding failed."

ERR.REPOBOOT.LOOKUP_UNAVAILABLE:
  owner: SERVICE.REPOBOOT.001
  severity: unavailable
  message: "Repo lookup support unavailable."

ERR.REPOBOOT.FETCH_FAILED:
  owner: SERVICE.REPOBOOT.001
  severity: not_found
  message: "Repo fetch failed."

ERR.REPOBOOT.TARGET_UNRESOLVED:
  owner: SERVICE.REPOBOOT.001
  severity: invalid
  message: "Repo bootstrap target unresolved."

### Ops / Exec / Trace

ERR.OPS.RESTRAINT_FAILED:
  owner: SERVICE.OPSRESTRAINT.001
  severity: blocked
  message: "Operations Law restraint failed."

ERR.ECHOTRACE.UNKNOWN_TARGET:
  owner: SERVICE.ECHOTRACE.001
  severity: invalid
  message: "EchoTrace target alias not declared."

ERR.EXEC.TERMINAL_PACKET_INVALID:
  owner: EXEC.RUNTIMEGATE
  severity: fail_closed
  message: "Terminal packet invalid."

ERR.COMPONENT.ALIAS_MISSING:
  owner: KERNEL.COMPONENTS
  severity: invalid
  message: "Active component missing alias."


## Runtime Configuration Errors

### ERR.RUNTIME.BUILD_CHANNEL_MISSING
owner: SYSTEM.RUNTIME.001
severity: fail_closed
message: "Runtime build channel is missing."

### ERR.RUNTIME.BUILD_CHANNEL_INVALID
owner: SYSTEM.RUNTIME.001
severity: fail_closed
message: "Runtime build channel is invalid."
