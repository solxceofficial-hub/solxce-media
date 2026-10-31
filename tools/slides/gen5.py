"""Batch 5: run-challenge decks (invite friends; 1 week / 2 weeks / 1 month;
most miles, longest total time, longest run, fastest time, most runs). Reuses gen4 helpers."""
import os, json
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gen4.py')).read()
exec(_src.split("S['021")[0])
_tail = _src[_src.index("CSS = '''"):].replace('shows4', 'shows5')
os.chdir(os.path.dirname(os.path.abspath(__file__)))

TYPES = [('Most miles', 'Total distance'), ('Longest time', 'Total time running'), ('Longest run', 'Single biggest run'),
         ('Fastest time', 'Quickest pace'), ('Most runs', 'Show up the most')]


def lb(t, title, dur, rows, left='3 days left', hi=0):
    hb, hf = HI(t)
    r = ''
    for i, (n, v) in enumerate(rows):
        on = i == hi
        r += (f'<div style="display:flex;align-items:center;gap:24px;padding:20px 24px;border-radius:24px;margin-top:10px;'
              f'background:{hb if on else "transparent"};color:{hf if on else t["cfg"]};border:{"none" if on else "2px solid " + t["line"]}">'
              f'<span style="font-family:\'Inter Display\';font-weight:900;font-size:44px;width:44px">{i+1}</span>'
              f'<span style="flex:1;font-size:40px;font-weight:700">{n}</span><span style="font-size:40px;font-weight:800">{v}</span></div>')
    return card(t, f'''<div style="display:flex;justify-content:space-between;align-items:center"><span class="small">RUN CHALLENGE · {dur}</span>
      <span style="font-size:24px;font-weight:800;padding:8px 18px;border-radius:99px;background:{hb};color:{hf}">{left}</span></div>
      <div style="font-size:64px;font-weight:800;letter-spacing:-2px;margin:14px 0 6px">{title}</div>{r}''', pad='34px 34px 30px')


def v_invite(t, who, ctype, dur):
    hb, hf = HI(t)
    if who == 'You':
        return card(t, f'''<div style="display:flex;align-items:center;gap:26px">
        <div style="width:110px;height:110px;border-radius:50%;background:{hb};color:{hf};display:flex;align-items:center;justify-content:center"><svg width="56" height="56" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M22 2 11 13M22 2l-7 20-4-9-9-4 20-7z"/></svg></div>
        <div><div style="font-size:44px;font-weight:800">Challenge sent</div><div style="font-size:32px;opacity:.75;margin-top:4px">{ctype} · {dur}</div></div></div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:34px">
        <div style="text-align:center;padding:26px;border-radius:28px;background:{hb};color:{hf};font-size:40px;font-weight:800">+ Invite more</div>
        <div style="text-align:center;padding:26px;border-radius:28px;border:3px solid {t["line"]};font-size:40px;font-weight:700;opacity:.8">Copy link</div></div>''')
    return card(t, f'''<div style="display:flex;align-items:center;gap:26px">
        <div style="width:110px;height:110px;border-radius:50%;background:{hb};color:{hf};display:flex;align-items:center;justify-content:center;font-family:'Inter Display';font-weight:900;font-size:56px">{who[0]}</div>
        <div><div style="font-size:44px;font-weight:800">{who} invited you</div><div style="font-size:32px;opacity:.75;margin-top:4px">{ctype} · {dur}</div></div></div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:34px">
        <div style="text-align:center;padding:26px;border-radius:28px;background:{hb};color:{hf};font-size:40px;font-weight:800">Accept</div>
        <div style="text-align:center;padding:26px;border-radius:28px;border:3px solid {t["line"]};font-size:40px;font-weight:700;opacity:.8">Decline</div></div>''')


def v_types(t, hi=None):
    hb, hf = HI(t)
    cells = ''.join(f'<div style="border-radius:30px;padding:28px;min-height:190px;display:flex;flex-direction:column;justify-content:space-between;background:{hb if i == hi else t["card"]};color:{hf if i == hi else t["cfg"]}"><span style="font-size:24px;font-weight:700;opacity:.7">0{i+1}</span><div><div style="font-size:40px;font-weight:800">{a}</div><div style="font-size:26px;opacity:.75;margin-top:4px">{b}</div></div></div>' for i, (a, b) in enumerate(TYPES))
    cells += f'<div style="border-radius:30px;padding:28px;min-height:190px;border:3px dashed {t["mute"]};display:flex;flex-direction:column;justify-content:center;font-size:32px;font-weight:800;line-height:1.3">1 week<br>2 weeks<br>1 month</div>'
    return f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">{cells}</div>'


