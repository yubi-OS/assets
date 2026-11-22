# av-composer Plan: yubiOS 25-Second 1080x1080 Square Social Cut (X, LinkedIn, HN)

- **Title:** `yubiOS: Assume Nothing. Prove Everything. (25s Square Launch Teaser)`
- **Resolution & Rate:** `1080x1080` (`1:1` Square), `30 fps`, `25.0s` (`751` frames `f0000.jpg`..`f0750.jpg`), `yuv420p` TV-range, `+faststart`
- **Soundtrack:** Custom `yubios-campaign-score-25s.mp3` (96 BPM Strudel/AM-2 `Am9 -> Fmaj9 -> G13 -> Cmaj9` Rhodes + sub-bass + C-major pentatonic bells) + `yubios-boot-sound-v5.mp3` + `yubios-browser-open.mp3` + tactile SFX

---

## Scene-by-Scene Storyboard (25.0 Seconds Total)

| Scene | Window (s) | Duration | Visuals & Copy | Audio Cues |
|---|---|---|---|---|
| **1. Hero & Trust Chain** | `0.0 - 6.0s` | `6.0s` | Visible at `t=0`: `yubiOS` header + `ASSUME NOTHING. PROVE EVERYTHING.` + uncropped `yubiOS_Technical_Preview.jpg` + 4 trust pills (`PIV Slot 9a UKI`, `FIDO2 LUKS2 + ext4 homed`, `ed25519-sk SSH + pam-u2f`, `OP-TEE 4.11 fTPM + StMM`). | `yubios-boot-sound-v5.mp3` (`0.0s`) + `yubios-campaign-score-25s.mp3` (`0.0s`) + `bell0.ogg` (`0.5s`) |
| **2. Live ROCK 5B 5-Step Enrollment** | `6.0 - 12.5s` | `6.5s` | Dual-console (`ttyS2` + `tty1`) terminal stepping through `refs/logs/fvf13-224bf224.new` (`asciinema.org/a/y9sHQPQTIbTWNIyr`): `[1/5]` Slot 9a `SetupMode 1->0`, `[2/5]` LUKS2 FIDO2, `[3/5]` `systemd-homed` `LUKS2 + ext4`, `[4/5]` `ed25519-sk`, `[5/5]` `pam-u2f` -> `secureboot: Secure boot enabled` + GNOME Wayland & Antimony v156. | `bell3.ogg` (`6.0s`), `key1.wav` (`7.0s`), `key3.wav` (`8.2s`), `bong1.ogg` (`10.2s`), `yubios-browser-open.mp3` (`10.8s`) |
| **3. Pre-Installed Boards, x86 & GP TEE** | `12.5 - 19.0s` | `6.5s` | 2x2 hardware grid (`Radxa ROCK 5B 16GB $399`, `Pine64 RockPro64 4GB $249`, `Pine64 PineTab2 R&D Investigation`, `x86-64 UEFI Setup Mode $25+`) + Two-Stage GlobalPlatform TEE Certification banner (`$10,000` Phase 1 Lab Pre-Test -> `~$100,000` Phase 2 Full Cert). | `switch1.ogg` (`12.5s`), `select8.ogg` (`14.5s`), `drop1.ogg` (`16.5s`) |
| **4. Rewards & Call to Action** | `19.0 - 25.0s` | `6.0s` | `SIGNED, SEALED, DELIVERED: IT'S YOURS.` + 5 backer tiers (`$25` x86 Setup, `$99` Assured Node Pass, `$249` RockPro64 Kit, `$399` ROCK 5B 16GB Flagship, `$749` TEE Lab Patron) + `github.com/yubi-OS/yubiOS`. | `bell0.ogg` (`19.0s`), `bong1.ogg` (`21.5s`), fade-out (`23.0 - 25.0s`) |
