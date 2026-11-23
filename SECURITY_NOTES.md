# Security notes

Review date: 14 September 2026. Scope: current tracked text, notebook JSON and text entries in the preserved ZIP, plus manual review of featured projects and selected risky patterns. This is a source-level review, not a penetration test or a guarantee about repository history, images, binary model metadata or dependency vulnerabilities.

## Credentials and secret scanning

No recognizable live API-key, cloud-key, private-key or token signature was found in the scanned text. Values were not printed in reports. The GitHub Skills expressions using `secrets.GITHUB_TOKEN` reference a runtime-provided token; they are not literal leaked credentials. Those course workflows are now archived and inactive.

Known demo credential handling remains:

| Location | Finding | Action before real use |
| --- | --- | --- |
| `val.js` | Hard-coded account/PIN checks; values intentionally redacted | Replace with actual server-side authentication. Do not use real banking details. |
| `login.html` | Client-side account data, including a password field, stored in localStorage | Never enter reused or real passwords. Remove stored data and replace the demo authentication design. |
| `Madhampatti rangaraj Groups/index.html` | Browser-local password-bearing user records and login checks | Not authentication. Use server-side password hashing, access controls and session handling in a future application. |

These are toy mechanisms, not confirmed active service credentials. If any value has ever been reused for a real service, rotate it there and remove it from current files and history using a separately reviewed cleanup. Moving a file or adding `.gitignore` does not erase past exposure.

## Brain-tumor prototype: repaired boundaries

- POST-only `/predict`; GET returns 405 instead of a server error.
- 6 MB request cap, JPEG/PNG allowlist, content-format verification and a 16-million-pixel limit.
- Original filename is sanitized only to determine extension. A private temporary directory and fixed generated filename prevent path traversal and cross-request name collisions.
- Temporary uploads are removed on both success and failure. They are not served publicly or logged.
- Explicit template path and repository-relative default model path work independently of the launch directory.
- Debug is off and the development server binds to loopback by default.
- Model/setup failures return a useful 503 page instead of exposing a stack trace. Responses are marked `no-store`.
- CLI prediction no longer unpickles data or retrains. Historical scripts are preserved under `archive/brain-tumor-original/` and must not be run as the maintained service.

These controls do not make this a public or clinical service. It lacks authentication, rate limiting, CSRF protection, production process supervision and application-level concurrency limits. Use only synthetic/non-sensitive sample images on a local machine. The model cannot verify scan suitability, consent, provenance or clinical validity.

Model files can execute library-level deserialization logic; only load trusted local artifacts. `BRAIN_TUMOR_MODEL_PATH` is an optional **process environment** setting, never a user-uploaded model selector. `.env.example` documents it; the app does not automatically load dotenv files. The pinned TensorFlow version is a legacy compatibility target, not a claim of current production security.

## Historical projects needing separate repairs

| Area | Source evidence | Remaining limitation |
| --- | --- | --- |
| User-derived HTML | Book, Friends, Interview Board, Cycle Marathon and other DOM examples | Several values are interpolated into `innerHTML`; use `textContent` or safe DOM construction and validate inputs. No repository-wide XSS repair is claimed. |
| Participant registration | `Cycle Marathon/server.js` and `public/script.js` | No authentication, schema validation or private participant storage; missing `data/` directory and synchronous file writes. |
| Dance booking | `Tango/app.js` | Unauthenticated admin route and interpolated booking values. Do not collect real contact information. |
| Other forms | Friend, Sports Sponsorship, banking and identity-form demos | Submission/validation/storage semantics are incomplete or illustrative; use sample data only. |
| Static servers | Several Express `.listen()` calls omit a host | May bind beyond loopback; restrict access when running historical projects. |
| Third-party scripts/images | CDN dependencies and copied HTML in Book/Biscuits; remote jewellery images | Availability, provenance and integrity require review. Some image URLs use HTTP. |
| Dependency setup | Historical npm manifests, root Vite/Parcel mismatch, missing manifests | No lockfiles or full npm vulnerability audit; do not infer production readiness from a successful static preview. |

Source-pattern searches found no direct `eval()` call, explicit Python/Node shell-execution call, permissive CORS setup or hard-coded private LAN IP in current application source at audit time. Absence of a pattern is not proof of absence of all equivalent behavior. Archive content is historical material, not an actively supported runtime.

## Medical and predictive claims

The brain-tumor app is an **educational / research image-classification prototype. Not intended for medical diagnosis.** The 30% web and 50% CLI thresholds are manual, unvalidated cutoffs. Training and inference normalization differ. Synthetic smoke tests confirm execution only, not diagnostic accuracy.

Employee analysis uses synthetic records and must not be used for hiring, firing or other employment decisions. Milk, diabetes and oil/gas browser “prediction” demos are rules, not validated AI or safety systems.

## Guidance for future changes

Use isolated environments, real input schemas, safe output rendering, least-privilege access and synthetic test fixtures. Keep credentials, uploads, local environments, caches and data exports out of commits. Review licenses/credits before using third-party media in a public portfolio. This task did not publish a site, enable cloud hosting or send any messages.

## Implementation references

Upload limits and filename handling follow the documented Flask mechanisms; content verification and temporary-file cleanup are additional application controls. See [Flask upload patterns](https://flask.palletsprojects.com/en/stable/patterns/fileuploads/) and [Flask configuration](https://flask.palletsprojects.com/en/stable/config/). Model setup should be checked against [TensorFlow installation documentation](https://www.tensorflow.org/install/pip) and [Keras model loading](https://keras.io/api/models/model_saving_apis/model_saving_and_loading/).
