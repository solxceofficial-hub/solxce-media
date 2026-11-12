import os, json

T = {
 'black':  dict(bg='#08080a', fg='#f4f4f2', mute='#a3a3aa', acc='#ff3352', card='#141417', cfg='#f4f4f2', line='#26262b', inv=False, glow=True),
 'paper':  dict(bg='#f4f3ef', fg='#0b0b0c', mute='#5f5f65', acc='#ff3352', card='#0b0b0c', cfg='#f4f4f2', line='#26262b', inv=True, glow=False),
 'volt':   dict(bg='#d7e04a', fg='#0b0b0c', mute='#3d4010', acc='#0b0b0c', card='#0b0b0c', cfg='#f4f4f2', line='#2a2a2e', inv=True, glow=False),
 'orange': dict(bg='#ff6a2a', fg='#1a0b05', mute='#4a1e0a', acc='#fff4e6', card='#1a0b05', cfg='#fff4e6', line='#3a2215', inv=True, glow=False),
 'cobalt': dict(bg='#2440e6', fg='#ffffff', mute='#d4dbff', acc='#ffffff', card='#0f1a6b', cfg='#ffffff', line='#2a3a9c', inv=False, glow=False),
 'cyan':   dict(bg='#5ed3e8', fg='#071a26', mute='#1d4a5c', acc='#071a26', card='#071a26', cfg='#eaf8fb', line='#1e3a4c', inv=True, glow=False),
 'purple': dict(bg='#1a0b33', fg='#f3ecff', mute='#b9a8dc', acc='#b48cff', card='#2a1650', cfg='#f3ecff', line='#3d2670', inv=False, glow=True),
 'red':    dict(bg='#ff3352', fg='#0b0b0c', mute='#3a0a12', acc='#0b0b0c', card='#0b0b0c', cfg='#f4f4f2', line='#2a2a2e', inv=True, glow=False),
}
RED = '#ff3352'

def brand(t):
    f = 'filter:invert(1)' if t['inv'] else ''
    return f'<div class="brand"><img src="../logo-x.png" style="{f}"><span>SOLXCE</span></div>'

def glow(t, x=300, y=900):
    if not t['glow']: return ''
    return f'<div style="position:absolute;left:{x}px;top:{y}px;width:800px;height:800px;border-radius:50%;background:{t["acc"]};opacity:.28;filter:blur(170px)"></div>'

def wrap(t, inner, extra=''):
    return f'<section class="slide" style="background:{t["bg"]};color:{t["fg"]}">{glow(t)}{brand(t)}{extra}{inner}</section>'

def tag(t, text):
    bg = t['acc'] if t['acc'] not in ('#ffffff', '#fff4e6', '#eaf8fb') else t['fg']
    fg = t['bg'] if bg in (t['fg'], '#0b0b0c', '#071a26', '#1a0b05') else '#ffffff'
    if bg == RED or bg == '#b48cff': fg = '#ffffff' if bg == RED else '#1a0b33'
    return f'<div><span class="tag" style="background:{bg};color:{fg}">{text}</span></div>'

def hook(t, title, sub, size=170):
    return wrap(t, f'''<div class="content" style="gap:54px">
      <h1 class="h" style="font-size:{size}px">{title}</h1>
      <p class="p" style="color:{t["fg"]};opacity:.85;font-size:48px">{sub}</p>
      <div class="swipe">Swipe <svg width="56" height="40" viewBox="0 0 56 40" fill="none" stroke="currentColor" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20h44M34 6l14 14-14 14"/></svg></div></div>''')

def slide(t, label, head, body='', visual='', size=130):
    return wrap(t, f'''<div class="content">{tag(t, label) if label else ''}
      <h2 class="h" style="font-size:{size}px">{head}</h2>
      {f'<p class="p" style="color:{t["mute"]}">{body}</p>' if body else ''}
      {visual}</div>''')

# ---------- visuals ----------
def card(t, inner, pad='38px 44px', extra=''):
    return f'<div class="card" style="background:{t["card"]};color:{t["cfg"]};padding:{pad};{extra}">{inner}</div>'

