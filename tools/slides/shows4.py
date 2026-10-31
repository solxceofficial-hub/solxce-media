
# ---------- batch 4 helpers (no swipe prompts) ----------
def hook(t, title, sub, size=170):
    return wrap(t, f'''<div class="content" style="gap:54px">
      <h1 class="h" style="font-size:{size}px">{title}</h1>
      <p class="p" style="color:{t["fg"]};opacity:.85;font-size:48px">{sub}</p></div>''')

def v_bigs(t, num, unit='', size=260):
    return f'<div style="font-family:\'Inter Display\';font-weight:900;font-size:{size}px;letter-spacing:-10px;line-height:.9">{num}<span style="font-size:{int(size*.32)}px;letter-spacing:-2px">{unit}</span></div>'

def v_price(t):
    return f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
      <div style="border-radius:36px;padding:34px;border:4px solid {t["fg"]}"><div class="small" style="opacity:.75">MONTHLY</div><div style="font-family:'Inter Display';font-weight:900;font-size:84px;margin-top:8px">$9.99</div><div style="font-size:28px;opacity:.75">per month</div></div>
      <div style="border-radius:36px;padding:34px;background:{t["card"]};color:{t["cfg"]}"><div class="small" style="opacity:.8">ANNUAL · SAVE 33%</div><div style="font-family:'Inter Display';font-weight:900;font-size:84px;margin-top:8px">$79.99</div><div style="font-size:28px;opacity:.8">= $6.67 / month</div></div></div>'''

HX16 = ['Run 1', 'SkiErg', 'Run 2', 'Sled Push', 'Run 3', 'Sled Pull', 'Run 4', 'Burpee Broad Jumps',
        'Run 5', 'Row', 'Run 6', 'Farmers Carry', 'Run 7', 'Sandbag Lunges', 'Run 8', 'Wall Balls']

def v_16(t):
    cells = ''.join(f'<div style="border-radius:20px;padding:16px 18px;background:{HI(t)[0] if not n.startswith("Run") else t["card"]};color:{HI(t)[1] if not n.startswith("Run") else t["cfg"]};font-size:26px;font-weight:700;min-height:96px;display:flex;flex-direction:column;justify-content:space-between"><span style="font-size:20px;opacity:.7">{i+1:02d}</span>{n}</div>' for i, n in enumerate(HX16))
    return f'<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px">{cells}</div>'

def v_duo(t, la, a, lb, b):
    return f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">
      <div style="border-radius:32px;padding:30px;border:3px dashed {t["mute"]};color:{t["fg"]}"><div class="small" style="opacity:.8">{la}</div><div style="font-size:38px;font-weight:700;margin-top:10px;line-height:1.25">{a}</div></div>
      <div style="border-radius:32px;padding:30px;background:{HI(t)[0]};color:{HI(t)[1]}"><div class="small" style="opacity:1;color:inherit">{lb}</div><div style="font-size:38px;font-weight:800;margin-top:10px;line-height:1.25">{b}</div></div></div>'''

def v_poll(t, a, b):
    def opt(k, x, hi):
        return f'<div style="display:flex;align-items:center;gap:26px;padding:30px 34px;border-radius:32px;background:{HI(t)[0] if hi else t["card"]};color:{HI(t)[1] if hi else t["cfg"]}"><span style="font-family:\'Inter Display\';font-weight:900;font-size:80px;width:80px">{k}</span><span style="font-size:42px;font-weight:800">{x}</span></div>'
    return f'<div style="display:flex;flex-direction:column;gap:16px">{opt("A", a, True)}{opt("B", b, False)}</div>'

def starter2(t, title, items, last):
    cells = ''.join(f'<div style="border-radius:32px;background:{t["card"]};color:{t["cfg"]};padding:30px;display:flex;align-items:flex-end;height:230px"><span style="font-size:32px;font-weight:700;line-height:1.15">{x}</span></div>' for x in items)
    cells += f'<div style="border-radius:32px;background:{HI(t)[0]};color:{HI(t)[1]};padding:26px;display:flex;flex-direction:column;justify-content:space-between;height:230px"><img src="../logo-x.png" style="width:110px"><span style="font-size:30px;font-weight:800;line-height:1.15">{last}</span></div>'
    return wrap(t, f'''<div class="content"><h2 class="h" style="font-size:118px">{title}</h2>
      <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:16px">{cells}</div></div>''')

def week2(t, days):
    cells = ''.join(f'<div style="border-radius:24px;padding:22px 10px;text-align:center;background:{HI(t)[0] if hi else t["card"]};color:{HI(t)[1] if hi else t["cfg"]}"><div style="font-size:22px;font-weight:700;letter-spacing:2px;opacity:.75">{d}</div><div style="font-size:30px;font-weight:800;margin-top:6px">{s}</div></div>' for d, s, hi in days)
    return f'<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px">{cells}</div>'


def HI(t):
    return ('#f4f4f2', '#0b0b0c') if t['bg'] == RED else (RED, '#fff')

def v_posts(t, labels=('Week 1', 'Squat PR', 'Week 12')):
    hb, hf = HI(t); out = []
    for i, l in enumerate(labels):
        bg, fg, ic = (hb, hf, PLAY) if i == 1 else (t["card"], t["cfg"], PIC)
        out.append(f'<div style="height:250px;border-radius:36px;background:{bg};color:{fg};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px">{ic}<span style="font-size:26px;font-weight:700">{l}</span></div>')
    return f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px">{"".join(out)}</div>'

STATIONS = ['SkiErg', 'Sled Push', 'Sled Pull', 'Burpee Broad Jumps', 'Row', 'Farmers Carry', 'Sandbag Lunges', 'Wall Balls']
S = {}
P = T

S['021-no-excuse-november'] = (t := P['red']) and [
  hook(t, 'No-excuse November: 4 rules.', 'Screenshot this. Follow it till the 30th.', 170),
  slide(t, 'RULE 01', 'Follow the split.', body="No making it up at the gym.", visual=v_split(t), size=150),
  slide(t, 'RULE 02', 'Log every meal.', body='Snacks too. Especially snacks.', visual=v_fuel(t), size=150),
  slide(t, 'RULE 03', 'Run twice a week.', body='Route, distance, pace, time. Tracked.', visual=v_run(t), size=150),
  slide(t, 'RULE 04', 'Post the proof.', visual=v_posts(t, ('Nov 1', 'Mid-month', 'Nov 30')), size=160),
  cta(t)]

