# yubiOS boot sound v4 (candidate)

Fourth iteration of the "Trust Chain" boot sound. v1, v2 and v3 stay in their folders. This is a candidate. It passes 6 of 9 gated bands under the expanded reference envelope (AM-2). The misses are listed below.

## What changed from v3

v3 rose in one even curve. v4 is built in sections, and the sections are what make it feel dynamic:

- A sparse opening: a low hum, a quiet noise floor, and one bell per second.
- A build: the pad opens its filter from 340 Hz to 1600 Hz, the bells get louder and brighter, and an accent layer adds weight on the root and fifth.
- A breath in the sixth second: the pad, bells, accents, kick and noise all drop out for one second.
- A cadence: a G7 chord, then Cmaj9 at full brightness, with a low C underneath and the confirmation bell on the last second.

## Measured status

AM-2 gate for v4h. measurement/candidate_table_am2.txt lists every candidate from v2i to v4h.

| quantity | v4h | AM-2 band | result |
|---|---|---|---|
| fractal D (edge-standard) | 1.584 | 1.318 to 1.417 | fail |
| fractal r2 | 0.999 | 0.98 or more | pass |
| complexity slope | -1.998 | -1.978 to -1.949 | fail |
| spectral centroid | 491 Hz | 351.2 to 823.7 | pass |
| rolloff (85 percent) | 770 Hz | 471.9 to 1414 | pass |
| spectral flatness | 0.0042 | 0.003781 to 0.009337 | pass |
| spectral beta (1/f exponent) | 2.87 | 1.553 to 2.677 | fail |
| dynamic range | 11.2 dB | 6.288 to 16.61 | pass |
| onsets per second | 3.4 | 2.53 to 4.57 | pass |

The taste fractal verdict is off here. The references disagree on it, so it is reported and not gated.

## Listener check

Fast-tier listening pass, same rubric on every clip, scored 1 to 10. These are language-model judgements from one pass each.

| clip | warmth | richness | clarity | restraint | arrival |
|---|---|---|---|---|---|
| v1 (shipped) | 8 | 7 | 9 | 8 | 9 |
| v2i | 8 | 7 | 8 | 8 | 8 |
| v3i | 8 | 6 | 7 | 8 | 5 |
| v4d (more swell, no breath) | 8 | 7 | 7 | 8 | 4 |
| v4g | 8 | 6 | 7 | 8 | 3 |
| v4h (this folder) | 8 | 7 | 8 | 8 | 7 |

The sectioned version (v4h) raised arrival from 4 to 7 and clarity to 8 over the continuous swell (v4d). Measured dynamic range is not the same as perceived dynamism: v4d measured 13.6 dB and scored lower on arrival.

## Caveats

- Fractal D sits about 0.2 above the reference band in every candidate, v1 through v4. Texture, vibrato, transient ticks, noise level and sectioning did not move it. The fractal axis is weak evidence for audio.
- Flatness and the complexity slope conflict through the white noise floor. Louder white raises flatness and makes the complexity slope more negative. v4h favours flatness.
- Beta is slightly over its ceiling.
- The taste engine was built for images. Audio went through log-spectrogram images as an analogy.
- The renderer is Strudel 1.3.0's own offline export. It reproduces the v1 shape, not sample for sample.
- The listener is a language model and can describe detail it cannot actually hear.
- None of this measures whether the sound is a masterpiece. Listen and decide.

## Files

- yubios-boot-sound-v4.wav: 44.1 kHz stereo 16-bit, 10.0 s (Strudel export)
- yubios-boot-sound-v4.mp3: 320 kbps
- boot-sound-v4.strudel: the score. Paste it into https://strudel.cc/ and press Ctrl+Enter.
- measurement/: pre-registration (AM-1 and AM-2), candidate table under AM-2, listener table, 17-window reference set and envelope, features, taste outputs, and gate and listener records for v4h.
