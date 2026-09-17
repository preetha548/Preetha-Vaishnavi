# Repository audit

Baseline: commit `663ccbe3c51ac2441f059395f7a7f44d1f2c0016`, inspected 14 September 2026, before any portfolio-task code changes. This report records the original state; later repairs are described in CHANGES_SUMMARY.md. The earlier untracked personal invitation is not part of this GitHub baseline.

## Scope and method

Inspected all 387 tracked paths: 117 top-level project folders, seven Python files, 15 package manifests, one notebook, two HDF5 models, and one ZIP. Read source as text, extracted imports/entry points/local asset references, compared SHA-256 hashes, checked archive entries without executing them, and scanned text for security indicators. Runtime validation of selected projects follows the audit. Generated notebook outputs and binary screenshots are not proof that current source works.

Six browsing categories (folder counts are exclusive; several technologies overlap):

- AI / ML and data analysis: 4 folders.
- Design / UI experiments: 33 folders.
- Interactive / JavaScript: 25 folders.
- Learning exercises: 4 folders.
- Node.js / backend experiments: 23 folders.
- Web development: 28 folders.

The root brain-tumor scripts are an additional logical project, separate from these folder counts. The notebook is an unrelated random smoothie chart, not a brain-tumor training notebook.

## Recommended featured projects

| Project | Evidence and honest assessment |
| --- | --- |
| Brain Tumor Image Classification | TensorFlow/Keras CNN training and saved models, OpenCV/Pillow preprocessing, Flask inference. Strongest ML discussion material, but initially missing template and safe upload handling; educational prototype only. |
| Employee Performance Analytics & Prediction | 200 synthetic records, pandas summaries, 30 numbered chart sections plus feature importance, random-forest training and evaluation. Self-contained learning analysis, not real employee validation. |
| Marketing Social-Post UI | Two implemented carousel cards, like/repost toggles, share/copy handling and CSS illustrations. More interaction than a static landing page; not a marketing service or real social network. |
| Jewellery Store Frontend | Multi-section product gallery and layout. Existing footer credits Jak Ashuraliev: present as a credited adaptation/study, not wholly original authorship. Script has an unmatched wrapper and duplicated handlers; repair before showcasing. |
| Rock Paper Scissors | Playable random-opponent game with score persistence and reset. Chosen over Flight/Bus because its core interaction is present and cohesive. |

Flight Booking is an Express-served visual UI, not booking software, and its `public` directory is absent. Bus Booking has a small jQuery seat demonstration but incorrect range/selection logic and no booking persistence. They belong in the index with limitations, not as full applications.

## Python and AI/data findings

- `Arrays/array.py`: imports `array`.
- `Company IT Prediction analysis/app.py`: imports `numpy`, `pandas`, `seaborn`, `matplotlib.pyplot`, `sklearn.model_selection`, `sklearn.ensemble`, `sklearn.metrics`, `sklearn.preprocessing`.
- `Drug addiction Analysis/app.py`: imports `pandas`, `matplotlib.pyplot`.
- `Environmental prediction/app.py`: imports `numpy`, `matplotlib.pyplot`, `sklearn.linear_model`.
- `app.py`: imports `os`, `tensorflow`, `numpy`, `tensorflow.keras.preprocessing`, `PIL`, `cv2`, `keras.models`, `flask`, `werkzeug.utils`.
- `mainTest.py`: imports `cv2`, `keras.models`, `PIL`, `numpy`, `matplotlib.pyplot`, `pickle`.
- `mainTrain.py`: imports `cv2`, `os`, `tensorflow`, `tensorflow`, `PIL`, `numpy`, `sklearn.model_selection`, `keras.utils`, `keras.models`, `keras.layers`, `keras.layers`, `keras.utils`.

- No Python requirements files or dependency locks exist in the baseline.
- Root `app.py` loads a model relative to the current directory, requests missing `templates/index.html`, and returns `None` for GET `/predict`. Uploads lack size/type validation, can overwrite a sanitized filename, and are retained indefinitely. Debug mode is always enabled.
- `mainTrain.py` expects absent `datasets/no` and `datasets/yes`, processes only filenames with a fragile `.jpg` check, and trains nine epochs despite a filename containing “10Epochs”. It normalizes with `keras.utils.normalize(axis=1)`.
- Both inference scripts instead divide by 255. This preprocessing mismatch requires a controlled future experiment, not a silent change to inference.
- `app.py` uses a manual 30% class-1 score threshold; `mainTest.py` uses 50%. Neither threshold is medically validated; outputs are model scores, not calibrated disease probabilities.
- `mainTest.py` additionally loads four missing pickle files, uses a machine-specific image path, and unexpectedly retrains the model for nine epochs during a supposed prediction run.
- `Drug addiction Analysis/app.py` actually plots a ten-row illustrative suicide-prevention/support dataset; it is descriptive analysis, not drug-addiction prediction.
- `Environmental prediction/app.py` fits linear regression to six hard-coded temperature values without sourced measurements or held-out validation.
- `Suicide prediction analysis/index.html` is empty; only an image accompanies it.
- `Milk AI Detector`, `Diabetes Prediction`, and `Oil gas` use JavaScript heuristics. `Gen AI` uses a fixed response dictionary. Do not advertise these as trained AI models.

