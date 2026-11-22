# Platform Requirements, Flipper One Teardown & Certification Strategy

This document records the platform rules for **Kickstarter** and **GoFundMe**, the structural teardown of the **Flipper One** Kickstarter campaign (`https://www.kickstarter.com/projects/flipper-devices/flipper-one/`), and the cost/process mechanics of **GlobalPlatform TEE Security Evaluation**.

---

## 1. Kickstarter Platform Requirements (Technology / Hardware)

Kickstarter enforces strict review gates on campaigns in the **Technology -> Hardware** and **Technology -> Software** categories. Every field below must be populated in the Kickstarter Project Editor before submitting for Trust & Safety review.

### Required Editor Tabs & Field Limits

| Tab / Field | Platform Rule / Limit | yubiOS Campaign Entry |
|---|---|---|
| **Project Title** | Max `60` characters; must name the product and core function | `yubiOS: FIDO2-First Immutable Linux OS & Open ARM64 TEE` (`55` chars) |
| **Project Subtitle** | Max `135` characters; scannable hook shown on discovery cards | `Pre-installed on ROCK 5B & RockPro64, or run on x86 Setup Mode. Your U2F/HSM signs boot, decrypts disk, and attests your node.` (`127` chars) |
| **Category** | Primary + Subcategory | `Technology` -> `Hardware` (with `Open-Source Software` tag) |
| **Project Location** | City, State, Country of legal entity / bank account | `Los Angeles, CA, USA` |
| **Project Image (Primary)** | `16:9` ratio (`1024x576` min, `1920x1080` ideal); JPEG/PNG `< 50 MB` | `ads/yubiOS_Technical_Preview.jpg` (`https://raw.githubusercontent.com/yubi-OS/assets/main/ads/yubiOS_Technical_Preview.jpg`) |
| **Project Video** | Optional but strongly recommended (`16:9` MP4/MOV); must show real working hardware, no photorealistic CGI | Rendered 90.0s walkthrough ([`assets/yubios-kickstarter-hero.mp4`](assets/yubios-kickstarter-hero.mp4)) combining the live Radxa ROCK 5B asciinema (`https://asciinema.org/a/y9sHQPQTIbTWNIyr`), HDMI/UART dual-console capture, GNOME Wayland + Antimony v156 desktop, and `yubios-boot-sound-v5.mp3` |
| **Funding Goal** | All-or-Nothing threshold; creator receives `$0` if missed | `$10,000 USD` (Phase 1 Accredited 3rd-Party TEE Lab Pre-Testing & Hardware Gate) |
| **Campaign Duration** | `1` to `60` days (`30` days recommended by Kickstarter) | `30 days` |
| **Platform & Payment Fees** | `5%` Kickstarter fee + `~3-5%` Stripe payment processing (`~8-10%` total) | Net proceeds at `$10,000` goal: `~$9,050-$9,200` (accounted for in budget table) |
| **Hardware Policy Gate** | Photorealistic 3D renders and simulated UI that do not exist are **prohibited**. Must show real prototypes, actual logs, and honest maturity state. | Satisfied via committed UART logs (`fvf13-224bf224.new`, `fvf14-a76322cd.new`), live asciinema (`y9sHQPQTIbTWNIyr`), and explicit `Technical Preview` badges on all visuals. |
| **Plan Tab (Hardware)** | Mandatory production schedule & milestone breakdown | Populated with 4-stage engineering, lab pre-test, node rollout, and board fulfillment schedule. |
| **Risks & Challenges** | Mandatory disclosure of supply-chain, firmware, and certification risks | Covers DRAM/SBC pricing, PineTab2 SPI-less boot investigation, eFuse/RPMB hardware gates, and accredited lab remediation cycles. |
| **Use of AI Disclosure** | Mandatory yes/no disclosure on whether AI tools assisted project development or assets | Full disclosure included: AI-assisted engineering and background graphic foundations under strict cryptographic verification (`PINNED.md`, `yubiOS.rego`, two-build reproducibility, human-verified hardware logs). |

---

## 2. GoFundMe Platform Requirements (Step-by-Step Setup)

GoFundMe uses a keep-what-you-raise (flexible funding) model suited for staged open-source R&D and community-backed laboratory testing.

