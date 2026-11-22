# av-composer Creative Brief: yubiOS Crowdfunding Hero Video

## Objective
Produce a 90.0-second (`1920x1080`, `30 fps`) crowdfunding hero video for both the **Kickstarter** and **GoFundMe** campaigns of **yubiOS**, strictly adhering to the `av-composer` zero-external-calls contract.

## Brand & Visual System
- **Primary Visual:** `ads/yubiOS_Technical_Preview.jpg` + canonical `logo.png`
- **Palette:** Deep space obsidian (`#040511`, `#09071c`), neon magenta (`#ff2a9d`), electric violet (`#a855f7`), cyber cyan (`#53d5fa`), and verification lime (`#89ff35`).
- **Audio Signature:** Uses the project's own measured `yubios-boot-sound-v5.mp3` at `t=0.0s` and `yubios-browser-open.mp3` at `t=36.0s` layered over the `vol12.mp3` rhythmic bed and discrete hardware-touch SFX.
- **Core Claims Covered:**
  1. Owner-held U2F/HSM root of trust (PIV Slot `9a` Secure Boot signing, FIDO2 `hmac-secret` LUKS2 + `systemd-homed`, `ed25519-sk` SSH, `pam-u2f`).
  2. Live Radxa ROCK 5B (`rk3588`, 16 GB) 5-step hardware enrollment proof of life (`https://asciinema.org/a/y9sHQPQTIbTWNIyr`, logs `fvf13-224bf224.new` & `fvf14-a76322cd.new`).
  3. Pre-installed hardware on Radxa ROCK 5B (`$399`) and Pine64 RockPro64 (`$249`), PineTab2 (`rk3566`) active investigation, and x86-64 UEFI Setup-Mode support (`$25+`).
  4. Early access to remotely verified Assured Nodes (`$99`) via `yubios-attest` mutual strongbox attestation.
  5. Two-stage GlobalPlatform TEE Certification plan (`$10,000` Phase 1 initial third-party accredited lab testing -> `~$100,000` Phase 2 full community TEE certification).