## Node.js, dependencies and missing folders

Many `package.json` files run a static development server; their presence alone does not imply a backend. Actual Node.js sources are listed below. Only Cycle Marathon and Flight booking declare Express locally; standalone `http` examples need no third-party server dependency.

- `Ad`: express; no local package manifest.
- `Candid photography`: express, path; no local package manifest.
- `Chess`: express; no local package manifest.
- `Chocolate bouque`: express, path; no local package manifest.
- `Cycle Marathon`: express, fs; local package manifest present.
- `Diary`: http; no local package manifest.
- `Family Budget`: express; no local package manifest.
- `Farmland`: express; no local package manifest.
- `Feelings Chart`: express; no local package manifest.
- `Flight booking`: express, path; local package manifest present.
- `Friend`: express; no local package manifest.
- `Letter box`: http; no local package manifest.
- `Pininterest`: express; no local package manifest.
- `Sample Questions`: express; no local package manifest.
- `Sports Sponshorship form`: body-parser, express, path; no local package manifest.
- `Sweet offer`: express; no local package manifest.
- `Tango`: express; no local package manifest.
- `Toast`: express; no local package manifest.
- `Tomato Ketchup`: express; no local package manifest.
- `Whatsapp call`: express; no local package manifest.
- `calendar`: tailwindcss/defaultConfig; no local package manifest.
- `ola`: express; no local package manifest.
- `timetable`: express, path; no local package manifest.

- Root `server.js` also requires undeclared Express and an absent `public/index.html`.
- Missing static directories: `Candid photography/public`, `Chocolate bouque/public`, `Flight booking/public`, `Pininterest/public`, `Sports Sponshorship form/public`, `Whatsapp call/public`, root `public`, and `timetable/public`. Cycle Marathon has a public directory, but lacks its writable `data` directory.
- Root `app.js` imports absent `library/index.js`; the todo app is incomplete.
- Root Vite config references absent `src`, Vite and React/Tailwind plugins not declared in the root Parcel manifest. The root package describes a cat API app, but its HTML is a college timetable.
- `Google Maps/package.json` and `sandbox.config.json` are byte-identical: likely export/configuration mix-up.
- Historical Parcel 1 and Tailwind 0.6 manifests and other unlocked npm ranges need separate compatibility/dependency review; no vulnerability-free claim is made.

## Missing local assets / references

Static literal-path scan found the following candidates. Route-like links and root-relative URLs require interpretation; external image/CDN availability is not assumed.

| Source | Line | Reference |
| --- | --- | --- |
| `Book/index.html` | 117 | `new` |
| `Icecream parlour/index.html` | 7 | `C:\Users\vaish\OneDrive\Pictures\icecream.jpg` |
| `Icecream parlour/index.html` | 16 | `C:\Users\vaish\OneDrive\Pictures\Images\ice1.jpg` |
| `Icecream parlour/index.html` | 17 | `C:\Users\vaish\OneDrive\Pictures\Images\ice2.jpg` |
| `Icecream parlour/index.html` | 18 | `C:\Users\vaish\OneDrive\Pictures\Images\ice3.jpg` |
| `Job Application/index.html` | 8 | `/style.css` |
| `Marriage Certificate/style.css` | 13 | `marriage.jpg` |
| `Solar ads/index.html` | 20 | `c:\Users\vaish\Downloads\WhatsApp Image 2026-08-08 at 11.10.17 PM (2).jpeg` |
| `Solar ads/index.html` | 135 | `script.js` |
| `Solar ads/index.html` | 559 | `c:\Users\vaish\Downloads\WhatsApp Image 2026-08-08 at 11.10.17 PM (2).jpeg` |
| `Toast/server.js` | 133 | `/avocado-toast.png` |
| `Wishlist/index.html` | 10 | `favicon.png` |
| `Wishlist/index.html` | 11 | `favicon.png` |
| `Wishlist/index.html` | 14 | `data.js` |
| `Wishlist/index.html` | 15 | `item.js` |
| `Wishlist/index.html` | 16 | `script.js` |
| `payment.html` | 7 | `css/style.css` |
| `reception gift/index.html` | 154 | `C:\Users\SAI\Pictures\Images\Gift.jpg` |

