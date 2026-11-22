#!/usr/bin/env python3
"""
Deterministic SVG -> PNG renderer for yubiOS Kickstarter & GoFundMe campaign visuals.
Matches the dark-first neon magenta/violet/cyan/lime brand kit in yubi-OS/assets/ads.
Uses chrome-headless-shell for pixel-accurate SVG rasterization.
"""
from pathlib import Path
import base64
import hashlib
import shutil
import subprocess

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
SOURCE = ROOT / "source"
ASSETS.mkdir(parents=True, exist_ok=True)

LOGO_URI = "data:image/png;base64," + base64.b64encode((SOURCE / "logo.png").read_bytes()).decode()

FONT_SANS = "Inter, 'Liberation Sans', 'DejaVu Sans', sans-serif"
FONT_MONO = "'JetBrains Mono', 'Liberation Mono', 'DejaVu Sans Mono', monospace"

def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )

def svg_header(w: int, h: int, title: str, badge_text: str = "TECHNICAL PREVIEW • PHASE 1 CAMPAIGN") -> str:
    badge_w = max(392, len(badge_text) * 9 + 64)
    badge_x = w - badge_w - 44
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <title>{esc(title)}</title>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#040511"/>
      <stop offset="55%" stop-color="#09071c"/>
      <stop offset="100%" stop-color="#120824"/>
    </linearGradient>
    <linearGradient id="pinkCyan" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#ff2a9d"/>
      <stop offset="55%" stop-color="#a855f7"/>
      <stop offset="100%" stop-color="#53d5fa"/>
    </linearGradient>
    <linearGradient id="cardBg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#12112a" stop-opacity="0.94"/>
      <stop offset="100%" stop-color="#0a0919" stop-opacity="0.97"/>
    </linearGradient>
    <linearGradient id="cardHighlight" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#231138" stop-opacity="0.96"/>
      <stop offset="100%" stop-color="#0f0c24" stop-opacity="0.96"/>
    </linearGradient>
    <filter id="glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="5" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="logoClip"><rect x="48" y="34" width="52" height="52" rx="12"/></clipPath>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#ffffff" stroke-opacity="0.035" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="{w}" height="{h}" fill="url(#bg)"/>
  <rect width="{w}" height="{h}" fill="url(#grid)"/>
  <circle cx="{w-140}" cy="90" r="220" fill="#ff1493" fill-opacity="0.08" filter="url(#glow)"/>
  <circle cx="220" cy="{h-60}" r="240" fill="#53d5fa" fill-opacity="0.06" filter="url(#glow)"/>

  <!-- Header Bar -->
  <rect x="44" y="30" width="60" height="60" rx="15" fill="#ff1493" fill-opacity="0.14" stroke="#ff54b4" stroke-opacity="0.6"/>
  <image href="{LOGO_URI}" x="48" y="34" width="52" height="52" preserveAspectRatio="xMidYMid slice" clip-path="url(#logoClip)"/>
  <text x="118" y="69" fill="#faf6ff" font-family="{FONT_SANS}" font-size="32" font-weight="700" letter-spacing="-0.8">yubiOS</text>
  <line x1="242" y1="42" x2="242" y2="78" stroke="#3f3a5a" stroke-width="1.5"/>
  <text x="260" y="66" fill="#d3c9db" font-family="{FONT_MONO}" font-size="14" font-weight="700" letter-spacing="1.2">ASSUME NOTHING. PROVE EVERYTHING.</text>

  <rect x="{badge_x}" y="38" width="{badge_w}" height="40" rx="20" fill="#110e24" stroke="#ff2a9d" stroke-opacity="0.65" stroke-width="1.5"/>
  <circle cx="{badge_x+24}" cy="58" r="5" fill="#89ff35" filter="url(#glow)"/>
  <text x="{badge_x+40}" y="63" fill="#faf6ff" font-family="{FONT_MONO}" font-size="12.5" font-weight="700" letter-spacing="0.8">{esc(badge_text)}</text>
  <line x1="44" y1="104" x2="{w-44}" y2="104" stroke="#282342" stroke-width="1.5"/>
