# Friendslop deep-study game profiles, part 3 (batches 5 and 6, 20 games)

Compiled 2026-11-11 from existing study files only (no new web research): `research_notes\Friendslop genre market research\deep_profiles_batch_5.md` and `deep_profiles_batch_6.md`, `data\deep_study_numbers.csv`, `data\deep_study_selection.csv`, `data\deep\{appid}\summary.md` and `themes.md`, plus the method notes `layer2_review_themes.md` and `layer2_tooling_method.md`.

**Tags.** [P] verified primary (Steam API/store/histogram, read 2026-11-10/11). [D] developer or publisher claim. [T] third-party (incl. SteamCharts player figures, press, guides). [I] inference. [S] computed from the review sample (n given).

**Read these caveats before using any number.**
- Review sample: games with >1,000 reviews use 500 newest + 500 most-helpful (not random; helpful stratum skews to launch-period, long or joke reviews; recent stratum skews to late adopters and sale buyers). Games with <=1,000 reviews are a census. Playtime figures are hours *at review*.
- Theme counts are multilingual keyword matches (codebook v4: micro precision ~0.86 / recall ~0.90 in-sample, ~0.77 / 0.66 on the frozen holdout). They are mentions, not severity. Some quotes in the theme files are false positives (e.g. "minor bugs" checkbox templates, "optimizing your layout" counted as performance); quotes below were picked to match the theme. Praise counts are on positive reviews; complaint counts on all codable reviews. German, French, Portuguese and Turkish recall is low.
- Player "month 1/3/6/12" figures are SteamCharts calendar-month *proxies* (average of the monthly averages of the calendar months overlapping days 1-30, 61-90, 151-180, 331-365), not exact window averages.
- Sentiment histogram counts sit near the Steam-purchase subset, not the all-language total; use them for shape.
- Price history was blocked for every game (gg.deals 403, ITAD API 403, SteamDB 403). Discounts come only from developer posts and the current store price.

---

## 1. Supermarket Together

**appid 2709570 | stratum: hit | pair P05 (reference game: co-op store sim) | released 2024-08-09 (full release) | free to play, one $4.99 cosmetic DLC [P] | 1-16 players, solo with hireable staff [P] | DeadDevsTellNoLies, self-published [P] | core type: job_simulation | 101,350 reviews, 94.3% positive (Very Positive) [P]**

| metric | value |
|---|---|
| Median h at review (all / pos / neg) | 8.31 / 8.55 / 3.79 (n=1000 / 956 / 44) [S] |
| <2h / >10h / >50h | 12.9% / 44.9% / 9.2% [S] |
| Top 3 languages | English 35.3%, Russian 15.4%, German 8.3% [P] |
| SteamCharts all-time peak | 47,731 (2024-08) [T] |
| Month 1 / 3 / 6 / 12 avg proxy | 17,124 / 9,530 / 8,797 / 5,846 [T] |
| Current players | 2,877 (2026-11-11) [P] |

**Core loop & inputs.** Stock shelves, run checkouts, clean and chase shoplifters through an in-game day, then spend profit and franchise points on space, products, perks and staff [P]. First-person carry/drop, hand tablet for pricing and ordering, broom swing (hits shoplifters and friends), later tools and a rideable kart [D]. Built-in voice or text chat: not found.
**Dependence on each other.** One shared store and money pool; demand scales with player count, so the work is split [P]. Host can kick, set permissions or "jail" lazy friends [D].
**Failure / dead players.** No death or game-over. Since 2025-02 unpaid invoices bring a debt-collector squad and unpaid staff stop showing up (switchable per save) [D]. A jailed player waits out the host's punishment count [D].

**What it gets right.** Good value/free 187 (22.2% of codable positives), fun with friends 174 (20.6%), addictive 46, progression 37, relaxing/cozy 34 [S, n=844 codable positives]. "Didn't think a supermarket simulator would keep us busy for hours, but here we are."

**Where players push back.** Bugs 44, repetitive 38, monetisation/DLC 34 (mostly neutral mentions of the optional DLC), grind 18, toxic randoms 14 [S, n=887 codable]. The 43 codable negatives cite price/progress loss 5, bugs 4, performance 4; tech failure appears in 25.6% of negatives. "there is no freaking autosave and i lost all the price update i just done LOL" / "the only thing I would hope to see improved is multiplayer anti troll measures." **<2h** (n=126 codable): praise is friends 18 and free 15; complaints performance 7, bugs 5, price 5; tech failure in 43.8% of these negatives. **>20h** (n=235, only 5 negative): value 70, friends 50, addictive 24; mild repetitive/bugs/DLC mentions (16-17 each).

**Sentiment over time.** 92.2% in launch month, peaking at 97.3% in Nov 2024 when monthly reviews jumped +151% (15,354 up) without a player rise; this coincides with the Autumn Sale/Steam Awards nomination window [P timing, I cause]. Since then 91-95% every month, with a small Nov 2025 repeat (95.1%) [P].

**What happened after launch.** Weekly patch cadence ("a full year of weekly updates", 2025-08-16) [D]: host tools, pharmacy, customisation, employee rework, invoices/loans (2025-02), Order Packaging, autosave (only 2025-07-16), Manufacturing (2026-01), Plaza layout (2026-06), Supermarket Kart (2026-08) [D]. Players fell from 21,371 avg (Aug 2024) to ~5-7k and then stayed flat for 20 months [T]. Bumps: Jan 2025 +33% (winter event and holidays [I]), Jan 2026 +21% (Manufacturing [I]), Jul 2026 +21% (Plaza [I]); Sep 2026 -26% after the alien event ended [I]. Mar-Apr 2025 drop: cause unknown. Monetisation stays one DLC: "There won't be more." [P]. Reach claim: "10 million downloads… 8,5 million unique users" (2025-01-01) [D].

**Launch path & team.** No announcement, demo, playtest or Next Fest found; first Steam post is launch day [P]. Viral in launch week via free price and press ("surprise hit", PCGamesN; 12-15k concurrent within a day per Japanese press) [T]. Team: "The two members of this project" [D]; later posts say "I". Developer on workload: changelog "around every Wednesday" to handle daily mails [D]; autosave was requested "in forums, private messages, email… Reddit, Twitter" [D].

**Unknowns.** Wishlists, engine, location, dev time, real-time session length, DLC discount levels, price history, the cause of the Mar-Apr 2025 decline, voice chat.

---

## 2. Gamble With Your Friends

**appid 3892270 | stratum: hit | no pair | released 2026-05-01 (1.0) | $7.99, launch week $4.99 (-38%) [D/P] | 1-6 players, friends-only, solo "not advised" [P] | TEAM GWYF / TENSTACK (Swedish) | core type: other (casino co-op) | 26,960 reviews, 89.7% positive (Very Positive) [P]**

| metric | value |
|---|---|
| Median h at review (all / pos / neg) | 4.53 / 4.75 / 2.60 (n=1000 / 889 / 111) [S] |
| <2h / >10h / >50h | 16.1% / 15.7% / 0.8% [S] |
| Top 3 languages | English 58.4%, Russian 12.2%, Simplified Chinese 6.1% [P] |
| SteamCharts all-time peak | 24,666 (2026-09-13) [T]; ITAD page claims 42,848, Automaton ~38,000 (unreconciled) [T] |
| Month 1 / 3 / 6 / 12 avg proxy | 10,859 / 6,467 / 5,904 / not yet [T] |
| Current players | 2,215 [P] |

**Core loop & inputs.** Each 5-minute casino "day", the team gambles from one shared bank across 17 games on 4 tower floors to hit a loan shark's quota, then spends Tickets on odds-bending items and cosmetics [P]. Full game "Around 2-3 hours… with 3 endings" [D]. First-person physics, bets/keypads, items, emotes, **proximity voice**, ping, selling body parts for Tickets [P/D].
**Dependence on each other.** One shared bank: "one bad all-in can ruin the run for everyone" [P].
**Failure / dead players.** Missing quota means "face the consequences"; the exact consequence and what dead players do: not found.

**What it gets right.** Fun with friends 175 (22.3% of codable positives), addictive 50, funny 40, good value 39, progression 21 [S, n=784]. "Stress & Dopamine This is the most fun I've had with friends in some time."

**Where players push back.** Repetitive 41, too short 33, bugs 26, RNG/balance 23, needs friends 19, cheaters 15 [S, n=892]. Negatives (n=108) lead with repetitive 21 (19.4%), price 10, too short 9, RNG 9; refunds mentioned in 6.5% of negatives. "it was fun for like an hour, but you very quickly run out of new stuff" **<2h** (n=146, 44 negative): repetitive 11, bugs 8, needs friends 6, "clone / cash grab" 6. **>20h** is tiny (n=35; 33 positive), mostly friends and addictive praise.

**Sentiment over time.** Very flat: weekly 85-92% from launch to November [P]. Lowest week 85.1% (2026-09-04) during the unexplained September player spike; the 2026-10-02 week jumped +82% in volume at 90.8% [P].

