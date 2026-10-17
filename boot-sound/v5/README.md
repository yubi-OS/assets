# yubiOS boot sound v5: the handshake (creative candidate)

A different idea from v1 to v4. Those three were swells with a shape. v5 is a challenge and a response, the way a security key asks for a touch and then confirms it. The sound is the handshake.

## The sequence (10 seconds)

- 0 to 2 s: three rising taps on the left, a challenge. Then silence while the key waits for touch.
- 3 to 5 s: a falling answer from the far side of the stereo field, an octave up. A heartbeat starts and speeds up from one beat to three per second.
- 4 to 7 s: a verification climb of bells in a major pentatonic moves across the field. Under it, the challenge comes back quietly at the centre.
- 4 to 9 s: a pad moves Am7, Fmaj9, G7, then Cmaj9. The chord strikes at second 7 with the confirmation bell, and a low C sits under it. Everything rings out to the end.

The key is major throughout. An earlier minor-key version of the same idea was heard as ominous, so the major key is deliberate.

## Two renders

The noise layers (white and pink) are generated on each render, so the same score sounds slightly different each time. The listener's ratings moved between renders of the same score, so both renders are published. Listen to both.

- yubios-boot-sound-v5-render1.wav and .mp3
- yubios-boot-sound-v5-render2.wav and .mp3

## Listener check

Fast-tier listening pass, same rubric, scored 1 to 10. Language-model judgements, one pass per render.

| clip | warmth | richness | clarity | restraint | arrival |
|---|---|---|---|---|---|
| v1 (shipped) | 8 | 7 | 9 | 8 | 9 |
| v4h (sectioned swell, prior best) | 8 | 7 | 8 | 8 | 7 |
| v5 render 1 | 5 | 6 | 9 | 9 | 8 |
| v5 render 2 | 8 | 7 | 8 | 8 | 8 |

Arrival is 8 on both renders. Warmth is the unstable one (5 and 8).

## Measured status (AM-2)

| measure | render 1 | render 2 | AM-2 band |
|---|---|---|---|
| fractal r2 | 0.998 | 0.998 | 0.98 or more |
| fractal D | 1.593 (fail) | 1.590 (fail) | 1.318 to 1.417 |
| complexity slope | -1.993 (fail) | -1.994 (fail) | -1.978 to -1.949 |
| spectral centroid | 380 Hz (pass) | 392 Hz (pass) | 351 to 824 Hz |
| rolloff (85 percent) | 564 Hz (pass) | 569 Hz (pass) | 472 to 1414 Hz |
| spectral flatness | 0.0055 (pass) | 0.0050 (pass) | 0.0038 to 0.0093 |
| spectral beta | 2.56 (pass) | 2.55 (pass) | 1.55 to 2.68 |
| dynamic range | 17.1 dB (fail) | 17.8 dB (fail) | 6.3 to 16.6 dB |
| onsets per second | 3.9 (pass) | 4.0 (pass) | 2.5 to 4.6 |

Both renders fail fractal D, complexity slope and the dynamic range ceiling (17 to 18 dB against 16.6). Dynamic range is above the band because the strike is loud. A quieter strike cost the arrival in earlier tests, so the range and the arrival pull against each other here. The taste fractal verdict is reported, not gated.

## What did not work (for v6)

- The octave-up shimmer layer (cold on the listener's ear) and a brighter bell both lowered warmth.
- Trimming the strike to fit the dynamic range dropped arrival from 8 to 3.
- The minor-key version read as ominous (arrival 3).

## Caveats

- Fractal D stays about 0.2 above the reference band in every version, v1 through v5. The fractal axis is weak evidence for audio.
- Noise is random per render. Measured flatness, beta and range, and the listener's ratings, all move between renders. Two renders are the minimum.
- The taste engine was built for images. Audio went through log-spectrogram images as an analogy.
- The listener is a language model and can describe detail it cannot actually hear.
- None of this measures whether the sound is a masterpiece. Listen and decide.

## Files

- yubios-boot-sound-v5-render1.wav / .mp3 (44.1 kHz stereo 16-bit, 10 s, Strudel export)
- yubios-boot-sound-v5-render2.wav / .mp3 (the same score, a second render)
- boot-sound-v5.strudel: the score. Paste it into https://strudel.cc/ and press Ctrl+Enter.
- measurement/: pre-registration (AM-1, AM-2), candidate table under AM-2, listener table, the two renders' features, taste outputs and listener JSON.