S['022-dark-at-5pm'] = (t := P['purple']) and [
  hook(t, "It's dark at 5pm now. Run anyway.", "The clocks changed. Your goals didn't.", 160),
  slide(t, 'MORNING OR LUNCH', 'Pick a time. Log the run.', visual=v_run(t, '2.40 mi', "9'05\"", '21:48'), size=124),
  slide(t, 'EVERY ROUTE', 'Mapped, start to finish.', visual=v_run(t), size=130),
  slide(t, 'NOT FEELING IT?', "Do today's split instead.", visual=v_split(t), size=124),
  slide(t, 'THE WEEK', 'Run days on the calendar.', visual=v_week(t), size=130),
  cta(t)]

S['023-pov-first-week'] = (t := P['black']) and [
  hook(t, 'POV: your first week on Solxce.', "Day 1 you open the app. Here's what's waiting.", 160),
  slide(t, 'DAY 1', "Today's split is already there.", visual=v_split(t), size=124),
  slide(t, 'DAY 2', 'Breakfast, lunch, the snack. Logged.', visual=v_fuel(t), size=118),
  slide(t, 'DAY 4', 'First run, mapped.', visual=v_run(t), size=150),
  slide(t, 'DAY 7', 'You post the week.', visual=v_posts(t, ('Day 1', 'First PR', 'Day 7')), size=150),
  cta(t)]

S['024-protein-habits'] = (t := P['volt']) and [
  hook(t, '4 protein habits that actually stick.', 'Number 3 changed everything for me.', 160),
  slide(t, 'HABIT 01', 'Protein at breakfast.', body='Start the count early.', visual=v_fuel(t, '520', '1', '0', '41g'), size=140),
  slide(t, 'HABIT 02', 'Plan the snack.', body="Don't let it plan you.", visual=v_fuel(t, '1,210', '2', '1', '96g', hi='Snacks'), size=150),
  slide(t, 'HABIT 03', 'Log it as you eat.', body='Not at 11pm from memory.', visual=v_fuel(t), size=150),
  slide(t, 'HABIT 04', 'Check the total before dinner.', body='Example goal:', visual=v_bigs(t, '142', 'g'), size=118),
  cta(t)]

S['025-first-hyrox'] = (t := P['orange']) and [
  hook(t, 'First HYROX? Read this.', '4 things first-timers wish they knew.', 170),
  slide(t, '01', "It's 8 runs + 8 stations.", visual=v_16(t), size=124),
  slide(t, '02', 'The running adds up.', body='Eight 1 km runs, one before every station.', visual=v_bigs(t, '8', ' km'), size=140),
  slide(t, '03', 'Pacing is everything.', body='Time every split so you see where you fade.', visual=v_hyrox(t), size=130),
  slide(t, '04', 'Rehearse the full race.', body='Run all 16 splits in training. Compare month to month.', visual=v_bigs(t, '16', ' splits'), size=124),
  cta(t)]

S['026-gym-bro-translations'] = (t := P['paper']) and [
  hook(t, 'Gym bro translations.', 'What they say vs what they mean.', 180),
  slide(t, '01', 'Translation:', visual=v_quote(t, '"Just one more set."', 'Four more sets.'), size=150),
  slide(t, '02', 'Translation:', visual=v_quote(t, '"I eat enough protein."', 'Has never counted it once.'), size=150),
  slide(t, '03', 'Translation:', visual=v_quote(t, '"Rest day."', 'Third rest day in a row.'), size=150),
  slide(t, '04', 'Translation:', visual=v_quote(t, '"I\'ll start Monday."', "Solxce has today's split ready. Today."), size=150),
  cta(t)]

S['027-what-6-67-gets'] = (t := P['cobalt']) and [
  hook(t, '$6.67 a month. Here’s what you get.', "That's the annual plan, broken down.", 150),
  slide(t, 'THE PLAN', '$79.99 a year.', visual=v_price(t), size=150),
  slide(t, 'TRAIN + FUEL', 'Your split and your food log.', visual=v_fuel(t), size=124),
  slide(t, 'RUN + POST', 'Runs mapped. Progress posted.', visual=v_run(t), size=124),
  slide(t, 'NEW', 'HYROX mode. All 16 splits.', visual=v_hyrox(t), size=124),
  cta(t)]

S['028-gym-friend-myths'] = (t := P['black']) and [
  hook(t, '4 myths your gym friend still believes.', 'Send this to them.', 150),
  slide(t, 'MYTH 01', 'More apps = more organized.', visual=v_myth(t, 'One app per thing', 'Lifts, food, runs and posts in one app.'), size=118),
  slide(t, 'MYTH 02', "Lifters don't run.", visual=v_myth(t, 'Running is for runners', 'Plenty of lifters run. Track route, distance, pace and time.'), size=130),
  slide(t, 'MYTH 03', 'Protein is a bodybuilder thing.', visual=v_myth(t, "I don't need to count it", 'Everyone eats it. Counting it tells you where you stand.'), size=118),
  slide(t, 'MYTH 04', 'HYROX is just running.', visual=v_myth(t, "It's a running race", '8 runs + 8 stations. 16 splits to time.'), size=124),
  cta(t)]

S['029-comment-your-pace'] = (t := P['cyan']) and [
  hook(t, 'Comment your mile pace. No judgment.', "I'll go first.", 160),
  slide(t, 'MINE TODAY', 'Easy 5K.', visual=v_run(t), size=170),
  slide(t, 'SLOW DAYS', 'Log them too.', visual=v_run(t, '4.00 mi', "10'31\"", '42:04'), size=170),
  slide(t, 'EVERY RUN', 'Route, distance, pace, time.', visual=v_tiles(t, [('Route', 'Mapped'), ('Distance', 'Miles'), ('Pace', 'Per mile'), ('Time', 'Total')]), size=124),
  slide(t, 'GOOD DAYS', 'Post them.', visual=v_posts(t, ('Easy run', 'Mile PR', 'Long run')), size=170),
  cta(t)]