def v_split(t):
    rows = ''.join(f'<div style="border-top:1px solid {t["line"]}">{x}</div>' for x in ['Barbell Squats', 'Romanian Deadlifts', 'Leg Press', 'Hanging Knee Raises'])
    return card(t, f'''<div style="display:flex;justify-content:space-between"><span class="small">• TODAY'S SPLIT</span><span style="font-size:26px;font-weight:600">Schedule ›</span></div>
      <div style="font-size:70px;font-weight:800;letter-spacing:-2px;margin:10px 0 12px">Legs &amp; Core</div>
      <div style="font-size:34px;line-height:1.75">{rows}</div>''')

def v_fuel(t, cal='1,840', meals='3', snacks='1', protein='142g', hi='Protein'):
    def row(k, v):
        b = f'<b style="background:{RED};color:#fff;padding:4px 18px;border-radius:14px">{v}</b>' if k == hi else f'<b>{v}</b>'
        return f'<div class="row" style="border-top:1px solid {t["line"]}"><span>{k}</span>{b}</div>'
    return card(t, f'''<div style="font-family:'Inter Display';font-weight:900;font-size:30px;letter-spacing:3px;margin-bottom:8px">DAILY CONS-<span style="color:{RED}">X</span>-PTION</div>
      {row('Calories', cal)}{row('Meals', meals)}{row('Snacks', snacks)}{row('Protein', protein)}''', pad='30px 44px 14px')

def v_run(t, d='3.10 mi', p="8'42\"", tm='26:59'):
    return card(t, f'''<svg viewBox="0 0 800 280" width="100%" style="display:block;border-radius:24px">
        <rect width="800" height="280" fill="#1c2232"/><rect x="560" y="0" width="240" height="150" fill="#1f3d35"/>
        <g stroke="#2c3548" stroke-width="14" fill="none"><path d="M0 90H800M0 200H800M150 0V280M360 0V280M560 0V280"/></g>
        <path d="M70 250V200H150V90H360V140H560Q640 140 640 90V40" stroke="{RED}" stroke-width="12" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        <circle cx="70" cy="250" r="14" fill="#fff"/><circle cx="640" cy="40" r="18" fill="#fff"/><circle cx="640" cy="40" r="11" fill="{RED}"/></svg>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:22px;padding:0 10px">
        <div><div class="small">DISTANCE</div><div style="font-size:48px;font-weight:800">{d}</div></div>
        <div><div class="small">PACE</div><div style="font-size:48px;font-weight:800">{p}</div></div>
        <div><div class="small">TIME</div><div style="font-size:48px;font-weight:800">{tm}</div></div></div>''', pad='28px')

PIC = '<svg width="70" height="70" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="16" rx="3"/><circle cx="9" cy="10" r="2"/><path d="m21 16-5-5-9 9"/></svg>'
PLAY = '<svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>'

def v_posts(t, labels=('Week 1', 'Squat PR', 'Week 12')):
    out = []
    for i, l in enumerate(labels):
        if i == 1:
            out.append(f'<div style="height:250px;border-radius:36px;background:{RED};color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px">{PLAY}<span style="font-size:26px;font-weight:700">{l}</span></div>')
        else:
            out.append(f'<div style="height:250px;border-radius:36px;background:{t["card"]};color:{t["cfg"]};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px">{PIC}<span style="font-size:26px;font-weight:600">{l}</span></div>')
    return f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px">{"".join(out)}</div>'

def v_tiles(t, items):
    cells = ''.join(card(t, f'<div style="font-family:\'Inter Display\';font-weight:900;font-size:52px">{a}</div><div style="font-size:26px;opacity:.7">{b}</div>', pad='30px 34px') for a, b in items)
    return f'<div style="display:grid;grid-template-columns:repeat(2,1fr);gap:16px">{cells}</div>'

def v_big(t, num, unit=''):
    return f'<div style="font-family:\'Inter Display\';font-weight:900;font-size:300px;letter-spacing:-14px;line-height:.9">{num}<span style="font-size:90px;letter-spacing:-2px">{unit}</span></div>'

