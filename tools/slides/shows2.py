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
S = {}

t = T['paper']
S['11-stopped-doing'] = [
  hook(t, 'Things I stopped doing after Solxce.', 'Number 4 is the big one.', 150),
  slide(t, '01', 'Stopped guessing my protein.', body='It’s counted now. 142g, not "probably."', visual=v_fuel(t), size=124),
  slide(t, '02', 'Stopped skipping leg day.', body="It's on my split. It's on my screen.", visual=v_split(t), size=130),
  slide(t, '03', 'Stopped losing my runs.', body='Every route mapped.', visual=v_run(t), size=130),
  slide(t, '04', 'Stopped juggling 4 apps.', visual=v_tiles(t, TILES), size=130),
  cta(t),
]
t = T['black']
S['12-unpopular-opinions'] = [
  hook(t, 'Unpopular gym opinions.', 'Fight me in the comments.', 190),
  slide(t, 'OPINION 01', "If it's not logged, it didn't happen.", visual=v_run(t), size=124),
  slide(t, 'OPINION 02', 'Your protein is lower than you think.', visual=v_fuel(t, '1,640', '3', '2', '84g'), size=118),
  slide(t, 'OPINION 03', 'Rest days should be planned, not random.', visual=v_week(t), size=118),
  slide(t, 'OPINION 04', 'Nobody needs 4 fitness apps.', visual=v_tiles(t, TILES), size=130),
  cta(t),
]
t = T['volt']
S['13-hyrox-athletes'] = [
  hook(t, 'HYROX athletes, read this.', 'Solxce just added HYROX mode.', 170),
  slide(t, 'NEW', '16 splits. All timed.', body='8 runs and 8 stations, logged in one place.', visual=v_hyrox(t), size=140),
  slide(t, 'FIND IT', 'Spot your weakest station.', body='Wall balls at 6:44? Now you know what to train.', visual=v_big(t, '6:44'), size=124),
  slide(t, 'FUEL IT', 'Eat like you race.', body='Calories and protein tracked in the same app.', visual=v_fuel(t), size=150),
  slide(t, 'POST IT', 'Share the finish.', body='Post your race photos and videos on Solxce.', visual=v_posts(t, ('Start line', 'Wall balls', 'Finish')), size=150),
  cta(t),
]
t = T['cobalt']
S['14-start-from-zero'] = [
  hook(t, "How I'd start the gym from zero.", 'Four steps. No overthinking.', 160),
  slide(t, 'STEP 1', 'Follow a split.', body="Don't make it up every day.", visual=v_week(t), size=160),
  slide(t, 'STEP 2', 'Hit your protein.', body='Count it, every meal.', visual=v_fuel(t), size=160),
  slide(t, 'STEP 3', 'Add a run.', body='Even 2 miles counts when it’s logged.', visual=v_run(t, '2.00 mi', "9'15\"", '18:30'), size=160),
  slide(t, 'STEP 4', 'Post the progress.', body='Week 1 is the photo you’ll want later.', visual=v_posts(t), size=150),
  cta(t),
]
t = T['orange']
S['15-signs-you-need'] = [
  hook(t, 'Signs you need Solxce.', 'If 2 or more hit, it’s time.', 190),
  slide(t, 'SIGN 01', 'Your notes app is full of workouts.', body='"Squat 135 3x8??"', visual=v_vs(t, 'Messy notes', "Today's split, ready"), size=118),
  slide(t, 'SIGN 02', '"I think I ran 2 miles."', visual=v_vs(t, 'Guessing', 'Distance, pace, time, mapped'), size=124),
  slide(t, 'SIGN 03', 'Your camera roll is 80% gym pics.', visual=v_vs(t, 'Nobody sees them', 'Posted on Solxce'), size=118),
  slide(t, 'SIGN 04', 'You have 3+ fitness apps.', visual=v_vs(t, '3 logins, 3 subscriptions', 'One app for all of it'), size=124),
  cta(t),
]
t = T['black']
S['16-lazy-vs-locked'] = [
  hook(t, 'Lazy vs locked in.', 'Which one were you this week?', 200),
  slide(t, 'THE PLAN', 'Walking in.', visual=v_split2(t, 'Wanders the gym. Copies someone.', "Opens Solxce. Today's split is there."), size=150),
  slide(t, 'THE FOOD', 'Protein.', visual=v_split2(t, '"I probably hit it."', '142g, counted.'), size=170),
  slide(t, 'THE CARDIO', 'The run.', visual=v_split2(t, '"Like a mile or two?"', '3.10 mi, mapped.'), size=170),
  slide(t, 'THE PROOF', 'Progress.', visual=v_split2(t, 'Gym pics nobody sees.', 'Posted on Solxce.'), size=170),
  cta(t),
]
t = T['cyan']
S['17-every-feature'] = [
  hook(t, 'Every Solxce feature in 5 slides.', 'Swipe fast.', 160),
  slide(t, 'TRAIN', "Today's split.", body='Your lifts for the day, ready when you open the app.', visual=v_split(t), size=150),
  slide(t, 'FUEL', 'Daily<br>cons-X-ption.', body='Calories, meals, snacks and protein.', visual=v_fuel(t), size=120),
  slide(t, 'RUN', 'Run<br>track-X-ing.', body='Route, distance, pace and time.', visual=v_run(t), size=130),
  slide(t, 'NEW', 'HYROX mode.', body='All 16 race splits, timed.', visual=v_hyrox(t), size=150),
  cta(t),
]
t = T['purple']
S['18-four-week-plan'] = [
  hook(t, 'My 4-week reset plan.', 'Save this for Monday.', 180),
  slide(t, 'WEEK 1', 'Pick a split and stick to it.', visual=v_week(t), size=124),
  slide(t, 'WEEK 2', 'Log every meal.', body='Find out where your protein really is.', visual=v_fuel(t), size=150),
  slide(t, 'WEEK 3', 'Add 2 runs.', body='Map them. Watch the pace.', visual=v_run(t), size=160),
  slide(t, 'WEEK 4', 'Post the progress.', body='Week 1 vs week 4. Let people see it.', visual=v_posts(t, ('Week 1', 'New PR', 'Week 4')), size=150),
  cta(t),
]
t = T['red']
S['19-things-gym-people-say'] = [
  hook(t, 'Things gym people say.', 'And how Solxce answers.', 190),
  slide(t, '', 'Every Monday:', visual=v_quote(t, '"What do I even train today?"', "Today's split is on your screen. Legs & Core."), size=130),
  slide(t, '', 'After dinner:', visual=v_quote(t, '"I definitely hit my protein."', 'Daily cons-X-ption says 84g. Not quite.'), size=130),
  slide(t, '', 'After cardio:', visual=v_quote(t, '"I ran like 5k I think."', 'It was 3.10 miles. Route mapped, pace logged.'), size=130),
  slide(t, '', 'After a PR:', visual=v_quote(t, '"Nobody saw it."', 'Post the video on Solxce.'), size=130),
  cta(t),
]
t = T['paper']
S['20-comment-your-split'] = [
  hook(t, 'Comment your split.', 'PPL? Upper/lower? Bro split? Go.', 190),
  slide(t, 'MINE', 'This week:', visual=v_week(t), size=150),
  slide(t, 'TODAY', "What's on the screen.", visual=v_split(t), size=140),
  slide(t, 'THE RULE', "Don't skip what's scheduled.", body="It's right there when you open the app.", visual=v_big(t, '0', ' skips'), size=130),
  phone(t, 'Your split,', 'on one screen.'),
  cta(t),
]