**What happened after launch.** Dev claims: 500K copies in 3 days, 1M in a week, 2M in a month [D]. Poland regional price cut after feedback (2026-05-04) [D]; patches made the default lobby Friends Only [D]; V1.0.30 (2026-07-24) added 13 languages, per-save rules and Endless Mode [D]. Players fell -31%, -28%, -28% (Jun-Aug) [T], then **Sep +60% (peak 24,666)** with no developer post, sale or press found: cause unknown [P/T]. No real-money in-game purchases promised [D]; only DLC is a $1.99 soundtrack [P].

**Launch path & team.** Announced ~2025-08-17: "30K+ wishlists in 3 days" [D]; selective TESTERSTACK playtest ("we're a small team") [D]; no demo, Next Fest not found; 170K+ wishlists by launch [D]. About 8.5 months from reveal to 1.0. "A small Swedish studio" [D]; studio philosophy: "games you can finish in a couple of sessions" [D].

**Unknowns.** Team size, engine, prior games, quota-fail consequence, dead-player state, discount percentages, cause of the September spike, the true all-time peak.

---

## 3. Species: Unknown

**appid 2747330 | stratum: hit | no pair | Early Access 2025-10-23 | $9.99 (launch week -10%) [P/D] | 1-4 players [D] | WanadevStudio (Lyon), self-published | core type: escape_survival | 12,884 reviews, 90.9% positive (Very Positive) [P]**

| metric | value |
|---|---|
| Median h at review (all / pos / neg) | 14.98 / 14.17 / 18.38 (n=1000 / 817 / 183) [S] |
| <2h / >10h / >50h | 3.8% / 63.4% / 10.8% [S] |
| Top 3 languages | English 66.6%, French 9.1%, Russian 7.7% [P] |
| SteamCharts all-time peak | 4,822 (2026-10-30) [T] |
| Month 1 / 3 / 6 / 12 avg proxy | 668 / 497 / 394 / 471 [T] |
| Current players | 1,074 [P] |

**Core loop & inputs.** Take a contract, board a derelict ship, read clues to identify which procedurally chosen creature is hunting you, complete the objective, extract for credits, upgrade [P]. Missions "about 30 minutes" [D]. FPS movement, weapons, tracker, shield, ally-healing syringe, carry/throw canisters; voice chat at launch (not proximity); proximity chat and radio from 2026-04-16 [D].
**Dependence on each other.** Shared objectives, creature-specific group strategy, healing allies [P/D]. Week 1: ~80% of matches multiplayer, 50% of sessions duos, mostly private [D].
**Failure / dead players.** Death in contract with limited respawns per contract type [D]; exact rules and dead-player activity: not found.

**What it gets right.** Monsters 239 (31.0% of codable positives), visuals/audio 214, potential 198, fun with friends 190, horror 170, progression 141 [S, n=772]. "This is basically casual Alien Isolation, with many aspects of the xenomorph split into different monsters"

**Where players push back.** Too little content 112, repetitive 81, bugs 73, RNG/balance 62, lost progress 59, grind 59 [S, n=954]. Negatives (n=182; median 18.4 h, *longer* than positives) lead with lost progress 28, RNG 26, repetitive 25, grind 25; tech failure in 30.2%. "Developers wiped all progress from every player in an update." / "Locking progression behind RNG is definitely a choice of all time." **<2h** is small (n=35): praise for atmosphere; complaints performance 4, content 4. **>20h** (n=367): lost progress 38, grind 37, content 36 - long-term players carry the complaints.

**Sentiment over time.** 91-97% weekly for a year [P]. Week of 2026-10-29: **349 up / 471 down (42.6%)** after the Stormrock update's progression reset; next week back to 87.6% after the dev apology and save restoration [P/D].

**What happened after launch.** Dev claims: 28,000 players week 1, 100,000 in a month, 250,000 and ~300K wishlists by Feb 2026 [D]. The Lab (2026-01) +7%; first sale -20% (Mar 2026); **first new specimen 0.21 (2026-05-21): players +163%, peak 4,530** [T]; Jul -46% with no content and the map delay [I]; anti-cheat patch (2026-10-09); Stormrock new map + reset (2026-10-29): peak 4,822, last-30-day avg 917 (+81%) [T]. Price increases promised with content and at 1.0, none yet [P]. Supporter Pack DLC $9.99 [P].

**Launch path & team.** Announced 2024-05-29; Scream Fest reveal; streamer playtest (2025-05); closed beta (2025-06); demo 2025-09-24; Next Fest Oct 2025; EA 10 days later [D]. ~42K wishlists before launch [I], 85K in week 1 [D]. Two full-time developers within a ~10-person studio; UE5 + EOS; first non-VR game after Ragnarock [D]. Regret: "we underestimated how strongly some of you would feel about losing progress" [D].

**Unknowns.** Exact death/respawn rules, dead-player role, price history, cause of Sep 2026 review bump, 1.0 date (target ~2 years after EA [D]).

---

## 4. GRAIN ROT

**appid 4450620 | stratum: mid | no pair | released 2026-08-07 (1.0) | $9.99, launch -10% [P/D] | 1-5 players [D] | Beck & Branch Games (duo) / Neem Interactive | core type: extraction | 2,638 reviews, 88.1% positive (Very Positive) [P]**

| metric | value |
|---|---|
| Median h at review (all / pos / neg) | 8.32 / 8.61 / 5.71 (n=1000 / 872 / 128) [S] |
| <2h / >10h / >50h | 11.2% / 41.9% / 3.7% [S] |
| Top 3 languages | English 54.0%, Russian 19.5%, Simplified Chinese 5.7% [P] |
| SteamCharts all-time peak | not tracked (HTTP 404) |
| Month 1 / 3 / 6 / 12 avg proxy | not found (not tracked) |
| Current players | 303 (snapshot 2026-11-11 02:04 UTC; batch note gives 333) [P] |

**Core loop & inputs.** Ride a cursed elevator into procedural ruins, smash or rip out furniture, scavenge or feed items to the Grinder for gold while Corrupted enemies close in; extract and rebuild the Outpost to go deeper [P]. Melee mallet, dropkick, carry furniture, build constructs, swap wooden vessels, emotes, voice that distorts with the Rot [D].
**Dependence on each other.** Shared extraction ("If everyone breaks, your loot is lost") and shared Outpost; friendly-fire trolling is a feature, with an optional grief-protection toggle [P/D].
**Failure / dead players.** A broken vessel becomes a **Spark** that guides the team and searches for a new host "before you fade out completely" [P]. Total wipe loses the loot; Expedition Mode (1.1) adds permadeath [D].

**What it gets right.** Fun with friends 182 (23.7% of codable positives), progression 119, monsters 118, visuals 106, potential 104, horror 67 [S, n=768]. "upgrading different rooms actually gives you permanent benefits like more health, speed, strength"

**Where players push back.** Too little content 78, bugs 69, repetitive 41, performance 36, difficulty 32, needs friends 31 [S, n=891]. Negatives (n=123) lead with bugs 29 (23.6%) and too short 15; tech failure in 33.3%. "kicks you in the nut with a VERY short questline, missing content and pretending it's a full released game" / "it should be tagged as early access". **<2h** (n=100, 31 negative): repetitive 10, needs friends 9, performance 7. **>20h** (n=161): bugs 14, content 14, grind 10, but friends praise rises to 32% of positives.

**Sentiment over time.** 86.8-90.8% in the first four weeks, drifting to 78.6-84% by Oct-Nov 2026 as volume fell from 1,014 reviews in launch week to ~25-50 a week [P].

**What happened after launch.** Patches 1.01-1.07 in the first week, incl. a public server browser (1.07) [D]; 1.08 grief protection; 1.1 Expedition permadeath mode + new biome with 15% off (2026-09-24) [D]; October update with third-floor quests, achievements, cloud saves, Twitch Drops [D]. Updates gave only +15-20 reviews a week [P]. Dev claim: "more than 250,000 of you" players (2026-09-24) [D]. No DLC [P].

**Launch path & team.** Announced ~2026-05-30 ("20,000 wishlists in 3 days") [D]; Next Fest June 2026 demo with ~350K downloads, "top 15 most-played" [D]; ~250K wishlists by 2026-07-28 [D]; 24h free full game for Discord members; 1.0 about 10 weeks after reveal. Press release calls it "Mega-viral" with no platform named [D]. Indie duo [D]; Stockholm and Unreal per weak third-party sources [T].

**Unknowns.** Player-count history, session length, wishlist-to-sales conversion, whether the post-launch 20% discount goal was hit, team background, dev time.

---

## 5. Climb The Backrooms

**appid 3575300 | stratum: mid | no pair | released 2025-07-11 (1.0) | $4.99 [P] | 1-4 players, Death Run up to 10 [D] | LovDEV (solo), self-published | core type: climbing_traversal | 1,256 reviews, 80.7% positive (Very Positive) [P]**