def v_durs(t, hi=1):
    hb, hf = HI(t)
    c = ''.join(f'<div style="border-radius:32px;padding:36px 20px;text-align:center;background:{hb if i == hi else t["card"]};color:{hf if i == hi else t["cfg"]}"><div style="font-family:\'Inter Display\';font-weight:900;font-size:96px;line-height:1">{n}</div><div style="font-size:30px;font-weight:700;margin-top:8px">{u}</div></div>' for i, (n, u) in enumerate([('1', 'WEEK'), ('2', 'WEEKS'), ('1', 'MONTH')]))
    return f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:14px">{c}</div>'


S = {}
P = T
F4 = [('Maya', '18.4 mi'), ('You', '16.9 mi'), ('Jordan', '12.2 mi'), ('Sam', '9.7 mi')]

S['c01-gym-partner'] = (t := P['red']) and [
  hook(t, 'Challenge your gym partner.', 'Loser buys the coffee.', 170),
  slide(t, 'STEP 1', 'Send the invite.', visual=v_invite(t, 'You', 'Most miles', '1 week'), size=150),
  slide(t, 'STEP 2', 'Pick the rules.', body='Most miles, longest time, longest run, fastest time or most runs.', visual=v_durs(t, 0), size=150),
  slide(t, 'STEP 3', 'Watch the board.', visual=lb(t, 'Most miles', '1 WEEK', [('You', '14.2 mi'), ('Chris', '13.8 mi')], '2 days left'), size=150),
  slide(t, 'STEP 4', 'Collect your coffee.', body='Every run counts automatically with Solxce run tracking.', visual=v_run(t), size=140),
  cta(t)]

S['c02-most-miles-7-days'] = (t := P['black']) and [
  hook(t, 'Most miles in 7 days. Who wins?', 'A friendly challenge. Very unfriendly leaderboard.', 160),
  slide(t, 'THE CHALLENGE', 'Most miles. One week.', visual=v_durs(t, 0), size=140),
  slide(t, 'DAY 4', 'It’s close.', visual=lb(t, 'Most miles', '1 WEEK', F4, '3 days left', 1), size=160),
  slide(t, 'EVERY RUN', 'Counts automatically.', body='Route, distance, pace and time, tracked.', visual=v_run(t), size=140),
  slide(t, 'YOUR TURN', 'Invite your crew.', visual=v_invite(t, 'Maya', 'Most miles', '1 week'), size=150),
  cta(t)]

S['c03-pov-invite'] = (t := P['purple']) and [
  hook(t, 'POV: your friend invites you to a run challenge.', 'You haven’t run since summer.', 140),
  slide(t, '9:02 PM', 'The notification.', visual=v_invite(t, 'Alex', 'Most runs', '2 weeks'), size=150),
  slide(t, 'DAY 1', 'You accept. Obviously.', body='Pride is a powerful pre-workout.', visual=v_run(t, '1.80 mi', "10'05\"", '18:09'), size=140),
  slide(t, 'DAY 10', 'Somehow you’re winning.', visual=lb(t, 'Most runs', '2 WEEKS', [('You', '8 runs'), ('Alex', '7 runs'), ('Taylor', '5 runs')], '4 days left'), size=140),
  slide(t, 'DAY 14', 'New habit unlocked.', body='That’s the point of a challenge.', visual=v_bigs(t, '9', ' runs'), size=150),
  cta(t)]

S['c04-five-ways'] = (t := P['volt']) and [
  hook(t, '5 ways to beat your friends this week.', 'Pick your battle.', 170),
  slide(t, 'THE OPTIONS', 'Five challenges.', visual=v_types(t, 0), size=140),
  slide(t, 'FOR GRINDERS', 'Most miles or most runs.', body='Volume wins.', visual=lb(t, 'Most runs', '1 WEEK', [('Jess', '6 runs'), ('You', '5 runs'), ('Omar', '4 runs')], '2 days left', 1), size=130),
  slide(t, 'FOR SPEED', 'Fastest time.', body='One fast run can steal the crown.', visual=v_run(t, '3.10 mi', "7'21\"", '22:48'), size=150),
  slide(t, 'FOR DISTANCE', 'Longest run.', body='Go long once. Hold on.', visual=v_bigs(t, '10.4', ' mi'), size=150),
  cta(t)]

