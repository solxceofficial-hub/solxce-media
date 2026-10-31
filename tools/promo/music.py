"""Original, royalty-free beat generator for Solxce promo videos.
Every sound is synthesized from scratch, so the audio is safe for ads on TikTok and Instagram.
Styles: house (gym/upbeat), trap (hype), phonk (gymtok), drive (cinematic build for HYROX/running).
"""
import numpy as np
from scipy.signal import butter, sosfilt
import wave

SR = 44100
rng = np.random.default_rng(7)


def mf(m):  # midi -> Hz
    return 440.0 * 2 ** ((m - 69) / 12)


def env(n, a=0.002, d=0.2):
    t = np.arange(n) / SR
    e = np.exp(-t / max(d, 1e-4))
    na = max(1, int(a * SR))
    e[:na] *= np.linspace(0, 1, na)
    return e


def filt(x, kind, f, order=2):
    if isinstance(f, (list, tuple)):
        f = [min(v, SR / 2 - 100) for v in f]
    else:
        f = min(f, SR / 2 - 100)
    return sosfilt(butter(order, f, kind, fs=SR, output='sos'), x)


def kick(punch=1.0, dur=0.42, low=45):
    n = int(dur * SR); t = np.arange(n) / SR
    f = low + (160 - low) * np.exp(-t / 0.035)
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = np.sin(ph) * env(n, 0.001, 0.16 * punch + 0.06)
    x[:int(0.004 * SR)] += rng.uniform(-.6, .6, int(0.004 * SR))
    return np.tanh(x * 1.6)


def clap(dur=0.3):
    n = int(dur * SR); x = np.zeros(n)
    for k, off in enumerate([0, 0.011, 0.022]):
        s = int(off * SR); m = n - s
        x[s:] += rng.uniform(-1, 1, m) * env(m, 0.0005, 0.012 if k < 2 else 0.11)
    return filt(x, 'bandpass', [900, 6000]) * 1.4


def snare(dur=0.28):
    n = int(dur * SR); t = np.arange(n) / SR
    body = np.sin(2 * np.pi * 190 * t) * env(n, 0.001, 0.05)
    nz = filt(rng.uniform(-1, 1, n), 'highpass', 1500) * env(n, 0.001, 0.09)
    return body * 0.6 + nz


def hat(open_=False):
    n = int((0.25 if open_ else 0.06) * SR)
    x = filt(rng.uniform(-1, 1, n), 'highpass', 7500) * env(n, 0.0005, 0.08 if open_ else 0.018)
    return x * (0.5 if open_ else 0.4)


def bass808(note, dur, glide_from=None):
    n = int(dur * SR); t = np.arange(n) / SR
    f = np.full(n, mf(note))
    if glide_from is not None:
        g = np.exp(-t / 0.06); f = mf(note) + (mf(glide_from) - mf(note)) * g
    f = f * (1 + 0.6 * np.exp(-t / 0.012))
    x = np.sin(2 * np.pi * np.cumsum(f) / SR)
    e = np.minimum(1, (t / 0.003)) * np.exp(-t / max(dur * 0.9, 0.05))
    rel = min(n, int(0.02 * SR)); e[-rel:] *= np.linspace(1, 0, rel)
    return np.tanh(x * e * 2.2) * 0.8


def saw(f, n, detune=(-0.12, 0, 0.12)):
    t = np.arange(n) / SR; out = np.zeros(n)
    for d in detune:
        ff = f * 2 ** (d / 12); ph = rng.uniform(0, 1)
        out += 2 * ((t * ff + ph) % 1) - 1
    return out / len(detune)


def chord(notes, dur, cutoff=2500, d=None):
    n = int(dur * SR)
    x = sum(saw(mf(m), n) for m in notes) / len(notes)
    x = filt(x, 'lowpass', cutoff)
    return x * env(n, 0.004, d if d else dur * 0.5)


def pad(notes, dur, cutoff=1400):
    n = int(dur * SR); t = np.arange(n) / SR
    x = sum(saw(mf(m), n, (-0.08, 0.08)) for m in notes) / len(notes)
    x = filt(x, 'lowpass', cutoff)
    a = np.minimum(1, t / 0.25); r = np.minimum(1, (dur - t) / 0.25)
    return x * a * np.clip(r, 0, 1) * 0.5


def cowbell(note, dur=0.32):
    n = int(dur * SR); t = np.arange(n) / SR; f = mf(note)
    x = np.sign(np.sin(2 * np.pi * f * t)) + np.sign(np.sin(2 * np.pi * f * 1.48 * t))
    x = filt(x, 'bandpass', [f * 0.8, f * 4])
    return x * env(n, 0.001, 0.09) * 0.5


def impact(dur=1.6):
    n = int(dur * SR)
    boom = kick(2.5, dur, 35) * 1.1
    nz = filt(rng.uniform(-1, 1, n), 'lowpass', 5000) * env(n, 0.001, 0.5) * 0.35
    return boom + nz


def riser(dur):
    n = int(dur * SR); t = np.arange(n) / SR
    x = rng.uniform(-1, 1, n)
    out = np.zeros(n); seg = 2048
    for i in range(0, n, seg):
        fc = 400 + 9000 * (i / n) ** 2
        out[i:i + seg] = filt(x[i:i + seg], 'bandpass', [fc * 0.7, fc * 1.3], 1)
    return out * (t / dur) ** 2 * 0.6


