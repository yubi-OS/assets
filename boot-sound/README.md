# yubiOS Boot Sound — "Trust Chain"

The yubiOS boot sound, composed in Strudel (strudel.cc) and rendered with
strudel's own offline renderer (`renderPatternAudio`, OfflineAudioContext,
44100 Hz stereo, 10.0 s).

## Inspiration

Two videos of the OS startup-sound lineage:

- [Evolution of All Windows Startup and Shutdown Sounds (1993-2021)](https://www.youtube.com/watch?v=reJbTyqa30Q)
  — the harmonic swell that resolves into a stable, warm chord.
- [All Ubuntu Startup & Shutdown Sounds](https://www.youtube.com/watch?v=VNnSTli4oSQ)
  — the humanist chime character and the soft confirmation bell.

yubiOS maps that lineage onto its own identity: a FIDO2-first boot chain
where every layer is verified before it runs. The sound is that chain.

## Structure (8 s boot + 2 s tail)

| Time | Layer | Boot stage |
|---|---|---|
| 0-8 s | low sine hum (c2, slow attack) | power on |
| 0-8 s | 8 ascending pentatonic bells (triangle, one per second) | verification ladder: firmware → kernel → initrd → rootfs → services → user |
| 0-8 s | warm sawtooth pad, low-pass filter opening 900→3600 Hz | trust established |
| 6 s | single bell (g5) with 3 s release + long reverb | root of trust confirmed |

## Files

- `yubios-boot-sound.wav` — the render (44100 Hz, stereo, 16-bit PCM, 10.0 s, peak 0.58, no clipping)
- `yubios-boot-sound.mp3` — convenience encode (320 kbps)
- `boot-sound.strudel` — the canonical score; paste into https://strudel.cc/ and press Ctrl+Enter to hear it live

## Provenance

- Composed with the `strudel-live-coding` skill against the strudel corpus in
  yubi-OS/knowledge (`knowledge/strudel/`): Mini-Notation, `$:` stacks,
  patterned `lpf`, signals-era envelope + `room` conventions all follow the
  official workshop.
- Rendered from the score with @strudel/web 1.3.0's offline renderer in a
  headless browser; the WAV is the score, not a hand approximation.
- All oscillators (sine / triangle / sawtooth): no samples, fully
  reproducible offline.

## Verification

- Duration 10.00 s, 2ch, 44100 Hz, 16-bit PCM
- Per-second RMS 0.09-0.15 (gentle build, peak at the pad open, quiet tail)
- Dominant frequency climbs ~281 Hz → ~1328 Hz across the ladder (verified by
  zero-crossing analysis per second)
