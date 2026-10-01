# yubiOS Browser App-Open Sound — "Open Window"

The sound played when the yubiOS browser (provenance-gated Chromium) opens a
window. Companion to the boot sound [boot-sound/](../boot-sound/): the same
trust-chain motif (ascending bells on C major pentatonic) compressed into a
one-shot UI gesture.

## Files

- `yubios-browser-open-24b-192k.wav` — hi-res master (192000 Hz, stereo, 24-bit PCM, 4.0 s, peak 0.420, TPDF-dithered from the float32 render)
- `yubios-browser-open.wav` — compatibility render (44100 Hz, stereo, 16-bit PCM, 4.0 s)
- `yubios-browser-open.mp3` — convenience encode (320 kbps, from the hi-res master)
- `browser-open.strudel` — the canonical score; paste into https://strudel.cc/ and press Ctrl+Enter to hear it live

## Structure

| Time | Layer | Meaning |
|---|---|---|
| 0.0 s | C5 bell (triangle) + soft c3 sine landing | window opens |
| 0.5 s | G5 bell (triangle) | chain continues |
| 1.0 s | G6 sparkle (triangle, 1.2 s release + long reverb) | page ready |
| 1.5-2.7 s | decay to silence | one-shot, no loop |

Effective content is ~1.0 s; the tail rings out to ~2.7 s. Quiet by design:
UI sounds sit under other audio, peak 0.42.

## Provenance

- Composed with the `strudel-live-coding` skill against the strudel corpus in
  yubi-OS/knowledge (`knowledge/strudel/`); same conventions as the boot
  sound (`setcpm`, `$:` stacks, one-shot `/8` spans, `room` reverb, ADSR).
- Rendered at full float32 precision via an OfflineAudioContext at 192 kHz
  (strudel's built-in WAV export is 16-bit; the 24-bit master was encoded
  from the raw rendered AudioBuffer with TPDF dither).
- All oscillators (triangle / sine): no samples, fully reproducible offline.

## Verification

- 4.000 s, 2ch, 192000 Hz, 24-bit PCM (master) / 16-bit PCM (compat)
- One-shot verified: 100 ms-window RMS peaks within the first 1.6 s
  (max 0.152), decays monotonically to 0.000 by 2.8 s, no loop restarts
- Peak 0.420, no clipping
