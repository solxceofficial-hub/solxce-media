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
    return wrap(t, f'''<div style="position:absolute;left:80px;right:80px;top:300px"><div class="h" style="font-size:118px">{line1}<br><span style="color:{t["acc"] if t["acc"]!=t["fg"] else RED}">{line2}</span></div></div>
      <img src="../hand-phone.png" style="position:absolute;right:-20px;bottom:-60px;width:740px;filter:drop-shadow(0 40px 80px rgba(0,0,0,.5))">''')

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

# ---------- extra visuals ----------
HX = [('SkiErg', '4:21'), ('Sled Push', '3:48'), ('Sled Pull', '4:55'), ('Burpee Broad Jumps', '5:37'),
      ('Row', '4:40'), ('Farmers Carry', '1:52'), ('Sandbag Lunges', '4:58'), ('Wall Balls', '6:44')]

def v_hyrox(t):
    rows = ''.join(f'<div style="display:flex;justify-content:space-between;padding:10px 18px;border-radius:14px;background:{RED if n=="Wall Balls" else "rgba(255,255,255,.07)"};font-size:28px"><span>{n}</span><b>{tm}</b></div>' for n, tm in HX)
    return card(t, f'''<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px"><span class="small">HYROX MODE · 8 STATIONS</span><span style="font-family:'Inter Display';font-weight:900;font-size:44px">1:19:47</span></div>
      <div style="display:flex;flex-direction:column;gap:8px">{rows}</div>''', pad='30px 34px')

def v_list(t, items, check=True):
    mark = (f'<span style="width:52px;height:52px;flex:none;border-radius:14px;background:{t["card"]};display:flex;align-items:center;justify-content:center">'
            f'<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="{t["cfg"]}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12 5 5 9-10"/></svg></span>')
    return '<div style="display:flex;flex-direction:column">' + ''.join(
        f'<div style="display:flex;align-items:center;gap:24px;padding:24px 0;border-top:3px solid {t["fg"]};font-size:42px;font-weight:700">{mark if check else ""}{x}</div>' for x in items) + '</div>'

def v_quote(t, q, a):
    abg, afg = ('#f4f4f2', '#0b0b0c') if t['bg'] == RED else (RED, '#fff')
    return f'''<div style="display:flex;flex-direction:column;gap:18px">
      <div style="align-self:flex-start;max-width:90%;padding:26px 34px;border-radius:36px 36px 36px 8px;background:{t["card"]};color:{t["cfg"]};font-size:50px;font-weight:700">{q}</div>
      <div style="align-self:flex-end;max-width:90%;padding:26px 34px;border-radius:36px 36px 8px 36px;background:{abg};color:{afg};font-size:44px;font-weight:600;line-height:1.3">{a}</div></div>'''

def v_week(t):
    days = [('MON', 'Push'), ('TUE', 'Pull'), ('WED', 'Legs'), ('THU', 'Rest'), ('FRI', 'Upper'), ('SAT', 'Run'), ('SUN', 'Rest')]
    cells = ''.join(f'<div style="border-radius:24px;padding:22px 10px;text-align:center;background:{RED if d=="WED" else t["card"]};color:{"#fff" if d=="WED" else t["cfg"]}"><div style="font-size:22px;font-weight:700;letter-spacing:2px;opacity:.75">{d}</div><div style="font-size:30px;font-weight:800;margin-top:6px">{s}</div></div>' for d, s in days)
    return f'<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px">{cells}</div>'