def v_vs(t, bad, good):
    return f'''<div style="display:flex;flex-direction:column;gap:16px">
      <div style="display:flex;align-items:center;gap:24px;padding:28px 34px;border-radius:30px;border:3px dashed {t["mute"]};font-size:38px;font-weight:600;color:{t["mute"]}"><span style="font-size:44px">✕</span><span style="text-decoration:line-through">{bad}</span></div>
      <div style="display:flex;align-items:center;gap:24px;padding:28px 34px;border-radius:30px;background:{t["card"]};color:{t["cfg"]};font-size:38px;font-weight:700"><span style="color:{RED};font-size:44px">✓</span>{good}</div></div>'''

def phone(t, line1, line2):
    # BANNED (Nov 12, 2026): the hand-holding-phone photo must never be used again.
    raise RuntimeError('phone() slide removed: the hand-holding-phone photo is banned')

def cta(t, line='Out now on iOS.'):
    f = 'filter:invert(1)' if t['inv'] else ''
    btn_bg, btn_fg = (t['fg'], t['bg'])
    return f'''<section class="slide" style="background:{t["bg"]};color:{t["fg"]}">{glow(t,140,600)}
      <img src="../logo-x.png" style="position:absolute;left:190px;top:300px;width:700px;{f}">
      <div style="position:absolute;left:0;right:0;top:590px;text-align:center;font-family:'Inter Display';font-weight:900;font-size:110px;letter-spacing:10px">SOLXCE</div>
      <div style="position:absolute;left:80px;right:80px;top:770px;text-align:center">
        <div class="h" style="font-size:100px">{line}</div>
        <div style="display:flex;justify-content:center;gap:20px;margin-top:50px">
          <div style="padding:28px 38px;border-radius:40px;border:4px solid {t["fg"]}"><div class="small" style="color:inherit;opacity:.75">MONTHLY</div><div style="font-family:'Inter Display';font-weight:900;font-size:72px">$9.99</div></div>
          <div style="padding:28px 38px;border-radius:40px;background:{t["fg"]};color:{t["bg"]}"><div class="small" style="color:inherit;opacity:.8">ANNUAL · SAVE 33%</div><div style="font-family:'Inter Display';font-weight:900;font-size:72px">$79.99</div></div>
        </div>
        <div style="margin:50px auto 0;display:inline-flex;align-items:center;gap:22px;padding:30px 56px;border-radius:999px;background:{btn_bg};color:{btn_fg};font-size:44px;font-weight:800"><svg width="46" height="46" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v13M6 11l6 6 6-6M5 21h14"/></svg>Download on the App Store</div>
        <p class="p" style="color:inherit;opacity:.85;margin-top:34px;font-size:40px">Search "Solxce" · Link in bio</p>
      </div></section>'''

# ---------- starter pack ----------
def starter(t):
    items = [
        ('Gallon water jug', '<path d="M8 3h8v3l2 3v12H6V9l2-3z"/><path d="M6 13h12"/>'),
        ('Lifting straps', '<path d="M4 12c4-6 12-6 16 0"/><path d="M4 12c4 6 12 6 16 0"/>'),
        ('Same playlist since 2019', '<circle cx="8" cy="17" r="3"/><circle cx="18" cy="15" r="3"/><path d="M11 17V5l10-2v12"/>'),
        ('Pre-workout scoop', '<path d="M4 10h12v4a6 6 0 0 1-12 0z"/><path d="M16 12h5"/>'),
        ('Mirror selfie angle', '<rect x="6" y="2" width="12" height="20" rx="2"/><circle cx="12" cy="18" r="1"/>'),
    ]
    cells = ''.join(f'<div style="border-radius:32px;background:{t["card"]};color:{t["cfg"]};padding:26px;display:flex;flex-direction:column;gap:14px;height:250px;justify-content:space-between"><svg width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{svg}</svg><span style="font-size:30px;font-weight:700;line-height:1.15">{name}</span></div>' for name, svg in items)
    cells += f'<div style="border-radius:32px;background:{RED};color:#fff;padding:26px;display:flex;flex-direction:column;justify-content:space-between;height:250px"><img src="../logo-x.png" style="width:120px"><span style="font-size:30px;font-weight:800;line-height:1.15">Solxce on the home screen</span></div>'
    return wrap(t, f'''<div class="content"><h2 class="h" style="font-size:118px">Gym rat starter pack</h2>
      <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:16px">{cells}</div></div>''')

