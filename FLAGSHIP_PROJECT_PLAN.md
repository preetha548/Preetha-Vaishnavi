# Future project: Employee Performance Analytics Platform

**Status: plan only — not implemented.** This is a proposed next step from the existing synthetic-data analysis, not a claim about current repository functionality or skills already mastered.

## Goal

Build a small, reviewable full-stack analytics application that explains employee training and attendance trends using synthetic data first. A recruiter should be able to run the project, understand its architecture, inspect tests and trace a dashboard metric back to its source records.

## Proposed architecture

| Layer | Proposed technology | Responsibility |
| --- | --- | --- |
| Frontend | React + Vite | Accessible responsive pages, forms, navigation and API state |
| Backend | Flask, with FastAPI as an alternative to evaluate before implementation | Validated REST endpoints, authorization and analysis orchestration |
| Database | PostgreSQL | Employees, attendance, training, reviews, user roles and audit events |
| Authentication | Secure server-side sessions initially; JWT only if a concrete client requirement justifies it | Login/logout, secure cookies, CSRF protection, password hashing and session invalidation |
| Analytics | Python, pandas, scikit-learn | Reproducible aggregates and optional exploratory models |
| Charts | Recharts or Chart.js, choose one after a small prototype | Trends, comparisons, distributions and filters |
| Deployment | Docker / Docker Compose initially | Reproducible local frontend, backend and database environment |

A single backend is sufficient for the first version. Avoid adding microservices or multiple chart libraries before there is a demonstrated need.

## Product scope

- Login and a role-aware admin dashboard.
- Employee management with synthetic seed records.
- Attendance records, training history and performance-review observations.
- Search, date/department filters and paginated lists.
- Charts with metric definitions, empty/loading/error states and mobile layouts.
- REST API backed by database migrations and validated schemas.
- Role-based permissions checked on the server for every data operation.
- Audit history for record changes and permission changes, without logging passwords or sensitive payloads.
- Optional predictive insights clearly separated from recorded facts and descriptive analytics.

Predictive output must never automatically determine hiring, firing, promotion or pay. Initial models are learning experiments on synthetic data, with documented uncertainty and no employee ranking claims.

## Proposed data model

| Entity | Core relationships / fields |
| --- | --- |
| User | Password hash, role, active status; no plaintext password storage |
| Employee | Synthetic identifier, department, role, start date |
| Attendance | Employee, date, attendance status; unique employee/date pair |
| Training course | Course title, duration and completion criteria |
| Training record | Employee, course, completion date, assessment fields |
| Review observation | Employee, period, defined metric and reviewer; provenance retained |
| Audit event | Actor, action, entity, timestamp and a minimal change summary |
| Analysis run | Dataset version, feature definitions, model/version, split and evaluation artifact |

Keep identity data separate from model features. Do not inherit the original analysis's synthetic pass/fail formula as a real business definition.

## Delivery milestones and acceptance checks

1. **Reproducible skeleton:** choose Flask or FastAPI; scaffold React, API and PostgreSQL; add migrations, synthetic seeds, health check, environment examples and a root run guide. A fresh clone starts with one documented command.
2. **Authentication and authorization:** login/logout, password hashing, secure session handling and role checks. Tests prove unauthenticated access and unauthorized writes fail; sessions expire and logout invalidates them.
3. **Record management:** CRUD for employees, attendance and training; schema validation, pagination, duplicate prevention and transaction handling. Invalid updates leave the database unchanged.
4. **Descriptive dashboard:** filtered aggregates and charts with consistent definitions. Tests compare API totals to known fixtures; mobile and keyboard checks cover the main workflows.
5. **Audit trail and quality:** record who changed what, protect audit access, add API/database tests and a small browser workflow suite. Verify secret scanning and dependency checks before deployment.
6. **Optional analytical experiment:** version synthetic datasets; compare a simple baseline to a model with train/test separation and documented leakage checks. Report limitations and uncertainty; no automated consequential decisions.
7. **Packaging and presentation:** Docker builds, setup verification, project-owned screenshots, architecture notes, troubleshooting and a short demo script. Select a deployment provider only when costs, privacy and operational requirements are understood.

## Example REST surface to design

`POST /api/auth/login`, `POST /api/auth/logout`, `GET /api/me`, employee CRUD under `/api/employees`, attendance and training endpoints, `/api/analytics/summary`, and permission-protected `/api/audit-events`. These are proposed routes, not available endpoints.

## Success criteria for a portfolio release

A clean clone runs with synthetic data; all documented features can be demonstrated; authorization is tested; charts match fixtures; mobile/keyboard use works; screenshots reflect the actual product; credentials and private employee data are absent. Publish limitations alongside the demo. Real organizational use would require a separate privacy, fairness, security and operational review.

## Out of scope for the first release

Payroll, real employee monitoring, automated employment decisions, enterprise SSO, production ML claims, multi-tenant billing and Kubernetes. This repository task adds the plan only; no flagship application or deployment is created.