def v_split2(t, left, right):
    return f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">
      <div style="border-radius:32px;padding:30px;border:3px dashed {t["mute"]};color:{t["mute"]}"><div class="small" style="opacity:1">LAZY</div><div style="font-size:36px;font-weight:700;margin-top:10px;line-height:1.25">{left}</div></div>
      <div style="border-radius:32px;padding:30px;background:{RED};color:#fff"><div class="small" style="opacity:1;color:#fff">LOCKED IN</div><div style="font-size:36px;font-weight:800;margin-top:10px;line-height:1.25">{right}</div></div></div>'''

TILES = [('Train', "Today's split"), ('Fuel', 'Calories & protein'), ('Run', 'Routes & pace'), ('Post', 'Photos & videos')]
def v_myth(t, myth, fact):
    return f'''<div style="display:flex;flex-direction:column;gap:16px">
      <div style="padding:30px 36px;border-radius:32px;border:3px dashed {t["mute"]};color:{t["mute"]}"><div class="small" style="opacity:1">MYTH</div><div style="font-size:42px;font-weight:700;margin-top:8px;text-decoration:line-through">{myth}</div></div>
      <div style="padding:30px 36px;border-radius:32px;background:{t["card"]};color:{t["cfg"]}"><div class="small" style="opacity:1;color:{RED}">FACT</div><div style="font-size:42px;font-weight:800;margin-top:8px;line-height:1.25">{fact}</div></div></div>'''

def v_persona(t, items):
    cells = ''.join(f'<div style="border-radius:32px;padding:30px;background:{RED if i==0 else t["card"]};color:{"#fff" if i==0 else t["cfg"]};display:flex;flex-direction:column;gap:10px;min-height:250px;justify-content:space-between"><span style="font-family:\'Inter Display\';font-weight:900;font-size:54px;opacity:.5">{chr(65+i)}</span><div><div style="font-size:42px;font-weight:800">{a}</div><div style="font-size:26px;opacity:.8;margin-top:6px">{b}</div></div></div>' for i, (a, b) in enumerate(items))
    return f'<div style="display:grid;grid-template-columns:repeat(2,1fr);gap:14px">{cells}</div>'

def v_steps(t, steps):
    return '<div style="display:flex;flex-direction:column;gap:14px">' + ''.join(
        f'<div style="display:flex;align-items:center;gap:26px;padding:26px 30px;border-radius:30px;background:{t["card"]};color:{t["cfg"]}"><span style="width:70px;height:70px;flex:none;border-radius:50%;background:{RED};color:#fff;display:flex;align-items:center;justify-content:center;font-family:\'Inter Display\';font-weight:900;font-size:36px">{i+1}</span><div><div style="font-size:40px;font-weight:800">{a}</div><div style="font-size:26px;opacity:.75">{b}</div></div></div>' for i, (a, b) in enumerate(steps)) + '</div>'

S = {}

t = T['black']
S['21-myths-vs-facts'] = [
  hook(t, 'Fitness myths that need to die.', 'Swipe if you believed #3.', 170),
  slide(t, 'MYTH 01', 'You need an app for everything.', visual=v_myth(t, 'One app for lifts, one for food, one for runs', 'Solxce does lifts, food, runs and posts in one.'), size=118),
  slide(t, 'MYTH 02', '"I eat enough protein."', visual=v_myth(t, 'Eyeballing it works', "Eyeballing isn't counting. Solxce counts calories, meals, snacks and protein."), size=124),
  slide(t, 'MYTH 03', 'Winging it is fine.', visual=v_myth(t, 'Decide what to train at the gym', "Today's split is set before you walk in."), size=140),
  slide(t, 'MYTH 04', "Runs don't need tracking.", visual=v_myth(t, '"I felt fast"', 'Distance, pace and time, logged on every run.'), size=124),
  cta(t),
]
t = T['paper']
S['22-gym-mistakes'] = [
  hook(t, 'Gym mistakes I made so you don’t have to.', 'Number 2 is the sneaky one.', 140),
  slide(t, 'MISTAKE 01', 'No plan, every day.', body="Fix: follow a split. Solxce shows today's.", visual=v_split(t), size=140),
  slide(t, 'MISTAKE 02', 'Never tracking protein.', body='Fix: count every meal and snack.', visual=v_fuel(t), size=130),
  slide(t, 'MISTAKE 03', 'Skipping cardio.', body='Fix: add runs, and log every one.', visual=v_run(t), size=150),
  slide(t, 'MISTAKE 04', 'Not taking progress pics.', body='Fix: post them. Future you will thank you.', visual=v_posts(t), size=130),
  cta(t),
]
t = T['purple']
S['23-gym-personality'] = [
  hook(t, 'Pick your gym personality.', 'Comment your letter.', 170),
  slide(t, '', 'Which one are you?', visual=v_persona(t, [('The Lifter', 'Lives by the split'), ('The Runner', 'Every mile counts'), ('The HYROX Athlete', 'Runs + stations'), ('The Poster', 'Progress or it didn’t happen')]), size=130),
  slide(t, 'A · THE LIFTER', 'Your split, ready.', visual=v_split(t), size=150),
  slide(t, 'B · THE RUNNER', 'Every route mapped.', visual=v_run(t), size=140),
  slide(t, 'C · THE HYROX ATHLETE', 'All 16 splits.', visual=v_hyrox(t), size=150),
  cta(t, 'Solxce fits all four.<br>Out now on iOS.'),
]
t = T['volt']
S['24-monday-plan'] = [
  hook(t, 'Your week starts now.', 'Here’s the plan. Save it.', 190),
  slide(t, 'THE WEEK', 'Every day has a job.', visual=v_week(t), size=140),
  slide(t, 'EVERY DAY', 'Open the app. Do the split.', visual=v_split(t), size=124),
  slide(t, 'EVERY MEAL', 'Log it.', visual=v_fuel(t), size=170),
  slide(t, 'SATURDAY', 'Run day.', visual=v_run(t), size=170),
  cta(t),
]
t = T['cyan']
S['25-how-it-works'] = [
  hook(t, 'How Solxce works in 30 seconds.', 'Ready? Swipe.', 160),
  slide(t, '', '5 taps to a tracked day.', visual=v_steps(t, [('Open Solxce', "Today's split is waiting"), ('Train', 'Do the lifts on screen'), ('Log meals', 'Calories and protein add up'), ('Hit start on your run', 'Route and pace mapped'), ('Post it', 'Photos or video')]), size=124),
  slide(t, 'STEP 1–2', 'Train.', visual=v_split(t), size=180),
  slide(t, 'STEP 3', 'Fuel.', visual=v_fuel(t), size=180),
  slide(t, 'STEP 4–5', 'Run. Post.', visual=v_run(t), size=180),
  cta(t),
]
t = T['orange']
S['26-bag-vs-phone'] = [
  hook(t, "What's in your gym bag vs on your phone.", 'One of these is doing more work.', 140),
  slide(t, 'THE BAG', 'Shoes. Straps. Water. Headphones.', body='Gets you through the session.', visual=v_big(t, '4', ' items'), size=124),
  slide(t, 'THE PHONE', "Today's split.", visual=v_split(t), size=150),
  slide(t, 'THE PHONE', 'Your food log.', visual=v_fuel(t), size=150),
  slide(t, 'THE PHONE', 'Your runs. Your posts.', visual=v_tiles(t, TILES), size=140),
  cta(t),
]
t = T['cobalt']
S['27-rate-your-week'] = [
  hook(t, 'Rate your week out of 10.', 'Be honest. Comment your score.', 180),
  slide(t, '', 'Score yourself:', visual=v_list(t, ['Followed your split', 'Hit protein 5+ days', 'Ran at least twice', 'Logged every workout', 'Posted your progress'], check=False), size=150),
  slide(t, 'UNDER 5?', 'You need a plan.', body="Solxce puts today's split on your screen.", visual=v_split(t), size=150),
  slide(t, 'UNDER 5?', 'You need to count.', body='Every meal, snack and gram of protein.', visual=v_fuel(t), size=150),
  slide(t, '10/10?', 'Post the proof.', visual=v_posts(t, ('Monday', 'PR day', 'Sunday')), size=170),
  cta(t),
]
t = T['red']
S['28-how-to-fail'] = [
  hook(t, 'How to fail your fitness goals.', 'A step-by-step guide.', 180),
  slide(t, 'STEP 1', 'Never have a plan.', body="(Or open Solxce and see today's split.)", visual=v_split(t), size=150),
  slide(t, 'STEP 2', 'Guess your protein.', body='(Or let Solxce count it.)', visual=v_fuel(t), size=150),
  slide(t, 'STEP 3', "Don't track your runs.", body='(Or map every one.)', visual=v_run(t), size=140),
  slide(t, 'STEP 4', 'Use 4 different apps.', body='(Or just one.)', visual=v_tiles(t, TILES), size=140),
  cta(t, 'Or don’t fail.<br>Out now on iOS.'),
]
t = T['volt']
S['29-hyrox-prep'] = [
  hook(t, 'HYROX in a few weeks? Track these 3 things.', 'Save this for race prep.', 140),
  slide(t, '01', 'Your 1 km pace.', body='Over half the race is running. Know your number.', visual=v_big(t, "5:18", '/km'), size=150),
  slide(t, '02', 'Your weakest station.', body='Wall balls at 6:44? That’s your homework.', visual=v_hyrox(t), size=140),
  slide(t, '03', 'Your race sim.', body='Run the full 16 splits in training. Compare month to month.', visual=v_big(t, '16', ' splits'), size=150),
  slide(t, 'BONUS', 'Fuel the build.', visual=v_fuel(t), size=170),
  cta(t),
]
t = T['paper']
S['30-why-solxce'] = [
  hook(t, 'Why Solxce exists.', 'A short story about too many apps.', 190),
  slide(t, 'THE PROBLEM', 'Fitness apps made you pick one thing.', body='A lift app. A food app. A run app. Somewhere else to post.', visual=v_tiles(t, [('App 1', 'Lifts'), ('App 2', 'Food'), ('App 3', 'Runs'), ('App 4', 'Posting')]), size=118),
  slide(t, 'THE IDEA', 'What if it was one screen?', visual=v_big(t, '1'), size=140),
  phone(t, 'So we built', 'Solxce.'),
  slide(t, 'NOW', 'Train. Fuel. Run. Post. HYROX.', body='All of it, one app.', visual=v_tiles(t, TILES), size=124),
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

os.makedirs('shows3', exist_ok=True)
for name, slides in S.items():
    html = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{name}</title><style>{CSS}</style></head><body>{"".join(slides)}{FIT}</body></html>'
    open(f'shows3/{name}.html', 'w').write(html)
print(json.dumps({k: len(v) for k, v in S.items()}))