| metric | value |
|---|---|
| Median h at review (all / pos / neg) | 3.23 / 3.47 / 1.73 (n=1000 / 799 / 201) [S] |
| <2h / >10h / >50h | 18.5% / 2.9% / 0.4% [S] |
| Top 3 languages | English 77.5%, German 4.5%, Turkish 3.3% [P] |
| SteamCharts all-time peak | 262 (2025-09, monthly peak) [T] |
| Month 1 / 3 / 6 / 12 avg proxy | 24 (Jul missing) / 54 / 24 / 20 [T] |
| Current players | 2 [P] |

**Core loop & inputs.** Climb handcrafted and procedural Backrooms levels by stacking, dragging and throwing physics objects, solve riddles, evade or fight entities [P]. Grab/rotate/throw, push friends, proximity voice only from 2025-08-19, emotes, coin hat shop [D].
**Dependence on each other.** Cooperative stacking and puzzles [P].
**Failure / dead players.** Death with ragdoll scream; checkpoints/"Save Anytime" [P/D]. Dead-player activity: not found.

**What it gets right.** Fun with friends 188 (26.6% of codable positives), funny 92, value 78, horror 70, potential 54, rage-as-fun 32 [S, n=707]. A visible developer presence is a praise driver: "10/10 dev joined the game and it was funny cause he killed my teammate." [S]

**Where players push back.** Too short 90, bugs 74, repetitive 41, trolls 29 (mostly the dev trolling, as praise), clone/low effort 22, price 17 [S, n=895]. Negatives (n=188, 57.7% under 2 h): bugs 29, repetitive 26, low effort 16, price 13. "The levels are short, around a minute long, and the whole experience feels broken." **<2h** (n=171, 108 negative): bugs 18, repetitive 14, price 10, clone 10 - early quitters. **>20h**: only 10 reviews, not interpretable.

**Sentiment over time.** Launch week 46% (6/7) [P]; recovered to 88-93% during the Aug-Sep 2025 voice-chat/1.2 surge; dips to 54-62% around late Dec 2025-Jan 2026 (cause unknown); small and volatile since [P].

**What happened after launch.** 1.1 (10+ levels, 2025-07-19), proximity chat (2025-08-19), push friends, 1.2 cosmetics (2025-09-08) [D]. Sep 2025 +190% (avg 68, peak 262) after voice chat and 1.2; dev credits creators/streamers, none identified [D/I]. 1.3 Death Run, public lobbies, server browser (2026-05-02); -40% Backrooms Banquet sale tied to the Backrooms film (2026-05-27) [D]. Decay to ~4-6 avg from Aug 2026 [T]. No DLC.

**Launch path & team.** No announcement, demo or Next Fest found; store page live before 2025-06-27 [P]. Solo developer ("I've been working tirelessly") after "months of development" [D].

**Unknowns.** Location, engine, prior games, viral source, discount history beyond -40%, Christmas update content, session length (RAWG "1 hour" is weak [T]).

---

## 6. Log Riders

**appid 4082750 | stratum: mid | no pair | released 2026-02-12 (1.0) | $4.99, launch -10% [P/D] | exactly 2 (or solo controlling both; local split keyboard, online, Remote Play) [P] | Bluespy Studios, self-published | core type: shared_object | 785 reviews, 70.2% positive (Mostly Positive) [P]**

| metric | value |
|---|---|
| Median h at review (all / pos / neg) | 1.83 / 2.17 / 1.29 (census n=785 / 551 / 234) [S] |
| <2h / >10h / >50h | 53.1% / 1.1% / 0.0% [S] |
| Top 3 languages | English 28.0%, Simplified Chinese 21.4%, Russian 18.1% [P] |
| SteamCharts all-time peak | 596 (2026-03, monthly peak) [T] |
| Month 1 / 3 / 6 / 12 avg proxy | 175 / 64 / 50 / not yet [T] |
| Current players | 9 [P] |

**Core loop & inputs.** Two lumberjacks on one physics log; each moves forward or back to roll and balance it past obstacles, checkpoint to checkpoint [P]. Forward/back only, keyboard halves or one controller with two sticks (full controller support from 2026-04-18), emotes, text chat, coin cosmetics [D]. A full run is roughly an hour or more (achievement relaxed from 30 to 60 min) [D/I].
**Dependence on each other.** Total: one shared log [P].
**Failure / dead players.** Both fall and reset to a checkpoint; difficulty sets checkpoint density (Easy +50% to Impossible) [D]. No waiting player [I].

**What it gets right.** Fun with a friend 123 (24.7% of codable positives), funny 63, rage-as-fun 57, simple 37, visuals 33, physics 24 [S, n=498]. "The amount of communication, frustration, and laughter in just 1 hour of playing so far is crazy lol"

**Where players push back.** Lost progress/checkpoints 29, bugs 28, controls 24, difficulty 23, too short 22, performance 17 [S, n=705]. Negatives (n=207, 67.5% under 2 h): difficulty 15, bugs 12, connection 12, repetitive 11. "My friend insta uninstalled after we died within 5 minutes of playing because there isn't a checkpoint." / "the controls are way too difficult, I would prefer a normal right and left". **<2h** is the majority (n=375, 142 negative): checkpoints 17, controls 16, difficulty 13. **>20h**: 3 reviews, not interpretable.

**Sentiment over time.** Launch week 81.4%, then 61.8-66% in weeks 2-4 as difficulty complaints mounted; partial recovery to ~78-79% in March after checkpoint rebalances; mostly 40-70% weekly from April on low volume [P].

**What happened after launch.** Difficulty and checkpoint rebalances, Easy mode, Mac/Linux (Feb), Impossible mode back (Mar; month peak 596, cause unknown) [D]; controller support, China servers, Deck Verified with -20% (Apr; players -50%) [D/T]; Log Village map + log skins with -30% Summer Sale (2026-06-25; Jul +33%, peak 262) [D/T]. No DLC; some paid-coin items made free [D]. A PlayStation concept page lists release "to be determined" [T].

**Launch path & team.** Announced 2026-01-30, 13 days before launch, with an 80.lv feature [T]; Next Fest and viral moment not found. Developer: "Based on your feedback, we adjusted the overall checkpoint balance" [D]. Unity per 80.lv [T]; Turkey per one unverified site [T].

**Unknowns.** Team size, dev time, prior games, cause of the March peak, whether the demo existed (snippet only), stranger matchmaking.

---

## 7. Super Shout Showdown

**appid 4011300 | stratum: flop | pair P09 (vs Mage Arena: shout spell incantations into the mic in PvP duels) | Early Access 2026-08-06/07 | $7.99, launch -20%, $5.99 (-25%) on 2026-11-11 [P/D] | Duels, Team Battle, FFA up to 16 [P] | Rezero Studio (solo or very small [I]), self-published | core type: versus | 152 reviews, 86.2% positive (Very Positive) [P]**

| metric | value |
|---|---|
| Median h at review (all / pos / neg) | 2.53 / 2.78 / 1.37 (census n=152 / 131 / 21) [S] |
| <2h / >10h / >50h | 37.5% / 12.5% / 0.7% [S] |
| Top 3 languages | English 42.1%, Traditional Chinese 19.7%, Russian 9.2% [P] |
| SteamCharts all-time peak | 204 (2026-08-16) [T] |
| Month 1 / 3 / 6 / 12 avg proxy | 34 / 8 (Nov missing) / not yet / not yet [T] |
| Current players | 6 [P] |

**Core loop & inputs.** Pick an anime spell loadout, chant custom incantations into the microphone to cast, win duels, team fights or 16-player FFA [P]. Shouting mode ("longer chants give stronger spells"; scream after a hit to heal), Typing mode replaced by Hand Seal mode (2026-09-28), Tapping mode, voice changer, chat with auto-translation, VRoid avatars [D].
**Dependence on each other.** Mostly PvP; team combos in Team Battle [P].
**Failure / dead players.** Losing a match; in FFA you take spells from defeated players [D]. Spectator mode only from 2026-10-22 [D]; earlier behaviour not found.

**What it gets right.** Fun with friends 19, funny 14, voice gimmick 14, potential 13, unique concept 10, value 9 [S, n=126 codable positives]. "I played along with 7 other friends, we had a blast until all our voices gave out."

**Where players push back.** Connection/lobby 8, crashes 7, bugs 6, more content 6, performance 5, balance 5 [S, n=147]. The 21 negatives: tech failure in 38.1%; connection 4, bugs/crashes/performance 3 each. "I only got to play the tutorial and the practice mode because there was 0 rooms across all 3 regions." / "A bit clunky, voice recognition doesn't work sometimes." **<2h** (n=54): crashes 4, connection 4, mic problems 3. **>20h**: 6 codable, not interpretable.