S['c05-pick-length'] = (t := P['cobalt']) and [
  hook(t, '1 week, 2 weeks or 1 month?', 'Pick your challenge length.', 170),
  slide(t, 'THE LENGTHS', 'Short, medium, brutal.', visual=v_durs(t, 1), size=140),
  slide(t, '1 WEEK', 'A sprint.', body='Perfect for a quick bet with a friend.', visual=lb(t, 'Fastest time', '1 WEEK', [('Leo', "7'48\"/mi"), ('You', "8'02\"/mi"), ('Ana', "8'40\"/mi")], '5 days left', 1), size=150),
  slide(t, '1 MONTH', 'A habit.', body='Most runs over 30 days builds the routine.', visual=v_bigs(t, '30', ' days'), size=160),
  slide(t, 'COMMENT', 'Which one are you picking?', visual=v_poll(t, '1 week sprint', '1 month grind'), size=130),
  cta(t)]

S['c06-fastest-mile'] = (t := P['orange']) and [
  hook(t, 'Fastest time wins. Tag your rival.', 'One run. No excuses.', 170),
  slide(t, 'THE RULE', 'Fastest time takes it.', visual=v_types(t, 3), size=130),
  slide(t, 'THE BOARD', 'Seconds matter.', visual=lb(t, 'Fastest time', '2 WEEKS', [('Priya', "7'12\"/mi"), ('You', "7'15\"/mi"), ('Dan', "7'59\"/mi")], '6 days left', 1), size=150),
  slide(t, 'TRACKED', 'Pace, time, route.', visual=v_run(t, '1.00 mi', "7'15\"", '7:15'), size=150),
  slide(t, 'GO', 'Tag the one who thinks they’re faster.', size=120, visual=v_invite(t, 'You', 'Fastest time', '2 weeks')),
  cta(t)]

S['c07-tag-friend'] = (t := P['paper']) and [
  hook(t, 'Tag the friend you’d beat in a run challenge.', 'Then actually invite them.', 140),
  slide(t, 'HOW', 'Invite in two taps.', visual=v_invite(t, 'You', 'Longest run', '1 month'), size=150),
  slide(t, 'CHOOSE', 'Your best event.', visual=v_types(t, 2), size=150),
  slide(t, 'PROVE IT', 'The board doesn’t lie.', visual=lb(t, 'Longest run', '1 MONTH', [('You', '11.2 mi'), ('Nico', '9.8 mi'), ('Bea', '7.5 mi')], '12 days left'), size=150),
  slide(t, 'BONUS', 'Post the win.', visual=v_posts(t, ('Start', 'Long run', 'Winner')), size=160),
  cta(t)]

S['c08-longest-run'] = (t := P['cyan']) and [
  hook(t, 'Longest run challenge. Who’s built for distance?', 'One big run decides it.', 140),
  slide(t, 'THE RULE', 'Your single longest run.', visual=v_bigs(t, '1', ' run'), size=140),
  slide(t, 'WEEK 2', 'Someone went long.', visual=lb(t, 'Longest run', '2 WEEKS', [('Rosa', '13.1 mi'), ('You', '10.0 mi'), ('Kai', '8.6 mi')], '3 days left', 1), size=150),
  slide(t, 'YOUR ANSWER', 'The weekend long run.', visual=v_run(t, '13.30 mi', "9'31\"", '2:06:37'), size=140),
  slide(t, 'START ONE', 'Invite your run club.', visual=v_invite(t, 'Rosa', 'Longest run', '2 weeks'), size=150),
  cta(t)]

S['c09-group-chat'] = (t := P['red']) and [
  hook(t, 'Your group chat needs a run challenge.', 'Less memes. More miles.', 160),
  slide(t, 'STEP 1', 'Invite the whole chat.', visual=v_invite(t, 'Group chat', 'Most miles', '2 weeks'), size=150),
  slide(t, 'STEP 2', 'Let the trash talk begin.', visual=lb(t, 'Most miles', '2 WEEKS', [('Tay', '22.0 mi'), ('Marco', '19.4 mi'), ('You', '18.1 mi'), ('Jo', '6.2 mi')], '5 days left', 2), size=140),
  slide(t, 'STEP 3', 'Someone always ghosts.', body='(Jo, we see you.)', visual=v_bigs(t, '6.2', ' mi'), size=150),
  slide(t, 'STEP 4', 'Winner posts the screenshot.', visual=v_posts(t, ('Day 1', 'Final board', 'Winner')), size=130),
  cta(t)]

