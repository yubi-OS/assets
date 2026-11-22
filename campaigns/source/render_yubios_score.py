#!/usr/bin/env python3
"""
Synthesizes the custom yubiOS campaign score (90.0s hero + 25.0s square cut)
from the yubiOS 'Owner Orbit & Handshake' Strudel harmonic progression (Am9 -> Fmaj9 -> G13 -> Cmaj9
/ Dm9 -> Em7 -> Fmaj7#11 -> G13) tuned to the AM-2 warm spectral envelope.
Uses numpy (if available) or pure stdlib math/array/wave for fast stereo 44.1 kHz synthesis.
"""
import math
import random
import subprocess
import wave
from array import array
from pathlib import Path

SR = 44100

def midi_to_freq(m: float) -> float:
    return 440.0 * (2.0 ** ((m - 69.0) / 12.0))

# Chords as MIDI notes: (bass_midi, [chord_voicing_midis], [arp_pentatonic_midis])
PROGRESSION = [
    # Bar 1: Am9 (A1, E3 G3 B3 C4 E4)
    (45, [64, 67, 71, 72, 76], [72, 74, 76, 79, 81, 84, 81, 79]),
    # Bar 2: Fmaj9 (F1, C3 E3 G3 A3 E4)
    (41, [60, 64, 67, 69, 76], [69, 72, 74, 76, 79, 81, 79, 76]),
    # Bar 3: G13sus4 (G1, D3 F3 A3 B3 E4)
    (43, [62, 65, 69, 71, 76], [71, 74, 76, 79, 81, 83, 79, 74]),
    # Bar 4: Cmaj9 (C2, E3 G3 B3 D4 G4)
    (48, [64, 67, 71, 74, 79], [72, 76, 79, 83, 86, 83, 79, 76]),
    # Bar 5: Dm9 (D1, A2 C3 E3 F3 A3)
    (38, [57, 60, 64, 65, 69], [74, 76, 79, 81, 84, 86, 81, 76]),
    # Bar 6: Em7 (E1, B2 D3 G3 B3 D4)
    (40, [59, 62, 67, 71, 74], [71, 74, 76, 79, 83, 79, 76, 74]),
    # Bar 7: Fmaj7#11 (F1, C3 E3 A3 B3 E4)
    (41, [60, 64, 69, 71, 76], [72, 76, 79, 81, 83, 84, 81, 76]),
    # Bar 8: G13 -> Cmaj9 turnaround (G1, D3 F3 A3 B3 D4)
    (43, [62, 65, 69, 71, 74], [74, 76, 79, 81, 84, 86, 88, 84]),
]

