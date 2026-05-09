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