**Sentiment over time.** 85-86% in the first two weeks, 62.5% in the week of 2026-08-28, otherwise 75-100% on single-digit weekly volumes [P].

**What happened after launch.** Near-weekly updates: streamer mode, spells/loadouts, visual overhaul, Hand Seal mode, community chants, bots in all modes (2026-10-14), spectator + translation, cloud speech recognition (2026-11-04) because the local model failed on some hardware [D]. None moved players: 51 avg (Aug) → 18 (Sep, -65%) → 8 (Oct, -56%) → ~3 last 30 days [T]. Bots and room tags point to thin lobbies [I]. "We do not currently plan to change the price" after EA [P]. No DLC.

**Launch path & team.** Store page and devlogs from Nov 2025; playtests Jan and Feb 2026; demo 2026-05-19; Next Fest June 2026 (16-player FFA preview); EA 2026-08-07, planned to last 3-6 months [D/P]. No viral moment found; a clip contest offered keys [D]. Developer "Reyz" writes in first person; GMT+7 times and Thai/Indonesian localisation suggest Southeast Asia [I]. Statement: Shouting Mode was "sometimes even causing [crashes]" on limited hardware [D].

**Unknowns.** Team size, engine, location (inferred only), wishlists, match length, Next Fest demo numbers.

---

## 8. Mortuar

**appid 2921000 | stratum: flop | pair P10 (vs Phasmophobia/Demonologist: identify ghost type with equipment, then banish) | released 2024-07-09 | free to play, no DLC [P] | 1-4 players [P] | three named individuals (Romanian names [I]) / "mortuargame" | core type: investigation | 89 reviews, 37.1% positive (Mostly Negative) [P]**

| metric | value |
|---|---|
| Median h at review (all / pos / neg) | 0.40 / 0.58 / 0.27 (census n=89 / 33 / 56) [S] |
| <2h / >10h / >50h | 95.5% / 2.2% / 0.0% [S] |
| Top 3 languages | English 53.9%, Russian 15.7%, Simplified Chinese 7.9% [P] |
| SteamCharts all-time peak | toolkit: not available (HTTP 500); chart-data monthly peaks 8 (Jul 2024), max 10 (Jan 2026) [T] |
| Month 1 / 3 / 6 / 12 avg proxy | not found |
| Current players | 0 [P] |

**Core loop & inputs.** Visit a church or mansion in a forest modelled on Hoia Baciu, use ghost-hunting tools (EMF reader, flashlight, holy cross and more) to identify the ghost type, then follow the journal ritual to banish it [P]. Voice chat exists; the ghost "is always listening to you!", implying voice-reactive AI [P/I].
**Dependence on each other.** Faster identification and safer banishing with friends [P].
**Failure / dead players.** Ghost drains sanity, then hunts [P]. Death rules and dead-player role: not found.

**What it gets right.** Horror/tension 5, fun with friends 4, atmosphere 3, monsters/exorcism variety 3 [S, n=30 codable positives]. "Unique exorcism minigames for each type of ghost is a nice addition to the usual ghost hunting formula."

**Where players push back.** Bugs 14, performance 8, crashes 3, lag 3, low effort 3, no tutorial 3 [S, n=80 codable]; tech failure in 46% of codable negatives. "Game is buggy, we could not even open an entry gate and items were moving on their own." / "The multiplayer aspect of it is so lag even RTX 4080 cannot save it." **<2h** is nearly the whole sample (n=78 codable) with the same bug/performance profile. **>20h**: one review, none codable.

**Sentiment over time.** 48% in launch month (12 up / 13 down), 27% in Aug 2024, then 0-3 reviews a month, mostly negative [P].

**What happened after launch.** One developer post: a quick patch on 2024-07-11 (gate bug, voice-chat lobby bug, journal pop-up), "listening to your feedback" [D]. No later updates found. Monthly player peaks 0-10 throughout [T].

**Launch path & team.** Announcement, demo, Next Fest: not found. Self-labelled publisher [P]. Likely a Romanian student or hobby team [I].

**Unknowns.** Engine, dev time, team background, intent (student project or commercial), session length, death rules, player averages.

---

## 9. A Game About Penguins

**appid 4061800 | stratum: flop | pair P11 (vs WEBFISHING: cute-animal hangout, no fail state) | released 2026-08-10 | $9.99, launch discount not found [P] | max players not found | CO's Entertainment (Türkiye) / Ultimate Publishing (Ultimate Games S.A. / PlayWay S.A.) [P] | core type: hangout_no_fail | 52 reviews, 94.2% positive (Very Positive) [P]**

| metric | value |
|---|---|
| Median h at review (all / pos / neg) | 2.33 / 2.43 / 1.52 (census n=52 / 49 / 3) [S] |
| <2h / >10h / >50h | 42.3% / 11.5% / 0.0% [S] |
| Top 3 languages | English 48.1%, Simplified Chinese 15.4%, Turkish 13.5% [P] |
| SteamCharts all-time peak | toolkit: not available (HTTP 500); chart-data samples max ~25 at launch (Aug 2026) [T] |
| Month 1 / 3 / 6 / 12 avg proxy | not found; chart-data sample means Aug 12.8, Sep 1.6, Oct 1.3, Nov 0.4 [T] |
| Current players | 0 [P] |

**Core loop & inputs.** Live as a custom penguin on an online social island: slide (tricks, ramps, stat upgrades), swim, fish 98 species, do quests, decorate a house, play minigames and races [P]. Snowboards, skis, snowmobiles, gliders, slap/bump "wobbly physics", snowballs, emotes, global text chat, in-game phone, sandbox building; voice implied ("fire up your mics") [D].
**Dependence on each other.** None required; "Peace Mode" opts out of slaps [D].
**Failure / dead players.** None (cosy hangout) [P].

**What it gets right.** Fun with friends 19 (40.4% of codable positives), relaxing/cozy 15, visuals 12, addictive 4, content variety 4, strangers/community 4 [S, n=47]. "Jokes aside, it's a fun and cozy game to play with friends."

**Where players push back.** Very little: connection 3 ("Can't join other lobbies as well?"), repetitive 3, single mentions of bugs, crashes and performance [S, n=50]. Only 3 negatives; one cites AI art: "The AI disclosure does say 'minor visual stylization'" [S]. "35 mins to playing and it already crashed twice on me." **<2h** (n=22): same praise mix. **>20h**: 3 reviews.

**Sentiment over time.** 25 up / 1 down in launch week, then 0-2 reviews a week; positive throughout [P].

**What happened after launch.** About 15 patches in the first three weeks (lobbies, save transfer from the free prologue, fishing overhaul, Steam Deck) [D]. v1.0.3 invites solo players into existing online rooms, a thin-population signal [I]. v1.0.9 redrew "previously AI-generated icons… by hand" [D]. The major update of 2026-10-01 (gliders, Penguin Games) was delayed because the only 3D artist broke his right hand [D]. Players collapsed after launch week and no update moved them [T]. The free prologue "First Catch" (July 2026) may have absorbed demand [I].

**Launch path & team.** Made in Türkiye festival (Nov 2025), demo and Next Fest Feb 2026, devlogs, free prologue July 2026, 1.0 on 2026-08-10 [D]. The publisher's community manager posted the launch announcements [P]. Named team: Alican (only 3D artist), Berk, Enes [D]. Devlog: "the best moments on the island happen when players stop following a plan" [D].

**Unknowns.** Wishlists, prologue player counts, max lobby size, engine, dev time, publisher marketing, session length.

---

## 10. Bound To Fail

**appid 4508090 | stratum: flop | no pair | released 2026-04-23 | $5.99, discounts not found [P] | solo to 32 in one hosted game [P] | CORNER STACK, self-published | core type: climbing_traversal | 22 reviews, 95.5% positive (Positive) [P]**

| metric | value |
|---|---|
| Median h at review (all / pos / neg) | 2.45 / 2.42 / 7.47 (census n=22 / 21 / 1) [S] |
| <2h / >10h / >50h | 40.9% / 4.5% / 0.0% [S] |
| Top 3 languages | English 68.2%, French 18.2%, Korean 9.1% [P] |
| SteamCharts all-time peak | not tracked (HTTP 404) |
| Month 1 / 3 / 6 / 12 avg proxy | not found |
| Current players | 0 [P] |

**Core loop & inputs.** 2.5D physics platformer: tied to a chair, jump and roll with "incredibly grippy feet" to climb; a fall loses height, Getting-Over-It style [P]. Jump, roll, full controller support, rebindable keys, character customisation [P/D]. Voice/text chat: not found.
**Dependence on each other.** None; players "fail together" in parallel ("Invite up to 31 friends") [P].
**Failure / dead players.** Falling loses progress; quit and resume "even in multiplayer" [P]. No waiting state.

**What it gets right.** Funny 5, visuals 3, addictive 3, potential 3, rage-as-fun 3 [S, n=21 codable positives]. "My confidence is getting worse every minute, but i cant stop playing!"

