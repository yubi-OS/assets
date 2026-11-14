# Revised campaign foundation prompts

Mode: built-in image generation and image editing, followed by exact SVG typography and canonical-logo placement. The current delivery contains only the dark and light full-page layouts.

## Dark composition edit

Input: the previous dark seal foundation. Preserve its visual identity while correcting framing and removing the bottom light trail.

> Use case: precise-object-edit. Edit this yubiOS campaign foundation to correct composition. Keep the exact same jewel-like layered glass flower sphere, cyan rim, violet folds, hot-pink inner glow, fine etched textures and blue-black backdrop. Reframe the sphere SMALLER and better inset: for this 16:9 image, its full outer silhouette must fit within x=57% to 94%, y=20% to 84%, centered at x=75.5%, y=52%. This is crucial: generous deliberate right margin, no part near the right edge, no large sphere looming into header or footer. The seal should be vertically centered in the main body of a poster, balanced with a left headline occupying x=6%-45%, y=28%-75%. The left 54% stays quiet clean dark space for later typography. Remove the long cyan-magenta light filament across the bottom entirely; let the sphere float subtly above a small soft violet shadow, keep the bottom 12% and top 16% clean dark for readable branding and footer. Preserve the identity and visual quality of the sphere, not a redesigned symbol. No lettering, words, logos, badges, watermark or UI. One single full-bleed 16:9 landscape background.

Actual output: `foundations/seal-dark.png`, 1672 × 941 PNG. The SVG renderer uniformly reframes the generated foundation at x=-335, y=-146, width=2400, height=1350 in its 1920 × 1080 viewBox. This brings the visible sphere to approximately x=1090–1770 and y=200–870, with its center aligned against the headline block.

## Light companion edit

Inputs: revised dark foundation as composition target; previous light foundation as palette/material reference.

> Use case: lighting-weather. Make the light-mode companion of image 1, using image 2 only as the opal material/palette reference. PRESERVE IMAGE 1 COMPOSITION EXACTLY: same sphere location, same size, same silhouette, same internal ribbon arrangement and etched texture, same empty left area, same shadow location, same framing. The only changes are lighting and material: turn blue-black background into clean pale pearl with slight lavender tint, turn dark smoked glass into bright translucent opal glass with crisp cyan outer edges, violet folds, hot-pink inner core and sparse acid-lime glints. Keep the form substantial and detailed, not washed out. Preserve the clean top and bottom areas. No long light filament across bottom. No typography, labels, badges, logos or watermark. One full-bleed 16:9 landscape background.

Actual output: `foundations/seal-light.png`, 1672 × 941 PNG. Uses the same SVG framing as the dark version.

## Current layout

- Exact wording: `Signed, Sealed, Delivered: It's Yours`, using a typographic apostrophe in the artwork.
- Three introductory lines; a larger ownership line.
- Dark: off-white headline and hot-pink-to-cyan ownership gradient.
- Light: navy headline and magenta-to-indigo ownership gradient.
- Canonical logo embedded unchanged.
- Status: **Technical Preview**, in a compact 328 × 56 px badge with 24 px side padding, a 10 px dot, a 12 px gap, and a 30 px label at layout size.
- Footer: project URL and **Open-source project**, both 30 px at layout size.
- Footer separated from art by a clear rule and consistent margins.
- Full-width layouts removed at the project owner's request.