# ---------- shows ----------
S = {}
t = T['black']
S['01-before-after'] = [
  hook(t, 'My gym life before vs after Solxce.', 'Same person. Very different results.', 160),
  slide(t, 'BEFORE', 'Walked in and winged it.', visual=v_vs(t, 'Copy whoever’s on the next bench', "Open Solxce, today's split is there"), size=128),
  slide(t, 'BEFORE', 'Protein was a vibe.', visual=v_vs(t, '"I probably hit it"', '142g logged, every meal counted'), size=140),
  slide(t, 'BEFORE', 'Runs never happened.', body='At least not on paper.', visual=v_vs(t, '"Like 2 miles?"', '3.10 mi · 8\'42" pace · route mapped'), size=128),
  slide(t, 'BEFORE', 'PRs died in my camera roll.', visual=v_vs(t, '400 unseen gym pics', 'Posted the set on Solxce'), size=118),
  cta(t),
]
t = T['volt']
S['02-delete-apps'] = [
  hook(t, 'Delete 3 apps today.', "Keep the one that does all of it.", 180),
  slide(t, 'DELETE', 'Your workout notes app.', body="Solxce has today's split ready.", visual=v_split(t), size=130),
  slide(t, 'DELETE', 'Your calorie counter.', body='Solxce counts meals, snacks and protein.', visual=v_fuel(t), size=130),
  slide(t, 'DELETE', 'Your run tracker.', body='Solxce maps every route.', visual=v_run(t), size=130),
  slide(t, 'KEEP', 'One app. Four jobs.', visual=v_tiles(t, [('Train', "Today's split"), ('Fuel', 'Calories & protein'), ('Run', 'Routes & pace'), ('Post', 'Photos & videos')]), size=140),
  cta(t),
]
t = T['orange']
S['03-day-of-eating'] = [
  hook(t, 'What I eat in a day, fully logged.', 'No guessing. Every number counted.', 150),
  slide(t, 'BREAKFAST', 'Eggs, toast, coffee.', visual=v_fuel(t, '520', '1', '0', '32g'), size=140),
  slide(t, 'LUNCH', 'Chicken, rice, greens.', visual=v_fuel(t, '1,120', '2', '0', '86g'), size=140),
  slide(t, 'SNACK', 'Greek yogurt.', visual=v_fuel(t, '1,290', '2', '1', '104g', hi='Snacks'), size=150),
  slide(t, 'DINNER', 'Salmon and potatoes.', visual=v_fuel(t), size=140),
  cta(t),
]
t = T['cobalt']
S['04-excuses'] = [
  hook(t, 'Your excuses vs Solxce.', 'We heard them all.', 180),
  slide(t, 'EXCUSE 01', '"I don\'t know what to train."', body="Today's split is already on your screen.", visual=v_split(t), size=118),
  slide(t, 'EXCUSE 02', '"I can\'t track food."', body='Solxce counts it for you.', visual=v_fuel(t), size=130),
  slide(t, 'EXCUSE 03', '"I forget my runs."', body='Hit start. Every mile gets mapped.', visual=v_run(t), size=140),
  slide(t, 'EXCUSE 04', '"Nobody sees my progress."', body='Post photos and videos on Solxce.', visual=v_posts(t), size=118),
  cta(t),
]
t = T['paper']
S['05-leg-day-steps'] = [
  hook(t, 'How to stop skipping leg day in 3 steps.', 'Step 3 is the one that keeps you honest.', 140),
  slide(t, 'STEP 1', 'Open Solxce.', body="Leg day is on the schedule. No more 'I'll do it tomorrow.'", visual=v_big(t, '1'), size=150),
  slide(t, 'STEP 2', 'Do the four lifts.', body='They’re listed. Just go in order.', visual=v_split(t), size=140),
  slide(t, 'STEP 3', 'Post the last set.', body='Film it. Post it. Now people know.', visual=v_posts(t, ('Squats', 'Last set', 'Leg press')), size=140),
  phone(t, 'All of it on', 'one screen.'),
  cta(t),
]
t = T['cyan']
S['06-runners'] = [
  hook(t, 'Runners, you need to see this.', 'Your runs deserve more than "I went for a jog."', 160),
  slide(t, '', 'Every route, mapped.', visual=v_run(t), size=150),
  slide(t, '', 'Pace. Distance. Time.', body='Logged automatically on every run.', visual=v_big(t, '8\'42"', '/mi'), size=130),
  slide(t, '', 'Then fuel it right.', body='Calories and protein in the same app.', visual=v_fuel(t), size=150),
  slide(t, '', 'And post the proof.', body='Share photos and videos of your runs.', visual=v_posts(t, ('Start', 'Finish line', 'Splits')), size=150),
  cta(t),
]
t = T['paper']
S['07-what-79-gets'] = [
  hook(t, 'What $79.99 a year actually gets you.', 'Break it down with me.', 150),
  slide(t, 'THE MATH', '$1.54 a week.', body='That’s $79.99 ÷ 52 weeks.', visual=v_big(t, '$1.54', '/wk'), size=150),
  slide(t, 'YOU GET', 'A plan every day.', body="Today's split, scheduled.", visual=v_split(t), size=150),
  slide(t, 'YOU GET', 'Food and run tracking.', body='Calories, protein, routes, pace.', visual=v_fuel(t), size=140),
  slide(t, 'YOU GET', 'A place to post.', body='Photos and videos of your progress.', visual=v_posts(t), size=150),
  cta(t),
]
t = T['purple']
S['08-week1-week12'] = [
  hook(t, 'Week 1 vs Week 12.', 'Post both. Let people see the jump.', 190),
  slide(t, 'WEEK 1', 'Start posting on day one.', body='Your first photo is the one you’ll thank yourself for.', visual=v_posts(t, ('Day 1', 'First set', 'Week 1')), size=130),
  slide(t, 'EVERY DAY', 'Show up with a plan.', body="Today's split is waiting in Solxce.", visual=v_split(t), size=130),
  slide(t, 'EVERY DAY', 'Feed the progress.', body='Protein logged, not guessed.', visual=v_fuel(t), size=140),
  slide(t, 'WEEK 12', 'Post the glow-up.', body='Same app, 12 weeks of proof.', visual=v_posts(t, ('Week 1', 'Week 12', 'New PR')), size=140),
  cta(t),
]
t = T['black']
S['09-starter-pack'] = [
  hook(t, 'The gym rat starter pack.', 'Tag the one who has all of these.', 170),
  starter(t),
  slide(t, 'THE MISSING PIECE', 'The app that runs your whole day.', visual=v_tiles(t, [('Train', "Today's split"), ('Fuel', 'Calories & protein'), ('Run', 'Routes & pace'), ('Post', 'Photos & videos')]), size=118),
  phone(t, 'Now it fits', 'in one hand.'),
  slide(t, '', 'Tag your gym partner.', body='Whoever you tag has to download it.', visual=v_big(t, '@'), size=150),
  cta(t),
]
t = T['red']
S['10-red-flags'] = [
  hook(t, 'Gym red flags.', 'How many are you guilty of?', 200),
  slide(t, 'RED FLAG 01', 'No plan. Just vibes.', body="Fix: today's split in Solxce.", visual=v_split(t), size=140),
  slide(t, 'RED FLAG 02', '"Protein? Probably."', body='Fix: Daily cons-X-ption counts it.', visual=v_fuel(t), size=140),
  slide(t, 'RED FLAG 03', 'Ran, but no proof.', body='Fix: every route mapped.', visual=v_run(t), size=140),
  slide(t, 'RED FLAG 04', 'Four fitness apps.', body='Fix: one app that does all four.', visual=v_tiles(t, [('Train', "Today's split"), ('Fuel', 'Calories & protein'), ('Run', 'Routes & pace'), ('Post', 'Photos & videos')]), size=140),
  cta(t),
]

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

os.makedirs('shows', exist_ok=True)
for name, slides in S.items():
    html = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{name}</title><style>{CSS}</style></head><body>{"".join(slides)}{FIT}</body></html>'
    open(f'shows/{name}.html', 'w').write(html)
print(json.dumps({k: len(v) for k, v in S.items()}))
