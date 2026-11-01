"""Render decks listed in tools/promo/videos.py to slides/<name>/tt-N.jpg (1080x1920) and ig-N.jpg (1080x1350 crop)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'promo'))
from playwright.sync_api import sync_playwright
from PIL import Image
import videos
OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'slides'))
only = set(sys.argv[1:])
todo = [v for v in videos.VIDEOS if 'html' in v and (not only or v['name'] in only)]
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1920})
    for v in todo:
        d = os.path.join(OUT, v['name'])
        if os.path.exists(os.path.join(d, 'ig-1.jpg')): continue
        src = open(v['html']).read().replace('</head>', '<style>.swipe{display:none!important}</style></head>', 1)
        for a, c in (v.get('sub_fix') or {}).items(): src = src.replace(a, c)
        tmp = os.path.join(os.path.dirname(v['html']), '_jpg_' + os.path.basename(v['html']))
        open(tmp, 'w').write(src)
        pg.goto('file://' + tmp)
        try: pg.wait_for_selector('body[data-ready]', timeout=6000)
        except Exception: pass
        pg.wait_for_timeout(250)
        s = pg.locator('section.slide'); os.makedirs(d, exist_ok=True)
        for i in range(s.count()):
            s.nth(i).screenshot(path='/tmp/_r.png')
            im = Image.open('/tmp/_r.png').convert('RGB').resize((1080, 1920))
            im.save(f'{d}/tt-{i+1}.jpg', quality=90); im.crop((0, 210, 1080, 1560)).save(f'{d}/ig-{i+1}.jpg', quality=90)
        os.remove(tmp); print(v['name'], s.count(), flush=True)
    b.close()
