# Solxce promo video pipeline

Used by the monthly scheduled task to make and post new TikTok / Instagram Reels.

- `slides/` : slide decks. Each `shows*/NAME.html` is a 1080x1920 deck of 6 `<section class="slide">`
  (hook, 4 feature slides, CTA). `gen*.py` are the generators that wrote them (helpers in `_h*.py`, decks in `shows*.py`).
  `gen4.py` (= gen3 helpers + `shows4.py` + output) writes `shows4/`; its fit script also shrinks headlines that overflow sideways.
  Palette: red #ff3352, black #08080a, paper #f4f3ef, volt #d7e04a, orange #ff6a2a, cobalt #2440e6, cyan #5ed3e8, purple #1a0b33.
  Fonts: system 'Inter' / 'Inter Display' (Black). Keep text between y 290-1520 and 150px from the right edge.
- `promo/music.py` : original synthesized beats (house/trap/phonk/drive), safe for business accounts and ads.
- `promo/promo.py` + `promo/videos.py` : renders each deck to a beat-synced MP4 + cover + caption.txt.
  Paths in videos.py point at `../slides/shows*`. Batch 4 entries carry a `theme` key used to alternate the schedule.
- `../videos/`, `../covers/` : published media. Metricool pulls from
  `https://raw.githubusercontent.com/solxceofficial-hub/solxce-media/main/<path>`.
- `posted.txt` : every video already scheduled (don't repeat a hook).

NEW FEATURE (Oct 31, 2026): Run challenges. Users invite friends to a challenge over 1 week, 2 weeks
or 1 month, competing on most miles, longest total time, longest run, fastest time, or most runs.
Feature it in roughly 1 of every 3 posts (challenge-a-friend, leaderboard, "who wins" comment bait, tag-a-friend).

Only claim real features: run challenges with friends (above), today's split, food tracking (calories/meals/snacks/protein), run tracking
(route/distance/pace/time), posting photos/videos, HYROX mode (16 splits). $9.99/mo or $79.99/yr.
No fake testimonials.