**Where players push back.** Difficulty/unfairness 3 (two of them praise it as "punishing"), single mentions of performance, content and controls [S, n=22]. The one negative (Korean) calls the game unreasonable and unpleasant [S]. Requests: "More maps and stuff". **<2h** (n=9): all positive. **>20h**: none.

**Sentiment over time.** 10 up / 0 down in launch week, then 0-2 a week [P].

**What happened after launch.** Two developer posts only: demo plus Discord key giveaway (2026-04-15) and a hotfix (2026-04-27) [P]. No content updates found. Third-party review 7/10 (duuro.net, snippet) [T].

**Launch path & team.** Demo 8 days before release; a Keymailer page (press keys) [D/T]; Next Fest and viral moment not found. Posters "matt" and "KnuddCS" [P].

**Unknowns.** Location, team size, engine, prior games, session length, sales, player counts.

---

## 11. RV There Yet?

**appid 3949040 | stratum: hit | pair P04 (reference game: friends operate one vehicle through a physics course) | released 2025-10-21 (1.0, no EA) | $7.99, no discounts found [P/D] | 1-4 players; solo is hard [P] | Nuggets Entertainment (Skövde), self-published | core type: shared_object | 91,202 reviews, 90.1% positive (Very Positive) [P]**

| metric | value |
|---|---|
| Median h at review (all / pos / neg) | 9.47 / 9.99 / 5.96 (n=1000 / 886 / 114) [S] |
| <2h / >10h / >50h | 6.6% / 47.4% / 2.8% [S] |
| Top 3 languages | English 42.2%, Russian 23.8%, Turkish 5.5% [P] |
| SteamCharts all-time peak | 56,960 (2025-11; Oct 2025 not tracked) [T]; 100,002 on 25 Oct 2025 per a SteamDB news item [T] |
| Month 1 / 3 / 6 / 12 avg proxy | 15,113 (Oct missing) / 8,518 / 3,965 / 4,963 [T] |
| Current players | 2,210 [P] |

**Core loop & inputs.** Up to 4 share one RV and drive it home through hostile back-country maps, winching it over or through obstacles, repairing it and keeping each other alive between gas-station checkpoints [P]. Drive/ride, front and rear physics winches via remote, carry/throw items, welder, flares, food, EpiPens, beer, proximity voice (PTT or toggle) [P]. Key rebinding and controller support came later [P]. Campaign ~6 h per HowLongToBeat [T].
**Dependence on each other.** One vehicle and shared inventory; the driver needs others on the winch: "the driver will have a hard time completing this journey alone" [P].
**Failure / dead players.** Downed at 0 health and revivable with an EpiPen; if the RV is destroyed or all die, restart from the last checkpoint [T]. Dead players spectate, then auto-respawn after a timer (guide snippet, unverified) [T].

**What it gets right.** Fun with friends 234 (30.2% of codable positives), funny 125, physics chaos 60, value 46, relaxing 44, visuals 41 [S, n=776]. "Friendslop of the highest order, with physics so bugged it goes back to being a fun feature."

**Where players push back.** Bugs 120 (in 39.6% of negatives), repetitive 31, lost progress 29, too short 26, needs friends 25, difficulty 23 [S, n=882]; tech failure in 50% of codable negatives. "janky physics can add to the charm, but RV There Yet offers so little besides that" / "Half the time is now spent waiting for people to reconnect" **<2h** (n=61): needs friends 7, bugs 5, repetitive 4. **>20h** (n=183, 9 negative): bugs 24 still lead, then performance 8, content 7.

**Sentiment over time.** Launch week 84.4% amid connection and crash complaints (acknowledged by the dev on 10-23) [P/D]; rose to 89-94% through November; **week of 2025-11-25: 15,878 up (97.9%)**, coinciding with the Autumn Sale/Steam Awards nominations [P timing, I cause] (it later won "Sit Back and Relax" [T]). Since Dec 2025 stable at 83-91% weekly; Map 3 lifted review volume +236% at 88% [P].

**What happened after launch.** Five hotfixes in 10 days; KB/M rebinding (11-06); ban button against trolls (12-02); **Map 2 (2025-12-16)** with 16-language localisation held January flat (8,560, +1%) [T]; Feb -48% with no update; server browser and achievements (2026-03-18); Xbox/Game Pass (2026-06-30); Jul +34% (Summer Sale timing [I]); **Map 3 (2026-09-10): Sep avg 5,736 (+159%), peak 23,131** [T]; crossplay + PS5/Switch 2 (2026-10-29), no visible Steam lift yet [I]. Monetisation: $1.99 soundtrack, all maps free, merch pre-orders (2026-10-26) [P]. Sales claims: 1.3M in the first week, 2M in eight days, 4.5M by Dec 2025 [D/T].

**Launch path & team.** 8-week game-jam origin; announced 2025-10-14 and released 7 days later with "300k+ wishlists" [D]. Viral moment before announcement: a post using the leaked hidden store page's assets went viral on TikTok; Valve gave a store takeover; "all of the game's marketing was organic" [D, via GIB]. No demo, playtest or Next Fest. Founders Tim Badylak (ex-CEO Coffee Stain Publishing) and Kristoffer Andersson; core built "in a week by four people"; funded by Coffee Stain co-founder Stefan Hanna; Unreal [D/T]. Statements: expected it "might sell 20,000 or so units in a year"; "We didn't focus on replayability at all"; "it's more of a slog right now" [D].

**Unknowns.** Total studio size, exact Oct 2025 averages (SteamCharts gap), discount history, 2-player balance, weaker-player handling, Game Pass and console numbers.

---

## 12. Bopl Battle

**appid 1686940 | stratum: hit | no pair | released 2023-11-16 (1.0) | $9.99 [P] | local and online FFA or team vs team; no singleplayer, no bots [P]; max players not found in sources | Johan Grönvall ("Zap", solo) / Zapray Games (own company) | core type: versus | 26,263 reviews, 97.2% positive (Overwhelmingly Positive) [P]**

| metric | value |
|---|---|
| Median h at review (all / pos / neg) | 11.96 / 11.86 / 15.60 (n=1000 / 974 / 26) [S] |
| <2h / >10h / >50h | 9.2% / 55.9% / 14.7% [S] |
| Top 3 languages | English 79.9%, Russian 3.3%, German 3.1% [P] |
| SteamCharts all-time peak | 2,175 (2025-02) [T] |
| Month 1 / 3 / 6 / 12 avg proxy | 416 / 483 / 550 / 417 [T] |
| Current players | 284 [P] |

**Core loop & inputs.** 2D arena brawler: each slime picks a combo of 3 abilities from a large pool; last slime standing wins the round, wins accumulate over a match [P]. Move, jump, aim, three ability slots (physics/stage manipulation, movement, damage, revive, Duplicator); KB/M for one local player only, others need controllers [P]. No voice chat found; Discord or couch [I].
**Dependence on each other.** Competitive; in team mode, ability combos with a partner [P].
**Failure / dead players.** Death is out for the round unless revived; dead-player activity not documented, likely watching the round end [I].

**What it gets right.** Fun with friends 171 (21.2% of codable positives), funny 57, value 48, physics chaos 38, simple 37, unique 34 [S, n=808]. "Out of 20 matches, we cracked up laughing at least 10 times."

**Where players push back.** Needs friends 32 (all in positive reviews), bugs 23, more content 18, repetitive 16, lag 14, grind 11 [S, n=832]. Only 24 codable negatives (median 15.6 h): lag 5 (20.8%), bugs 3. "online play is so laggy its unbearable." / "This game is fun but there is no online multiplayer with random people and I don't have friends" (pre-matchmaking). **<2h** (n=84, 1 negative): friends 16, value 8. **>20h** (n=302, 8 negative): friends 66; needs-friends 12 and lag 7 are the main gripes.

**Sentiment over time.** 98.1% at launch; every month since 94.5-98.6% [P]. Review volume rose +52% in Apr 2024 with matchmaking [P].

**What happened after launch.** About 10 hotfixes in 2 weeks; replays and slime-eating (Dec 2023; Dec avg +67%, word of mouth plus Winter Sale [I]); **online matchmaking incl. demo players (2024-04-09): Apr +47%**, held ~575 in May-Jun [T/I]; Duplicator (Aug 2024, +17%); **Magnet gun (2025-02-06): +68%, all-time peak 2,175** [T]; soundtrack DLC €4.99 (2025-05); 60 new levels (2025-05-29); Youtooz plush (2025-06) [P]. Last developer post 2025-07-07; slow decline to ~230 avg, with holiday bumps (Dec 2025 +25%, Jan 2026 +14%) [T/I]. Free demo kept updated and in the matchmaking pool [P]. Modding community exists [P].

