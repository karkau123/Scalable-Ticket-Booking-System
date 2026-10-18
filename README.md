# Scalable Ticket Booking System

An incremental implementation of an event ticket booking platform. The goal is
to understand and demonstrate the complete booking flow, especially preventing
overselling when many users reserve seats at the same time.

## Current implementation

The first milestone provides a runnable FastAPI service, a versioned liveness
endpoint, interactive API documentation, and basic HTTP contract tests.
Authentication, event management, reservations, and infrastructure are planned
work; they are not implemented yet.

## Local setup (Windows PowerShell)

Requires Python 3.12 or newer. The initial implementation was verified with Python 3.13.
Run these commands from the repository root:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt -c requirements-dev.lock.txt
.\.venv\Scripts\python.exe -m uvicorn services.api.app.main:app --reload
```

Using the environment's Python directly avoids needing to change PowerShell's
script execution policy. Docker, PostgreSQL, Redis, and Kafka are not required
for this milestone.

- Health: <http://127.0.0.1:8000/api/v1/health> returns `{"status":"ok"}`.
- Interactive docs: <http://127.0.0.1:8000/docs>.
- OpenAPI schema: <http://127.0.0.1:8000/openapi.json>.

The health endpoint checks process liveness. Dependency readiness checks will be
added when external services are introduced.

## Verification

```powershell
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m ruff format --check .
.\.venv\Scripts\python.exe -m pip check
```

`requirements.txt` lists runtime dependencies; `requirements-dev.txt` adds local
development tools. `requirements-dev.lock.txt` records the complete dependency
set verified for this milestone.

## Build sequence

Each step should add a working feature or fix a reproduced issue, with checks
that demonstrate the behavior. The schedule is a guide, not a claim that future
features already work.

| Week | Scope | Evidence of completion |
| --- | --- | --- |
| 1 | API foundation, configuration, PostgreSQL, migrations, event catalog | Start locally, apply migrations, create and browse events |
| 2 | Authentication, authorization, inventory and reservations over gRPC | Enforce ownership and reserve, confirm, and release seats |
| 3 | Orders, idempotency, Kafka workers, reservation expiry | Exercise payment outcomes, retries, and abandoned reservations |
| 4 | Concurrency tests, failure handling, CI, deployment and interview notes | Demonstrate capacity invariants under contention and explain tradeoffs |

After this first commit, the next small steps are environment-based API
configuration, local PostgreSQL setup, and the initial event schema/migration.
Fixes should come from observed failures and include the reproduction or test.

## Reference and attribution

This learning implementation uses the MIT-licensed EventSphere project supplied
in `Downloads/eventsphere-main/eventsphere-main` as its architectural reference.
The reference is credited to Mathusanth. This repository documents its own
implemented scope and verification results.

The planned architecture follows the reference's public FastAPI service,
internal gRPC inventory service, PostgreSQL persistence, Redis coordination,
and Kafka workers. Those components will be introduced and evaluated as the
implementation progresses.

FastAPI's [first steps guide](https://fastapi.tiangolo.com/tutorial/first-steps/)
documents the application and interactive documentation basics used here.
The test dependencies follow Starlette's
[test client guide](https://starlette.dev/testclient/).
