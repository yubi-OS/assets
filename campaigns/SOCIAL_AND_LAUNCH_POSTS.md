# yubiOS Launch Seeding & Social Campaign Kit (HN, X, LinkedIn, Reddit, Press)

This file pairs with the **25.0-second `1080x1080` square video** ([`assets/yubios-kickstarter-square.mp4`](assets/yubios-kickstarter-square.mp4)), the **90.0-second `1920x1080` hero video** ([`assets/yubios-kickstarter-hero.mp4`](assets/yubios-kickstarter-hero.mp4)), and the primary campaign image ([`ads/yubiOS_Technical_Preview.jpg`](https://raw.githubusercontent.com/yubi-OS/assets/main/ads/yubiOS_Technical_Preview.jpg)).

All posts follow the [`pr-launch`](../../skills/github-yubios-KS9n5GAT/pr-launch/SKILL.md) sequencing and [`docs/PR.md`](https://github.com/yubi-OS/yubiOS/blob/main/docs/PR.md) claim-ledger rules:
- **T=0 (9:00-11:00 AM ET, Thursday ideal):** Hacker News (`Show HN`) + Lobste.rs
- **T+30m:** X/Twitter 5-post thread (with [`yubios-kickstarter-square.mp4`](assets/yubios-kickstarter-square.mp4) attached to Post 1) + LinkedIn Company Page post
- **T+60m:** `r/linux` and `r/netsec` (staggered 45 minutes apart)
- **T+120m:** Direct email briefings to Phoronix, LWN.net, The Register, and Ars Technica, followed by `r/privacy` and `r/linuxhardware`

---

## 1. Hacker News (`Show HN`)

**Title (79/80 chars):**
```text
Show HN: yubiOS - FIDO2-first immutable Linux with U2F/HSM & OP-TEE (RK3588/x86)
```

**URL:** `https://github.com/yubi-OS/yubiOS`

**First Comment / Text Body:**
```text
Hi HN,

We're building yubiOS (https://github.com/yubi-OS/yubiOS), an LGPL-2.1, bootc-delivered immutable Linux OS where a physical U2F/HSM security key (YubiKey 5 series as reference hardware) acts as the owner-held identity and authorization root across the stack, paired with an open ARM64 OP-TEE 4.11 Secure World (fTPM + EDK2 StandaloneMM) for platform measurement.

Why we split the two trust roots:
Most Linux setups either leave Secure Boot on factory keys or bind LUKS2 auto-decryption to an onboard OEM TPM that releases disk keys before a human is even in the room. We wanted a clean separation between two questions:
1. "Is the authorized human owner physically present?" -> Answered by your removable U2F/HSM token:
   - UEFI Secure Boot & Type2 UKI signing via PIV slot 9a (RSA-2048, systemd-sbsign + PKCS#11)
   - Root LUKS2 (p3 -> LVM usr_a/usr_b/yubios-root) decryption via FIDO2 hmac-secret (systemd-cryptenroll, PIN + touch)
   - Per-user LUKS2 + ext4 home directories (/var/home/<user>.home) via systemd-homed FIDO2
   - Hardware-resident OpenSSH ed25519-sk keys + pam-u2f (>= 1.3.1) for sudo and local login
2. "Did the expected firmware, kernel, and OS image boot?" -> Answered on ARM64 by TF-A BL31 v2.15 + OP-TEE 4.11 (hosting ms-tpm-20-ref fTPM on PCRs 0..7, 11 + StandaloneMM authenticated UEFI variable store) + read-only composefs (verity=require) /usr with a 3-way A/B OverlayFS and automatic local composefs OCI UKI re-signing on updates (ADR-034).

Proof of life on real silicon (Radxa ROCK 5B, RK3588 16 GB):
- Live hardware enrollment & Secure Boot reboot asciicast: https://asciinema.org/a/y9sHQPQTIbTWNIyr
- Raw UART captures in-repo: refs/logs/fvf13-224bf224.new (5,622 lines: 5-step U2F/HSM enrollment, SetupMode 1 -> 0, enforcing UEFI Secure Boot reboot) and refs/logs/fvf14-a76322cd.new (23,167 lines: 3-boot capture into GNOME Wayland + Antimony Browser v156 with engine-layer C2PA provenance inspection).

Hardware & Crowdfunding (Kickstarter & GoFundMe Phase 1 - $10,000 Goal):
We're launching a two-stage community campaign to take our open-source ARM64 OP-TEE 4.11 configuration through GlobalPlatform TEE Security Evaluation (TEE Protection Profile, Common Criteria EAL2+ augmented with AVA_VAN_AP.3):
- Campaign 1 (now, $10,000 goal): Funds initial 3rd-party accredited security lab pre-testing, authoring the formal Security Target (ST), OP-TEE conformance/fuzz harness runs, and sacrificial ROCK 5B OTP eFuse ROTPK (OMN-45) + eMMC RPMB write-lock (OMN-46) validation.
- Campaign 2 (follow-up if Phase 1 lab pre-test passes, ~$100,000 goal): Funds the GlobalPlatform Certification Body fee ($29k-$36k) + 3-month accredited lab white-box/black-box penetration evaluation to become the first open-source, community-funded project to pursue GlobalPlatform TEE certification.

What backers receive (and how to run it on your own hardware today):
- Early access to a dedicated Assured Node on our infrastructure verified remotely via yubios-attest (mutual strongbox attestation combining an OP-TEE fTPM PCR quote + U2F/HSM PIV signature), OR
- Pre-installed hardware in hand on Radxa ROCK 5B (RK3588, 16 GB) or Pine64 RockPro64 (RK3399, 4 GB) flashed in SetupMode=1 so the 5-step first-boot wizard binds the full root of trust to your own U2F/HSM. (We also build a CI target for Pine64 PineTab2 RK3566, currently under active UART/USB-boot investigation in OMN-167.)
- Expanding to x86-64 UEFI Setup Mode: For users without our ARM64 boards or firmware, our x86-64 Setup-Mode kit enrolls your U2F/HSM PIV Slot 9a PK/KEK/db keys directly into motherboards in UEFI SetupMode=1, giving you U2F/HSM UKI signing and FIDO2 LUKS2/ext4 homed above the OEM UEFI boundary.

Every ADR (ADR-001..ADR-034), blocker (docs/BLOCKERS.md), and pinned SHA (PINNED.md) is in the repo. Happy to answer questions about the PIV/CCID vs. FIDO2/hidraw split, OP-TEE StandaloneMM variable signing, or the GlobalPlatform TEE pre-test scope.
```

---

## 2. X / Twitter 5-Post Launch Thread (Attach `yubios-kickstarter-square.mp4` to Post 1)

**Post 1/5 (Attach [`assets/yubios-kickstarter-square.mp4`](assets/yubios-kickstarter-square.mp4)):**
```text
Assume Nothing. Prove Everything.

Meet yubiOS (v0.8.94 Technical Preview): an open-source, FIDO2-first immutable Linux OS where your physical U2F/HSM token signs UEFI Secure Boot (PIV Slot 9a), decrypts LUKS2 & ext4 systemd-homed, holds resident ed25519-sk SSH keys, and attests your node.

Repo: https://github.com/yubi-OS/yubiOS
Live ROCK 5B hardware demo: https://asciinema.org/a/y9sHQPQTIbTWNIyr
```

**Post 2/5:**
```text
Why split the trust chain into two hardware domains?

1. Owner Identity Root (Your U2F/HSM): Answers "Is the human owner present?" Unplug your key and signing/decryption authority leaves the room with you.
2. Platform Integrity Root (ARM64 OP-TEE 4.11 TEE): Hosts an open fTPM (PCRs 0..7, 11) + EDK2 StandaloneMM authenticated UEFI variables + composefs (verity=require) /usr.
```

**Post 3/5:**
```text
Pre-installed ARM64 hardware + Bring-Your-Own x86-64 UEFI Setup Mode:

• Radxa ROCK 5B (RK3588, 16 GB): Flagship pre-installed kit ($399) with GNOME Wayland & Antimony v156 C2PA browser
• Pine64 RockPro64 (RK3399, 4 GB): Sovereign node kit ($249)
• Pine64 PineTab2 (RK3566): Active UART/USB-boot R&D (OMN-167)
• x86-64 PCs/Servers: Enroll your own U2F/HSM Slot 9a PK/KEK/db keys in UEFI SetupMode=1 ($25+ kit)
```

**Post 4/5:**
```text
Our Two-Stage Path to GlobalPlatform TEE Certification (Common Criteria EAL2+ / AVA_VAN_AP.3):

• Campaign 1 (Now - $10,000 goal): Initial 3rd-party accredited security lab pre-testing, Security Target (ST) authoring, and sacrificial ROCK 5B eFuse ROTPK + eMMC RPMB proofs.
• Campaign 2 (Next - ~$100,000 goal): If Phase 1 passes, crowd-certify the first open-source GlobalPlatform TEE.
```

**Post 5/5:**
```text
What contributing members receive:

• Early access to a remotely attested Assured Node ($99) verified via yubios-attest (live fTPM PCR quote + U2F/HSM PIV signature), OR
• Your own pre-installed Radxa ROCK 5B ($399) or RockPro64 ($249) in hand, configured to bind its entire root of trust to your U2F/HSM on first boot.

Full UART logs (fvf13 & fvf14) + 34 ADRs: https://github.com/yubi-OS/yubiOS
```

---

## 3. LinkedIn Post (Attach `yubios-kickstarter-square.mp4` or `yubiOS_Technical_Preview.jpg`)

```text
Assume Nothing. Prove Everything. Your keys. Your machine. Verifiably yours.

We are launching the Phase 1 crowdfunding campaign ($10,000 goal on Kickstarter and GoFundMe) for yubiOS: an open-source (LGPL-2.1), bootc-delivered immutable Linux® operating system where the owner's physical U2F/HSM hardware token authorizes every security boundary.

What is proven on real Radxa ROCK 5B (RK3588, 16 GB) silicon today (v0.8.94 Technical Preview):
• UEFI Secure Boot & Type2 UKI Signing: On-device PK/KEK/db minting from U2F/HSM PIV slot 9a into OP-TEE 4.11 StandaloneMM (SetupMode: 1 -> 0) and automatic local composefs OCI UKI re-signing on updates (ADR-034).
• Full-Disk & Home Encryption: LUKS2 root (p3 -> LVM usr_a/usr_b/yubios-root) and per-user LUKS2 + ext4 systemd-homed volumes gated by FIDO2 hmac-secret (PIN + physical touch).
• Hardware-Resident SSH & Sudo: OpenSSH ed25519-sk resident keys and pam-u2f (>= 1.3.1) local privilege confirmation.
• Desktop & Provenance Browser: GNOME Wayland desktop shipping with our checksum-pinned Antimony Browser v156 (engine-layer C2PA content provenance gating) and two-build bit-for-bit reproducible CI (PINNED.md + yubiOS.rego).

Watch the unedited 5-step hardware enrollment and enforcing Secure Boot reboot on Asciinema:
https://asciinema.org/a/y9sHQPQTIbTWNIyr

Why we are raising $10,000 in Phase 1 (and our ~$100,000 Phase 2 horizon):
We are aiming to take our open-source ARM64 TF-A v2.15 + OP-TEE 4.11 (fTPM + StandaloneMM) stack through GlobalPlatform TEE Security Evaluation (TEE Protection Profile, Common Criteria EAL2+ / AVA_VAN_AP.3).
1. Campaign 1 ($10,000 Goal - Now): Funds initial third-party accredited security laboratory pre-testing, Security Target (ST) authoring, conformance/fuzz harnesses, and sacrificial ROCK 5B eFuse ROTPK (OMN-45) + eMMC RPMB (OMN-46) validation.
2. Campaign 2 (~$100,000 Goal - Next Phase): Once Phase 1 lab readiness passes and the pre-assessment report is published in our repo, a follow-up campaign will invite the community to fund the formal GlobalPlatform Certification Body filing and 3-month accredited lab penetration evaluation.

What contributing members receive:
• Early access to a remotely attested Assured Node ($99) on yubi-OS infrastructure verified via yubios-attest, OR
• A pre-installed Radxa ROCK 5B 16 GB ($399) or Pine64 RockPro64 4 GB ($249) shipped ready to bind its full root of trust to your own U2F/HSM on first power-on (with Pine64 PineTab2 RK3566 under active R&D investigation in OMN-167), OR
• The x86-64 UEFI Setup-Mode Enrollment Kit ($25+) to bring U2F/HSM Slot 9a Secure Boot signing and FIDO2 LUKS2/ext4 homed to standard x86 PCs and servers that support enrolling custom keys in Setup Mode.

Explore the repository, 34 ADRs, and raw hardware UART captures:
https://github.com/yubi-OS/yubiOS

(Independent open-source project; not affiliated with or endorsed by Yubico, Radxa, Pine64, or GlobalPlatform. Linux® is a registered trademark of Linus Torvalds.)
```

---

## 4. Reddit Technical Posts (`r/linux` and `r/netsec`)

### `r/linux` Post
**Title:**
```text
yubiOS (v0.8.94 Technical Preview): FIDO2-first bootc/composefs Linux with U2F/HSM Secure Boot signing, ext4 systemd-homed, and open ARM64 OP-TEE fTPM/StMM (ROCK 5B, RockPro64, and x86 Setup Mode)
```

**Body:**
```text
Project repo: https://github.com/yubi-OS/yubiOS
Live Radxa ROCK 5B hardware enrollment asciicast: https://asciinema.org/a/y9sHQPQTIbTWNIyr
Raw UART captures: refs/logs/fvf13-224bf224.new (5,622 lines) & refs/logs/fvf14-a76322cd.new (23,167 lines)

We've been building yubiOS around Lennart Poettering's "Fitting Everything Together" image model and bootc, with one structural constraint: owner-facing authority (Secure Boot signing, LUKS2 decryption, systemd-homed, SSH, and sudo) lives on a physical U2F/HSM token in your hand rather than an OEM-controlled TPM, while platform measurement lives in an open ARM64 OP-TEE 4.11 Secure World (fTPM + EDK2 StandaloneMM).

What is working on hardware today (v0.8.94):
1. Dual-console first-boot wizard (yubiOS-enroll.service mirrored across HDMI /dev/tty1 and UART /dev/ttyS2):
   - Step 1/5: Generates PK, KEK, and db from U2F/HSM PIV slot 9a, enrolls them into OP-TEE StandaloneMM (SetupMode: 1 -> 0), re-signs systemd-boot and the Type2 UKI via PKCS#11, and commits to an on-device composefs OCI repo (/var/lib/yubiOS/oci, ADR-034).
   - Step 2/5: Formats p3 as LUKS2 + LVM (usr_a 1%, usr_b 1%, yubios-root 96%), enrolls FIDO2 hmac-secret (PIN + touch), and mounts a 3-way /usr OverlayFS over composefs (verity=require).
   - Step 3/5: Creates a per-user LUKS2 + ext4 home volume (/var/home/yubios.home) decrypted via systemd-homed FIDO2.
   - Step 4/5 & 5/5: Generates resident OpenSSH ed25519-sk keys and registers pam-u2f (>= 1.3.1).
2. Enforcing Secure Boot into GNOME Wayland + Antimony v156 (our Chromium 156 fork with C++ engine-layer C2PA provenance gating).
3. Two-build bit-for-bit reproducibility gate across isolated rootless BuildKit containers (ADR-014 + yubiOS.rego OPA policy).

Hardware availability & $10k Phase 1 Accredited TEE Lab Campaign:
We're launching a Kickstarter and GoFundMe ($10,000 Phase 1 goal) to fund initial 3rd-party accredited security laboratory pre-testing of our ARM64 TF-A + OP-TEE 4.11 stack against the GlobalPlatform TEE Protection Profile (EAL2+ / AVA_VAN_AP.3). If Phase 1 passes, a second campaign (~$100k) will let the community crowd-certify the first open-source GlobalPlatform TEE.
- Pre-installed hardware tiers are available for Radxa ROCK 5B (RK3588 16 GB, $399) and Pine64 RockPro64 (RK3399 4 GB, $249), plus early access to remotely attested Assured Nodes ($99, verified via yubios-attest). Pine64 PineTab2 (RK3566) is under active UART/USB-boot investigation (OMN-167).
- We are also shipping an x86-64 UEFI Setup-Mode kit so anyone with a standard x86 motherboard that supports enrolling custom keys in SetupMode=1 can sign UKIs and systemd-boot with their U2F/HSM Slot 9a key.

Feedback and architectural review welcome!
```

### `r/netsec` Post
**Title:**
```text
Separating Owner Identity Root (U2F/HSM PIV+FIDO2) from Platform Integrity Root (ARM64 OP-TEE 4.11 fTPM+StandaloneMM) in yubiOS + Phase 1 GlobalPlatform TEE Pre-Testing
```

**Body:**
```text
Repository & ADRs (ADR-001..ADR-034): https://github.com/yubi-OS/yubiOS
Threat Model & Mitigations: https://github.com/yubi-OS/yubiOS/blob/main/docs/THREAT_MODEL.md
Hardware Enrollment Asciicast (Radxa ROCK 5B): https://asciinema.org/a/y9sHQPQTIbTWNIyr

We wanted to share the security architecture of yubiOS (v0.8.94 Technical Preview) and get feedback from r/netsec as we prepare our Target of Evaluation (TOE) for Phase 1 third-party accredited TEE laboratory pre-testing.

Architectural summary:
- Boundary 1 (UEFI Secure Boot & Type2 UKI): U2F/HSM PIV slot 9a (RSA-2048 via PKCS#11) signs PK/KEK/db and the Type2 UKI (.linux + .initrd + .cmdline + .splash). On ARM64 (RK3588/RK3399), authenticated UEFI variables live in OP-TEE 4.11 EDK2 StandaloneMM inside TrustZone (36,864 KiB no-map reserved memory). On x86-64 machines supporting UEFI SetupMode=1, PK/KEK/db enroll into motherboard NVRAM with a first-boot CHIPSEC SPI/SMM check (ADR-024).
- Boundary 2 (Immutable /usr & Day-2 Re-Signing): Root mounts composefs (verity=require) anchored to a SHA-512 digest in the signed UKI cmdline, with a 3-way A/B /usr OverlayFS on LVM. Kernel/package updates trigger yubiOS-uki-resign (ADR-034), requiring physical U2F/HSM touch to sign the updated UKI and commit to a local composefs OCI store (/var/lib/yubiOS/oci).
- Boundary 3 (LUKS2 & ext4 systemd-homed): Decryption is bound to FIDO2 hmac-secret (PIN + physical touch) rather than unattended TPM PCR unsealing, mitigating cold-boot/evil-maid auto-unseal without human presence.
- Boundary 4 (Mutual Strongbox Attestation - yubios-attest): Combines an OP-TEE fTPM quote (PCRs 0..7, 11 + IMA SHA-256 event log) with a U2F/HSM PIV signature so remote clients can verify both platform boot state and physical token custody before dispatching workloads to an Assured Node.

We are raising $10,000 in Phase 1 (Kickstarter/GoFundMe) for initial accredited security lab pre-testing, Security Target (ST) authoring under the GlobalPlatform TEE Protection Profile (EAL2+ / AVA_VAN_AP.3), and sacrificial ROCK 5B OTP eFuse ROTPK (OMN-45) + eMMC RPMB write-lock (OMN-46) proofs, ahead of a ~$100,000 Phase 2 community certification campaign. Questions on the threat model or active blockers (docs/BLOCKERS.md) are very welcome.
```

---

## 5. Press Pitch (Phoronix / LWN.net / The Register / Ars Technica)

```text
Subject: yubiOS v0.8.94: FIDO2-first immutable Linux on RK3588/x86 launches $10k Phase 1 GlobalPlatform TEE lab campaign

Hi [Name],

Quick technical milestone that may interest your readers:

yubiOS (https://github.com/yubi-OS/yubiOS) has published its v0.8.94 Technical Preview and live Radxa ROCK 5B (RK3588, 16 GB) hardware proof of life (https://asciinema.org/a/y9sHQPQTIbTWNIyr), demonstrating a full 5-step physical U2F/HSM ceremony:
1. On-device PK/KEK/db Secure Boot key generation from U2F/HSM PIV slot 9a into ARM64 OP-TEE 4.11 StandaloneMM (SetupMode: 1 -> 0) and PKCS#11 Type2 UKI signing
2. LUKS2 root + 3-way /usr OverlayFS over composefs (verity=require) decrypted via FIDO2 hmac-secret
3. Per-user LUKS2 + ext4 systemd-homed encrypted home directories
4. Hardware-resident ed25519-sk SSH keys and pam-u2f sudo authentication
5. Enforcing UEFI Secure Boot reboot into GNOME Wayland and Antimony v156 (our Chromium 156 fork with engine-layer C2PA provenance gating)

Alongside the technical preview, we are launching a two-stage crowdfunding campaign (Kickstarter & GoFundMe):
- Phase 1 ($10,000 goal): Funds initial third-party accredited security laboratory pre-testing and Security Target (ST) authoring for our open ARM64 TF-A v2.15 + OP-TEE 4.11 (fTPM + StandaloneMM) stack under the GlobalPlatform TEE Protection Profile (Common Criteria EAL2+ / AVA_VAN_AP.3), plus sacrificial eFuse ROTPK and eMMC RPMB lockdown proofs.
- Phase 2 (~$100,000 goal, launched once Phase 1 lab pre-testing passes): Aims to make yubiOS the first open-source, community-funded project to complete formal GlobalPlatform TEE certification.

Backers receive early access to remotely attested Assured Nodes (verified via our yubios-attest mutual fTPM + U2F/HSM daemon), pre-installed Radxa ROCK 5B (RK3588) or Pine64 RockPro64 (RK3399) hardware kits, or our x86-64 UEFI Setup-Mode enrollment kit for standard PCs and servers. (Pine64 PineTab2 RK3566 support is also under active R&D investigation.)

All 34 ADRs, raw UART logs (refs/logs/fvf13-224bf224.new and fvf14-a76322cd.new), and campaign visual assets (https://github.com/yubi-OS/assets/tree/main/campaigns) are public under LGPL-2.1. Happy to answer any technical questions.

Best,
Jenny Latuu
Founder / Lead Developer, yubi-OS
```