| Setup Step / Field | Platform Rule / Limit | yubiOS Campaign Entry |
|---|---|---|
| **Where will funds go?** | Country + ZIP code where bank withdrawals occur (sets currency) | `United States` (`Los Angeles, CA`, Currency: `USD`) |
| **Who are you fundraising for?** | `Yourself` (personal or company account), `Someone else`, or `Charity` | `Yourself` (yubi-OS project / company operating account for accredited lab engagement & hardware fulfillment) |
| **Category** | Primary discovery bucket | `Business` / `Creative` / `Community` (Technology & Open-Source Security Infrastructure) |
| **Fundraiser Title** | Max `60` characters; specific cause + call to action | `Certify yubiOS: Open-Source U2F/HSM Linux & GlobalPlatform TEE` (`62` -> trimmed to `58` chars: `Certify yubiOS: Open-Source U2F/HSM Linux & ARM64 TEE Lab`) |
| **Cover Media** | Bright `16:9` image (`720x405` min, `1920x1080` ideal) or video link | `ads/yubiOS_Technical_Preview.jpg` |
| **Starting Goal** | Can be adjusted upward as milestones are hit; no penalty if under goal | `$10,000 USD` (Phase 1 Accredited Lab Pre-Testing; stretches toward Phase 2 `$100,000` full certification) |
| **Transaction Fee** | `0%` platform fee; `2.9% + $0.30` per donation payment processing fee | `~$9,680` net on `$10,000` raised |
| **Story Body** | Minimum `100` words (`600-1,200` words optimal); must explain who you are, what is already built, exact use of funds, and what contributors get | Full narrative + line-item `$10,000` lab budget + Assured Node / ROCK 5B / RockPro64 contributor fulfillment tiers + asciinema proof of life. |

---

## 3. Flipper One Campaign Playbook: How We Adapt It to yubiOS

The Flipper One Kickstarter campaign (`https://www.kickstarter.com/projects/flipper-devices/flipper-one/`) launched on November 17, 2026 and raised over `$15.4M` from `28,000+` backers by following eight specific structural rules. Here is how each maps directly onto yubiOS:

| Flipper One Pattern | How Flipper Devices Used It | How yubiOS Adapts It |
|---|---|---|
| **1. Lead with Open Mainline & Zero Vendor Lock-In** | Opens immediately with *"Mainline Linux kernel support, No binary blobs, No vendor-locked BSP"* before listing secondary features. | Opens with **Owner-Held Hardware Trust & Reproducible Open Source**: no opaque OEM TPM lock-in, digest-pinned inputs (`PINNED.md`), `yubiOS.rego` OPA policy gates, and two-build bit-for-bit reproducible OCI images. |
| **2. Clean Layer / Category Split** | Frames *Layer 0 (Flipper Zero: NFC/RFID/Sub-GHz)* vs. *Layer 1 (Flipper One: IP networking, Linux compute, SDR, local AI)*. | Frames **Domain 1 (Owner Identity Root: Physical U2F/HSM Token)** vs. **Domain 2 (Platform Integrity Root: ARM64 OP-TEE 4.11 fTPM & StandaloneMM)**. Answers *"Is the owner present?"* separately from *"Did the expected OS boot?"* |
| **3. "Why 2 Processors?" Architectural Diagram** | Explains why RP2350 (power/display/boot recovery) and RK3576 (Linux compute) sit side-by-side. | **"Why U2F/HSM + OP-TEE Secure World?"** Explains why PIV Slot `9a` + FIDO2 `hmac-secret` live on your removable U2F/HSM while OP-TEE `4.11` (`fTPM` + `StandaloneMM`) runs in ARM TrustZone on the RK3588/RK3399 SoC. |
| **4. Single-Cable / Out-of-the-Box Workflows** | Shows concrete modes (*Pocket Linux Lab via USB-C*, *Desktop Mode*, *Recovery & Debugger*) with `1360px` visual banners + 3-4 bullets each. | Shows concrete yubiOS modes: **Dual-Console First-Boot Enrollment (HDMI + UART)**, **GNOME Wayland Desktop + Antimony v156 Provenance Browser**, **x86-64 UEFI Setup-Mode Signing**, and **Remote Assured Node (`yubios-attest`)**. |
| **5. Radical "Build in Public" Developer Portal** | *"We're publishing our task trackers, internal discussions, half-finished docs, and architectural debates. All the messy stuff companies usually keep behind closed doors."* | Highlights `github.com/yubi-OS/yubiOS`: 34 published ADRs (`docs/ADR.md`), live `BLOCKERS.md` and `TODO.md`, unedited 28,000+ line hardware UART captures (`fvf13`, `fvf14`), and public GitHub Actions CI. |
| **6. Honest Unfinished-Hardware Callouts** | Explicitly marks the SDR module with a warning (`⚠️ technical specifications are not yet finalized, and we're still actively researching`) rather than over-promising. | Explicitly marks **Pine64 PineTab2 (`rk3566`)** as under active hardware investigation (SPI-less boot recovery and USB-boot installer testing in `OMN-167`), while offering pre-installed units on proven **Radxa ROCK 5B (`rk3588`)** and **RockPro64 (`rk3399`)**. |
| **7. Candid Pricing & BOM Transparency** | Prices the flagship Flipper One at `$399` and explains openly that DRAM and UFS costs make `$399` an at-cost community rate. | Prices the **Pre-Installed Radxa ROCK 5B (16 GB RAM) Flagship Kit** at `$399` (and RockPro64 Kit at `$249`, Assured Node Pass at `$99`) with a transparent breakdown of board + 128 GB industrial microSD + pre-flashing + Phase 1 lab allocation. |
| **8. Inline Mini-FAQs Under Technical Sections** | Places 2-question blockquote FAQs directly underneath complex sections (e.g., *Flipper SIM FAQ*, *LoRa Module FAQ*) so readers never stay confused. | Places inline mini-FAQs directly beneath the **U2F/HSM Enrollment**, **x86-64 Setup Mode**, **GlobalPlatform TEE Certification**, and **Assured Node** sections. |