S['030-thanksgiving-plate'] = (t := P['orange']) and [
  hook(t, 'Thanksgiving plate, logged.', 'Yes, you can still track today.', 170),
  slide(t, 'THE PLATE', 'Turkey. Stuffing. Pie.', body='Example day:', visual=v_fuel(t, '2,650', '2', '3', '118g'), size=140),
  slide(t, 'THE RULE', "Log it. Don't skip it.", body='One big day is just one big day.', visual=v_bigs(t, '1', ' day'), size=140),
  slide(t, 'TURKEY TROT', 'Track the 5K.', visual=v_run(t, '3.11 mi', "9'12\"", '28:36'), size=160),
  slide(t, 'FRIDAY', "Back to today's split.", visual=v_split(t), size=140),
  cta(t)]

S['031-turkey-trot'] = (t := P['volt']) and [
  hook(t, 'Running a turkey trot? Do this first.', '4 steps before Thursday.', 150),
  slide(t, 'STEP 1', 'Know your pace.', visual=v_run(t), size=160),
  slide(t, 'STEP 2', 'Two practice runs this week.', visual=week2(t, [('MON', 'Run', True), ('TUE', 'Upper', False), ('WED', 'Run', True), ('THU', 'Race', True)]), size=124),
  slide(t, 'STEP 3', 'Fuel the morning.', visual=v_fuel(t, '640', '1', '1', '38g'), size=150),
  slide(t, 'STEP 4', 'Post the finish.', visual=v_posts(t, ('Start line', 'Finish', 'Pie')), size=160),
  cta(t)]

S['032-black-friday-cart'] = (t := P['black']) and [
  hook(t, 'Black Friday shopping list: 1 item.', 'The only cart that pays you back.', 150),
  slide(t, 'IN THE CART', 'Solxce annual.', visual=v_price(t), size=150),
  slide(t, 'THAT WORKS OUT TO', '$6.67 a month.', visual=v_bigs(t, '33%', ' off monthly', 220), size=140),
  slide(t, 'WHAT YOU GET', 'Train. Fuel. Run. Post.', visual=v_tiles(t, TILES), size=130),
  slide(t, 'ALSO', 'HYROX mode.', visual=v_hyrox(t), size=160),
  cta(t)]

S['033-december-tomorrow'] = (t := P['cobalt']) and [
  hook(t, 'December starts tomorrow. Be ready.', 'Set it up tonight.', 160),
  slide(t, 'THE WEEK', 'Plan it now.', visual=v_week(t), size=160),
  slide(t, 'DAY 1', "Today's split, waiting.", visual=v_split(t), size=140),
  slide(t, 'EVERY MEAL', 'Count it.', visual=v_fuel(t), size=170),
  slide(t, 'COLD RUNS', 'Still count.', visual=v_run(t), size=170),
  cta(t)]

S['034-cardio-day-types'] = (t := P['purple']) and [
  hook(t, 'Types of people on cardio day.', 'Which one are you? Comment the letter.', 170),
  slide(t, '', 'Pick one.', visual=v_persona(t, [('The Incline Walker', '12% and a podcast'), ('The Sprinter', 'Done in 8 minutes'), ('The Scroller', 'Mostly on the phone'), ('The Tracker', 'Pace, route, time logged')]), size=150),
  slide(t, 'D · THE TRACKER', 'Every route mapped.', visual=v_run(t), size=140),
  slide(t, 'BE D', 'Know your pace.', visual=v_run(t, '2.00 mi', "8'55\"", '17:50'), size=160),
  slide(t, 'THEN', 'Lift tomorrow.', visual=v_split(t), size=170),
  cta(t)]

S['035-log-a-day'] = (t := P['paper']) and [
  hook(t, 'How to log a full day of food.', 'Watch the numbers add up.', 160),
  slide(t, 'BREAKFAST', 'Eggs + toast.', visual=v_fuel(t, '480', '1', '0', '32g'), size=170),
  slide(t, 'LUNCH', 'Chicken rice bowl.', visual=v_fuel(t, '1,140', '2', '0', '84g'), size=150),
  slide(t, 'SNACK', 'Greek yogurt.', visual=v_fuel(t, '1,320', '2', '1', '102g', hi='Snacks'), size=160),
  slide(t, 'DINNER', 'Salmon + potatoes.', visual=v_fuel(t), size=150),
  cta(t)]

S['036-worst-hyrox-station'] = (t := P['red']) and [
  hook(t, "What's your worst HYROX station?", 'Comment it. Be honest.', 160),
  slide(t, 'THE 16', 'Pick one.', visual=v_16(t), size=170),
  slide(t, 'NOT SURE?', 'Time it.', body='Your slowest split tells you.', visual=v_hyrox(t), size=170),
  slide(t, 'HYROX MODE', '16 splits. Every one timed.', visual=v_bigs(t, '16', ' splits'), size=124),
  slide(t, 'THEN', 'Train it.', visual=v_split(t), size=170),
  cta(t)]

S['037-day-after-leg-day'] = (t := P['cyan']) and [
  hook(t, 'Me the day after leg day.', 'Every. Single. Time.', 180),
  slide(t, '9:00 AM', 'Took the elevator one floor.', visual=v_bigs(t, '1', ' floor'), size=124),
  slide(t, '12:00 PM', 'Sitting down is a commitment.', visual=v_vs(t, 'Sit down fast', 'Lower slowly, hold the desk'), size=124),
  slide(t, '6:00 PM', 'Still logged the protein.', visual=v_fuel(t), size=124),
  slide(t, '9:00 PM', "Checked tomorrow's split.", visual=v_split(t), size=124),
  cta(t)]