S['c10-most-runs-month'] = (t := P['black']) and [
  hook(t, 'Most runs in a month. Consistency wins.', 'Not the fastest. The most stubborn.', 150),
  slide(t, 'THE CHALLENGE', 'Most runs. 30 days.', visual=v_durs(t, 2), size=140),
  slide(t, 'THE SECRET', 'Short runs count too.', body='A 1-mile run is still a run.', visual=v_run(t, '1.05 mi', "9'40\"", '10:09'), size=140),
  slide(t, 'DAY 21', 'The board.', visual=lb(t, 'Most runs', '1 MONTH', [('You', '17 runs'), ('Mia', '15 runs'), ('Ben', '11 runs')], '9 days left'), size=160),
  slide(t, 'DAY 30', 'Habit built.', visual=v_bigs(t, '24', ' runs'), size=160),
  cta(t)]

S['c11-leaderboard-check'] = (t := P['volt']) and [
  hook(t, 'Leaderboard check: day 5 of 7.', 'Who’s sweating?', 170),
  slide(t, 'MOST MILES', 'Tight at the top.', visual=lb(t, 'Most miles', '1 WEEK', F4, '2 days left', 1), size=150),
  slide(t, 'THE MOVE', 'One long run flips it.', visual=v_run(t, '5.20 mi', "8'55\"", '46:22'), size=150),
  slide(t, 'DAY 7', 'Flipped.', visual=lb(t, 'Most miles', '1 WEEK', [('You', '22.1 mi'), ('Maya', '20.3 mi'), ('Jordan', '14.0 mi')], 'Final'), size=170),
  slide(t, 'NEXT', 'Run it back. 2 weeks.', visual=v_durs(t, 1), size=150),
  cta(t)]

S['c12-30-seconds'] = (t := P['cobalt']) and [
  hook(t, 'Start a run challenge in 30 seconds.', 'Here’s how.', 170),
  slide(t, '', '4 taps.', visual=v_steps(t, [('Open Solxce', 'Go to challenges'), ('Pick a type', 'Miles, time, longest, fastest, most runs'), ('Pick a length', '1 week, 2 weeks or 1 month'), ('Invite friends', 'They get the invite instantly')]), size=150),
  slide(t, 'TYPE', 'Choose your event.', visual=v_types(t, 1), size=150),
  slide(t, 'LENGTH', 'Choose your timeline.', visual=v_durs(t, 1), size=150),
  slide(t, 'DONE', 'Now go run.', visual=lb(t, 'Longest time', '2 WEEKS', [('You', '3h 12m'), ('Eli', '2h 58m'), ('Zoe', '2h 10m')], '13 days left'), size=160),
  cta(t)]

S['c13-couples'] = (t := P['purple']) and [
  hook(t, 'Couples run challenge. Who’s winning?', 'Relationship status: competitive.', 160),
  slide(t, 'THE INVITE', 'Sent at breakfast.', visual=v_invite(t, 'Your partner', 'Most miles', '1 month'), size=150),
  slide(t, 'WEEK 2', 'It’s getting personal.', visual=lb(t, 'Most miles', '1 MONTH', [('Them', '31.4 mi'), ('You', '30.9 mi')], '16 days left', 1), size=150),
  slide(t, 'THE TRUTH', 'Every mile is logged.', body='No “I ran yesterday, trust me.”', visual=v_run(t), size=150),
  slide(t, 'COMMENT', 'Who wins in your house?', visual=v_poll(t, 'Me, obviously', 'Them (don’t tell them)'), size=140),
  cta(t)]

S['c14-coworkers'] = (t := P['orange']) and [
  hook(t, 'Office run challenge: 2 weeks, most miles.', 'Finally, something to talk about besides meetings.', 140),
  slide(t, 'MONDAY', 'Invites go out.', visual=v_invite(t, 'Dana', 'Most miles', '2 weeks'), size=150),
  slide(t, 'DAY 9', 'Accounting is winning?', visual=lb(t, 'Most miles', '2 WEEKS', [('Dana', '24.6 mi'), ('Raj', '21.0 mi'), ('You', '19.8 mi'), ('Kim', '15.3 mi')], '5 days left', 2), size=140),
  slide(t, 'LUNCH BREAK', 'Sneak in a run.', visual=v_run(t, '3.00 mi', "8'50\"", '26:30'), size=150),
  slide(t, 'TAG', 'Tag the coworker you’d beat.', visual=v_durs(t, 1), size=130),
  cta(t)]

