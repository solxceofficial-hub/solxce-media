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