'''

def svg_footer(w: int, h: int, left_note: str = "Open-source project • github.com/yubi-OS/yubiOS") -> str:
    return f'''
  <line x1="44" y1="{h-48}" x2="{w-44}" y2="{h-48}" stroke="#282342" stroke-width="1"/>
  <text x="44" y="{h-22}" fill="#978fa8" font-family="{FONT_MONO}" font-size="12.5">{esc(left_note)}</text>
  <text x="{w-44}" y="{h-22}" text-anchor="end" fill="#978fa8" font-family="{FONT_SANS}" font-size="12">Independent community project. Not affiliated with Yubico. Linux® is a registered trademark of Linus Torvalds.</text>
</svg>'''

def build_banner_01_architecture() -> str:
    w, h = 1360, 480
    s = [svg_header(w, h, "yubiOS Two-Domain Security Architecture")]
    s.append(f'<text x="44" y="152" fill="#faf6ff" font-family="{FONT_SANS}" font-size="33" font-weight="700" letter-spacing="-0.6">Two Separate Trust Questions. Two Independent Hardware Domains.</text>')
    s.append(f'<text x="44" y="182" fill="#c8cce2" font-family="{FONT_SANS}" font-size="17.5">Conventional Linux blurs user login and board integrity into a single OEM-controlled TPM. yubiOS splits them cleanly.</text>')

    s.append(f'''
    <rect x="44" y="206" width="618" height="208" rx="16" fill="url(#cardHighlight)" stroke="#ff2a9d" stroke-width="2"/>
    <rect x="68" y="226" width="300" height="28" rx="14" fill="#ff2a9d" fill-opacity="0.2" stroke="#ff2a9d"/>
    <text x="84" y="245" fill="#ff7ac6" font-family="{FONT_MONO}" font-size="12" font-weight="700">DOMAIN 1 • OWNER IDENTITY ROOT</text>
    <text x="68" y="282" fill="#ffffff" font-family="{FONT_SANS}" font-size="24" font-weight="700">Your Physical U2F/HSM Token</text>
    <text x="68" y="308" fill="#d3c9db" font-family="{FONT_SANS}" font-size="15">Answers: &quot;Is the authorized human owner physically present?&quot;</text>
    <text x="68" y="338" fill="#faf6ff" font-family="{FONT_MONO}" font-size="13.5">• PIV Slot 9a (PKCS#11) : Signs systemd-boot &amp; Type2 UKI</text>
    <text x="68" y="360" fill="#faf6ff" font-family="{FONT_MONO}" font-size="13.5">• FIDO2 hmac-secret     : Decrypts LUKS2 root &amp; systemd-homed</text>
    <text x="68" y="382" fill="#faf6ff" font-family="{FONT_MONO}" font-size="13.5">• FIDO2 ed25519-sk      : Resident SSH keys + pam-u2f sudo</text>

    <rect x="698" y="206" width="618" height="208" rx="16" fill="url(#cardBg)" stroke="#53d5fa" stroke-width="2"/>
    <rect x="722" y="226" width="328" height="28" rx="14" fill="#53d5fa" fill-opacity="0.16" stroke="#53d5fa"/>
    <text x="738" y="245" fill="#7ce2ff" font-family="{FONT_MONO}" font-size="12" font-weight="700">DOMAIN 2 • PLATFORM INTEGRITY ROOT</text>
    <text x="722" y="282" fill="#ffffff" font-family="{FONT_SANS}" font-size="24" font-weight="700">ARM64 OP-TEE 4.11 Secure World (TEE)</text>
    <text x="722" y="308" fill="#d3c9db" font-family="{FONT_SANS}" font-size="15">Answers: &quot;Did the expected firmware, kernel, and OS image boot?&quot;</text>
    <text x="722" y="338" fill="#faf6ff" font-family="{FONT_MONO}" font-size="13.5">• TF-A BL31 v2.15 + U-Boot : Owner-provisioned UEFI Secure Boot</text>
    <text x="722" y="360" fill="#faf6ff" font-family="{FONT_MONO}" font-size="13.5">• OP-TEE StandaloneMM      : Authenticated PK / KEK / db store</text>
    <text x="722" y="382" fill="#faf6ff" font-family="{FONT_MONO}" font-size="13.5">• OP-TEE fTPM + Composefs  : PCRs 0..7, 11 + verity=require /usr</text>
    ''')

    s.append(svg_footer(w, h))
    return "\n".join(s)

def build_banner_02_hardware() -> str:
    w, h = 1360, 560
    s = [svg_header(w, h, "yubiOS Hardware & Platform Lineup")]
    s.append(f'<text x="44" y="150" fill="#faf6ff" font-family="{FONT_SANS}" font-size="33" font-weight="700" letter-spacing="-0.6">Pre-Installed ARM64 Hardware + Bring-Your-Own x86-64 Setup Mode</text>')
    s.append(f'<text x="44" y="180" fill="#c8cce2" font-family="{FONT_SANS}" font-size="17.5">Get a pre-flashed board ready to bind to your U2F/HSM on first boot, or enroll your own x86-64 machine in UEFI Setup Mode.</text>')

    cards = [
        ("RADXA ROCK 5B", "RK3588 • 16 GB LPDDR4x", "FLAGSHIP • PROVEN", "#89ff35", "#ff2a9d", [
            "8-core (4×A76 + 4×A55)",
            "Full 5-step U2F/HSM enroll",
            "Enforcing UEFI Secure Boot",
            "OP-TEE 4.11 fTPM + StMM",
            "GNOME Wayland + Antimony",
            "Pre-installed reward tier",
        ]),
        ("PINE64 ROCKPRO64", "RK3399 • 4 GB LPDDR4", "SUPPORTED • PRE-INSTALLED", "#89ff35", "#a855f7", [
            "6-core (2×A72 + 4×A53)",
            "TF-A + OP-TEE + U-Boot UEFI",
            "Headless / Desktop / Flasher",
            "Mutual strongbox attestation",
            "Composefs verity=require /usr",
            "Pre-installed reward tier",
        ]),
        ("PINE64 PINETAB2", "RK3566 • 8 GB Mobile Tablet", "UNDER INVESTIGATION", "#fbbf24", "#64748b", [
            "4-core Cortex-A55 tablet",
            "CI firmware target built",
            "Active UART/USB-boot testing",
            "No SPI NOR recovery guard",
            "Stretch / R&D investigation",
            "Not sold until gate passes",
        ]),
        ("x86-64 BOARDS & PCs", "UEFI Setup Mode Machines", "EXPANDING • BYO HARDWARE", "#53d5fa", "#53d5fa", [
            "No custom board FW required",
            "Enroll PK/KEK/db in SetupMode",
            "Sign UKI via U2F/HSM Slot 9a",
            "FIDO2 LUKS2 + systemd-homed",
            "bootc OCI atomic upgrades",
            "Run on your existing PC/server",
        ]),
    ]

    cw = 298
    gap = 26
    for idx, (title, sub, status, dot_col, border_col, bullets) in enumerate(cards):
        x = 44 + idx * (cw + gap)
        y = 204
        s.append(f'<rect x="{x}" y="{y}" width="{cw}" height="288" rx="15" fill="url(#cardBg)" stroke="{border_col}" stroke-width="1.8"/>')
        s.append(f'<circle cx="{x+22}" cy="{y+26}" r="5" fill="{dot_col}"/>')
        s.append(f'<text x="{x+36}" y="{y+31}" fill="{dot_col}" font-family="{FONT_MONO}" font-size="11.5" font-weight="700">{esc(status)}</text>')
        s.append(f'<text x="{x+20}" y="{y+64}" fill="#ffffff" font-family="{FONT_SANS}" font-size="21" font-weight="700">{esc(title)}</text>')
        s.append(f'<text x="{x+20}" y="{y+86}" fill="#ff7ac6" font-family="{FONT_MONO}" font-size="12.5" font-weight="700">{esc(sub)}</text>')
        s.append(f'<line x1="{x+20}" y1="{y+100}" x2="{x+cw-20}" y2="{y+100}" stroke="#2b2644" stroke-width="1"/>')
        for b_idx, b in enumerate(bullets):
            by = y + 126 + b_idx * 26
            s.append(f'<text x="{x+20}" y="{by}" fill="#e2dcf0" font-family="{FONT_SANS}" font-size="14">• {esc(b)}</text>')

    s.append(svg_footer(w, h))
    return "\n".join(s)

def build_banner_03_proof_of_life() -> str:
    w, h = 1360, 520
    s = [svg_header(w, h, "yubiOS Live Hardware Proof of Life", "VERIFIED ON RADXA ROCK 5B HARDWARE")]
    s.append(f'<text x="44" y="150" fill="#faf6ff" font-family="{FONT_SANS}" font-size="33" font-weight="700" letter-spacing="-0.6">Proof of Life: Watch the 5-Step Hardware Enrollment on Real Silicon</text>')
    s.append(f'<text x="44" y="180" fill="#c8cce2" font-family="{FONT_SANS}" font-size="17.5">Recorded live over UART &amp; HDMI on a Radxa ROCK 5B (16 GB). Asciinema: asciinema.org/a/y9sHQPQTIbTWNIyr</text>')

    s.append(f'''
    <rect x="44" y="202" width="760" height="252" rx="14" fill="#060712" stroke="#53d5fa" stroke-opacity="0.7" stroke-width="1.5"/>
    <rect x="44" y="202" width="760" height="34" rx="14" fill="#131629"/>
    <circle cx="68" cy="219" r="6" fill="#ff5f56"/>
    <circle cx="88" cy="219" r="6" fill="#ffbd2e"/>
    <circle cx="108" cy="219" r="6" fill="#27c93f"/>
    <text x="134" y="224" fill="#97a0c4" font-family="{FONT_MONO}" font-size="12">ttyS2 / tty1 - yubiOS-enroll.service (refs/logs/fvf13-224bf224.new)</text>

    <text x="64" y="260" fill="#53d5fa" font-family="{FONT_MONO}" font-size="12.5">[boot] BL31: v2.15.0(release):yubiOS | OP-TEE 4.11 (fTPM + StandaloneMM)</text>
    <text x="64" y="282" fill="#89ff35" font-family="{FONT_MONO}" font-size="12.5">[1/5] yubiOS-enroll-sb   : PIV slot 9a PK/KEK/db -&gt; StMM (SetupMode 1 -&gt; 0)</text>
    <text x="64" y="304" fill="#89ff35" font-family="{FONT_MONO}" font-size="12.5">[2/5] yubiOS-enroll-luks : /dev/mmcblk1p3 LUKS2 FIDO2 hmac-secret + LVM</text>
    <text x="64" y="326" fill="#89ff35" font-family="{FONT_MONO}" font-size="12.5">[3/5] yubiOS-enroll-homed: /var/home/yubios.home LUKS2+ext4 FIDO2 bound</text>
    <text x="64" y="348" fill="#89ff35" font-family="{FONT_MONO}" font-size="12.5">[4/5] yubiOS-enroll-ssh  : OpenSSH resident ed25519-sk key generated on key</text>
    <text x="64" y="370" fill="#89ff35" font-family="{FONT_MONO}" font-size="12.5">[5/5] yubiOS-enroll-pam  : pam-u2f registered (/etc/yubico/u2f_keys)</text>
    <text x="64" y="396" fill="#ff7ac6" font-family="{FONT_MONO}" font-size="12.5">[reboot] secureboot: Secure boot enabled | Kernel locked down | YUBIOS_TPM_OK</text>
    <text x="64" y="418" fill="#faf6ff" font-family="{FONT_MONO}" font-size="12.5">[desktop] gdm-wayland-session + Antimony v156.0.8078.47-1 + local OCI signed</text>
    <text x="64" y="440" fill="#53d5fa" font-family="{FONT_MONO}" font-size="12">▶ Watch unedited capture: https://asciinema.org/a/y9sHQPQTIbTWNIyr</text>

    <rect x="828" y="202" width="488" height="252" rx="14" fill="url(#cardHighlight)" stroke="#ff2a9d" stroke-width="1.8"/>
    <text x="854" y="242" fill="#ffffff" font-family="{FONT_SANS}" font-size="22" font-weight="700">Zero Mockups. Raw Hardware Logs.</text>
    <text x="854" y="272" fill="#d3c9db" font-family="{FONT_SANS}" font-size="15">Every claim in this campaign links to a committed</text>
    <text x="854" y="292" fill="#d3c9db" font-family="{FONT_SANS}" font-size="15">UART capture and reproducible CI workflow:</text>
    <text x="854" y="324" fill="#89ff35" font-family="{FONT_MONO}" font-size="13">✓ fvf13-224bf224.new (5,622 lines)</text>
    <text x="854" y="344" fill="#c8cce2" font-family="{FONT_SANS}" font-size="13.5">  5-step U2F/HSM ceremony + Secure Boot</text>
    <text x="854" y="372" fill="#89ff35" font-family="{FONT_MONO}" font-size="13">✓ fvf14-a76322cd.new (23,167 lines)</text>
    <text x="854" y="392" fill="#c8cce2" font-family="{FONT_SANS}" font-size="13.5">  3-boot capture, GNOME Wayland, Antimony</text>
    <text x="854" y="422" fill="#89ff35" font-family="{FONT_MONO}" font-size="13">✓ Two-Build Bit-for-Bit Reproducibility</text>
    <text x="854" y="442" fill="#c8cce2" font-family="{FONT_SANS}" font-size="13.5">  Verified across isolated BuildKit daemons</text>
    ''')

    s.append(svg_footer(w, h))
    return "\n".join(s)

def build_banner_04_certification() -> str:
    w, h = 1360, 520
    s = [svg_header(w, h, "GlobalPlatform TEE Certification Strategy", "COMMUNITY-FUNDED TEE CERTIFICATION")]
    s.append(f'<text x="44" y="150" fill="#faf6ff" font-family="{FONT_SANS}" font-size="33" font-weight="700" letter-spacing="-0.6">Path to GlobalPlatform TEE Certification: Two-Stage Funding Model</text>')
    s.append(f'<text x="44" y="180" fill="#c8cce2" font-family="{FONT_SANS}" font-size="17.5">Aiming to become the first open-source, community-funded project to submit a TEE for GlobalPlatform Security Evaluation.</text>')

    s.append(f'''
    <rect x="44" y="204" width="618" height="248" rx="16" fill="url(#cardHighlight)" stroke="#ff2a9d" stroke-width="2.2"/>
    <rect x="68" y="224" width="320" height="30" rx="15" fill="#ff2a9d" fill-opacity="0.22" stroke="#ff2a9d"/>
    <text x="84" y="244" fill="#ff85cb" font-family="{FONT_MONO}" font-size="12.5" font-weight="700">CAMPAIGN 1 (NOW) • $10,000 GOAL</text>
    <text x="68" y="282" fill="#ffffff" font-family="{FONT_SANS}" font-size="24" font-weight="700">Initial 3rd-Party Accredited Lab Testing</text>
    <text x="68" y="312" fill="#e2dcf0" font-family="{FONT_SANS}" font-size="15">• Accredited security lab pre-evaluation &amp; gap readiness</text>
    <text x="68" y="338" fill="#e2dcf0" font-family="{FONT_SANS}" font-size="15">• Authoring the Security Target (ST) against TEE PP (EAL2+)</text>
    <text x="68" y="364" fill="#e2dcf0" font-family="{FONT_SANS}" font-size="15">• OP-TEE 4.11 fTPM + StandaloneMM conformance &amp; fuzz harness</text>
    <text x="68" y="390" fill="#e2dcf0" font-family="{FONT_SANS}" font-size="15">• Sacrificial board eFuse ROTPK + eMMC RPMB write-lock proof</text>
    <text x="68" y="424" fill="#89ff35" font-family="{FONT_MONO}" font-size="13" font-weight="700">Deliverable: Published Lab Pre-Assessment &amp; Frozen TOE</text>

    <rect x="698" y="204" width="618" height="248" rx="16" fill="url(#cardBg)" stroke="#53d5fa" stroke-width="2"/>
    <rect x="722" y="224" width="376" height="30" rx="15" fill="#53d5fa" fill-opacity="0.16" stroke="#53d5fa"/>
    <text x="738" y="244" fill="#7ce2ff" font-family="{FONT_MONO}" font-size="12.5" font-weight="700">CAMPAIGN 2 (NEXT PHASE) • ~$100,000 GOAL</text>
    <text x="722" y="282" fill="#ffffff" font-family="{FONT_SANS}" font-size="24" font-weight="700">Full GlobalPlatform TEE Certification</text>
    <text x="722" y="312" fill="#e2dcf0" font-family="{FONT_SANS}" font-size="15">• Launched only after Phase 1 lab readiness passes</text>
    <text x="722" y="338" fill="#e2dcf0" font-family="{FONT_SANS}" font-size="15">• GlobalPlatform Certification Body fee ($29k-$36k schedule)</text>
    <text x="722" y="364" fill="#e2dcf0" font-family="{FONT_SANS}" font-size="15">• Full accredited lab white-box + black-box penetration testing</text>
    <text x="722" y="390" fill="#e2dcf0" font-family="{FONT_SANS}" font-size="15">• Attack Catalog (AVA_VAN_AP.3) &amp; Evaluation Technical Report</text>
    <text x="722" y="424" fill="#53d5fa" font-family="{FONT_MONO}" font-size="13" font-weight="700">Milestone: First Community-Certified Open-Source TEE</text>
    ''')

    s.append(svg_footer(w, h))
    return "\n".join(s)

def build_banner_05_roadmap() -> str:
    w, h = 1360, 560
    s = [svg_header(w, h, "yubiOS Roadmap to Completion", "ENGINEERING & CERTIFICATION ROADMAP")]
    s.append(f'<text x="44" y="150" fill="#faf6ff" font-family="{FONT_SANS}" font-size="33" font-weight="700" letter-spacing="-0.6">Roadmap to Completion: From Technical Preview to Certified TEE</text>')
    s.append(f'<text x="44" y="180" fill="#c8cce2" font-family="{FONT_SANS}" font-size="17.5">Every phase is gated by public repo evidence, reproducible CI artifacts, and hardware UART logs.</text>')

    stages = [
        ("STAGE 0 • COMPLETE", "Nov 2026 (v0.8.94)", "Technical Preview Live", "#89ff35", [
            "✓ ROCK 5B 5-step U2F/HSM enroll",
            "✓ Enforcing UEFI Secure Boot",
            "✓ OP-TEE 4.11 fTPM + StMM live",
            "✓ Composefs + 3-way /usr Overlay",
            "✓ GNOME Wayland + Antimony v156",
            "✓ Two-build reproducible CI",
        ]),
        ("STAGE 1 • $10K CAMPAIGN", "Q1 2027", "3rd-Party Lab Pre-Test", "#ff2a9d", [
            "• Accredited lab pre-assessment",
            "• GlobalPlatform TEE PP ST draft",
            "• Sacrificial ROCK 5B eFuse burn",
            "• eMMC RPMB write-lock proof",
            "• RockPro64 pre-install batch QA",
            "• PineTab2 USB-boot investigation",
        ]),
        ("STAGE 2 • x86 & NODES", "Q2 2027", "x86 Setup & Assured Nodes", "#53d5fa", [
            "• x86-64 UEFI Setup-Mode installer",
            "• U2F/HSM Slot 9a signing on PC",
            "• Assured Node early-access launch",
            "• yubios-attest remote PCR+PIV",
            "• Pre-installed ROCK 5B & RockPro64",
            "  shipments to Stage 1 backers",
        ]),
        ("STAGE 3 • $100K CAMPAIGN", "Q3-Q4 2027", "GP TEE Certification", "#a855f7", [
            "• Community $100k cert campaign",
            "• Formal GP Cert Body filing",
            "• 3-month accredited lab eval",
            "• White-box + black-box pen test",
            "• Public Evaluation Tech Report",
            "• Production v1.0 release",
        ]),
    ]

    cw = 298
    gap = 26
    for idx, (tag, date_str, title, col, items) in enumerate(stages):
        x = 44 + idx * (cw + gap)
        y = 206
        s.append(f'<rect x="{x}" y="{y}" width="{cw}" height="284" rx="15" fill="url(#cardBg)" stroke="{col}" stroke-width="2"/>')
        s.append(f'<rect x="{x+18}" y="{y+18}" width="{cw-36}" height="26" rx="13" fill="{col}" fill-opacity="0.18"/>')
        s.append(f'<text x="{x+28}" y="{y+35}" fill="{col}" font-family="{FONT_MONO}" font-size="11" font-weight="700">{esc(tag)}</text>')
        s.append(f'<text x="{x+18}" y="{y+66}" fill="#ffffff" font-family="{FONT_SANS}" font-size="18" font-weight="700">{esc(title)}</text>')
        s.append(f'<text x="{x+18}" y="{y+88}" fill="#97a0c4" font-family="{FONT_MONO}" font-size="12">{esc(date_str)}</text>')
        s.append(f'<line x1="{x+18}" y1="{y+100}" x2="{x+cw-18}" y2="{y+100}" stroke="#2b2644" stroke-width="1"/>')
        for i_idx, item in enumerate(items):
            iy = y + 124 + i_idx * 25
            s.append(f'<text x="{x+18}" y="{iy}" fill="#e2dcf0" font-family="{FONT_SANS}" font-size="13.2">{esc(item)}</text>')

    s.append(svg_footer(w, h))
    return "\n".join(s)

def build_banner_06_rewards() -> str:
    w, h = 1360, 580
    s = [svg_header(w, h, "yubiOS Backer Reward Tiers", "EARLY ACCESS • HARDWARE & ASSURED NODES")]
    s.append(f'<text x="44" y="150" fill="#faf6ff" font-family="{FONT_SANS}" font-size="33" font-weight="700" letter-spacing="-0.6">What Contributing Members Receive: Assured Nodes or Hardware in Hand</text>')
    s.append(f'<text x="44" y="180" fill="#c8cce2" font-family="{FONT_SANS}" font-size="17.5">Every hardware unit ships pre-flashed with yubiOS and binds its full root of trust to your own U2F/HSM on first boot.</text>')

    tiers = [
        ("$25", "x86 Setup Builder", "DIGITAL • OPEN SOURCE", "#97a0c4", [
            "Name in repo CREDITS.md",
            "x86 UEFI Setup-Mode Kit",
            "U2F/HSM Slot 9a scripts",
            "Signed SLSA provenance",
            "Lab pre-test updates",
        ]),
        ("$99", "Assured Node Pass", "CLOUD NODE EARLY ACCESS", "#53d5fa", [
            "Assured Node early access",
            "on yubi-OS infrastructure",
            "yubios-attest remote check",
            "fTPM PCR + PIV quote",
            "Verify boot before run",
        ]),
        ("$249", "RockPro64 Kit", "PRE-INSTALLED RK3399", "#a855f7", [
            "RockPro64 (RK3399, 4GB)",
            "Pre-flashed 64GB microSD",
            "TF-A + OP-TEE 4.11 + UEFI",
            "5-step U2F/HSM first boot",
            "+ 30-day Assured Node",
        ]),
        ("$399", "ROCK 5B Flagship", "PRE-INSTALLED RK3588 16G", "#ff2a9d", [
            "Radxa ROCK 5B (16GB RAM)",
            "Pre-flashed 128GB microSD",
            "Enforcing SB + OP-TEE fTPM",
            "GNOME Wayland + Antimony",
            "Root of trust -> YOUR key",
            "+ 90-day Assured Node",
        ]),
        ("$749", "TEE Lab Patron", "ROCK 5B 16G + 1YR NODE", "#89ff35", [
            "ROCK 5B (16GB) Flagship",
            "Dual-board flasher script",
            "1-year Assured Node pass",
            "Named sponsor in Phase 1",
            "Lab Pre-Assessment & ST",
        ]),
    ]

    cw = 236
    gap = 22
    for idx, (price, name, badge, col, lines) in enumerate(tiers):
        x = 44 + idx * (cw + gap)
        y = 204
        bg = "url(#cardHighlight)" if price == "$399" else "url(#cardBg)"
        sw = "2.5" if price == "$399" else "1.6"
        s.append(f'<rect x="{x}" y="{y}" width="{cw}" height="304" rx="15" fill="{bg}" stroke="{col}" stroke-width="{sw}"/>')
        s.append(f'<text x="{x+16}" y="{y+34}" fill="{col}" font-family="{FONT_MONO}" font-size="10.5" font-weight="700">{esc(badge)}</text>')
        s.append(f'<text x="{x+16}" y="{y+78}" fill="#ffffff" font-family="{FONT_SANS}" font-size="35" font-weight="700">{esc(price)}</text>')
        s.append(f'<text x="{x+16}" y="{y+106}" fill="#faf6ff" font-family="{FONT_SANS}" font-size="16.5" font-weight="700">{esc(name)}</text>')
        s.append(f'<line x1="{x+16}" y1="{y+120}" x2="{x+cw-16}" y2="{y+120}" stroke="#2b2644" stroke-width="1"/>')
        for l_idx, ln in enumerate(lines):
            ly = y + 146 + l_idx * 25
            s.append(f'<text x="{x+16}" y="{ly}" fill="#e2dcf0" font-family="{FONT_SANS}" font-size="12.6">• {esc(ln)}</text>')

    s.append(svg_footer(w, h))
    return "\n".join(s)

def render_svg_to_png(svg_content: str, svg_name: str, png_name: str, width: int, height: int):
    svg_path = SOURCE / svg_name
    html_path = SOURCE / (svg_name + ".html")
    png_path = ASSETS / png_name
    svg_path.write_text(svg_content, encoding="utf-8")
    html_doc = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body {{ width: {width}px; height: {height}px; overflow: hidden; background: #040511; }}
svg {{ display: block; width: {width}px; height: {height}px; }}
</style></head><body>{svg_content}</body></html>"""
    html_path.write_text(html_doc, encoding="utf-8")
    subprocess.run(
        [
            "chrome-headless-shell",
            "--headless",
            "--no-sandbox",
            "--disable-gpu",
            "--hide-scrollbars",
            f"--window-size={width},{height}",
            f"--screenshot={png_path}",
            f"file://{html_path.resolve()}",
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    html_path.unlink(missing_ok=True)
    print(f"Rendered {png_path.name} ({width}x{height}, {png_path.stat().st_size} bytes)")

def main():
    banners = [
        (build_banner_01_architecture(), "01-trust-architecture.svg", "01-trust-architecture-1360x480.png", 1360, 480),
        (build_banner_02_hardware(), "02-hardware-lineup.svg", "02-hardware-lineup-1360x560.png", 1360, 560),
        (build_banner_03_proof_of_life(), "03-enrollment-proof-of-life.svg", "03-enrollment-proof-of-life-1360x520.png", 1360, 520),
        (build_banner_04_certification(), "04-globalplatform-tee-certification.svg", "04-globalplatform-tee-certification-1360x520.png", 1360, 520),
        (build_banner_05_roadmap(), "05-roadmap-to-completion.svg", "05-roadmap-to-completion-1360x560.png", 1360, 560),
        (build_banner_06_rewards(), "06-reward-tiers.svg", "06-reward-tiers-1360x580.png", 1360, 580),
    ]
    for svg_str, s_name, p_name, w, h in banners:
        render_svg_to_png(svg_str, s_name, p_name, w, h)

    # Write SHA256SUMS
    sums = []
    for p in sorted(ASSETS.glob("*")):
        if p.is_file() and p.name != "SHA256SUMS":
            digest = hashlib.sha256(p.read_bytes()).hexdigest()
            sums.append(f"{digest}  assets/{p.name}")
    for p in sorted(SOURCE.glob("*.svg")):
        digest = hashlib.sha256(p.read_bytes()).hexdigest()
        sums.append(f"{digest}  source/{p.name}")
    (ROOT / "SHA256SUMS").write_text("\n".join(sums) + "\n", encoding="utf-8")
    print("Wrote SHA256SUMS")

if __name__ == "__main__":
    main()
