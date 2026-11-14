#!/usr/bin/env python3
"""Rebuild the two full-page campaign layouts and their delivery exports."""
from pathlib import Path
import base64
import subprocess
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / 'source'

def data_uri(path):
    return 'data:image/png;base64,' + base64.b64encode(path.read_bytes()).decode()

def text(x, y, size, content, color, weight=700, spacing=-2, family='Nimbus Sans, sans-serif', anchor='start'):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" fill="{color}" font-weight="{weight}" letter-spacing="{spacing}" font-family="{family}">{content}</text>'

def make_svg(theme):
    light = theme == 'light'
    ink = '#10142a' if light else '#f6f5ff'
    quiet = '#363c5c' if light else '#c8cce2'
    base = '#e1e5fa' if light else '#020616'
    start = '#c20b87' if light else '#ff43b0'
    end = '#475bc6' if light else '#53d5fa'
    badge = '#f3f1ff' if light else '#11142d'
    rule = '#a2a8c4' if light else '#3f4763'
    foundation = data_uri(SOURCE / 'foundations' / f'seal-{theme}.png')
    logo = data_uri(SOURCE / 'logo.png')
    svg = [f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="3840" height="2160" viewBox="0 0 1920 1080">
<title>yubiOS — Signed, Sealed, Delivered: It's Yours</title>
<desc>{theme.title()} full-page campaign artwork. Original yubiOS flower logo, large tagline, and a luminous layered glass sphere centered against the headline. Technical Preview.</desc>
<defs>
  <linearGradient id="ownership" x1="0" y1="0" x2="1" y2="0"><stop stop-color="{start}"/><stop offset="1" stop-color="{end}"/></linearGradient>
</defs>
<rect width="1920" height="1080" fill="{base}"/>
<!-- Uniformly reframe the foundation so the sphere balances the headline;
     its silhouette sits approximately x=1090..1770, y=200..870. -->
<image x="-335" y="-146" width="2400" height="1350" xlink:href="{foundation}" preserveAspectRatio="xMidYMid slice"/>
<!-- Canonical logo preserved as an embedded image, never regenerated. -->
<image x="112" y="88" width="80" height="80" xlink:href="{logo}"/>
<!-- Label measures 257.3 px; 24 px side padding + 10 px dot + 12 px gap. -->
<rect x="1480" y="100" width="328" height="56" rx="28" fill="{badge}" stroke="{rule}" stroke-width="1.5"/>
<circle cx="1509" cy="128" r="5" fill="{start}"/>
''']
    svg += [text(216, 151, 58, 'yubiOS', ink, spacing=-1.9),
            text(1526, 139, 30, 'Technical Preview', ink, spacing=0),
            text(112, 352, 98, 'Signed,', ink, spacing=-3.1),
            text(112, 465, 98, 'Sealed,', ink, spacing=-3.1),
            text(112, 578, 98, 'Delivered:', ink, spacing=-3.1),
            text(104, 786, 160, 'It’s Yours', 'url(#ownership)', spacing=-7)]
    svg.append(f'<path d="M 112 930 H 1808" stroke="{rule}" stroke-width="1.5"/>')
    svg.append(text(112, 992, 30, 'github.com/yubi-OS/yubiOS', quiet, 400, 0))
    svg.append(text(1808, 992, 30, 'Open-source project', quiet, 400, 0, anchor='end'))
    svg.append('</svg>')
    return '\n'.join(svg)

def main():
    (ROOT / 'png').mkdir(exist_ok=True)
    (ROOT / 'webp').mkdir(exist_ok=True)
    for theme in ('dark', 'light'):
        name = f'yubios-signed-sealed-delivered-fullpage-{theme}'
        svg_path = SOURCE / f'{name}.svg'
        svg_path.write_text(make_svg(theme))
        png_path = ROOT / 'png' / f'{name}-3840x2160.png'
        subprocess.run(['inkscape', str(svg_path), '--export-type=png', f'--export-filename={png_path}'], check=True, stdout=subprocess.DEVNULL)
        with Image.open(png_path) as im:
            im.convert('RGB').resize((1920, 1080), Image.Resampling.LANCZOS).save(ROOT / 'webp' / f'{name}-1920x1080.webp', quality=93, method=6)

    sheet = Image.new('RGB', (1360, 1690), '#121522')
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.truetype('/usr/share/fonts/opentype/urw-base35/NimbusSans-Regular.otf', 26)
    draw.text((40, 26), 'yubiOS / Technical Preview / Full-page campaign', font=font, fill='#f6f5ff')
    for n, theme in enumerate(('dark', 'light')):
        y = 92 + n*790
        name = f'yubios-signed-sealed-delivered-fullpage-{theme}-3840x2160.png'
        with Image.open(ROOT / 'png' / name) as im:
            im.thumbnail((1280, 720), Image.Resampling.LANCZOS)
            sheet.paste(im, (40, y))
        draw.text((40, y+733), f'{theme.title()} / 3840 × 2160', font=font, fill='#c8cce2')
    sheet.save(ROOT / 'preview.jpg', quality=94)

if __name__ == '__main__':
    main()