def render_score(duration_sec: float, out_wav: Path, out_mp3: Path, breath_windows):
    n_samples = int(duration_sec * SR)
    left = [0.0] * n_samples
    right = [0.0] * n_samples

    rng = random.Random(20261122)
    bar_dur = 2.5  # 96 BPM -> 1 bar = 2.5s, 1 beat = 0.625s, 8th = 0.3125s
    beat_dur = bar_dur / 4.0
    eighth_dur = bar_dur / 8.0
    sixteenth_dur = bar_dur / 16.0

    def in_breath(t: float) -> bool:
        for b0, b1 in breath_windows:
            if b0 <= t <= b1:
                return True
        return False

    def add_rhodes_chord(start_t: float, dur: float, midis, energy: float):
        s0 = int(start_t * SR)
        s1 = min(n_samples, int((start_t + dur + 1.2) * SR))
        freqs = [midi_to_freq(m) for m in midis]
        pan_phase = start_t * 0.7
        for i in range(s0, s1):
            dt = (i - s0) / SR
            # Warm ADSR envelope
            if dt < 0.035:
                env = dt / 0.035
            else:
                env = math.exp(-1.15 * (dt - 0.035))
            # Tine bell transient (decays fast)
            tine_env = math.exp(-14.0 * dt)
            val_l = 0.0
            val_r = 0.0
            for idx, f in enumerate(freqs):
                pan = 0.3 + 0.4 * (idx / max(1, len(freqs) - 1)) + 0.08 * math.sin(2.0 * math.pi * 1.5 * dt + pan_phase)
                # Warm fundamental + soft 2nd harmonic + gentle 4th tine
                sig = (
                    0.78 * math.sin(2.0 * math.pi * f * dt)
                    + 0.18 * math.sin(2.0 * math.pi * (2.0 * f) * dt + 0.3)
                    + 0.05 * tine_env * math.sin(2.0 * math.pi * (4.0 * f) * dt)
                )
                val_l += sig * (1.0 - pan)
                val_r += sig * pan
            scale = 0.085 * energy * env
            left[i] += val_l * scale
            right[i] += val_r * scale

    def add_sub_bass(start_t: float, dur: float, midi_note: float, amp: float):
        s0 = int(start_t * SR)
        s1 = min(n_samples, int((start_t + dur + 0.15) * SR))
        f = midi_to_freq(midi_note)
        for i in range(s0, s1):
            dt = (i - s0) / SR
            if dt < 0.015:
                env = dt / 0.015
            elif dt < dur:
                env = math.exp(-1.8 * (dt - 0.015))
            else:
                env = math.exp(-1.8 * (dur - 0.015)) * math.exp(-12.0 * (dt - dur))
            # Pure warm sub + subtle 2nd harmonic saturation
            sig = (0.82 * math.sin(2.0 * math.pi * f * dt) + 0.18 * math.sin(2.0 * math.pi * 2.0 * f * dt)) * env * amp
            left[i] += sig
            right[i] += sig

    def add_pentatonic_bell(start_t: float, midi_note: float, pan: float, amp: float):
        s0 = int(start_t * SR)
        s1 = min(n_samples, int((start_t + 0.95) * SR))
        f = midi_to_freq(midi_note)
        for i in range(s0, s1):
            dt = (i - s0) / SR
            env = (dt / 0.006) if dt < 0.006 else math.exp(-4.2 * (dt - 0.006))
            # Triangle-like warm bell (fundamental + 1/9 3rd harmonic)
            sig = (0.90 * math.sin(2.0 * math.pi * f * dt) - 0.10 * math.sin(2.0 * math.pi * 3.0 * f * dt)) * env * amp
            left[i] += sig * (1.0 - pan)
            right[i] += sig * pan

    def add_soft_kick(start_t: float, amp: float):
        s0 = int(start_t * SR)
        s1 = min(n_samples, int((start_t + 0.22) * SR))
        phase = 0.0
        for i in range(s0, s1):
            dt = (i - s0) / SR
            # Pitch envelope: 118 Hz dropping smoothly to 48 Hz
            f = 48.0 + 70.0 * math.exp(-28.0 * dt)
            phase += 2.0 * math.pi * f / SR
            env = math.exp(-11.5 * dt)
            sig = math.sin(phase) * env * amp
            left[i] += sig
            right[i] += sig

    def add_warm_rim(start_t: float, amp: float):
        s0 = int(start_t * SR)
        s1 = min(n_samples, int((start_t + 0.065) * SR))
        for i in range(s0, s1):
            dt = (i - s0) / SR
            env = math.exp(-55.0 * dt)
            # Woody clave/rim resonance (420 Hz + 890 Hz)
            sig = (0.65 * math.sin(2.0 * math.pi * 420.0 * dt) + 0.35 * math.sin(2.0 * math.pi * 890.0 * dt)) * env * amp
            left[i] += sig * 0.92
            right[i] += sig * 1.08

    def add_brushed_hat(start_t: float, amp: float, pan: float):
        s0 = int(start_t * SR)
        s1 = min(n_samples, int((start_t + 0.055) * SR))
        prev = 0.0
        for i in range(s0, s1):
            dt = (i - s0) / SR
            env = math.exp(-65.0 * dt)
            raw = rng.uniform(-1.0, 1.0)
            hp = raw - prev
            prev = raw
            sig = hp * env * amp
            left[i] += sig * (1.0 - pan)
            right[i] += sig * pan

    # Schedule bars across duration_sec
    n_bars = int(math.ceil(duration_sec / bar_dur))
    for bar_idx in range(n_bars):
        bar_t0 = bar_idx * bar_dur
        if bar_t0 >= duration_sec:
            break
        bass_m, chord_ms, arp_ms = PROGRESSION[bar_idx % len(PROGRESSION)]

        # Dynamic section energy curve: gentle under boot-sound (bar 0..3), full groove (bar 4+)
        if duration_sec > 30.0 and bar_idx < 4:
            energy = 0.55 + 0.10 * bar_idx
        else:
            energy = 0.88 + 0.12 * math.sin(bar_idx * 0.5)

        # 1. Warm Rhodes chord pad on beat 1 and gentle re-voicing on beat 3
        add_rhodes_chord(bar_t0, bar_dur * 0.95, chord_ms, energy)
        if not in_breath(bar_t0 + 2 * beat_dur):
            add_rhodes_chord(bar_t0 + 2 * beat_dur, bar_dur * 0.45, [m + 12 for m in chord_ms[:3]], energy * 0.42)

        # 2. Sub-bass groove (Beat 1 root, Beat 2.5 root, Beat 3.5 fifth, Beat 4 octave)
        bass_pattern = [
            (0.0, beat_dur * 1.35, bass_m, 0.22 * energy),
            (1.5 * beat_dur, beat_dur * 0.85, bass_m, 0.17 * energy),
            (2.5 * beat_dur, beat_dur * 0.75, bass_m + 7, 0.16 * energy),
            (3.25 * beat_dur, beat_dur * 0.65, bass_m + 12, 0.15 * energy),
        ]
        for offset, bdur, bm, bamp in bass_pattern:
            bt = bar_t0 + offset
            if bt < duration_sec and not in_breath(bt):
                add_sub_bass(bt, bdur, bm, bamp)

        # 3. C-major pentatonic verification climb bells (8th notes with stereo ping-pong)
        for e_idx, arp_m in enumerate(arp_ms):
            at = bar_t0 + e_idx * eighth_dur
            if at >= duration_sec or in_breath(at):
                continue
            # Slight J-Dilla / Nujabes swing on off-8ths
            if e_idx % 2 == 1:
                at += 0.018
            pan = 0.22 + 0.56 * ((e_idx % 4) / 3.0)
            b_amp = (0.095 if e_idx % 2 == 0 else 0.065) * energy
            add_pentatonic_bell(at, arp_m, pan, b_amp)
            # Dotted-16th stereo echo
            echo_t = at + 0.234
            if echo_t < duration_sec:
                add_pentatonic_bell(echo_t, arp_m, 1.0 - pan, b_amp * 0.36)

        # 4. Micro-percussion groove (after the initial 3.5s handshake opening on 90s cut)
        perc_active = (duration_sec <= 30.0) or (bar_t0 >= 3.5)
        if perc_active:
            # Kick on Beat 1, Beat 2.5, Beat 3.75
            for k_beat in (0.0, 1.5, 2.75):
                kt = bar_t0 + k_beat * beat_dur
                if kt < duration_sec and not in_breath(kt):
                    add_soft_kick(kt, 0.24 * energy)
            # Warm woody rim on Beat 2 and Beat 4
            for r_beat in (1.0, 3.0):
                rt = bar_t0 + r_beat * beat_dur
                if rt < duration_sec and not in_breath(rt):
                    add_warm_rim(rt, 0.14 * energy)
            # Swung 16th brushed shaker hats
            for s_idx in range(16):
                ht = bar_t0 + s_idx * sixteenth_dur + (0.012 if s_idx % 2 == 1 else 0.0)
                if ht < duration_sec and not in_breath(ht):
                    h_amp = (0.045 if s_idx % 4 == 2 else 0.025) * energy
                    add_brushed_hat(ht, h_amp, 0.35 + 0.3 * (s_idx % 2))

    # Final confirmation chord strike & warm fade-out on last 2.2s
    fade_len = int(2.2 * SR)
    for i in range(n_samples):
        if i > n_samples - fade_len:
            fade = (n_samples - i) / fade_len
            left[i] *= fade
            right[i] *= fade
        # Soft tanh warmth limiter
        l_val = math.tanh(left[i] * 1.15) * 0.88
        r_val = math.tanh(right[i] * 1.15) * 0.88
        left[i] = l_val
        right[i] = r_val

    pcm = array("h", [0] * (n_samples * 2))
    for i in range(n_samples):
        pcm[2 * i] = max(-32767, min(32767, int(left[i] * 32767)))
        pcm[2 * i + 1] = max(-32767, min(32767, int(right[i] * 32767)))

    with wave.open(str(out_wav), "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(SR)
        wf.writeframes(pcm.tobytes())

    subprocess.run(
        [
            "ffmpeg", "-y", "-v", "error",
            "-i", str(out_wav),
            "-c:a", "libmp3lame", "-b:a", "192k",
            str(out_mp3),
        ],
        check=True,
    )
    out_wav.unlink(missing_ok=True)
    print(f"Synthesized {out_mp3.name} ({duration_sec}s, {out_mp3.stat().st_size} bytes)")

def main():
    music_dir = Path("documents/github-yubios-KS9n5GAT/campaigns/video/composition/assets/music")
    music_dir.mkdir(parents=True, exist_ok=True)
    # 90s breath windows right at scene transitions (like boot-sound-v4h)
    breaths_90 = [(9.4, 10.0), (20.4, 21.0), (35.4, 36.0), (46.4, 47.0), (58.4, 59.0), (70.4, 71.0), (80.4, 81.0)]
    render_score(
        90.0,
        music_dir / "yubios-campaign-score-90s.wav",
        music_dir / "yubios-campaign-score-90s.mp3",
        breaths_90,
    )
    breaths_25 = [(4.7, 5.0), (11.7, 12.0), (18.2, 18.5)]
    render_score(
        25.0,
        music_dir / "yubios-campaign-score-25s.wav",
        music_dir / "yubios-campaign-score-25s.mp3",
        breaths_25,
    )

if __name__ == "__main__":
    main()
