# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Scope — STRICT BOUNDARIES

This session is scoped to the arclyt.io frontend repository.

- The ONLY external API this project consumes is the ops.arclyt.io API
- Do NOT reference, read, modify, or use code or files from any other project
- ops.arclyt.io is a separate repository — read its API contracts but do NOT modify it from this session
- All other APIs, endpoints, or configs not defined here are OUT OF SCOPE
- If unsure whether something is in scope, STOP and ask before proceeding

## Project Overview

Arclyt is a marketing website for a cloud consulting/modernization firm. It is a Vue 3 SPA deployed as a static site on AWS (S3 + CloudFront). The repo contains both the frontend (`src/`) and the AWS CDK infrastructure (`infra/`).

## Commands

### Frontend
```bash
npm install          # install deps
npm run dev          # dev server (Vite)
npm run build        # production build → dist/
npm run preview      # preview the dist/ build locally
```

### Infrastructure (from repo root)
```bash
npm run infra:install    # install CDK deps
npm run infra:bootstrap  # first-time CDK bootstrap (us-east-1)
npm run infra:deploy     # build infra TS + deploy all stacks
npm run infra:deploy-site # deploy only ArclytSiteStack
```

### Deploy frontend changes only (no infra changes)
```powershell
npm run build && aws s3 sync dist/ s3://arclyt-site-711305909128-us-east-1 --delete --region us-east-1 && aws cloudfront create-invalidation --distribution-id E3N0I6PH7QG06C --paths "/*"
```

## Architecture

### Frontend (`src/`)
Single-page app with no client-side router. `App.vue` composes all page sections as a vertical stack. The `/schedule` URL is handled with a `window.location.pathname` check in `onMounted` — it opens `ContactModal` and fires a GA event.

**Component page order:** `Header → Hero → Services → Capabilities → CertBar → FeaturedEngagements → Process → Stack → TechTicker → Footer`

**Global styles** are in `src/styles/main.css` via CSS custom properties (`--bg`, `--text`, `--accent`, `--accent2`, `--mono`, `--sans`, `--max`, etc.). All components use `<style scoped>`. The `.wrap` class (`max-width: 1080px; margin: 0 auto`) is the standard content container.

**Analytics:** `vue-gtag` is initialized in `main.js` (tag `G-0QDJTQPRZK`). `event()` calls from `vue-gtag` are used in `App.vue` and `ContactModal.vue`.

### Scheduling UI — two parallel implementations
There are **two scheduling components** with duplicated calendar/slot-picker logic:
- **`StrategyScheduler.vue`** — inline page section (3-step layout: Date → Time → Details). Shows times as static "EST".
- **`ContactModal.vue`** — modal opened via the `/schedule` path or CTA clicks. Adds timezone conversion (EST slots → user's local time via `Intl.DateTimeFormat`), a "comments" field, and auto-selects the first available date on open.

Both components call the same external scheduling API via `VITE_SCHEDULE_BASE_URL` / `VITE_SCHEDULE_TENANT_ID`. The modal is the more capable/current implementation.

### Environment Variables (`.env`)
| Variable | Purpose |
|---|---|
| `VITE_CONTACT_API_URL` | Lambda Function URL for contact form |
| `VITE_SCHEDULE_BASE_URL` | Base URL for scheduling API (external service) |
| `VITE_SCHEDULE_TENANT_ID` | Tenant ID for scheduling API |
| `CERT_ARN` | ACM certificate ARN (used by CDK, not Vite) |

`.env.development` overrides `VITE_SCHEDULE_BASE_URL` to `http://localhost:3001` for local development.

### Infrastructure (`infra/`)
Two CDK stacks:
- **`ArclytCertStack`** — ACM certificate for `arclyt.io` (must be in `us-east-1`). DNS validation is manual via Route53.
- **`ArclytSiteStack`** — S3 bucket (private, OAC) + CloudFront distribution + two Lambda Function URLs + DynamoDB table.

**Lambdas** (Python 3.12, in `infra/lambda/`):
- `contact-handler.py` — stores contact form submissions in DynamoDB, sends SES notification to `connect@arclyt.io`
- `schedule-handler.py` — stores strategy call bookings, sends HTML confirmation email to the user **and** an admin notification email

Both Lambdas share the same DynamoDB table (`arclyt-contact-submissions-{account}`). CORS is configured at the Function URL level — do **not** add CORS headers inside the Lambda response.

Infrastructure config is centralized in `infra/config.ts` (domain, regions, email addresses, source folder path).

## Known Issues / Technical Debt

- **Duplicated scheduler logic**: `StrategyScheduler.vue` and `ContactModal.vue` share ~80% of calendar/slot state logic. `StrategyScheduler.vue` is older; it sends `scheduledDate` as a human-readable string (e.g., "Monday, April 16") while `ContactModal.vue` sends an ISO date string — the backend receives inconsistent formats.
- **`StrategyScheduler.vue` has no timezone conversion**: Slots are displayed as "EST" regardless of the user's locale, unlike the modal which converts to local time.
- **No CSP headers**: CloudFront serves no `Content-Security-Policy` header.
- **Lambda CORS origins are hardcoded** to `arclyt.io` and `www.arclyt.io` in `site-stack.ts` via `corsConfig` — these are not derived from `config.ts`.