S['c15-miles-or-speed'] = (t := P['black']) and [
  hook(t, 'Most miles or fastest time?', 'Comment your pick. Defend it.', 170),
  slide(t, 'OPTION A', 'Most miles.', body='Volume. Patience. Grind.', visual=lb(t, 'Most miles', '1 WEEK', [('You', '21.0 mi'), ('Ty', '18.2 mi')], '1 day left'), size=160),
  slide(t, 'OPTION B', 'Fastest time.', body='One perfect run. Pure speed.', visual=lb(t, 'Fastest time', '1 WEEK', [('Ty', "6'58\"/mi"), ('You', "7'20\"/mi")], '1 day left', 1), size=160),
  slide(t, 'VOTE', 'Which are you?', visual=v_poll(t, 'Most miles', 'Fastest time'), size=160),
  slide(t, 'OR', 'Do both. Pick any of 5 challenges.', visual=v_types(t), size=120),
  cta(t)]

S['c16-passed-you'] = (t := P['red']) and [
  hook(t, 'Your friend just passed you on the leaderboard.', 'What are you doing about it?', 140),
  slide(t, '7:41 PM', 'You’re in 2nd.', visual=lb(t, 'Longest time', '1 WEEK', [('Sam', '2h 41m'), ('You', '2h 35m'), ('Liv', '1h 50m')], '1 day left', 1), size=160),
  slide(t, '7:43 PM', 'Shoes on.', visual=v_run(t, '2.40 mi', "9'10\"", '22:00'), size=170),
  slide(t, '8:10 PM', 'Back on top.', visual=lb(t, 'Longest time', '1 WEEK', [('You', '2h 57m'), ('Sam', '2h 41m'), ('Liv', '1h 50m')], '1 day left'), size=160),
  slide(t, 'THAT’S', 'The power of a challenge.', visual=v_durs(t, 0), size=140),
  cta(t)]

S['c17-things-people-say'] = (t := P['paper']) and [
  hook(t, 'Things people say during a run challenge.', 'Be honest, you’ve said #3.', 150),
  slide(t, '01', '“I’m just running easy this week.”', body='(Leads by 6 miles.)', visual=lb(t, 'Most miles', '1 WEEK', [('Them', '19.0 mi'), ('You', '13.0 mi')], '3 days left', 1), size=120),
  slide(t, '02', '“My watch died, that counts.”', body='Solxce logs route, distance, pace and time.', visual=v_run(t), size=120),
  slide(t, '03', '“Rematch. 2 weeks this time.”', visual=v_durs(t, 1), size=120),
  slide(t, '04', '“Who invited Coach?”', visual=v_invite(t, 'Coach', 'Fastest time', '1 week'), size=130),
  cta(t)]

S['c18-family-thanksgiving'] = (t := P['orange']) and [
  hook(t, 'Thanksgiving week family run challenge.', 'Race your cousins before dinner.', 150),
  slide(t, 'THE INVITE', 'Send it to the family chat.', visual=v_invite(t, 'Aunt Lisa', 'Most runs', '1 week'), size=130),
  slide(t, 'THE BOARD', 'Grandpa is winning?', visual=lb(t, 'Most runs', '1 WEEK', [('Grandpa', '5 runs'), ('You', '4 runs'), ('Cousin Max', '2 runs')], 'Thanksgiving', 1), size=140),
  slide(t, 'TURKEY TROT', 'Every run counts.', visual=v_run(t, '3.10 mi', "9'02\"", '28:01'), size=150),
  slide(t, 'COMMENT', 'Who wins at your table?', visual=v_poll(t, 'Me', 'Grandpa'), size=150),
  cta(t)]

S['c19-longest-time'] = (t := P['cyan']) and [
  hook(t, 'Not fast? Pick the longest-time challenge.', 'Time on your feet wins. Not pace.', 140),
  slide(t, 'THE RULE', 'Total time running.', visual=v_types(t, 1), size=150),
  slide(t, 'WHO WINS', 'Whoever keeps going.', visual=lb(t, 'Longest time', '2 WEEKS', [('You', '4h 05m'), ('Jamal', '3h 48m'), ('Kate', '3h 12m')], '4 days left'), size=150),
  slide(t, 'SLOW IS FINE', 'Every minute counts.', visual=v_run(t, '2.50 mi', "11'30\"", '28:45'), size=150),
  slide(t, 'START', 'Invite a friend at your pace.', visual=v_durs(t, 1), size=140),
  cta(t)]