def place(buf, snd, t, gain=1.0):
    s = int(t * SR)
    if s >= len(buf): return
    e = min(len(buf), s + len(snd)); buf[s:e] += snd[:e - s] * gain


PROG = {  # A minor: i - VI - III - VII
    'roots': [45, 41, 48, 43],
    'chords': [[57, 60, 64, 67], [53, 57, 60, 64], [55, 60, 64, 67], [55, 59, 62, 67]],
}

STYLES = {'house': 124, 'trap': 140, 'phonk': 130, 'drive': 118}


def make(style, total, out_path, bpm=None):
    """Write a WAV of `total` seconds. Returns bpm."""
    bpm = bpm or STYLES[style]
    beat = 60 / bpm; bar = beat * 4
    n = int((total + 0.05) * SR)
    drums = np.zeros(n); music = np.zeros(n); bassb = np.zeros(n)
    duck = np.ones(n)
    nbars = int(np.ceil(total / bar))
    kick_times = []

    for b in range(nbars):
        t0 = b * bar; ci = b % 4
        roots, chs = PROG['roots'][ci], PROG['chords'][ci]
        if style == 'house':
            for i in range(4):
                place(drums, kick(), t0 + i * beat); kick_times.append(t0 + i * beat)
                place(drums, hat(True), t0 + i * beat + beat / 2, 0.55)
                for s in (0.25, 0.75):
                    place(drums, hat(), t0 + i * beat + s * beat, 0.5)
            for i in (1, 3): place(drums, clap(), t0 + i * beat, 0.8)
            for i in range(4):
                place(bassb, bass808(roots + 12, beat * 0.4), t0 + i * beat + beat / 2, 0.55)
            for s in (0.5, 1.5, 2.75):
                place(music, chord(chs, beat * 0.6, 3200, 0.12), t0 + s * beat, 0.5)
        elif style == 'trap':
            place(drums, kick(1.2), t0); kick_times.append(t0)
            place(drums, kick(1.2), t0 + 2.5 * beat); kick_times.append(t0 + 2.5 * beat)
            place(drums, clap(), t0 + 2 * beat, 0.9)
            steps = 16 if b % 2 == 0 else 12
            for i in range(steps):
                place(drums, hat(), t0 + i * beat / 4, 0.55 if i % 2 == 0 else 0.35)
            if b % 2 == 1:
                for i in range(8): place(drums, hat(), t0 + 3 * beat + i * beat / 8, 0.3 + i * 0.03)
            place(bassb, bass808(roots - 12 + 12, beat * 2.4), t0, 0.95)
            place(bassb, bass808(roots + 12, beat * 1.4, glide_from=roots), t0 + 2.5 * beat, 0.85)
            mel = [chs[3] + 12, chs[2] + 12, chs[1] + 12, chs[2] + 12]
            for i, m in enumerate(mel):
                place(music, chord([m], beat * 0.9, 4000, 0.25), t0 + i * beat, 0.32)
            place(music, pad(chs, bar, 1100), t0, 0.35)
        elif style == 'phonk':
            for i in range(4):
                place(drums, kick(1.1), t0 + i * beat); kick_times.append(t0 + i * beat)
            for i in (1, 3): place(drums, snare(), t0 + i * beat, 0.8)
            for i in range(8): place(drums, hat(), t0 + i * beat / 2, 0.45)
            patt = [0, 3, 7, 10, 7, 3, 12, 10]
            for i, p in enumerate(patt):
                place(music, cowbell(69 + p - (0 if ci < 2 else 2)), t0 + i * beat / 2, 0.75)
            place(bassb, bass808(roots, beat * 1.8), t0, 1.0)
            place(bassb, bass808(roots, beat * 1.8), t0 + 2 * beat, 0.9)
        elif style == 'drive':
            intensity = min(1, b / 3)
            for i in range(4):
                place(drums, kick(0.9), t0 + i * beat, 0.6 + 0.4 * intensity); kick_times.append(t0 + i * beat)
            if b >= 1:
                for i in (1, 3): place(drums, snare(), t0 + i * beat, 0.6)
            for i in range(16 if b >= 2 else 8):
                step = beat / (4 if b >= 2 else 2)
                place(drums, hat(), t0 + i * step, 0.35)
            for i in range(8):
                place(bassb, bass808(roots + 12, beat * 0.45), t0 + i * beat / 2, 0.45)
            place(music, pad(chs, bar, 900 + 1200 * intensity), t0, 0.7)

    # sidechain duck on kicks
    dl = int(0.18 * SR); curve = 1 - 0.6 * np.exp(-np.arange(dl) / (0.05 * SR))
    for kt in kick_times:
        s = int(kt * SR); e = min(n, s + dl)
        if s < n: duck[s:e] = np.minimum(duck[s:e], curve[:e - s])

    mix = drums * 0.9 + (music * 0.8 + bassb * 0.75) * duck
    place(mix, impact(), 0, 0.9)  # instant energy on frame 1
    # tail: fade last 0.6 s
    f = int(0.6 * SR); mix[-f:] *= np.linspace(1, 0, f) ** 1.5
    mix = filt(mix, 'highpass', 28)
    mix = np.tanh(mix * 1.3)
    mix = mix / (np.max(np.abs(mix)) + 1e-9) * 0.89
    st = np.stack([mix, mix], 1)
    with wave.open(out_path, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((st * 32767).astype(np.int16).tobytes())
    return bpm


if __name__ == '__main__':
    import sys
    for s in STYLES:
        make(s, 16, f'demo-{s}.wav'); print('wrote', s)
