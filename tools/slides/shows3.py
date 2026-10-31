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