**Launch path & team.** Demo 2023-08-10, October 2023 Next Fest, launch 2023-11-16 [P]. Wishlists and viral moment: not found (a fan-wiki claim of tens of millions of views is unverified [T]). SteamSpy estimate 1-2M owners [T]. Solo developer: "I'm Zap, the solo developer of Bopl Battle" [D]; Unity [P]; Sweden [I]. On matchmaking: "there is no ranked-mode, since dividing the queue times further is probably a bad idea" [D].

**Unknowns.** Announcement date, wishlists, viral source, dev time, prior games, max lobby size, session length, discount history.

---

## 13. Super Battle Golf

**appid 4069520 | stratum: hit | no pair | released 2026-02-19 (1.0) | launch $7.99 with -20%; raised to $12.99 after 2026-07-23 [D/P] | 1-8 (up to 16 "at your own risk") [P] | Brimstone / Oro Interactive | core type: versus | 12,230 reviews, 92.9% positive (Very Positive) [P]**

| metric | value |
|---|---|
| Median h at review (all / pos / neg) | 7.16 / 7.32 / 5.74 (n=1000 / 916 / 84) [S] |
| <2h / >10h / >50h | 13.3% / 39.8% / 6.9% [S] |
| Top 3 languages | English 77.2%, Brazilian Portuguese 5.4%, Russian 3.8% [P] |
| SteamCharts all-time peak | 20,395 (2026-02) [T] |
| Month 1 / 3 / 6 / 12 avg proxy | 5,612 / 2,687 / 1,612 / not yet [T] |
| Current players | 1,069 [P] |

**Core loop & inputs.** Everyone plays the same hole at once: a race to sink the ball first while sabotaging others; points per hole [P]. Walk, aim, power swing, hit players with ball or club, 8-seat golf cart (ramming), items (orbital laser, mines, guns, rocket launcher, later Freeze Bomb, Rocket Driver), emotes, voice chat, Teams mode from 2026-07-16 [P/T].
**Dependence on each other.** Mostly competitive; shared cart; teams since July 2026 [P].
**Failure / dead players.** Knockouts, then respawn [I]; "Knockout Immunity" (2026-04) so bullied players are not chain-killed [P]. Rank-dependent item spawns and comeback points act as catch-up [D/P].

**What it gets right.** Fun with friends 262 (32.4% of codable positives), rage-as-fun 78, funny 69, physics chaos 63, fun with strangers 40, visuals 39 [S, n=810]. "It's frustrating, hilarious, and the kind of game that has everyone yelling one minute and laughing the next."

**Where players push back.** Toxic randoms/griefers 52, more content 34, bugs 29, needs friends 22, connection 17, repetitive 17 [S, n=891]. Negatives (n=81): toxicity 11 (13.6%), bugs 10, cheaters 8, connection 5. "now it is just a grief-fest where people just camp you so you can't actually do anything." / "Workshop, for more maps because 27 maps aint enough for longevity." **<2h** (n=120): friends praise 34; few complaints. **>20h** (n=196): bugs 9, toxicity 9, content 8, repetitive 8.

**Sentiment over time.** 96% launch week, 89.9-94% through spring (lowest in the Frozen Fairway week); 84.7-85.6% in late June-early July before the City update; back to 93-96% with the free weekend; 87-94% since [P].

**What happened after launch.** Dev claims: 100k players in 48 h, 400k copies in a week, 1M by 2026-03-30 [D]. **Frozen Fairway (2026-04-09)**: new biome, wind, vote kick, Knockout Immunity; April peak 18,552, nearly launch level [T]; Knockout Immunity complaints acknowledged ("we totally hear you") [D]. May -52%, Jun -41% [T]. **Attack on City (2026-07-16)** + free weekend 16-20 July + pre-announced price rise to $12.99: Jul avg +107%, peak 14,055 [T]. Aug -48%, Sep -34%, Oct flat at ~738 [T]. Console launch delayed to 2027-03-25 with crossplay; Workshop in progress; in-game reporting devlog (2026-10-31) [D]. "All updates (and all future updates) are part of the base game"; no DLC [D/P].

**Launch path & team.** Announced 2026-01-15, released 5 weeks later; ~100k wishlists in the 4 weeks after reveal [T]; community playtests, no demo or Next Fest found [D]. Viral source not identified (unreliable mention of Kinda Funny streams [T]). Brimstone, "members… spread from Europe to Southeast Asia"; "We made Super Battle Golf together in 4.5 months" [D]. Interview: core appeal "if I can't win, nobody else does"; players "disrupt each other so much that they stop actually playing golf" [D].

**Unknowns.** Team size (a "four-person team" snippet is unverified), engine (Unity/BepInEx inferred from Thunderstore mods [I]), publisher role, reaction to the price rise, session length.

---

## 14. The Escape: Together

**appid 2242760 | stratum: mid | no pair | Early Access 2023-01-13 (still EA in 2026-11) | $3.99; -40% sale in Feb 2023 [P] | 1-3 players [P] | Nightstuff Games (solo or very small Ukrainian dev [I]), self-published | core type: escape_survival | 2,509 reviews, 78.3% positive (Mostly Positive) [P]**

| metric | value |
|---|---|
| Median h at review (all / pos / neg) | 2.55 / 2.89 / 1.19 (n=1000 / 810 / 190) [S] |
| <2h / >10h / >50h | 38.7% / 2.5% / 0.1% [S] |
| Top 3 languages | English 40.8%, Russian 21.0%, Ukrainian 16.9% [P] |
| SteamCharts all-time peak | 618 (2024-04) [T] |
| Month 1 / 3 / 6 / 12 avg proxy | 17 / 4 / 6 / 22 [T] |
| Current players | 3 [P] |

**Core loop & inputs.** 1-3 siblings explore a house stalked by a paranormal entity, find tools, keys and codes, solve puzzles and escape before being killed; several maps, each with its own entity [P]. Move, sprint, pick up/drop, multi-slot inventory (Oct 2023), flashlight, crucifix, phone/laptop password puzzles, shared journal, escape car with jack, auto-injector revive; positional voice chat only since 2026-09-07 (v2.1) [P].
**Dependence on each other.** Shared journal notes, revive items, lootable dead teammate (v2.1) [P].
**Failure / dead players.** Death by ghost; revive possible "a couple times per game" [D]; run ends when all die. Spectator mode exists [P]. Before v2.1 one death could end the session for the others (bug) [P].

**What it gets right.** Horror/tension 225 (30.1% of codable positives), fun with friends 211, atmosphere 107, value 86, monsters 76, potential 67 [S, n=748]. "Amazing for the price, I would pay more for it."

**Where players push back.** Too short 74 (mostly positives asking for more maps), bugs 73, repetitive 34, not scary 27, no tutorial 16, performance 14 [S, n=921]. Negatives (n=173, 69.5% under 2 h): bugs 22, not scary 20, repetitive 15, price 10. "worst 2$ I've ever spent, the game isn't even scary!" / "The ghost is broken and if the host dies then all players get KICKED!" **<2h** (n=354, 118 negative): bugs 28, not scary 20, repetitive 14. **>20h**: 3 reviews.

**Sentiment over time.** 85% at launch, 75% in Feb 2023; 90-93% around the Oct-Nov 2023 Halloween/inventory update; 68-81% during the Dec 2023-Oct 2024 player rise (new, less committed buyers [I]); 95.2% in Nov 2024 (Halloween update); 62-67% in Apr-Jun 2025; 73% in the Mar 2026 spike month [P].

**What happened after launch.** ~20 patches in 2 weeks; maps 2 (Feb 2023), 3 (Jun 2023, +205%), 4 (Aug 2025, +59%); inventory (Oct 2023) [P/T]. **Nov 2023-Apr 2024 rise to 58 avg / 618 peak with no developer post Feb-Apr 2024: cause unknown** (streamer suspected, unverified). Mar 2026 +267% (peak 139): cause unknown. v2.1 (2026-09) voice chat, persistent lobby: +25% to 7 avg [T]. A free iOS version with IAP exists [T]. No DLC.

**Launch path & team.** Announcement, demo, Next Fest, wishlists: not found. "RELEASED!" post 2023-01-07 [P]. Developer calls Ukrainian "my native" language; later posts say "the team" [D]. Patch-note voice: "As many have requested some sort of inventory, here it is" [D]; 3-player cap "might increase… based on the feedback" (still 3) [D].

**Unknowns.** Engine, team size, launch price, viral sources of the 2024 and 2026 rises, run length, 1.0 plans.

---

## 15. Crashout Crew

**appid 3583210 | stratum: mid | no pair | released 2026-05-28 (1.0; Steam, Xbox, Game Pass day one [T]) | $7.99 [P] | 1-4 players [D] | Aggro Crab, self-published | core type: job_simulation | 1,248 reviews, 93.6% positive (Very Positive) [P]**