`Book/index.html` → `new` is a broken navigation candidate, not necessarily an asset. `/style.css` in Job Application exists when serving the whole root, but is not the project’s own stylesheet. `Wishlist` lacks its application scripts.

## Empty files

- `Birthday Card/README.md`
- `Job Application/server.js`
- `README.md`
- `Solar ads/style.css`
- `Suicide prediction analysis/index.html`
- `banner.png`
- `logo.png`
- `logo_lite-cbb357.png`
- `retro-games.jpg`
- `tests.html`
- `thumbnail.jpg`

Populate root README; archive unreferenced root placeholders. Retain in-project placeholders when moving them could alter existing paths. The zero-byte root `logo.png` also matches text in remote URLs, so retain it conservatively pending ownership clarification.

## Duplicates and suspicious root files

- Exact duplicate group: `Biscuits/Screenshot_29-7-2026_155649_.jpeg`, `Bus Booking System/Screenshot_29-7-2026_155649_.jpeg`.
- Exact duplicate group: `Biscuits/package.json`, `Homepage/NODEBOX/package.json`.
- Exact duplicate group: `Biscuits/sandbox.config.json`, `Bus Booking System/sandbox.config.json`, `Homepage/NODEBOX/sandbox.config.json`, `Icecream parlour/sandbox.config.json`, `Matrix/sandbox.config.json`, `Movie Review/NODEBOX/sandbox.config.json`, `Wishlist/sandbox.config.json`, `rock paper scissors/sandbox.config.json`, `sandbox.config.json`.
- Exact duplicate group: `Google Maps/package.json`, `Google Maps/sandbox.config.json`.
- Exact duplicate group: `index.html`, `timetable/index.html`.
- Exact duplicate group: `script.js`, `timetable/script.js`.
- Exact duplicate group: `server.js`, `timetable/server.js`.
- Exact duplicate group: `style.css`, `timetable/style.css`.

- 61 nonempty loose root image files can move to `screenshots/archive` after checking source references; retain original filenames because project attribution is uncertain.
- Archive `Projects.zip` intact: 80 entries, 429,236 uncompressed bytes, including projects absent from the working tree. Do not discard or blindly extract duplicates.
- Root `index.html`, `script.js`, `style.css`, and `server.js` match the timetable copies. Keep the root entry point to preserve existing URLs.
- Mixed banking, todo, keyboard, CSS/SCSS and build fragments have unclear ownership. Keep interconnected source files in place and document them rather than guessing a reorganization.
- Preserve root models and scripts with stable paths; add a dedicated documentation/dependency directory instead of relocating model files.
- Existing `.github` workflows are GitHub Skills course automation with write permissions that can modify README. Archive the course workflows and step files together to prevent future portfolio text replacement.
- Existing LICENSE is an MIT-form grant with “GitHub and others” attribution. Preserve it verbatim; it does not independently prove rights to every image or copied demo. Preserve ATTRIBUTIONS.md and inline author credits.

## Security findings

- Pattern scans found no recognizable live API-key/token signatures in tracked text or inspected ZIP text entries. This is not proof that the full git history, model metadata or image contents contain no secrets.
- Root `val.js` contains hard-coded demo account/PIN values (redacted here). These are bypassable client-side checks, not authentication.
- `login.html` and `Madhampatti rangaraj Groups/index.html` store/read password-bearing records in localStorage. Never enter real credentials in these demos.
- User-derived HTML insertion appears in Book, Friends, Interview Board, Cycle Marathon and other UI exercises. Review escaping before accepting untrusted data.
- Cycle Marathon exposes participant data without authentication and writes unvalidated input. Tango has an unauthenticated admin route and interpolates booking data; neither should collect real personal data as-is.
- Flask debug mode and upload handling need repair. Several Node apps listen without an explicit loopback host; run historical demos only in controlled local environments.
- No direct `eval()` or explicit Python/Node shell execution pattern found in tracked application source; no permissive CORS configuration or private LAN IP literal found in that scan.
- Public image/CDN dependencies, copied third-party HTML/scripts in Book/Biscuits, and personal-information form demos require attribution/privacy review before hosting.

## Complete project-folder inventory

Names below are historical paths. Titles and interaction signals come from source inspection, not a functionality guarantee. All folders are retained to preserve links.

