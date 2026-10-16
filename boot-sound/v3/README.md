# yubiOS boot sound v3 (candidate)

Third iteration of the "Trust Chain" boot sound. v1 and v2 stay in their folders. This is a candidate. It passes 7 of 9 gated bands under the expanded reference envelope (AM-2). It does not pass all of them, so it is not a finished sound.

## What changed from v2

- Wider dynamic swell. The pad and bells rise from a quiet start to a full arrival, so the measured dynamic range sits inside the reference envelope.
- A mid-level white floor, high-passed at 400 Hz, for flatness and a flatter spectral slope.
- A heavier pink layer, which brings the complexity slope closer to the references.
- The same structure as v1 and v2: a low sine hum, a two-per-second pentatonic ladder, a jazz-minor pad, and the confirmation bell at 6 s.

## Inspiration: 9 new references from the radio playlists

Ten-second excerpts, mono, from SAMPLMAN - Topic (seven tracks: "Soul.Drips/BrightRooms", "ITS A BEAUTIFUL DAY FOR A DAY SEVN", "FIVE", "SEETHROUGH.6", "Drifting Ughway", "Air Doom Peace", "Some Keys") plus Idealism "Both Of Us" and Tom Misch "It Runs Through Me". One SAMPLMAN track (ELVN) was blocked by YouTube and is not included. The earlier references (Nujabes "Feather", Jacob Collier "In The Real Early Morning") are in measurement/.

## Measured status

Measured against the bands in measurement/PREREG.md, amendment AM-2: the interquartile range of 17 time-matched 10 s references, widened by 10 percent. v3i results (measurement/candidate_table_am2.txt has every candidate):

| quantity | v3i | AM-2 band | result |
|---|---|---|---|
| fractal D (edge-standard) | 1.531 | 1.318 to 1.417 | fail |
| fractal r2 | 0.996 | 0.98 or more | pass |
| complexity slope | -2.023 | -1.978 to -1.949 | fail |
| spectral centroid | 449 Hz | 351 to 824 Hz | pass |
| rolloff (85 percent) | 798 Hz | 472 to 1414 Hz | pass |
| spectral flatness | 0.0080 | 0.0038 to 0.0093 | pass |
| spectral beta | 2.61 | 1.55 to 2.68 | pass |
| dynamic range | 8.9 dB | 6.3 to 16.6 dB | pass |
| onsets per second | 3.9 | 2.5 to 4.6 | pass |

The taste fractal verdict is off here. The references disagree on it (on 6, off 3), so it is reported and not gated.

## Listener check

Fast-tier listening pass, same rubric on every clip, scored 1 to 10. These are language-model judgements.

| clip | warmth | richness | clarity | restraint | arrival |
|---|---|---|---|---|---|
| v1 (shipped) | 8 | 7 | 9 | 8 | 9 |
| v2i | 8 | 7 | 8 | 8 | 8 |
| v3i (this folder) | 8 | 6 | 7 | 8 | 5 |

The listener finds v3 warmer and more floating than v2 and v1. It also hears the last note as suspended, not resolved, and rates arrival 5 against 8 and 9 before. That is a regression on arrival, and it is the first thing to fix in a v4.

## Caveats

- Fractal D still sits 0.1 to 0.2 above the references in every candidate, v1 through v3. Texture changes, vibrato, transient ticks and noise level did not move it. The fractal axis is weak evidence for audio.
- The taste engine was built for images. Audio went through log-spectrogram images as an analogy.
- The renderer is Strudel 1.3.0's own offline export. It reproduces the v1 shape (correlation 0.84 to 0.86 per channel) but not sample for sample.
- The listener is a language model and can describe detail it cannot actually hear.
- None of this measures whether the sound is a masterpiece. Listen and decide.

## Files

- yubios-boot-sound-v3.wav: 44.1 kHz stereo 16-bit, 10.0 s (Strudel export)
- yubios-boot-sound-v3.mp3: 320 kbps
- boot-sound-v3.strudel: the score. Paste it into https://strudel.cc/ and press Ctrl+Enter.
- measurement/: pre-registration (PREREG.md with AM-1 and AM-2), candidate table under AM-2, 17-window reference set and envelope, features, taste outputs, gate and listener notes for v3i, and features for the nine new references.