S['c20-red-flags'] = (t := P['red']) and [
  hook(t, 'Run challenge red flags. 🚩', 'How many is your friend guilty of?', 160),
  slide(t, 'RED FLAG 01', 'Picks fastest time because they did track.', visual=v_types(t, 3), size=110),
  slide(t, 'RED FLAG 02', 'Goes silent, then drops a 10-miler on day 7.', visual=lb(t, 'Most miles', '1 WEEK', [('Silent Steve', '24.0 mi'), ('You', '18.5 mi')], 'Final', 1), size=110),
  slide(t, 'RED FLAG 03', 'Screenshots the board every hour.', visual=v_posts(t, ('9 AM', '10 AM', '11 AM')), size=120),
  slide(t, 'GREEN FLAG', 'Invites you to a rematch.', visual=v_invite(t, 'Steve', 'Most miles', '2 weeks'), size=130),
  cta(t)]

S['c21-why-run-alone'] = (t := P['purple']) and [
  hook(t, 'Why run alone?', 'Race your friends from anywhere.', 190),
  slide(t, 'ANYWHERE', 'Different cities. Same board.', visual=lb(t, 'Most miles', '1 MONTH', [('Ava (Austin)', '41 mi'), ('You', '38 mi'), ('Noah (NYC)', '33 mi')], '10 days left', 1), size=130),
  slide(t, 'ANY LEVEL', 'Pick a challenge that fits.', visual=v_types(t, 4), size=140),
  slide(t, 'ANY LENGTH', 'A week to a month.', visual=v_durs(t, 2), size=150),
  slide(t, 'TRACKED', 'Every run counts.', visual=v_run(t), size=160),
  cta(t)]

S['c22-day1-day30'] = (t := P['black']) and [
  hook(t, 'Day 1 vs Day 30 of a monthly run challenge.', 'Same person. Different habits.', 140),
  slide(t, 'DAY 1', '“I’ll do a couple runs.”', visual=v_run(t, '1.20 mi', "11'10\"", '13:24'), size=140),
  slide(t, 'DAY 12', 'Competitive mode on.', visual=lb(t, 'Most runs', '1 MONTH', [('Rae', '9 runs'), ('You', '8 runs'), ('Cole', '6 runs')], '18 days left', 1), size=140),
  slide(t, 'DAY 30', 'Running is just… normal now.', visual=v_run(t, '4.00 mi', "9'05\"", '36:20'), size=130),
  slide(t, 'RESULT', '20 runs in 30 days.', visual=v_bigs(t, '20', ' runs'), size=140),
  cta(t)]

S['c23-which-challenge'] = (t := P['volt']) and [
  hook(t, 'Which run challenge fits you?', 'Comment your number.', 170),
  slide(t, '', 'Pick one.', visual=v_types(t), size=160),
  slide(t, 'THE GRINDER', 'Most miles or most runs.', visual=lb(t, 'Most miles', '2 WEEKS', [('You', '26.3 mi'), ('Iris', '24.0 mi')], '2 days left'), size=140),
  slide(t, 'THE SPRINTER', 'Fastest time.', visual=lb(t, 'Fastest time', '1 WEEK', [('You', "6'49\"/mi"), ('Max', "7'05\"/mi")], '4 days left'), size=150),
  slide(t, 'THE DIESEL', 'Longest run or longest time.', visual=v_bigs(t, '15.0', ' mi'), size=140),
  cta(t)]

S['c24-december-challenge'] = (t := P['cobalt']) and [
  hook(t, 'December starts tomorrow. Start a challenge tonight.', 'One month. Your friends. Most runs.', 130),
  slide(t, 'THE PLAN', '1-month challenge.', visual=v_durs(t, 2), size=150),
  slide(t, 'THE EVENT', 'Most runs wins.', body='Holiday-proof: short runs count.', visual=v_types(t, 4), size=150),
  slide(t, 'THE CREW', 'Invite them now.', visual=v_invite(t, 'You', 'Most runs', '1 month'), size=150),
  slide(t, 'DEC 31', 'Imagine this board.', visual=lb(t, 'Most runs', '1 MONTH', [('You', '22 runs'), ('Mel', '19 runs'), ('Gus', '14 runs')], 'Final'), size=150),
  cta(t)]

exec(_tail)