| metric | value |
|---|---|
| Median h at review (all / pos / neg) | 3.65 / 3.68 / 2.15 (n=1000 / 940 / 60) [S] |
| <2h / >10h / >50h | 22.7% / 11.3% / 0.2% [S] |
| Top 3 languages | English 71.7%, Simplified Chinese 6.6%, Russian 6.5% [P] |
| SteamCharts all-time peak | 819 (2026-06; tracking starts June); 2,620 on 31 May per steambase [T] |
| Month 1 / 3 / 6 / 12 avg proxy | 251 (May missing) / 91 / 33 (Nov missing) / not yet [T] |
| Current players | 32 [P] |

**Core loop & inputs.** Drive drift-capable forklifts in a warehouse to grab, stack and ship chaotic physics boxes against shift timers; each contract has 5 shifts with hazards; earnings buy upgrades that reset per contract [P]. Drive, boost, drift, "Easy-Grab" forks, stress meter ("don't crash out"), TipTap videos, gamepad recommended [P]. Mic use implied by the demo [P]. Total "about 8-10 hours… over 20 contracts" [D].
**Dependence on each other.** Shared quota, money, upgrades and trucks [P].
**Failure / dead players.** Fail the shift or contract quota; no death [I]. Crashing out is a stress state that makes "your friends' lives even tougher" [P].

**What it gets right.** Fun with friends 260 (30.4% of codable positives), visuals 86, physics chaos 71, funny 70, value 60, simple 51 [S, n=855]. "something like overcooked to play with pals for a dozen hours, but with less cooking and more forklift crashes"

**Where players push back.** The "crashes" theme (135) is mostly in-game forklift crashes in positive reviews (keyword false positive). Real complaints: repetitive 39, too short 31, bugs 30, needs friends 24, difficulty 20 [S, n=913]. Negatives (n=58): repetitive 18 (31.0%), bugs 10, real crashes 8, performance 5; tech failure 34.5%. "It can be fun for a few hours but the amount of content is disappointing." / "This is a one and done." **<2h** (n=209): repetitive 13 (8 in negatives), needs friends 11. **>20h** (n=26): friends praise 13, bugs 4.

**Sentiment over time.** 94.4% launch week, 92-94% in June, one 62.5% week (2026-06-25, n=16), then 81-100% on single-digit weekly volumes [P].

**What happened after launch.** Patches 1.2.4 and 1.3.6 fixed launch crashes, a BSOD and save-file problems; 1.3.7 raised the final contract timer (it "kinda was" impossible); Youtooz merch; OST DLC $2.99 [P/D]. No content update; monotonic decline: Jun 251 → Jul 121 → Aug 61 → Oct 33 [T]. A tracker saw $4.95 at some date [T]. "We don't have plans to add public lobbies or matchmaking at this stage." [D]

**Launch path & team.** Announced 2025-10-02; October 2025 Next Fest demo (extended a week, then removed); release ~7 months later after "over a year of development" [D]. No viral moment or wishlists found. Aggro Crab: Going Under, Another Crab's Treasure, co-developer of PEAK [T]; Unity [I]. Launch-week candour: "We totally overlooked that the red and green barrels are SUPER hard to differentiate if you're colorblind" [D].

**Unknowns.** Team size, location (not verified), wishlists, Game Pass player numbers, discount history, full-May player average.

---

## 16. MAZEBOUND: Hunt, Gather, Run!

**appid 3616260 | stratum: mid | no pair | released 2026-05-13 (1.0) | $9.99, launch -20% [P/T] | solo to 4 (8 untested) [D] | Absam Studios ("Sam & Abbie"), self-published | core type: escape_survival | 731 reviews, 81.9% positive (Very Positive) [P]**

| metric | value |
|---|---|
| Median h at review (all / pos / neg) | 6.50 / 7.03 / 3.76 (census n=731 / 599 / 132) [S] |
| <2h / >10h / >50h | 15.2% / 26.8% / 0.7% [S] |
| Top 3 languages | English 70.9%, Russian 10.8%, Brazilian Portuguese 5.3% [P] |
| SteamCharts all-time peak | 475 (2026-05) [T] |
| Month 1 / 3 / 6 / 12 avg proxy | 123 / 38 / 17 (Nov missing) / not yet [T] |
| Current players | 7 [P] |

**Core loop & inputs.** Enter a maze, gather branches, crates and food, craft weapons, torches and defences, haul items in a physics cart, fight or flee monsters and find the way out [P]. Melee (Boinker 2000, axes), ballista, crafting, cart cargo, hunger, willpower, named saves; "Microphone recommended" [P]. Half the first maze took "roughly four hours" in the demo [D].
**Dependence on each other.** Shared cart and cargo, host-saved world, revives (from 2026-06-03) [P].
**Failure / dead players.** "Expect To Die. A Lot." [P]. Normal: respawn or wait for a revive; Hardcore (2026-06-19) is permadeath [P]. Spectate: not found.

**What it gets right.** Fun with friends 155 (28.4% of codable positives), monsters 131, horror 101, potential 60, value 54, unique 54 [S, n=545]. "genuinely scary at time while still being goofy and silly throughout the rest of it"

**Where players push back.** Bugs 81, more content 44, difficulty/RNG 32, performance 26, repetitive 25, lag 19 [S, n=673]. Negatives (n=128): bugs 29 (22.7%), repetitive 18, difficulty 12, lag 10; tech failure 32%. "Items glitch out of the cart all the time." / "I like the idea of a difficult game in theory but in practice this is just tedious" **<2h** (n=103, 49 negative): bugs 9, repetitive 6, crashes 4. **>20h** (n=21): monsters and potential praised; bugs 4, difficulty 4.

**Sentiment over time.** 89.5% in launch week, dropping to 75-77% in weeks 2-3 during save and lag bugs (acknowledged by the dev), recovering to 87% after the 2026-06-03 save rework; 57-100% on small volumes since [P].

**What happened after launch.** About 15 hotfixes in 3 weeks (desync, a region-specific multiplayer bug, save crashes, VPN, cart physics) [P]; multiplayer save rework and revives (Jun; Jun +11%, the only rise) [T]; Hardcore mode + solo speedrun competition with gift-card prizes [P]; public server browser and 6 community languages (2026-07-19; Jul -57%) [P/T]; FR/DE/ES (Aug); Sep +24% with no developer post, cause unknown; QoL 10 (2026-10-10) [P/T]. No DLC.

**Launch path & team.** Free singleplayer prototype on itch.io [T]; demo 2025-10-24; Next Fest Feb 2026 (stated plan) [D]; release-date trailer 2026-03-30. Wishlists and viral moment: not found. Husband-and-wife team per Japanese press [T]; developed over "the last year or so" [D]. Developer: "Sorry I've been quiet for the past few days. We were visiting family" during save bugs [D].

**Unknowns.** Location, engine, wishlists, Next Fest numbers, cause of the September bump.

---

## 17. Sunset Summit

**appid 3874450 | stratum: flop | pair P01 (vs PEAK: co-op summit climb with tools) | released 2026-09-09 (slipped from 21 Aug) | $4.99 list, $3.99 (-20%) on 2026-11-11 [P] | solo to 8 [P] | Joe and Andrew Fender / Future Friends Games | core type: climbing_traversal | 126 reviews, 83.3% positive (Very Positive) [P]**

| metric | value |
|---|---|
| Median h at review (all / pos / neg) | 3.31 / 3.32 / 3.25 (census n=126 / 105 / 21) [S] |
| <2h / >10h / >50h | 29.4% / 17.5% / 0.0% [S] |
| Top 3 languages | English 31.7%, Korean 15.9%, Simplified Chinese 12.7% [P] |
| SteamCharts all-time peak | 412 (2026-09-13) [T] |
| Month 1 / 3 / 6 / 12 avg proxy | 48 / not yet / not yet / not yet [T] |
| Current players | 12 [P] |

**Core loop & inputs.** Elderly hikers climb one of 16 handcrafted routes across 4 floating islands to reach the summit before sunset, using axes, ropes and gear, with frequent checkpoints [P]. Jump/long jump, balance (harder with altitude), climbing axes with energy cost, rope, delivery drone, pogo stick, umbrella, grappling gun (Oct), camera, proximity chat plus walkie-talkies, text chat [P]. "each route has around 1 hour playtime" [D].
**Dependence on each other.** Ropes and drones to help teammates; a carry achievement [P].
**Failure / dead players.** Falls mean instant checkpoint respawn; sunset means game over; Cozy/Normal/Hard/Custom difficulty [P]. Early finishers wait at the summit [P].

**What it gets right.** Fun with friends 23 (25% of codable positives), value 14, funny 11, relaxing 6, visuals 5, teamwork 5 [S, n=92]. "Fun and forgiving, great place to hang out with friends!"

**Where players push back.** Bugs 17, performance 7, checkpoints/progress 7, crashes 5, connection 4 [S, n=111]. Negatives (n=19): tech failure in 52.6%; bugs 6, crashes 4, performance 3. "crashes constantly, never had this problem with any other games" / "the crystal map with ice blocks and the checkpoints are broken." **<2h** (n=31): value and friends praise 7 each; bugs 7. **>20h**: 3 reviews.

