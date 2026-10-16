# yubiOS boot sound v2 (candidate)

Second iteration of the "Trust Chain" boot sound. v1 stays in the parent folder. This one is a candidate, not a finished sound. The gold-set agreement it was held to has not been reached. Details below.

## What changed from v1

- Lower and warmer. The v1 ladder ran up into a bright bell register. v2 sits in the C3 to C4 range, with a darker filter on the pad and the bells.
- Jazz voicings. The pad moves through minor-9, major-7, minor-9 and dominant chords, then resolves to a major 9 in the last second.
- A quiet noise bed. A low white floor and a pink layer swell with the pad, so the sound has some air instead of pure oscillator sheen.
- Same structure as v1: a low sine hum, a two-per-second pentatonic ladder, a sawtooth pad, and the confirmation bell at 6 s.

## Inspiration

Two tracks from the radio playlists, as 40 s clips: Nujabes, "Feather" (lo-fi, jazz-hop) and Jacob Collier, "In The Real Early Morning" (orchestral). Only these two could be pulled. YouTube blocked the other five radio tracks from both analysis hosts.

## Measured status

Measured against bands fixed before any candidate was measured (measurement/PREREG.md). Ten candidates (v2a to v2j) were tested. The best one, the file in this folder, passes 7 of 10 gated bands:

| band | value | pass band | result |
|---|---|---|---|
| fractal D (edge-standard) | 1.510 | 1.28 to 1.40 | fail |
| fractal r2 | 0.996 | 0.98 or more | pass |
| complexity slope | -2.02 | -2.05 to -1.94 | pass |
| spectral centroid | 433 Hz | 330 to 460 Hz | pass |
| rolloff (85 percent) | 706 Hz | 480 to 660 Hz | fail |
| spectral flatness | 0.0029 | 0.002 to 0.010 | pass |
| spectral beta (1/f exponent) | 2.91 | 2.0 to 3.9 | pass |
| dynamic range | 4.7 dB | 4 to 35 dB | pass |
| onsets per second | 3.9 | 1.5 to 6.0 | pass |
| taste fractal verdict | off | on | fail |

Not reached: the fractal D band and the rolloff band. The fractal verdict fails for the same reason as D. The full candidate table is in measurement/candidate_gate_summary.md.

## Listener check

Fast-tier listening pass, same rubric on every clip, scored 1 to 10. These are language-model judgements.

| clip | warmth | richness | clarity | restraint | arrival |
|---|---|---|---|---|---|
| v1 (shipped) | 8 | 7 | 9 | 8 | 9 |
| v2 (this folder) | 8 | 7 | 8 | 8 | 8 |
| Nujabes, Feather (reference) | 8.5 | 7 | 6.5 | 8 | not rated |
| Collier, Early Morning (reference) | 9 | 6 | 8 | 9 | 4 |

On this pass v2 matches v1 on warmth, richness and restraint, and sits one point lower on clarity and arrival.

## Caveats

- The taste engine was built for images. Audio went through log-spectrogram images as an analogy. The fractal axis does not separate a pure 440 Hz sine (D 1.45) from the references, so it is weak evidence for audio.
- The gold set is two clips. Time-matched 10 s windows of those clips put fractal D at 1.31 to 1.36 for Nujabes and 1.39 to 1.47 for Collier. The D band is therefore itself uncertain (measurement/PREREG.md, sensitivity note).
- The renderer is Strudel 1.3.0's own offline export. It reproduces the v1 shape (correlation 0.84 to 0.86 per channel) but not sample for sample, and it runs about 2 dB hotter than the shipped v1 WAV.
- The listener is a language model. It can describe detail it cannot actually hear.
- None of this measures whether the sound is a masterpiece. Listen to it and decide.

## Files

- yubios-boot-sound-v2.wav: 44.1 kHz stereo 16-bit, 10.0 s (Strudel export)
- yubios-boot-sound-v2.mp3: 320 kbps
- boot-sound-v2.strudel: the score. Paste it into https://strudel.cc/ and press Ctrl+Enter.
- measurement/: pre-registration, candidate gate summary, gate for this candidate, features for the references, controls, v1 and v2, taste scorer outputs, taste matrix run, and listener notes.
