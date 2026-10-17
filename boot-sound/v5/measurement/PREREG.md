# Boot sound v2: pre-registration (written before any v2 measurement)

Date: 2026-10-16. Measured inputs so far: 2 gold references, v1, 3 negative controls (all in features/, taste/).

## Gold set (human-chosen radio inspirations, 40 s each, mono 22.05 kHz analysis)
- G1 Nujabes, "Feather" (radio playlist, lofi)
- G2 Jacob Collier, "In The Real Early Morning" (radio playlist, orchestral)
Limitation (stated up front): only 2 of the 7 intended radio tracks were obtainable. YouTube returned bot-gate 403s to both the sandbox and rock1 for the rest. A two-track gold set is thin; agreement with it is a measured match, not a verdict on quality.

## Negative controls (must NOT satisfy the gold agreement)
- C1 pure 440 Hz sine (10 s). C2 white noise (10 s). C3 random-pitch saw arpeggio (10 s).

## Audio-applicable taste axes (decided now, before v2)
- fractal_band: edge-standard-v1 on the 512x512 log-STFT spectrogram (gated).
- complexity_economy: caller slope from gzip structure of the spectrogram (gated on slope band; the worker verdict is reported, not gated, because the two gold refs disagree on it).
- symmetry_present: not applicable to a time-frequency image. Reported, never gated.
- scale_coherence: not reachable through the features path (clef returns 500 without the extractor). Excluded and stated.
- branch_exponent, sv_balance, family, symmetry_variation: not applicable to audio. Excluded.

## Gated bands (fixed now; gold min/max widened by a fixed absolute margin, not tuned)
| quantity | band | basis |
|---|---|---|
| fractal D (edge-standard) | 1.28 .. 1.40 | gold 1.331, 1.347, margin 0.05 |
| fractal r2 | >= 0.98 | instrument gate |
| fractal_band worker verdict | on | gold both on |
| complexity gzip slope | -2.05 .. -1.94 | gold -1.990, -1.997 |
| spectral centroid (Hz) | 330 .. 460 | gold 394, 393 |
| rolloff85 (Hz) | 480 .. 660 | gold 563, 581 |
| spectral flatness | 0.002 .. 0.010 | gold 0.005, 0.004 |
| spectral beta (1/f exponent) | 2.0 .. 3.9 | gold 2.43, 3.45 |
| dynamic range (dB) | 4 .. 35 | gold 4.4, 33.4 |
| onsets per second | 1.5 .. 6.0 | gold 4.95, 2.28 |

Reported, not gated: tempo proxy (meaningless on a 10 s drone), L/R stereo correlation, edge symmetry score.

## Listener gate (secondary, fast tier, same rubric on all clips)
Warmth >= 8 and restraint >= 8. Gold: warmth 8.5 / 9.0, restraint 8 / 9. Listener output is an LLM judgement and is reported as such.

## Agreement and stop rule
- AGREEMENT = all 10 gated bands pass (fractal r2, verdict included) AND listener warmth >= 8 AND restraint >= 8.
- Validity check (instrument, not candidate): report how many gated bands each negative control passes. A control passing every gated band would mean the instrument cannot discriminate, which is flagged.
- Max 6 iterations (v2 .. v7). Stop early on AGREEMENT. If not reached, stop and report the failing bands and whether the failure is the candidate or the instrument.
- A band is never moved after a candidate is measured. A failed band is reported as a failure.
- The gold agreement does not decide "masterpiece". Jenny's ear does.

## Amendment AM-1 (logged 2026-10-16 15:12 PT, before v2f was measured)
- Reason: Jenny's instruction "dont stop till the gold set agrees". The six-candidate cap is raised to ten (v2a..v2j).
- No band, control, listener threshold or stop condition is changed.
- Each candidate is still measured under the same fixed bands. Candidates are reported individually, including the failures.

## Sensitivity check (post-hoc, reported only, NOT used for any gate)
Gold clips re-measured in matched 10 s windows (0, 10, 20, 30 s; files features/gw_*.json, taste/es_gw_*.json). Results: Nujabes windows D 1.31-1.36 (inside the pre-registered band), Collier windows D 1.39-1.47 (partly outside it). Collier dynamic range in 10 s windows is 22-37 dB, far above the 10 s candidates (4-5 dB). The 40 s-based bands therefore fit the Nujabes reference better than the Collier one. This does not change the gate result, and it is reported as a limitation.

## Amendment AM-2 (logged 2026-10-16 16:09 PT, before any v3 candidate was scored against it)
- Reason: the 2-clip gold set was narrow. Nine further radio references (SAMPLMAN x7, Idealism, Tom Misch) were measured in matched 10 s windows, giving 17 references in total (Nujabes x4, Collier x4, SAMPLMAN x7, Idealism x1, Tom Misch x1). The min-to-max envelope was too loose to discriminate (SAMPLMAN spans centroid 183 to 1131 Hz), so it was not used.
- New rule: gated band per quantity = [P25 - 0.10*IQR, P75 + 0.10*IQR] over the 17 references. Pre-registered here, before scoring v3 candidates against it.
- Fractal verdict is NOT gated: the references disagree on it (on 6, off 3, not recorded for the 8 Collier and Nujabes windows).
- Earlier candidates (v2a to v2j, v3a to v3d) were scored under AM-0/AM-1 bands before AM-2 existed. They are re-scored here under AM-2 and reported both ways.

| quantity | P25 | median | P75 | AM-2 band |
|---|---|---|---|---|
| D | 1.3261 | 1.3843 | 1.4084 | [1.3179, 1.4166] |
| comp | -1.9753 | -1.9679 | -1.9512 | [-1.9777, -1.9488] |
| centroid | 390.5287 | 485.3628 | 784.2883 | [351.1528, 823.6643] |
| rolloff | 550.4078 | 735.4572 | 1335.3612 | [471.9125, 1413.8565] |
| flat | 0.0042 | 0.0050 | 0.0089 | [0.0038, 0.0093] |
| beta | 1.6465 | 2.4075 | 2.5836 | [1.5528, 2.6773] |
| dyn | 7.1487 | 8.7543 | 15.7542 | [6.2882, 16.6147] |
| ons | 2.7000 | 3.2000 | 4.4000 | [2.5300, 4.5700] |
