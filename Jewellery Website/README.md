# Jewellery Store Frontend

**Status: prototype / credited design adaptation.** Historical folder: `Jewellery Website`.

## Purpose and authorship

A multi-section jewellery storefront layout used for frontend practice. The existing footer credits **Jak Ashuraliev**; that attribution is retained. This repository does not establish that Preetha authored the original design. Present it as a credited adaptation/study, and verify the original design and image licenses before reuse.

## Implemented features

- Product-category and designer-collection galleries.
- About and contact sections.
- Section scrolling, active navigation styling and a sticky navigation threshold.
- Basic contact form layout, explicitly marked as a demo with no message delivery.

The duplicated, unterminated JavaScript wrapper has been replaced with a single guarded navigation setup. External/nonexistent links are no longer treated as valid local scroll targets. Reduced-motion preferences are respected for the scrolling animation.

## Technologies and setup

HTML, CSS, JavaScript and jQuery 3.7.1 loaded from a CDN. Images and CSS backgrounds use third-party hosts.

From this directory:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000`. Internet access is required for jQuery and external images. No Node backend or npm install is needed.

## Screenshots

No verified project-local screenshot is committed. Open the local page for the current view; unrelated root screenshots have not been relabeled as this project's output.

## Limitations

- No catalog API, cart, inventory, checkout, payments, account or email delivery.
- Third-party image links may break or be blocked as mixed content on HTTPS; descriptive `alt` text is provided.
- Placeholder product/about copy remains.
- The historical desktop CSS needs further responsive and accessibility work.

## Future improvements

Use original/licensed local media, add mobile layouts and form labels, replace placeholders, and implement a validated backend only if turning this into a real store. Keep the credited learning version traceable.
