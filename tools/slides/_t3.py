CSS = '''*{box-sizing:border-box}body{margin:0;background:#222;font-family:'Inter',sans-serif}
.slide{width:1080px;height:1920px;position:relative;overflow:hidden;margin:0 0 40px}
.brand{position:absolute;left:80px;top:170px;display:flex;align-items:center;gap:16px}
.brand img{width:96px}.brand span{font-family:'Inter Display',sans-serif;font-weight:900;font-size:38px;letter-spacing:4px}
.content{position:absolute;left:80px;right:150px;top:290px;bottom:400px;display:flex;flex-direction:column;justify-content:center;gap:36px}
.h{font-family:'Inter Display',sans-serif;font-weight:900;letter-spacing:-3px;line-height:.95;margin:0}
.p{font-size:44px;font-weight:500;line-height:1.35;margin:0}
.tag{display:inline-block;padding:14px 30px;border-radius:999px;font-weight:800;font-size:30px;letter-spacing:4px}
.card{border-radius:40px}
.row{display:flex;justify-content:space-between;align-items:center;padding:22px 0;font-size:40px}.row b{font-weight:800}
.small{font-size:24px;letter-spacing:4px;font-weight:700;opacity:.65}
.swipe{display:flex;align-items:center;gap:16px;font-size:36px;font-weight:700}'''
FIT = '''<script>window.addEventListener('load',()=>{document.querySelectorAll('.content').forEach(c=>{const h=c.querySelector('.h');let n=0;while(c.scrollHeight>c.clientHeight+2&&h&&n<40){h.style.fontSize=(parseFloat(getComputedStyle(h).fontSize)-6)+'px';n++}});document.body.dataset.ready=1})</script>'''

os.makedirs('shows3', exist_ok=True)
for name, slides in S.items():
    html = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{name}</title><style>{CSS}</style></head><body>{"".join(slides)}{FIT}</body></html>'
    open(f'shows3/{name}.html', 'w').write(html)
print(json.dumps({k: len(v) for k, v in S.items()}))