S['038-run-stats-explained'] = (t := P['black']) and [
  hook(t, 'Distance, pace, time: what each one tells you.', 'Runners, save this.', 140),
  slide(t, 'DISTANCE', 'How far you went.', visual=v_bigs(t, '3.10', ' mi'), size=140),
  slide(t, 'PACE', 'How fast, per mile.', visual=v_bigs(t, "8'42\"", '/mi'), size=140),
  slide(t, 'TIME', 'How long you were out.', visual=v_bigs(t, '26:59'), size=140),
  slide(t, 'ROUTE', 'Where you went. All in Solxce.', visual=v_run(t), size=124),
  cta(t)]

S['039-ppl-or-upper-lower'] = (t := P['volt']) and [
  hook(t, 'PPL or upper/lower? Pick one.', 'Comment A or B.', 170),
  slide(t, 'A', 'Push / Pull / Legs.', visual=week2(t, [('MON', 'Push', True), ('TUE', 'Pull', True), ('WED', 'Legs', True), ('THU', 'Rest', False)]), size=140),
  slide(t, 'B', 'Upper / Lower.', visual=week2(t, [('MON', 'Upper', True), ('TUE', 'Lower', True), ('WED', 'Rest', False), ('THU', 'Upper', True)]), size=150),
  slide(t, 'EITHER WAY', "Today's split, on screen.", visual=v_split(t), size=130),
  slide(t, 'YOUR VOTE', 'A or B?', visual=v_poll(t, 'Push / Pull / Legs', 'Upper / Lower'), size=170),
  cta(t)]

S['040-nobody-tells-beginners'] = (t := P['paper']) and [
  hook(t, 'Things nobody tells you when you start the gym.', 'Save this if you’re new.', 140),
  slide(t, '01', 'You need a plan, not motivation.', visual=v_split(t), size=118),
  slide(t, '02', 'Food matters as much as lifting.', visual=v_fuel(t), size=118),
  slide(t, '03', 'Cardio is allowed.', visual=v_run(t), size=150),
  slide(t, '04', 'Progress is slow. Document it.', visual=v_posts(t), size=124),
  cta(t)]

S['041-pov-hyrox-sim'] = (t := P['purple']) and [
  hook(t, 'POV: you just finished your first HYROX sim.', 'On the floor. Phone in hand.', 140),
  slide(t, 'RUN 8 DONE', 'Every split, timed.', visual=v_hyrox(t), size=140),
  slide(t, 'THE DAMAGE', 'Wall balls hurt.', visual=v_bigs(t, '6:44'), size=150),
  slide(t, 'THE TAKEAWAY', 'Now you know what to train.', visual=v_split(t), size=124),
  slide(t, 'THE POST', 'Post the finish.', visual=v_posts(t, ('Start', 'Wall balls', 'Finish')), size=160),
  cta(t)]

S['042-holiday-no-fall-off'] = (t := P['red']) and [
  hook(t, 'How to not fall off during the holidays.', '4 rules. Screenshot them.', 150),
  slide(t, 'RULE 1', 'Keep the split, even short.', visual=v_split(t), size=130),
  slide(t, 'RULE 2', 'Log the big meals too.', visual=v_fuel(t, '2,480', '3', '2', '121g'), size=130),
  slide(t, 'RULE 3', 'Run in the morning.', visual=v_run(t), size=140),
  slide(t, 'RULE 4', 'Post weekly check-ins.', visual=v_posts(t, ('Week 1', 'Week 2', 'Week 3')), size=130),
  cta(t)]

S['043-running-red-flags'] = (t := P['orange']) and [
  hook(t, 'Running red flags 🚩', 'How many is too many?', 180),
  slide(t, '🚩 01', 'No idea what your pace is.', visual=v_vs(t, '"I felt fast"', "8'42\" per mile, logged"), size=124),
  slide(t, '🚩 02', 'Same route. Never mapped.', visual=v_run(t), size=124),
  slide(t, '🚩 03', '"I ran like 5 miles."', visual=v_vs(t, '"Like 5 miles"', '4.62 mi, tracked'), size=124),
  slide(t, '🚩 04', 'Never posts the long run.', visual=v_posts(t, ('Long run', 'The route', 'After')), size=124),
  cta(t)]

S['044-annual-math'] = (t := P['cobalt']) and [
  hook(t, 'The math on Solxce annual.', 'Get your calculator out.', 180),
  slide(t, 'MONTHLY', '$9.99 × 12', visual=v_bigs(t, '$119.88', '', 200), size=150),
  slide(t, 'ANNUAL', 'One payment.', visual=v_bigs(t, '$79.99', '', 220), size=150),
  slide(t, 'YOU SAVE', '33%.', visual=v_bigs(t, '$6.67', '/mo', 220), size=170),
  slide(t, 'SAME APP', 'Every feature.', visual=v_tiles(t, TILES), size=160),
  cta(t)]

S['045-pov-protein-goal'] = (t := P['black']) and [
  hook(t, 'POV: it’s 9pm and you’re 14g short on protein.', 'We’ve all been here.', 140),
  slide(t, '9:00 PM', '14g to go.', visual=v_fuel(t, '1,690', '3', '1', '128g'), size=170),
  slide(t, '9:04 PM', 'Greek yogurt it is.', visual=v_bigs(t, '+14', 'g'), size=150),
  slide(t, '9:12 PM', 'Done.', visual=v_fuel(t), size=180),
  slide(t, 'TOMORROW', 'Do it again.', visual=v_split(t), size=170),
  cta(t)]

S['046-winter-gym-bag'] = (t := P['paper']) and [
  hook(t, 'Winter gym bag essentials.', 'The last one does the most.', 170),
  slide(t, 'THE LIST', 'Pack this:', visual=v_list(t, ['Hoodie for the walk in', 'Gloves for the run', 'Water bottle', 'Headphones', 'Solxce on your phone']), size=150),
  slide(t, 'THE PHONE', "Today's split.", visual=v_split(t), size=160),
  slide(t, 'THE GLOVES', 'For the cold run.', visual=v_run(t, '3.00 mi', "9'20\"", '28:00'), size=150),
  slide(t, 'THE HOODIE', 'For the post-gym pic.', visual=v_posts(t, ('Gym fit', 'PR set', 'After')), size=140),
  cta(t)]