---

## 4. GlobalPlatform TEE Certification Mechanics & Two-Campaign Budget

### How GlobalPlatform TEE Certification Works

GlobalPlatform's **TEE Security Evaluation** scheme is grounded in the **Common Criteria (CC v3.1 / ISO/IEC 15408)** standard and governed by the **TEE Protection Profile (`TEE PP`)**:
- **Assurance Level:** `EAL2+` (Evaluation Assurance Level 2 augmented with vulnerability analysis component `AVA_VAN_AP.3` and the GlobalPlatform TEE Attack Catalog).
- **Target of Evaluation (TOE) for yubiOS:** The ARM64 Secure World firmware stack comprising **ARM Trusted Firmware-A (`BL31 v2.15.0`)** and **OP-TEE OS `4.11`** hosting the **`fTPM`** (Microsoft `ms-tpm-20-ref` Trusted Application) and **EDK2 `StandaloneMM`** authenticated UEFI variable store on Rockchip `RK3588` / `RK3399`, paired with hardware ROTPK eFuse and eMMC RPMB write-protection.
- **Why Two Campaigns ($10,000 -> ~$100,000):**
  - Accredited security laboratories (such as Brightsight, Riscure/Keysight, Applus+, SERMA, or CEA-Leti) do not accept a raw open-source repo into a 3-month full evaluation without a formal **Security Target (ST)**, a frozen **Target of Evaluation (TOE)**, hardware fuse/RPMB lockdown proofs, and a pre-evaluation gap check.
  - **Campaign 1 ($10,000)** funds that exact readiness gate: accredited lab pre-assessment consultation, ST authoring against `TEE PP`, OP-TEE `xtest` + GlobalPlatform API conformance/fuzz harness runs, and sacrificial ROCK 5B eFuse ROTPK + eMMC RPMB hardware validation.
  - **Campaign 2 (~$100,000)** launches once the Phase 1 lab pre-assessment passes. It covers the fixed **GlobalPlatform Certification Body (CB) fee** (`$29,000` non-member / `$36,000` member fee schedule) plus **`$64,000-$71,000` for the accredited laboratory's 3-month full white-box + black-box evaluation** and Evaluation Technical Report (ETR).
  - By splitting the effort into a `$10,000` proving campaign followed by a `~$100,000` certification campaign, the community only funds the six-figure formal evaluation after third-party lab pre-testing confirms the TOE is ready.
