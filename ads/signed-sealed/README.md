# yubiOS — Signed, Sealed, Delivered: It's Yours

A full-page addition to the yubiOS brand kit. The campaign uses
title case and a colon, with **It's Yours** as the strongest visual statement.
The imagery extends the existing flower, layered owner-rings, blue-black,
hot-pink, violet, cyan, and sparse acid-lime visual language. The abstract glass
seal is campaign artwork, not a replacement logo or a certification mark.

## Finished compositions

| Placement | Dark | Light | Size |
|---|---|---|---|
| Full page / desktop hero | [PNG](png/yubios-signed-sealed-delivered-fullpage-dark-3840x2160.png) | [PNG](png/yubios-signed-sealed-delivered-fullpage-light-3840x2160.png) | 3840 × 2160, 16:9 |
| Full page / web | [WebP](webp/yubios-signed-sealed-delivered-fullpage-dark-1920x1080.webp) | [WebP](webp/yubios-signed-sealed-delivered-fullpage-light-1920x1080.webp) | 1920 × 1080 |

[Preview both layouts](preview.jpg).

The headline, logo, project URL, and status are baked into the PNG/WebP exports.
Use the supplied 16:9 aspect ratio; avoid cropping either edge or stretching
the image. For narrow screens use a proportional image instead of cropping
with `object-fit: cover`.

## Revised composition

The full-width variants have been removed. The full-page images now use a
clearly legible, tightly fitted **Technical Preview** badge and 30 px footer text in the
1920 × 1080 layout (60 px in the 4K exports). Footer text remains 15 px when
the whole image is displayed at 960 × 540. The previous status was 13 px and
the previous footer was 13–14 px at layout size.

The sphere is inset from the frame and optically centered against the headline
block, with consistent placement in both themes. A shared header/footer grid
keeps the logo, status, and project details aligned. The bottom light trail has
been removed to leave a clean, high-contrast footer area. Both themes were
visually reviewed, with an additional dark-image check at 960 × 540.

The status badge fits the measured label width with balanced 24 px side
padding. The footer reads **Open-source project**.

## Editable sources and rebuild

`source/` contains two self-contained SVG layouts with editable live text,
embedded background imagery, and the embedded canonical logo. The copied
`source/logo.png` is byte-identical to the repository's `logo.png`. The seal
foundations are separate under `source/foundations/`.

The built-in image generator produced the two text-free foundations at
1672 × 941. The layout renderer resamples these foundations for the 4K PNG
exports; they are not native-4K generated paintings. Typography is rendered
directly at the final export size. No generated lettering is used.

Requirements: Python 3, Pillow, Inkscape, and Nimbus Sans (URW Base35).
With those installed, run from this directory:

```sh
python3 source/render.py
```

This rebuilds the SVGs, PNGs, WebPs, and preview. SVG text remains editable;
install the named fonts to preserve line lengths when editing. The renderer
does not download dependencies or call image generation services. For future
edits, change `source/render.py`, since rerunning it recreates the SVGs.

## Brand use

- Keep the original yubiOS logo and the exact capitalization **yubiOS**.
- Tagline: **Signed, Sealed, Delivered: It's Yours**. Exports use a typographic
  apostrophe and layout line breaks, with no change in wording.
- Keep the **Technical Preview** status visible. This is the status supplied
  by the project owner for this revision.
- These images do not assert Yubico affiliation or endorsement.
- Use the dark version by default, with the light version for pale surfaces.

## Alt text

- **Full page, dark:** yubiOS flower logo and the words “Signed, Sealed,
  Delivered: It's Yours” beside a layered cyan, violet, and pink glass seal on
  a blue-black background. Marked Technical Preview.
- **Full page, light:** yubiOS flower logo and the same tagline beside a
  translucent opal, cyan, violet, and pink glass seal on a pale pearl
  background. Marked Technical Preview.

## Provenance

Created 2026-11-14, America/Los_Angeles, from the assets repository at commit
`527b5c4fe48bc65159e1e5f967d38c382fa6f78a`.
Brand references reviewed: `logo.png`, `new_logo/README.md`, `ads/README.md`,
`ads/source/v2/ad-landscape-1200x628.svg`, and the owner-rings light/dark
wallpapers. See [PROMPTS.md](source/PROMPTS.md) for generation instructions and
[SHA256SUMS](SHA256SUMS) for delivery integrity. Assets outside this campaign
directory are preserved.