S['047-unpopular-running-opinions'] = (t := P['cyan']) and [
  hook(t, 'Unpopular running opinions.', 'Comment the one you disagree with.', 170),
  slide(t, '01', 'Slow runs count.', body='A mile is a mile. Log it.', visual=v_run(t, '3.00 mi', "11'10\"", '33:30'), size=160),
  slide(t, '02', 'Treadmill miles are real miles.', visual=v_bigs(t, '1', ' mile'), size=124),
  slide(t, '03', "If it's not tracked, you'll forget it.", visual=v_run(t), size=118),
  slide(t, '04', 'Lifters should run.', body='And log today’s split too.', visual=v_split(t), size=150),
  cta(t)]

S['048-start-running'] = (t := P['volt']) and [
  hook(t, 'How to start running when you hate running.', '4 steps. Start this week.', 140),
  slide(t, 'STEP 1', 'Start with one mile.', visual=v_bigs(t, '1', ' mile'), size=150),
  slide(t, 'STEP 2', 'Track every run.', visual=v_run(t, '1.00 mi', "10'48\"", '10:48'), size=150),
  slide(t, 'STEP 3', 'Put runs on the calendar.', visual=v_week(t), size=130),
  slide(t, 'STEP 4', 'Compare your pace week to week.', visual=v_run(t, '1.00 mi', "9'57\"", '9:57'), size=118),
  cta(t)]

S['049-rate-my-day'] = (t := P['red']) and [
  hook(t, 'Rate my training day out of 10.', 'Be brutal in the comments.', 170),
  slide(t, 'TRAINING', 'Legs & Core.', visual=v_split(t), size=160),
  slide(t, 'FOOD', 'All logged.', visual=v_fuel(t), size=170),
  slide(t, 'CARDIO', 'Easy 5K.', visual=v_run(t), size=170),
  slide(t, 'POSTED', 'Obviously.', visual=v_posts(t, ('Squats', 'PR set', 'Post-run')), size=170),
  cta(t)]

S['050-sunday-reset'] = (t := P['paper']) and [
  hook(t, 'Sunday reset: 4 things to do tonight.', 'Monday you will thank you.', 150),
  slide(t, '01', "Check this week's split.", visual=v_week(t), size=130),
  slide(t, '02', 'Plan your protein.', visual=v_fuel(t), size=150),
  slide(t, '03', 'Pick your run days.', visual=v_run(t), size=150),
  slide(t, '04', 'Post last week.', visual=v_posts(t, ('Mon', 'PR day', 'Sun')), size=160),
  cta(t)]

S['051-hyrox-16-explained'] = (t := P['black']) and [
  hook(t, 'What are the 16 HYROX splits?', 'Explained in 15 seconds.', 160),
  slide(t, 'THE RUNS', '8 × 1 km.', body='One before every station.', visual=v_bigs(t, '8', ' runs'), size=170),
  slide(t, 'STATIONS 1–4', 'SkiErg. Sled Push. Sled Pull. Burpee Broad Jumps.', size=110),
  slide(t, 'STATIONS 5–8', 'Row. Farmers Carry. Sandbag Lunges. Wall Balls.', size=110),
  slide(t, 'HYROX MODE', 'Solxce times all 16.', visual=v_hyrox(t), size=130),
  cta(t)]

S['052-every-gym-session'] = (t := P['orange']) and [
  hook(t, 'Things that happen every gym session.', 'Tell me I’m wrong.', 160),
  slide(t, '01', "Someone's on your machine.", visual=v_bigs(t, '1', ' set left', 220), size=124),
  slide(t, '02', 'Playlist skips at the worst moment.', visual=v_vs(t, 'Hype song', 'Slow ballad mid-set'), size=118),
  slide(t, '03', 'You forget what you did last week.', body="Unless it's in Solxce.", visual=v_split(t), size=118),
  slide(t, '04', 'You check your protein in the car.', visual=v_fuel(t), size=118),
  cta(t)]

S['053-tracking-myths'] = (t := P['cyan']) and [
  hook(t, 'Tracking myths you can stop believing.', 'Comment which one you used to think.', 150),
  slide(t, 'MYTH 01', 'Tracking food is too much.', visual=v_myth(t, 'Only for meal-prep people', 'Logging meals and snacks shows what you actually eat.'), size=124),
  slide(t, 'MYTH 02', 'Progress pics are cringe.', visual=v_myth(t, 'Skip the photos', 'Week 1 photos are the ones you’ll want later.'), size=124),
  slide(t, 'MYTH 03', 'Runs need their own app.', visual=v_myth(t, 'Separate run app', 'Route, distance, pace and time, in Solxce.'), size=124),
  slide(t, 'MYTH 04', 'You have to train daily.', visual=v_myth(t, '7 days a week', 'Follow a split with rest days in it.'), size=124),
  cta(t)]

S['054-pov-back-after-3-days'] = (t := P['volt']) and [
  hook(t, 'POV: you open Solxce after skipping 3 days.', 'No guilt. Just the plan.', 140),
  slide(t, 'TODAY', 'The split is still there.', visual=v_split(t), size=130),
  slide(t, 'FOOD LOG', 'Empty. Fix that.', visual=v_fuel(t, '0', '0', '0', '0g'), size=150),
  slide(t, 'LAST RUN', 'Last week. Time for one.', visual=v_run(t), size=124),
  slide(t, 'THE MOVE', 'Start again today.', visual=v_bigs(t, 'Day 1'), size=140),
  cta(t)]

S['055-protein-myths'] = (t := P['black']) and [
  hook(t, 'Protein myths I believed way too long.', 'Number 2 was me for years.', 150),
  slide(t, 'MYTH 01', '"Only shakes count."', visual=v_myth(t, 'Protein = shakes', 'Every meal and snack adds to the total.'), size=130),
  slide(t, 'MYTH 02', '"I\'ll remember what I ate."', visual=v_myth(t, 'Memory works', "It doesn't. Log it when you eat it."), size=124),
  slide(t, 'MYTH 03', '"Bodybuilders only."', visual=v_myth(t, 'Not for me', 'Anyone who trains can track it.'), size=130),
  slide(t, 'THE FIX', 'Count it daily.', visual=v_fuel(t), size=150),
  cta(t)]