| Folder | Category | Observed page title / source evidence |
| --- | --- | --- |
| `Ad` | Node.js / backend experiments | Drink Prime - Pure Water |
| `Alumini registration form` | Design / UI experiments | Alumni Registration Form |
| `Annoucement banner` | Design / UI experiments | Image Banner |
| `Appraisal form` | Design / UI experiments | General Performance Evaluation Form |
| `Arrays` | Learning exercises | Python source |
| `Balcony exterior design` | Web development | Balcony Exterior Design |
| `Birthday Card` | Design / UI experiments | Parcel Sandbox |
| `Biscuits` | Design / UI experiments | Static Template |
| `Bistro preorder form` | Design / UI experiments | Hotel Bistro Pre-Order Form |
| `Blog` | Interactive / JavaScript | React Blog App |
| `Book` | Interactive / JavaScript | Welcome to Library |
| `Brand Protection` | Web development | dotNice Solutions - Brand Protection |
| `Bus Booking System` | Web development | Bus Booking System |
| `Cake box` | Design / UI experiments | 3D Cake |
| `Cake recipes` | Web development | Fresh and Delicious Bakery |
| `Candid photography` | Node.js / backend experiments | Candid Photography |
| `Cardboard kids activity` | Interactive / JavaScript | Nature Kids Activity |
| `Cardrive` | Interactive / JavaScript | Advanced Car Game |
| `Chart toppers` | Interactive / JavaScript | Pop Chart-Toppers Word Search |
| `Charts` | Design / UI experiments | 9 Charts Dashboard |
| `Charts dashboard` | Design / UI experiments | Charts Dashboard |
| `Chess` | Node.js / backend experiments | Chess Board |
| `Chikoo Kheer` | Design / UI experiments | Kheer Recipe |
| `Chocolate bouque` | Node.js / backend experiments | Chocolate Bouquet |
| `Christmas letter` | Design / UI experiments | Christmas Letter |
| `Company IT Prediction analysis` | AI / ML and data analysis | Python source |
| `Consumer Information Sheet` | Design / UI experiments | Consumer Information Sheet |
| `Crossword puzzle` | Interactive / JavaScript | Crossword Puzzle with Answers |
| `Cruise Travel Website` | Web development | Cruise Paradise |
| `Cycle Marathon` | Node.js / backend experiments | Cycle Marathon |
| `Dessert` | Web development | Dessert World |
| `Diabetes Prediction` | Interactive / JavaScript | Diabetes Prediction System |
| `Diary` | Node.js / backend experiments | Moment & Diary |
| `Digital Sorry` | Design / UI experiments | Digital Sorry |
| `Digital net solutions` | Web development | Digital Net Solutions |
| `Dragonfruit halwa` | Design / UI experiments | Dragon Fruit Halwa Recipe |
| `Drug addiction Analysis` | AI / ML and data analysis | Python source |
| `Eggless rosemilk cake` | Design / UI experiments | Eggless Rose Milk Cake |
| `Email news letter` | Design / UI experiments | Newsletter Subscription |
| `Environmental prediction` | AI / ML and data analysis | Python source |
| `Family Budget` | Node.js / backend experiments | Monthly Family Budget |
| `Farm Game` | Interactive / JavaScript | 🌾 Farm Game |
| `Farmland` | Node.js / backend experiments | Farm House |
| `Feelings Chart` | Node.js / backend experiments | Feelings Chart |
| `Flight booking` | Node.js / backend experiments | Flight Booking UI |
| `Flower box` | Interactive / JavaScript | FlowerBox React App |
| `Freedom fighters` | Design / UI experiments | Freedom Fighters Tribute |
| `Friend` | Node.js / backend experiments | Refer a Friend Form |
| `Friends` | Interactive / JavaScript | Friends Social Network |
| `Gen AI` | Interactive / JavaScript | Gen AI Chatbot |
| `Goal Planning Worksheet` | Design / UI experiments | Goal Setting Worksheet |
| `Google Maps` | Web development | Google Maps JavaScript API |
| `Gratitude letter` | Design / UI experiments | Thank You Letter |
| `Holland Farm` | Design / UI experiments | Deli Delights Menu |
| `Homepage` | Web development | Static Template |
| `Icecream parlour` | Web development | Code/export or image artifact; see source |
| `Instagram Login Page` | Web development | Advanced Instagram Clone |
| `Interview Board` | Interactive / JavaScript | Interview Board |
| `Jewellery Website` | Web development | Jewellery Website Landing Page |
| `Job Application` | Design / UI experiments | Application for Employment |
| `Kinderjoy website` | Web development | Kinder Joy Website |
| `Letter box` | Node.js / backend experiments | Letter Box |
| `Light toggle` | Interactive / JavaScript | Light Toggle |
| `Lotus  Biscoff Cheese Cake` | Design / UI experiments | Lotus Biscoff Cheesecake Recipe |
| `Love letter` | Design / UI experiments | React Love Letter |
| `Madhampatti` | Web development | Madhampatty Pakashala |
| `Madhampatti rangaraj Groups` | Web development | Madhampatty Foods |
| `Maravallikilangu parotta` | Design / UI experiments | Maravalli Kilangu Parotta Recipe |
| `Marketing Website` | Web development | LinkedIn Post Mockup |
| `Marriage Certificate` | Design / UI experiments | Marriage Certificate |
| `Masala milk` | Design / UI experiments | Masala Milk Recipe |
| `Matrix` | Learning exercises | Code/export or image artifact; see source |
| `Meet` | Interactive / JavaScript | Meet App |
| `Milk AI Detector` | Interactive / JavaScript | AI Milk Adulteration Detector |
| `Movie Review` | Web development | Static Template |
| `Multiplication chart` | Learning exercises | Multiplication Chart |
| `Office tour` | Web development | Office Tour Booking |
| `Oil gas` | Interactive / JavaScript | Oil & Gas Leakage Prediction |
| `Onam` | Web development | Onasadya 2026 |
| `Party Plan` | Interactive / JavaScript | Party Planner |
| `Pininterest` | Node.js / backend experiments | Pinterest Clone |
| `Platinum Ring` | Web development | Golden Ring Collection |
| `Portfolio` | Web development | Modern Portfolio |
| `Post office Savings bank` | Design / UI experiments | Post Office Savings Bank Form |
| `Project Chart` | Interactive / JavaScript | Full Dashboard |
| `Psychological website` | Web development | MindCare Psychology |
| `Sample Questions` | Node.js / backend experiments | Teacher Interview Questions |
| `School Contacts` | Web development | School Contact Initiative |
| `School Work Chart` | Design / UI experiments | Weekly Homework Chart |
| `Sentence card` | Design / UI experiments | Sentence Card |
| `Sight words` | Learning exercises | Sight Words |
| `Sir form` | Design / UI experiments | Duplicate Elector's Photo Identity Card Application |
| `Smoothie app` | Interactive / JavaScript | Advanced Smoothie Maker |
| `Solar ads` | Design / UI experiments | Solar Paradigm - Anniversary Sale; Solar Paradigm - Anniversary Sale |
| `Sponshorship form` | Design / UI experiments | Sponsorship Form |
| `Sports Sponshorship form` | Node.js / backend experiments | Sports Team Sponsorship Form |
| `Spotify  Clone UI` | Web development | Spotify Clone; Spotify - Web Player |
| `Story` | Interactive / JavaScript | Audio Story Book |
| `Suicide prediction analysis` | AI / ML and data analysis | Code/export or image artifact; see source |
| `Sweet offer` | Node.js / backend experiments | Swiggy Banner |
| `Tango` | Node.js / backend experiments | Tango Dance Studio |
| `Time Bomb` | Interactive / JavaScript | React Time Bomb |
| `Toast` | Node.js / backend experiments | Avocado Toast |
| `Tomato Ketchup` | Node.js / backend experiments | Homemade Tomato Ketchup |
| `Trophy` | Interactive / JavaScript | Golden Trophy Animation |
| `Vetribuilders website` | Web development | Vetri Builders |
| `Whatsapp call` | Node.js / backend experiments | WhatsApp Call UI |
| `Wishlist` | Web development | Wishlist |
| `Women's Day` | Design / UI experiments | Women's Day |
| `Youtube UI` | Web development | YouTube Clone UI |
| `calendar` | Node.js / backend experiments | Code/export or image artifact; see source |
| `ola` | Node.js / backend experiments | OLA Scooter |
| `reception gift` | Web development | Wooden Gift Box |
| `rock paper scissors` | Interactive / JavaScript | Rock Paper Scissors |
| `signals` | Interactive / JavaScript | Signal Clone Enhanced |
| `testbook` | Interactive / JavaScript | Testbook Coupon System |
| `timetable` | Node.js / backend experiments | College Schedule |

## Audit completion / safe implementation boundary

Audit complete before code edits. Next steps: write the README/index; move only verified unreferenced root artifacts and obsolete course automation; document five featured projects; repair featured-project bugs and Flask upload/inference setup; add tests, security notes and a future-only roadmap. Historical weaknesses outside featured projects remain documented rather than broadly rewritten.
