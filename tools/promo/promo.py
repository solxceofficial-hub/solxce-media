"""Solxce promo video maker.

Turns a slide deck (HTML page of <section class="slide"> 1080x1920, or a folder of 9:16 PNGs)
into a beat-synced MP4 with an original soundtrack, plus a cover image and ready-to-paste
TikTok / Instagram captions with hashtags.

    python3 promo.py                 # build every video in videos.py
    python3 promo.py 04-hyrox        # build one
"""
import os, sys, math, subprocess, json, shutil
import numpy as np
from PIL import Image
import music

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS = 1080, 1920, 30
OUT = os.path.join(HERE, 'out')

HIDE_SWIPE = """<style>.swipe{display:none!important}</style>"""


def slides_from_html(path, sub_fix=None):
    """Re-render each <section class="slide"> to an image, hiding 'Swipe ->' prompts."""
    from playwright.sync_api import sync_playwright
    src = open(path).read().replace('</head>', HIDE_SWIPE + '</head>', 1)
    for a, b in (sub_fix or {}).items():
        src = src.replace(a, b)
    tmp = os.path.join(os.path.dirname(path), '_video_' + os.path.basename(path))
    open(tmp, 'w').write(src)
    imgs = []
    try:
        with sync_playwright() as p:
            b = p.chromium.launch()
            pg = b.new_page(viewport={'width': W, 'height': H})
            pg.goto('file://' + tmp)
            try: pg.wait_for_selector('body[data-ready]', timeout=5000)
            except Exception: pass
            pg.wait_for_timeout(300)
            secs = pg.locator('section.slide')
            for i in range(secs.count()):
                f = os.path.join(OUT, '_tmp_slide.png')
                secs.nth(i).screenshot(path=f)
                imgs.append(Image.open(f).convert('RGB').resize((W, H)))
            b.close()
    finally:
        os.remove(tmp)
    return imgs


def slides_from_dir(d):
    fs = sorted(f for f in os.listdir(d) if f.lower().endswith(('.png', '.jpg', '.jpeg')))
    return [Image.open(os.path.join(d, f)).convert('RGB').resize((W, H)) for f in fs]


def timing(n, bpm):
    beat = 60 / bpm
    hook = max(4, round(2.2 / beat)); mid = max(4, round(2.5 / beat)); cta = max(6, round(3.4 / beat))
    beats = [hook] + [mid] * (n - 2) + [cta]
    starts = np.cumsum([0] + beats) * beat
    return starts, beat


def render(v):
    name, style = v['name'], v['style']
    os.makedirs(OUT, exist_ok=True)
    slides = slides_from_html(v['html'], v.get('sub_fix')) if 'html' in v else slides_from_dir(v['dir'])
    silent = v.get('silent', False)
    starts, beat = timing(len(slides), 120 if silent else music.STYLES[style])
    total = float(starts[-1])
    vdir = os.path.join(OUT, name); os.makedirs(vdir, exist_ok=True)
    wav = os.path.join(vdir, '_music.wav')
    if not silent: music.make(style, total, wav)
    slides[0].save(os.path.join(vdir, f'solxce-{name}-cover.jpg'), quality=92)

    mp4 = os.path.join(vdir, f'solxce-{name}.mp4')
    cmd = ['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y',
           '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
           *([] if silent else ['-i', wav]), '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p',
           '-profile:v', 'high', *(['-an'] if silent else ['-c:a', 'aac', '-b:a', '192k', '-shortest']), '-movflags', '+faststart', mp4]
    ff = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    white = Image.new('RGB', (W, H), (255, 255, 255))
    nframes = int(round(total * FPS))
    for f in range(nframes):
        t = f / FPS
        i = int(np.searchsorted(starts, t, side='right') - 1); i = min(i, len(slides) - 1)
        k = (t - starts[i]) * FPS                      # frames since cut
        p = (t - starts[i]) / (starts[i + 1] - starts[i])
        since_beat = (t - starts[i]) % beat
        pulse = 0 if silent else math.exp(-since_beat / 0.07)
        punch = 0.10 if i == 0 else 0.065
        scale = 1.0 + 0.04 * p + punch * math.exp(-k / 3.0) + 0.010 * pulse
        cw, ch = W / scale, H / scale
        drift = (1 if i % 2 else -1) * 12 * p
        x0 = (W - cw) / 2 + drift; y0 = (H - ch) / 2
        img = slides[i].resize((W, H), Image.BILINEAR, box=(x0, y0, x0 + cw, y0 + ch))
        a = (0.55 if i else 0.75) * math.exp(-k / 1.6)
        if a > 0.01:
            img = Image.blend(img, white, a)
        ff.stdin.write(img.tobytes())
    ff.stdin.close(); ff.wait()
    if not silent: os.remove(wav)

    cap = v['caption']
    txt = (f"TIKTOK CAPTION\n{cap}\n\n{' '.join(v['tags_tt'])}\n\n"
           f"INSTAGRAM REELS CAPTION (max 5 hashtags)\n{cap}\n\n{' '.join(v['tags_ig'][:5])}\n\n"
           + ("MUSIC: none. Add a trending sound inside TikTok or Instagram when you post.\n" if silent else f"MUSIC: original '{style}' beat, made for Solxce. Safe for ads and business accounts.\n")
           + f"LENGTH: {total:.1f}s · 1080x1920 · 30fps\n")
    open(os.path.join(vdir, 'caption.txt'), 'w').write(txt)
    print(f'{name}: {total:.1f}s, {len(slides)} slides, {style}')
    return mp4


if __name__ == '__main__':
    from videos import VIDEOS
    only = sys.argv[1:]
    for v in VIDEOS:
        if not only or v['name'] in only:
            render(v)