S['056-runner-starter-pack'] = (t := P['purple']) and [
  hook(t, 'The runner starter pack.', 'Tag the runner in your life.', 170),
  starter2(t, 'Runner starter pack', ['Three pairs of the same shoe', 'Race bib collection', 'Up at 5:30am', 'Gel in every pocket', 'Talks about pace. A lot.'], 'Every run mapped in Solxce'),
  slide(t, 'THE APP', 'Every route, logged.', visual=v_run(t), size=140),
  slide(t, 'THE STATS', 'Distance. Pace. Time.', visual=v_tiles(t, [('3.10 mi', 'Distance'), ("8'42\"", 'Pace'), ('26:59', 'Time'), ('Route', 'Mapped')]), size=130),
  slide(t, 'THE POST', 'Long run pic, obviously.', visual=v_posts(t, ('Sunrise', 'Long run', 'Medal')), size=124),
  cta(t)]

S['057-week-of-food'] = (t := P['paper']) and [
  hook(t, 'What a week of food logging looks like.', 'Real days, real numbers (example).', 150),
  slide(t, 'MONDAY', 'Locked in.', visual=v_fuel(t, '1,920', '3', '1', '148g'), size=170),
  slide(t, 'WEDNESDAY', 'Solid.', visual=v_fuel(t, '2,010', '3', '2', '139g'), size=170),
  slide(t, 'FRIDAY', 'Pizza night. Logged anyway.', visual=v_fuel(t, '2,380', '3', '2', '117g'), size=124),
  slide(t, 'SUNDAY', 'Back on it.', visual=v_fuel(t, '1,880', '3', '1', '151g'), size=170),
  cta(t)]

S['058-hyrox-vs-gym'] = (t := P['red']) and [
  hook(t, 'HYROX training vs regular gym training.', 'Which one are you doing?', 150),
  slide(t, 'THE GOAL', 'Different targets.', visual=v_duo(t, 'GYM', 'Get stronger', 'HYROX', 'Race faster'), size=150),
  slide(t, 'THE TRACKING', 'Different numbers.', visual=v_duo(t, 'GYM', 'Your split', 'HYROX', '16 splits timed'), size=150),
  slide(t, 'THE RUNNING', 'Very different.', visual=v_duo(t, 'GYM', 'Optional', 'HYROX', '8 km of it'), size=150),
  slide(t, 'THE APP', 'Solxce does both.', visual=v_tiles(t, [('Split', 'Gym days'), ('HYROX', '16 splits'), ('Runs', 'Mapped'), ('Food', 'Counted')]), size=150),
  cta(t)]

S['059-hit-protein-goal'] = (t := P['volt']) and [
  hook(t, 'How to hit your protein goal without overthinking.', '4 steps.', 140),
  slide(t, 'STEP 1', 'Know your number.', body='Example goal:', visual=v_bigs(t, '142', 'g'), size=150),
  slide(t, 'STEP 2', 'Protein at every meal.', visual=v_fuel(t, '1,210', '2', '0', '88g', hi='Meals'), size=130),
  slide(t, 'STEP 3', 'Pick snacks that help.', visual=v_fuel(t, '1,410', '2', '1', '108g', hi='Snacks'), size=130),
  slide(t, 'STEP 4', 'Check before dinner.', visual=v_fuel(t), size=150),
  cta(t)]

S['060-gym-confessions'] = (t := P['cobalt']) and [
  hook(t, 'Gym confessions. Comment yours.', 'No judgment zone.', 170),
  slide(t, '01', '"I\'ve never tracked a run."', visual=v_vs(t, 'Never tracked', 'Route, pace, time on every run'), size=124),
  slide(t, '02', '"I don\'t know my protein."', visual=v_vs(t, 'No idea', '142g, counted'), size=124),
  slide(t, '03', '"I skip legs when nobody\'s looking."', visual=v_vs(t, 'Skipped again', 'Legs & Core is on the split'), size=118),
  slide(t, '04', '"I have 4 fitness apps."', visual=v_vs(t, '4 apps', '1 app'), size=124),
  cta(t)]

S['061-pov-cold-run'] = (t := P['cyan']) and [
  hook(t, "POV: it's 34°F and you're running anyway.", 'Mile 1 is a lie.', 150),
  slide(t, 'MILE 1', "Can't feel your hands.", visual=v_run(t, '1.00 mi', "9'48\"", '9:48'), size=140),
  slide(t, 'MILE 2', 'Okay. Warming up.', visual=v_run(t, '2.00 mi', "9'21\"", '19:09'), size=140),
  slide(t, 'MILE 3', 'This is actually nice.', visual=v_run(t, '3.10 mi', "9'02\"", '28:01'), size=130),
  slide(t, 'AFTER', 'Post it. You earned it.', visual=v_posts(t, ('Frost', 'Mile 3', 'Hot coffee')), size=140),
  cta(t)]

S['062-lifters-who-run'] = (t := P['black']) and [
  hook(t, 'Lifters who run: 4 rules.', 'Hybrid era starts now.', 170),
  slide(t, 'RULE 1', 'Put runs on the calendar.', visual=v_week(t), size=130),
  slide(t, 'RULE 2', 'Keep the split going.', visual=v_split(t), size=140),
  slide(t, 'RULE 3', 'Eat for both.', visual=v_fuel(t), size=160),
  slide(t, 'RULE 4', 'Track pace, not just miles.', visual=v_run(t), size=124),
  cta(t)]

S['063-november-check-in'] = (t := P['orange']) and [
  hook(t, 'Halfway through November. Check in.', 'Comment your score out of 4.', 150),
  slide(t, '01', 'Followed your split?', visual=v_split(t), size=140),
  slide(t, '02', 'Hit protein most days?', visual=v_fuel(t), size=140),
  slide(t, '03', 'Ran this month?', body='Example month so far:', visual=v_bigs(t, '18', ' mi'), size=150),
  slide(t, '04', 'Posted your progress?', visual=v_posts(t, ('Nov 1', 'Nov 8', 'Nov 15')), size=130),
  cta(t)]