**Sentiment over time.** 79.2% in launch week (42/11), 86% week 2, then 70-100% on 1-7 reviews a week [P].

**What happened after launch.** Bug fixes (red screen, strafe) in September; Grappling Gun update (2026-10-12) with fireworks and radio: October avg 22 (-71%), no lift [T]. A -20% discount on 2026-11-11, reason not found [P]. No DLC; Summit Stamps are earned [P].

**Launch path & team.** Development since 2021 with a 2023 burnout pause; playtest as "RISE" (Aug 2025, aimed at a Next Fest demo); revealed at the PC Gaming Show 2026-06-07 with a demo; release date set for 21 Aug, actual launch 9 Sep with no slip announcement found [D/P]. Publisher PR calls it a "viral climbing game" without metrics [T]. Brothers behind DEVOUR (7M copies claimed) [D]. Joe Fender: "After the success of PEAK in 2025, I felt reassured that it was worth finishing." Store: "100% handcrafted, no AI" [P].

**Unknowns.** Wishlists, actual Next Fest participation, why the launch slipped, engine, location, publisher marketing, stranger play.

---

## 18. Speed Crew

**appid 2367480 | stratum: flop | no pair | Steam release 2024-01-31 (Switch 2023-06-08 at $19.99 [T]) | $9.99 [P] | 1-4, local couch, online, Remote Play [P] | Wild Fields (Ukraine; sister company of N-iX Game & VR Studio [T]), self-published | core type: shared_object | 88 reviews, 98.9% positive (Very Positive) [P]**

| metric | value |
|---|---|
| Median h at review (all / pos / neg) | 2.80 / 2.77 / 3.27 (census n=88 / 87 / 1) [S] |
| <2h / >10h / >50h | 25.0% / 9.1% / 1.1% [S] |
| Top 3 languages | English 52.3%, Ukrainian 18.2%, Russian 5.7% [P] |
| SteamCharts all-time peak | 23 (2024-02) [T] |
| Month 1 / 3 / 6 / 12 avg proxy | 4.9 (Jan missing) / 2.5 / 1.5 / not found (30 months missing) [T] |
| Current players | 4 [P] |

**Core loop & inputs.** Overcooked-like: the crew diagnoses and repairs race cars arriving in the pit lane with tools, against the clock, across 48 levels in 4 decades with moving platforms, weather and lava [P]. Move, pick up/use tools, slap, assign tasks, customise; Sabotage/Arcade mode lets one player be the rival against teammates [P]. Voice: not found.
**Dependence on each other.** Shared repair job per car; clean repairs "double your points" [P].
**Failure / dead players.** Medal/score thresholds per race; no death [P].

**What it gets right.** Fun with friends 28 (32.6% of codable positives), visuals 13, teamwork 11, funny 8, simple 7, relaxing 7 [S, n=86]. "loads of team work needed perfect way to spent a few nights over discord"

**Where players push back.** Bugs 9, too easy 4, content 3, repetitive 3 [S, n=87]. "Might be a tad too easy, we're beating most levels with good margin on our first try." The one negative: "the constant sync and lag issues in multiplayer make it very hard to be an enjoyable experience." **<2h** (n=21): all positive. **>20h**: 4 reviews.

**Sentiment over time.** 21/0 and 15/0 in the first two months, then 0-6 reviews a month; the only negative came in Mar 2025 [P].

**What happened after launch.** Steam Deck Verified (2024-02-21); 1.2.0 cross-platform play and Simplified Chinese (2024-03-05), the last developer post [P]. Players: 5 avg in Feb 2024, 0 in the last 30 days [T]. No DLC.

**Launch path & team.** Switch-first (announced March 2023), Steam demo and June 2023 Next Fest, Gamescom booth, Steam launch delayed to Q1 2024 [P/T]. Wishlists, viral moment: not found. "Speed Crew is our first game… We've decided to take some extra time" [D].

**Unknowns.** Team size, engine, Switch sales, discount history, why the Steam launch came 8 months after Switch.

---

## 19. Ticking Together

**appid 3673320 | stratum: flop | no pair | released 2025-12-03 | $4.99; -50% in Cyberpunk Fest Aug 2026 [P] | 1-4 players [P] | Furkan Baytak, Furkan Özkaya / Vellichor Games | core type: shared_object | 46 reviews, 95.7% positive (Positive) [P]**

| metric | value |
|---|---|
| Median h at review (all / pos / neg) | 2.45 / 2.45 / 1.68 (census n=46 / 44 / 2) [S] |
| <2h / >10h / >50h | 37.0% / 6.5% / 0.0% [S] |
| Top 3 languages | English 58.7%, Russian 21.7%, French 4.3% [P] |
| SteamCharts all-time peak | not tracked |
| Month 1 / 3 / 6 / 12 avg proxy | not found |
| Current players | 0 [P] |

**Core loop & inputs.** Carry a live bomb through cyberpunk parkour courses; it must be re-stabilised with a hand scan every 15 seconds and is tossed between teammates; a drop or missed scan loses the run [P]. Run, jump, slide, climb, dash, wallrun; manual or auto-throw; ping system; Vivox proximity voice [P]. "4 handcrafted levels plus a tutorial" (demo) [D].
**Dependence on each other.** One shared bomb; passing and scan timing [P].
**Failure / dead players.** Fall, trap, drop or timeout; respawn at the last checkpoint after a dissolve effect [P]. Spectate: not found.

**What it gets right.** Fun with friends 18 (40.9% of codable positives), visuals 11, physics chaos 9, funny 8, value 7, unique 7 [S, n=44]. "the movement is actually crisp and the 15-second timer adds so much pressure."

**Where players push back.** Controls 6, more content 5, lag 4, performance 4 (some false positives), bugs 3 [S, n=46]. "The controls could be refined slightly; they're a bit clunky at the moment." Negatives (2): "A good concept unfortunatly riddled with bugs." and infinite loading on join. **<2h** (n=17): controls 4, content 3. **>20h**: 1 review.

**Sentiment over time.** 33/0 in launch week; afterwards 0-2 reviews in a few scattered weeks [P].

**What happened after launch.** No content updates found; a 50% Cyberpunk Fest discount (3-10 Aug 2026) produced one (negative) review [P]. A separate prologue app exists [T].

**Launch path & team.** Devlogs #0-#3 from 2025-09-29; demo 2025-10-13 (the October 2025 Next Fest start, so likely a Next Fest demo [I]); release about 7 weeks later [P]. Turkey inferred from names [I]; "two interns" claim unverified [T].

**Unknowns.** Wishlists, demo numbers, engine, player counts, total content length, publisher role.

---

## 20. Toy Scrappers

**appid 3457790 | stratum: flop | no pair | released 2025-03-04 | $4.99 [P] | 2-16, no solo [P] | LoudScream / SlugShot Games | core type: versus (asymmetric hide-and-seek) | 22 reviews, 81.8% positive (Positive) [P]**

| metric | value |
|---|---|
| Median h at review (all / pos / neg) | 0.98 / 2.27 / 0.25 (census n=22 / 18 / 4) [S] |
| <2h / >10h / >50h | 54.5% / 13.6% / 0.0% [S] |
| Top 3 languages | Turkish 40.9%, English 31.8%, Korean 9.1% [P] |
| SteamCharts all-time peak | not tracked |
| Month 1 / 3 / 6 / 12 avg proxy | not found |
| Current players | 0 [P] |

**Core loop & inputs.** Clowns hunt toys; caught toys convert to the clown side [P]. Toy abilities: Decoy, Prop (turn into an object), Illusion (8 copies), Invisibility; clown abilities: Trap, Sense; LAN co-op/PvP [P]. Voice: not found.
**Dependence on each other.** Converted toys join the hunters [P].
**Failure / dead players.** Being caught makes you a clown, so you keep playing instead of waiting [P].

**What it gets right.** Fun with friends 8 of 17 codable positives (47%) [S]. "Played with 10 friends, it was a hell but soo fun."

**Where players push back.** Connection/lobby 5 of 20 codable, incl. all 3 codable negatives [S]: no open servers, quick join finds no lobby (Turkish reviews), and "no hay servidores… la latencia no bajaba de 999 ms" (no servers; latency never below 999 ms). All 4 negatives were written under 2 h (median 0.25 h) [S]. Request: "would love to see more maps and more interesting abilities". **>20h**: none.

**Sentiment over time.** 9/0 in launch week, 1/2 in week 2, then single reviews months apart [P].

**What happened after launch.** One developer post only: the launch (2025-03-04) [P]. SteamSpy 20,000-50,000 owners [T], far above the review count, so unreliable or giveaway-driven [I]. Package name "Clown Party" suggests a rename [I].

**Launch path & team.** Announcement, demo, wishlists: not found. LoudScream's only Steam title [T].

**Unknowns.** Team location, size, engine, player counts, rename history, marketing.