S['064-hybrid-athlete-signs'] = (t := P['purple']) and [
  hook(t, "Signs you're a hybrid athlete.", 'If 3 hit, welcome to the club.', 170),
  slide(t, '01', 'Lift days and run days.', visual=v_week(t), size=140),
  slide(t, '02', 'You know your pace and your squat.', visual=v_run(t), size=118),
  slide(t, '03', "You've looked up HYROX.", visual=v_hyrox(t), size=140),
  slide(t, '04', 'You eat like it.', visual=v_fuel(t), size=160),
  cta(t)]

S['065-hyrox-myths'] = (t := P['paper']) and [
  hook(t, 'HYROX myths, busted.', 'Thinking about your first race? Read this.', 180),
  slide(t, 'MYTH 01', '"It\'s only for elite athletes."', visual=v_myth(t, 'Pros only', 'There are divisions for first-timers. Train and show up.'), size=118),
  slide(t, 'MYTH 02', '"It\'s all strength."', visual=v_myth(t, 'Just stations', 'There are 8 km of running in it.'), size=140),
  slide(t, 'MYTH 03', '"Pacing doesn\'t matter."', visual=v_myth(t, 'Go hard from Run 1', 'Split times show where you fade.'), size=124),
  slide(t, 'MYTH 04', '"You can\'t time it alone."', visual=v_myth(t, 'Need a coach with a stopwatch', 'Solxce HYROX mode times all 16 splits.'), size=124),
  cta(t)]

S['066-pov-6am-crew'] = (t := P['volt']) and [
  hook(t, 'POV: you’re part of the 6am gym crew.', 'Quiet gym. Loud playlist.', 150),
  slide(t, '5:45 AM', 'Alarm. Snooze. No.', visual=v_bigs(t, '5:45'), size=150),
  slide(t, '6:02 AM', 'Open Solxce. Legs & Core.', visual=v_split(t), size=124),
  slide(t, '7:10 AM', 'Breakfast logged.', visual=v_fuel(t, '520', '1', '0', '41g'), size=150),
  slide(t, '7:15 AM', 'Posted before work.', visual=v_posts(t, ('Empty gym', 'Squats', 'Coffee')), size=140),
  cta(t)]

S['067-ranking-gym-days'] = (t := P['red']) and [
  hook(t, 'Ranking every gym day. Fight me.', 'Comment your #1.', 170),
  slide(t, 'MY RANKING', 'Best to worst:', visual=v_list(t, ['1. Push day', '2. Pull day', '3. Run day', '4. Rest day', '5. Leg day'], check=False), size=150),
  slide(t, '#1', 'Push day.', visual=week2(t, [('MON', 'Push', True), ('TUE', 'Pull', False), ('WED', 'Legs', False), ('THU', 'Run', False)]), size=170),
  slide(t, '#3', 'Run day deserves more love.', visual=v_run(t), size=124),
  slide(t, '#5', 'Leg day. Still doing it.', visual=v_split(t), size=140),
  cta(t)]

S['068-hyrox-training-day'] = (t := P['black']) and [
  hook(t, 'A day of HYROX training, tracked.', 'Morning to night.', 160),
  slide(t, '7 AM', 'Easy run.', visual=v_run(t, '3.00 mi', "9'30\"", '28:30'), size=170),
  slide(t, '12 PM', 'Fuel.', visual=v_fuel(t), size=180),
  slide(t, '6 PM', 'Stations, timed.', visual=v_hyrox(t), size=150),
  slide(t, '9 PM', 'Post the session.', visual=v_posts(t, ('Run', 'Sled push', 'Done')), size=150),
  cta(t)]

S['069-gym-thankful'] = (t := P['cobalt']) and [
  hook(t, 'Things gym people are thankful for.', 'Happy Thanksgiving 🦃', 160),
  slide(t, '01', 'Rest days.', visual=v_week(t), size=180),
  slide(t, '02', 'Leftover turkey. (Protein.)', visual=v_fuel(t, '2,240', '3', '1', '156g'), size=124),
  slide(t, '03', 'A dry morning run.', visual=v_run(t), size=150),
  slide(t, '04', 'Having it all in one app.', visual=v_tiles(t, TILES), size=124),
  cta(t)]

S['070-friendsgiving-guide'] = (t := P['orange']) and [
  hook(t, 'Friendsgiving survival guide for gym people.', 'Bring this energy.', 140),
  slide(t, '01', 'Bring the protein dish.', visual=v_fuel(t, '980', '1', '1', '74g', hi='Protein'), size=130),
  slide(t, '02', 'Log the plate. Yes, the pie too.', visual=v_fuel(t, '2,410', '3', '2', '119g', hi='Snacks'), size=118),
  slide(t, '03', 'Morning run first.', visual=v_run(t), size=150),
  slide(t, '04', 'Group pic goes on the feed.', visual=v_posts(t, ('The table', 'Pie', 'Group pic')), size=124),
  cta(t)]

S['071-dont-wait-for-january'] = (t := P['red']) and [
  hook(t, "Don't wait for January to start.", 'Starting now beats starting later.', 170),
  slide(t, 'THE MATH', 'December 1 is closer.', visual=v_bigs(t, 'Dec 1', '', 220), size=140),
  slide(t, 'NOW', 'Start the split.', visual=v_split(t), size=160),
  slide(t, 'NOW', 'Count your food.', visual=v_fuel(t), size=160),
  slide(t, 'NOW', 'Run.', visual=v_run(t), size=180),
  cta(t)]

S['072-running-mistakes'] = (t := P['paper']) and [
  hook(t, 'Running mistakes I made for a year.', 'Learn from my pain.', 160),
  slide(t, 'MISTAKE 01', 'Never tracking pace.', body='Fix: log every run.', visual=v_run(t), size=140),
  slide(t, 'MISTAKE 02', 'Same route, every day.', body='Fix: map new routes, compare them.', visual=v_run(t, '4.10 mi', "9'15\"", '37:55'), size=140),
  slide(t, 'MISTAKE 03', 'No strength days.', body="Fix: follow a split.", visual=v_split(t), size=150),
  slide(t, 'MISTAKE 04', 'Under-eating.', body='Fix: count it.', visual=v_fuel(t), size=160),
  cta(t)]

S['073-pov-pr-nobody-saw'] = (t := P['purple']) and [
  hook(t, 'POV: you hit a PR and nobody saw it.', 'Empty gym. Huge lift.', 150),
  slide(t, 'THE SET', 'Barbell Squats.', visual=v_split(t), size=150),
  slide(t, 'THE GYM', 'Empty.', visual=v_bigs(t, '0', ' witnesses', 220), size=180),
  slide(t, 'THE FIX', 'Post the video.', visual=v_posts(t, ('Warm-up', 'Squat PR', 'After')), size=160),
  slide(t, 'NOW', "It's on your profile forever.", visual=v_bigs(t, 'PR'), size=124),
  cta(t)]

S['074-snack-audit'] = (t := P['cyan']) and [
  hook(t, 'Snack audit: how many did you have today?', 'Comment your number.', 150),
  slide(t, '10 AM', 'Coffee + protein bar.', visual=v_fuel(t, '610', '1', '1', '46g', hi='Snacks'), size=140),
  slide(t, '3 PM', 'Chips from the office.', visual=v_fuel(t, '1,380', '2', '2', '92g', hi='Snacks'), size=140),
  slide(t, '10 PM', 'Cereal. Standing up.', visual=v_fuel(t, '2,060', '3', '3', '131g', hi='Snacks'), size=140),
  slide(t, 'THE POINT', 'Logged = honest.', visual=v_bigs(t, '3', ' snacks'), size=150),
  cta(t)]

S['075-track-every-run'] = (t := P['black']) and [
  hook(t, 'Track every run. Even the slow ones.', 'Here’s why.', 160),
  slide(t, '01', 'You see your pace change.', visual=v_run(t), size=130),
  slide(t, '02', 'You remember your routes.', visual=v_run(t, '5.00 mi', "9'40\"", '48:20'), size=130),
  slide(t, '03', 'You stay consistent.', visual=v_week(t), size=140),
  slide(t, '04', 'You can post the long ones.', visual=v_posts(t, ('Route', 'Long run', 'Finish')), size=124),
  cta(t)]

S['076-legs-core-today'] = (t := P['volt']) and [
  hook(t, "Legs & Core today. What's yours?", 'Drop your split in the comments.', 160),
  slide(t, 'TODAY', 'The split.', visual=v_split(t), size=170),
  slide(t, 'THE LIFTS', '4 moves.', visual=v_list(t, ['Barbell Squats', 'Romanian Deadlifts', 'Leg Press', 'Hanging Knee Raises']), size=170),
  slide(t, 'AFTER', 'Refuel.', visual=v_fuel(t), size=180),
  slide(t, 'YOUR TURN', 'Comment yours.', visual=v_poll(t, 'Legs today', 'Anything but legs'), size=150),
  cta(t)]

S['077-hits-different'] = (t := P['orange']) and [
  hook(t, 'Things that hit different when you train.', 'Number 4 is underrated.', 150),
  slide(t, '01', 'Food after leg day.', visual=v_fuel(t), size=150),
  slide(t, '02', 'A run with no wind.', visual=v_run(t), size=150),
  slide(t, '03', 'Week 12 photos.', visual=v_posts(t), size=160),
  slide(t, '04', "Opening the app and the plan's there.", visual=v_split(t), size=118),
  cta(t)]

S['078-monthly-or-annual'] = (t := P['red']) and [
  hook(t, 'Monthly or annual? Which would you pick?', 'Comment A or B.', 150),
  slide(t, 'A · MONTHLY', '$9.99 a month.', body='Go month to month.', visual=v_bigs(t, '$9.99', '/mo', 220), size=140),
  slide(t, 'B · ANNUAL', '$79.99 a year.', body='Save 33%.', visual=v_bigs(t, '$6.67', '/mo', 220), size=140),
  slide(t, 'SAME APP', 'Same features.', visual=v_tiles(t, TILES), size=160),
  slide(t, 'YOUR VOTE', 'A or B?', visual=v_poll(t, '$9.99 monthly', '$79.99 annual'), size=170),
  cta(t)]

S['079-hyrox-race-week'] = (t := P['purple']) and [
  hook(t, 'HYROX race week checklist.', 'Save this for the week before.', 170),
  slide(t, 'EARLY WEEK', 'Short, sharp runs.', visual=v_run(t, '2.00 mi', "8'20\"", '16:40'), size=140),
  slide(t, 'MIDWEEK', 'Light station touch-up.', visual=v_hyrox(t), size=130),
  slide(t, 'LATE WEEK', 'Eat. Sleep. Log it.', visual=v_fuel(t), size=140),
  slide(t, 'RACE DAY', 'Time all 16 splits.', visual=v_16(t), size=140),
  cta(t)]

S['080-thoughts-every-set'] = (t := P['paper']) and [
  hook(t, 'Thoughts I have during every set.', 'Rep 8 is a different person.', 170),
  slide(t, 'REP 1', 'Easy. Light. Why did I warm up?', visual=v_bigs(t, '1'), size=124),
  slide(t, 'REP 5', 'Why do I do this to myself.', visual=v_bigs(t, '5'), size=124),
  slide(t, 'REP 8', 'One more. ONE more.', visual=v_bigs(t, '8'), size=140),
  slide(t, 'REP 10', 'Posting this.', visual=v_posts(t, ('Warm-up', 'Rep 10', 'After')), size=160),
  cta(t)]

S['081-solxce-in-4-words'] = (t := P['cobalt']) and [
  hook(t, 'Solxce in 4 words.', 'Plus one bonus.', 190),
  slide(t, 'WORD 1', 'Train.', visual=v_split(t), size=200),
  slide(t, 'WORD 2', 'Fuel.', visual=v_fuel(t), size=200),
  slide(t, 'WORD 3', 'Run.', visual=v_run(t), size=200),
  slide(t, 'WORD 4', 'Post.', visual=v_posts(t), size=200),
  cta(t, 'Bonus: HYROX.<br>Out now on iOS.')]
