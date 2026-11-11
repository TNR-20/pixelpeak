# Matched pairs: why one game of the same idea took off and the other did not

Compiled 2026-11-11 from local research files only. No new web research was done; no pair fact was missing badly enough to need a store lookup.

**What a pair is.** Each pair is a hit and a game with nearly the same pitch that did much worse, chosen by hand on core type, theme and store text (`deep_study_selection.md`). 9 pairs are hit vs flop; P06 and P08 are hit vs mid because no eligible flop with the same pitch exists.

**Tags.** [P] verified primary (Steam API/store, developer Steam post, SteamCharts table read as counts); [D] developer or publisher claim; [T] third party (press, wiki, SteamCharts monthly proxies); [I] inference or classification; [S] computed from the review sample (500 newest + 500 most helpful, or all reviews if fewer than 1,000; not random). Numbers in the side-by-side tables carry their tag in the cell. [L1] marks a value from the layer-1 classification (an [I]-grade field).

**Sources.** `data\deep_study_comparison.csv` (built from `deep_study_numbers.csv`, `themes_by_game.csv`, `l1_classified.csv`, `clips_streamers.csv`, `mods_top.csv`), `deep_profiles_batch_1..8.md`, `data\deep\{appid}\themes.md`, `layer3_first_15_minutes.md` / `data\first15.csv`, `layer3_clips_streamers.md`.

**How to read the ranking.** "Evidence-backed" means a measured difference in the files that plausibly moves sales (review codes, player counts, dated events). "Plausible" means a real difference whose effect size we cannot measure. "Speculative" means a story that fits but has no direct support. In every pair the hit launched first, so first-mover advantage and streamer luck can never be separated from design. That limit is stated per pair and not repeated in every line.

**Small-n warning.** Flop review samples are tiny: 39 to 152 reviews [P], 38 to 147 codable [S]. One review moves a flop's theme share by 1 to 3 points. Read flop theme shares as direction, not size.

---

## P01 PEAK vs Sunset Summit (hit vs flop)

**Shared idea.** A co-op mountain climb with climbing tools, stamina and helping friends up; comedy tone; first person.

| | PEAK | Sunset Summit |
|---|---|---|
| Stratum | hit | flop |
| Release (first) | 2025-06-16 [P] | 2026-09-09 [P] |
| Early Access (store lists EA now) | no [P] | no [P] |
| Price (list, USD) | 7.99 [P] | 4.99 [P] |
| Max players | 4 [P] | 8 [L1] |
| Camera | first [I] | first [I] |
| Demo on store | no [P] | no [P] |
| Next Fest | none found | not confirmed (Oct 2025 intent) [D] |
| Publisher | Aggro Crab|Evil Landfall? [P] | Future Friends Games [P] |
| Team | not found (Landfall + Aggro Crab, ~13 at Aggro Crab) [T] | 2 brothers (DEVOUR devs) [D] |
| Reviews | 385,690 [P] | 126 [P] |
| % positive | 94.4 [P] | 83.3 [P] |
| Median h at review (all / pos / neg) | 14.1 / 14.3 / 12.3 [S] | 3.3 / 3.3 / 3.2 [S] |
| Reviews <2 h / >10 h / >50 h (%) | 3.7 / 61.6 / 16.5 [S] | 29.4 / 17.5 / 0.0 [S] |
| Top language (share %) | english (47.6) [P] | english (31.7) [P] |
| China share of reviews % | 6.7 [P] | 13.5 [P] |
| SteamCharts all-time peak | 169,910 [T] | 412 [T] |
| Month-1 / month-6 avg players | 57,223 / 25,161 [T] | 48 / n/a [T] |
| m6/m1 | 0.44 [I] | n/a [I] |
| Current players (2026-11-10/11) | 13,304 [P] | 12 [P] |
| Steam news items (patch notes) | 125 / 55 [P] | 18 / 12 [P] |
| Top praise theme (% of codable positives) | fun_with_friends (38.8) [S] | fun_with_friends (25.0) [S] |
| Top complaint theme (% codable) | bugs_glitches (7.0) [S] | bugs_glitches (15.3) [S] |
| Technical-failure mentions % | 15.4 [S] | 23.4 [S] |
| Refund mentions % | 0.6 [S] | 1.8 [S] |
| Codable reviews (n) | 858 [S] | 111 [S] |
| Top Twitch clip views | 11,461 [P] | not collected |
| Top mod downloads | 4,166,686 [P] | not collected |
| Proximity voice | yes [P] | yes, + walkie-talkies [P] |
| Solo | yes [P] | yes, offline [P] |
| Public lobbies | no, friends-only [P] | not found |
| Dead/waiting player | ghost; carried bodies / revive at statue or effigy [T] | instant respawn; early finishers wait at summit [P] |
| Interdependence / repeatability | high / runs [I] | high / finite [I] |

**Design**
- **Loop.** PEAK is a run: one procedural island that changes every 24 h, climbed through 4+ biomes; a wipe ends the run [P store; D]. Sunset Summit is 16 handcrafted routes of about 1 h each, about 16 h in total, with a sunset time limit [D store]. One is a repeatable run; the other is a finite course list [I].
- **Inputs.** Both have climbing with stamina, ropes and proximity voice [P]. PEAK adds a "helping hand" pull-up, carrying downed friends in the backpack and shared food and healing [T wiki]. Sunset Summit adds pogo sticks, a drone and a grappling gun [P].
- **Interdependence.** PEAK makes failure social: an unconscious scout needs someone else's bandage, a carry or a revive at a statue [T]. In Sunset Summit a fall means instant respawn at a frequent checkpoint [P], so a friend's mistake costs little. The designer's own line is "FUN OVER FRUSTRATION" [P store].
- **Readable goal.** In both, the goal is the visible mountain. In PEAK's first-session video it is stated at +21 s [T/M first15]. No usable first-session video exists for Sunset Summit (`layer3_first_15_minutes.md`).
- **Dead players.** In PEAK they are ghosts who spectate and keep talking, and can be revived [T]. Sunset Summit has no death to wait out [P].

**Execution.** Technical-failure mentions are 15.4% for PEAK and 23.4% for Sunset Summit [S]; bugs are the top complaint in both. Sunset Summit's negatives are mostly bugs (6 of 19 codable negatives) and crashes (4 of 19) [S]. Onboarding complaints: none in either game's early negatives (Sunset Summit 0 of 11 early English reviews) [S, `layer3_first_15_minutes.md`].

**Launch path**
- **PEAK.** A teaser in April 2025, announced 2025-06-12, released 4 days later, no demo or Next Fest [D]. It launched 38% off "so that you can get PEAK for a friend too" [D]. It sold 2M copies in 9 days [D]. It went viral in launch week through TikTok, Twitch and YouTube [D].
- **Sunset Summit.** Started in 2021, paused in 2023 by burnout, and finished "after the success of PEAK in 2025" [D]. It ran a playtest as RISE in Aug 2025 that was meant for Next Fest; participation is not confirmed [D/I]. It was revealed at the PC Gaming Show on 2026-06-07 with a demo, then slipped from 21 Aug to 9 Sep 2026 [P]. Publisher: Future Friends Games [P].
- **Follower?** Yes. It launched 15 months after PEAK [P] and the developer says PEAK's success is why it was finished [D].

**Price.** PEAK lists at $7.99 [P] but launched and is now sold at $4.95 [P]. Sunset Summit lists at $4.99 and was $3.99 on 2026-11-11 [P]. Sunset Summit is cheaper, and reviewers praise its value (P08 at 15.2% of codable positives [S]). Price does not explain the gap.

**Updates.** PEAK has 125 news items [P]: biome updates (Mesa, Roots, Final Ascent) each lifted the monthly average (+24%, +66%, +212%) [T]. Sunset Summit has 18 [P]: its one content update (Grappling Gun, 2026-10-12) gave no lift; Oct averaged 22 players [T].

**What reviewers say.** PEAK: "fun with friends" dominates (38.8% of codable positives [S]); complaints are small (bugs 7.0%, connection 5.1%, repetitive 4.9% [S]). Sunset Summit: also "fun with friends" (25.0%), then value (15.2%) and "funny" (12.0%) [S]. One reviewer calls it "Peak, but somehow crappier and better at the same time" [S quote].

**What most plausibly made the difference**
1. **Launch timing and timing relative to the hit** (evidence-backed). PEAK launched into an empty niche with a surprise launch; Sunset Summit launched 15 months later into a niche PEAK owned, and its own developer frames it as a PEAK follower [D].
2. **Social failure vs forgiving failure** (plausible). PEAK's revives, carries and ghosts create clip moments and banter; Sunset Summit's instant respawn removes them. This is design-level evidence only: no first-session video exists for Sunset Summit to test it.
3. **Content cadence** (evidence-backed for PEAK's retention, not for the launch). Three PEAK biome updates each lifted players [T]; Sunset Summit's single update did not.
4. **Studio audience** (plausible). Landfall/Aggro Crab had prior hits and audiences (Content Warning, Another Crab's Treasure) [T]. DEVOUR's developers also had a 7M-copy claim [D], so pedigree alone is not enough.
5. **Run vs finite course** (speculative for sales, plausible for retention; see the cross-pair synthesis).

**What cannot be separated.** First-mover advantage and PEAK's launch-week creator wave cannot be told apart from design. The match is good on mechanics, but not on timing.

---

## P02 Lethal Company vs Cargo Duty (hit vs flop)

**Shared idea.** A crew flies moon to moon gathering scrap or cargo while creatures attack; horror-comedy.

| | Lethal Company | Cargo Duty |
|---|---|---|
| Stratum | hit | flop |
| Release (first) | 2023-10-23 [P] | 2024-02-03 [P] |
| Early Access (store lists EA now) | yes [P] | no [P] |
| Price (list, USD) | 9.99 [P] | 0.00 [P] |
| Max players | 4 [T] | 6 [P] |
| Camera | first [I] | unknown [I] |
| Demo on store | no [P] | no [P] |
| Next Fest | none found | none found |
| Publisher | self [P] | self [P] |
| Team | 1 (solo) [T] | ~1 (solo) [I] |
| Reviews | 511,826 [P] | 103 [P] |
| % positive | 96.9 [P] | 68.9 [P] |
| Median h at review (all / pos / neg) | 14.0 / 13.5 / 23.4 [S] | 0.6 / 0.7 / 0.5 [S] |
| Reviews <2 h / >10 h / >50 h (%) | 8.2 / 57.6 / 23.7 [S] | 86.4 / 4.9 / 1.0 [S] |
| Top language (share %) | english (67.6) [P] | english (68.0) [P] |
| China share of reviews % | 3.8 [P] | 1.0 [P] |
| SteamCharts all-time peak | 239,369 [T] | n/a [T] |
| Month-1 / month-6 avg players | 20,005 / 25,326 [T] | n/a / n/a [T] |
| m6/m1 | 1.27 [I] | n/a [I] |
| Current players (2026-11-10/11) | 2,778 [P] | 0 [P] |
| Steam news items (patch notes) | 84 / 7 [P] | 2 / 1 [P] |
| Top praise theme (% of codable positives) | fun_with_friends (17.7) [S] | fun_with_friends (6.6) [S] |
| Top complaint theme (% codable) | bugs_glitches (5.0) [S] | bugs_glitches (4.5) [S] |
| Technical-failure mentions % | 9.2 [S] | 6.7 [S] |
| Refund mentions % | 0.9 [S] | 1.1 [S] |
| Codable reviews (n) | 898 [S] | 89 [S] |
| Top Twitch clip views | 218,000 [P] | not collected |
| Top mod downloads | 27,120,069 [P] | not collected |
| Proximity voice | yes [T] | unknown [L1] |
| Solo | yes [P] | yes [P] |
| Public lobbies | yes [I] | unknown [L1] |
| Dead/waiting player | spectate [T, not primary-verified] | not found |
| Interdependence / repeatability | medium / runs [I] | medium / runs [I] |

**Design**
- **Loop.** Lethal Company is a run: loot scrap from facilities, carry it back to the ship and meet a rising quota every 3-day cycle; missing it resets the run [P store; T wiki]. Cargo Duty is "goofy horror resource management", framed as "How long will you survive?" [P store], i.e. an open-ended survival timer [I].
- **Inputs and interdependence.** Lethal Company has proximity voice, two-handed scrap, a ship terminal for typed commands, and a "computer guy" role that guides the crew by radar [P/T]. Scrap counts only if it reaches the ship [T]. Cargo Duty: nothing beyond store text was found [I].
- **Readable goal.** Lethal Company's first-session host states the goal at +180 s [T/M first15]. In the Cargo Duty video the goal is never clear: a guess at +383 s, and at 01:43 "that be the whole game dude... I know it's two bucks but this can't be" [T/M]. 3 of Cargo Duty's 28 codable negatives say "no tutorial / unclear what to do" (the top negative complaint) [S].
- **Dead players.** Lethal Company: spectate [T]. Cargo Duty: not found.

**Execution.** Technical failure is 9.2% for Lethal Company and 6.7% for Cargo Duty [S]. Cargo Duty is not more broken; it is unclear. Its median playtime at review is 0.63 h, with 86% of reviews under 2 h [S].

**Launch path**
- **Lethal Company.** Development logs on Patreon from 2022, a teaser in Jul 2022, and small playtests from Aug 2023 [T]. No demo or Next Fest [T]. It went viral 3 to 4 weeks after launch through streamers, with weekly peak CCU going 611 → 43,268 [T]. The month-6 to month-1 ratio of 1.27 [I] reflects that late virality.
- **Cargo Duty.** No announcement, demo or Next Fest found [P]. It launched 2024-02-03 at A$3 and went free 2024-04-18 [D]. It has 2 news posts [P].
- **Follower?** Yes. It launched about 3.5 months after Lethal Company, during that game's peak [P].

**Price.** $9.99 vs about US$2, then free [P/D]. The cheaper game lost by far, and going free only added more players with lower sentiment (Apr 2024 at 47% positive) [P].

**Updates.** 84 news items vs 2 [P]. Lethal Company's updates (V40 to V80) kept lifting players, e.g. V80 +92% in Apr 2026 [T]. Cargo Duty stopped posting after May 2024 [P].

**What reviewers say.** Lethal Company: fun with friends 17.7%, monsters 12.7%, horror 12.2%, funny 11.0% of codable positives [S]. Cargo Duty: the praise is meme reviews (top praise 6.6% [S]); one complaint reads "45 minutes of boring content" [S quote].

**What most plausibly made the difference**
1. **Readable goal and a failure model** (evidence-backed). A quota with a deadline and loot that must physically reach the ship, against a survive-the-timer with no stated objective. The first-session video and the reviews agree.
2. **Effort and depth** (evidence-backed). About 17 months of development with playtests [T/I], against a two-post, near-abandoned release.
3. **Follower timing** (plausible). Cargo Duty launched as a cheap clone in the hit's shadow. Being a follower did not doom Demonologist (P10), so timing is not sufficient on its own.
4. **Price** (evidence against). The flop was cheaper and then free.

**What cannot be separated.** Lethal Company's streamer wave was luck plus fit; Cargo Duty never got a test. This is a weak-effort flop, so the pair says more about minimum viable depth than about fine design differences.

---

## P03 R.E.P.O. vs Treasure Hunters: Raid Together (hit vs flop)

**Shared idea.** A co-op raid of procedural levels to grab valuables for a payout, with monsters and physics loot.

| | R.E.P.O. | Treasure Hunters: Raid Together |
|---|---|---|
| Stratum | hit | flop |
| Release (first) | 2025-02-26 [P] | 2026-03-11 [P] |
| Early Access (store lists EA now) | yes [P] | no [P] |
| Price (list, USD) | 9.99 [P] | 9.99 [P] |
| Max players | 6 [L1] | 4 [L1] |
| Camera | first [I] | first [I] |
| Demo on store | no [P] | no [P] |
| Next Fest | none found | June 2025 (+ Four is a Party, Couch Co-op Fest) [D] |
| Publisher | self [P] | PlayWay S.A. [P] |
| Team | <10 staff (registry: 7) [T] | 1 (solo) [D] |
| Reviews | 435,350 [P] | 98 [P] |
| % positive | 96.0 [P] | 85.7 [P] |
| Median h at review (all / pos / neg) | 22.4 / 23.8 / 9.2 [S] | 1.7 / 1.9 / 1.4 [S] |
| Reviews <2 h / >10 h / >50 h (%) | 4.0 / 69.0 / 28.1 [S] | 53.1 / 7.1 / 1.0 [S] |
| Top language (share %) | english (41.1) [P] | english (46.9) [P] |
| China share of reviews % | 4.4 [P] | 6.1 [P] |
| SteamCharts all-time peak | 266,908 [T] | 46 [T] |
| Month-1 / month-6 avg players | 105,384 / 27,694 [T] | 7 / n/a [T] |
| m6/m1 | 0.26 [I] | n/a [I] |
| Current players (2026-11-10/11) | 22,496 [P] | 4 [P] |
| Steam news items (patch notes) | 109 / 11 [P] | 51 / 11 [P] |
| Top praise theme (% of codable positives) | fun_with_friends (33.2) [S] | fun_with_friends (45.8) [S] |
| Top complaint theme (% codable) | repetitive_boring (4.6) [S] | bugs_glitches (8.2) [S] |
| Technical-failure mentions % | 10.4 [S] | 15.5 [S] |
| Refund mentions % | 0.7 [S] | 0.0 [S] |
| Codable reviews (n) | 855 [S] | 97 [S] |
| Top Twitch clip views | 392,883 [P] | not collected |
| Top mod downloads | 10,868,439 [P] | not collected |
| Proximity voice | yes [D store] | yes [P] |
| Solo | yes [P] | yes [S] |
| Public lobbies | added in 0.2.0 [D] | yes [S] |
| Dead/waiting player | spectate; head must be carried back to revive [P/D] | free spectator [P] |
| Interdependence / repeatability | medium / runs [I] | medium / runs [I] |

**Design**
- **Loop.** Both are runs. R.E.P.O.: find physics-simulated valuables, carry them without breaking them to extraction, meet a quota, buy upgrades [D store]. Treasure Hunters: an Indiana Jones-style dungeon raid; grab the artifact and valuables, sell them for gear, unlock larger dungeons [P].
- **Inputs.** R.E.P.O.'s core verb is a physics grab beam: rotate and push/pull fragile items, which lose value when damaged; plus proximity voice and typed text spoken by your robot [D]. Treasure Hunters has whip, swing, kick, pistol, sword, dynamite, vault and lean [P]. It is a more conventional action set, and heavy treasure slows you down [P].
- **Interdependence.** R.E.P.O.: heavy and fragile items need several carriers; one quota and one money pool; a dead player's head must be carried back for revival [D/T]. Treasure Hunters: co-op puzzles and revives [P].
- **Readable goal.** In both first-session videos the goal comes within about 1 to 4 min [T/M]. R.E.P.O.'s first failure is a valuable losing value (+61 s), i.e. funny physics. Treasure Hunters' first failures are getting stuck and a bug, with "first real danger only ~10:48" [T/M].
- **Dead players.** R.E.P.O. added Death Head Possession (0.3.0): the dead recharge and act on the living [D]. Treasure Hunters: free spectator [P].

**Execution.** Technical failure is 10.4% vs 15.5% [S]. Treasure Hunters only gained controller support and netcode/desync fixes on 2026-11-10 [P].

**Launch path**
- **R.E.P.O.** No demo or Next Fest [P]. It went viral in launch week, peaking at 271k players on 2025-03-03 [P feed], with a shout-out from Lethal Company's creator [T]. Early Access, self-published [P].
- **Treasure Hunters.** It followed the full festival route. Announced around early 2024 [D], demo Nov 2024, Four is a Party Dec 2024, Couch Co-op Fest Feb 2025, Next Fest June 2025, free prologue Jul 2025, closed beta Oct 2025, 1.0 on 2026-03-11 [D]. Published by PlayWay [P]. Creator coverage existed: SQUEEZIE 1.29M views on YouTube [P, clips file]; Jerma/Vinny and Fooster first-session videos [T/M]. It sold 5,000 copies about 5 months after launch [D].
- **Follower?** In concept, no: it was announced about a year before R.E.P.O. launched [D]. At launch, yes: it shipped 1.0 12.5 months after R.E.P.O. [P], when the "Raid Together" positioning read as a clone [I].

**Price.** Both $9.99 list [P]. Price does not explain the gap.

**Updates.** 109 vs 51 news items [P]. R.E.P.O. updates moved players: v0.3.0 plus a free weekend lifted Nov 2025 by 164%; v0.4.0 lifted May 2026 by 105% [T]. Treasure Hunters patched heavily (9 patches in 2 weeks) with no visible lift [T].

**What reviewers say.** R.E.P.O.: fun with friends 33.2%, horror 19.5%, monsters 18.9%, funny 17.1% of codable positives [S]. Treasure Hunters: fun with friends 45.8%, atmosphere 15.7%, "potential" 12.1% [S]. The "potential" share is a typical flop sign: people like it and hope it grows [I].

**What most plausibly made the difference**
1. **A signature physics verb that produces comedy** (plausible, with supporting video evidence). Fragile loot and the grab beam turn every carry into a clip; Treasure Hunters' comedy came from banter and customisation, not failure [T/M].
2. **Timing relative to the hit** (evidence-backed as a fact, unmeasurable as an effect). Treasure Hunters reached 1.0 a year after R.E.P.O. and was read against it.
3. **The festival route did not substitute for a viral moment** (evidence-backed). Four festivals, a prologue, large creator videos, and still 98 reviews [P].
4. **Polish and controls** (plausible). There are more tech complaints, and controller support and netcode arrived late.

**What cannot be separated.** R.E.P.O. inherited Lethal Company's audience and endorsement; Treasure Hunters met a market already served. This is a good mechanical match, and the best pair evidence that creator coverage alone does not convert [I].

---

## P04 RV There Yet? vs Drive Together (hit vs flop) - WEAK MATCH

**Shared idea.** Friends jointly operate one vehicle through a physics course. **Why the match is weak:** RV There Yet? is a road trip with walking, winching, repairs and survival between checkpoints. Drive Together is a stunt-parkour track where each player owns one control (throttle, brake, left, right) [P/T]. The setting and the moment-to-moment game differ; only the "shared vehicle" mechanic is common. The only road-trip flops had no effort signal and were not eligible (`deep_study_selection.md`).

| | RV There Yet? | Drive Together |
|---|---|---|
| Stratum | hit | flop |
| Release (first) | 2025-10-21 [P] | 2026-05-15 [P] |
| Early Access (store lists EA now) | no [P] | no [P] |
| Price (list, USD) | 7.99 [P] | 4.49 [P] |
| Max players | 4 [P] | 8 [L1] |
| Camera | first [I] | third [I] |
| Demo on store | no [P] | no [P] |
| Next Fest | none found | Feb 2026 [P] |
| Publisher | self [P] | TARK Future Heroes [P] |
| Team | core of 4 for prototype; studio size not found [D] | not found |
| Reviews | 91,202 [P] | 73 [P] |
| % positive | 90.1 [P] | 68.5 [P] |
| Median h at review (all / pos / neg) | 9.5 / 10.0 / 6.0 [S] | 1.0 / 1.3 / 0.9 [S] |
| Reviews <2 h / >10 h / >50 h (%) | 6.6 / 47.4 / 2.8 [S] | 82.2 / 0.0 / 0.0 [S] |
| Top language (share %) | english (42.2) [P] | english (43.8) [P] |
| China share of reviews % | 4.8 [P] | 6.8 [P] |
| SteamCharts all-time peak | 56,960 [T] | n/a [T] |
| Month-1 / month-6 avg players | 15,113 / 3,965 [T] | n/a / n/a [T] |
| m6/m1 | 0.26 [I] | n/a [I] |
| Current players (2026-11-10/11) | 2,210 [P] | 0 [P] |
| Steam news items (patch notes) | 34 / 15 [P] | 15 / 5 [P] |
| Top praise theme (% of codable positives) | fun_with_friends (30.1) [S] | fun_with_friends (31.9) [S] |
| Top complaint theme (% codable) | bugs_glitches (13.6) [S] | bugs_glitches (20.3) [S] |
| Technical-failure mentions % | 18.2 [S] | 26.1 [S] |
| Refund mentions % | 0.3 [S] | 4.3 [S] |
| Codable reviews (n) | 882 [S] | 69 [S] |
| Top Twitch clip views | 34,817 [P] | not collected |
| Top mod downloads | 45,384 [P] | not collected |
| Proximity voice | yes [P] | unknown [L1] |
| Solo | yes, hard [P] | yes [P] |
| Public lobbies | unknown [L1] | not found |
| Dead/waiting player | spectate then timed respawn [T] | n/a |
| Interdependence / repeatability | high / finite [I] | high / finite [I] |

**Design**
- **Loop.** RV: drive and winch an RV home over 3 maps, about 6 h for the campaign [T], with checkpoints [T]. Drive Together: short parkour maps of about 30 min each [S quote] plus an 8-player race mode [P].
- **Interdependence.** RV: the driver needs others on the winch ("will have a hard time … alone" [P]); others can leave the vehicle. Drive Together: every move needs another player's input [P], so "one weak player stalls the whole car" [I].
- **Readable goal.** Both have in-world instructions [T/M]. RV's first-session video has laughter tags throughout. Drive Together's 2-player session gets its first laugh at +377 s; the players say the fun needs 4 and complain about input lag [T/M].
- **Dead players.** RV: spectate, then a timed respawn [T]. Drive Together: n/a.

**Execution.** Tech failure is 18.3% vs 26.1% [S]; bugs are the top complaint in both (RV 13.6%, Drive Together 20.3% of codable [S]). RV launched without keybinds, controller or localisation and shipped 5 hotfixes in its first 10 days [P].

**Launch path**
- **RV.** A summer-2025 game jam; announced 2025-10-14 and released 7 days later [P]. A leaked store page went viral on TikTok before the announcement [D]. It had 300k+ wishlists after about a week public [D], a Steam takeover [D] and 2M units in 8 days [D]. Funded by a Coffee Stain co-founder [D].
- **Drive Together.** Demo Jan 2026, wishlists from 5k to 20k [D], GG Con, Next Fest Feb 2026 [P], release 2026-05-15 [P]. Publisher TARK Future Heroes [P]. No viral moment [I].
- **Follower?** Yes. It released 7 months after RV [P]; its demo landed in RV's third month. Reviewers compare it to Chained Together ("another chained together ... with driving instead" [S quote]).

**Price.** $7.99 vs $4.49 [P]. 13.6% of Drive Together's codable negatives say the price is too high ("too expensive for unreal slop" [S quote]), even though it is cheaper.

**Updates.** 34 vs 15 news items [P]. RV's map 2 and map 3 updates moved players (Sep 2026 +159%) [T]. Drive Together has no posts after 2026-06-26 [P].

**What reviewers say.** RV: fun with friends 30.2%, funny 16.1%, physics chaos 7.7% [S]; bugs are tolerated ("physics so bugged it goes back to being a fun feature" [S quote]). Drive Together: fun with friends 34.0%; complaints are bugs, too short (13.0%) and price [S].

**What most plausibly made the difference**
1. **Pre-launch viral moment plus a short reveal-to-release window** (evidence-backed). The team says "we released the game on its peak hype cycle" [D].
2. **Content size and role variety** (plausible). A 6 h journey with several jobs (driver, winch, repair, scouting), against short maps where each player holds one control.
3. **Studio network** (plausible). A founder from Coffee Stain Publishing and a Steam takeover [D].
4. **Per-player agency** (speculative). Split controls make one player's lag or skill the whole group's problem.

**What cannot be separated.** The leaked-page virality is luck. The mechanical match is loose, so design conclusions from this pair should be weighted least.

---

## P05 Supermarket Together vs Out of Stock! (hit vs flop)

**Shared idea.** A co-op store simulation: restock, serve customers, chaos. **Match caveat:** Supermarket Together is first-person and sandbox-paced; Out of Stock! is top-down and level-based in the Overcooked style [T portfolio]. The core types match (job_simulation); the feel does not.

| | Supermarket Together | Out of Stock! |
|---|---|---|
| Stratum | hit | flop |
| Release (first) | 2024-08-09 [P] | 2025-10-31 [P] |
| Early Access (store lists EA now) | no [P] | no [P] |
| Price (list, USD) | 0.00 [P] | 6.99 [P] |
| Max players | 16 [L1] | 4 [L1] |
| Camera | first [I] | fixed (top-down) [T] [I] |
| Demo on store | no [P] | yes [P] |
| Next Fest | none found | June 2025 (+ Debut Festival Aug 2025) [P] |
| Publisher | self [P] | Rubika Supinfogame [P] |
| Team | not found | 15 (student project) [D] |
| Reviews | 101,350 [P] | 39 [P] |
| % positive | 94.3 [P] | 28.2 [P] |
| Median h at review (all / pos / neg) | 8.3 / 8.6 / 3.8 [S] | 2.6 / 1.3 / 3.0 [S] |
| Reviews <2 h / >10 h / >50 h (%) | 12.9 / 44.9 / 9.2 [S] | 35.9 / 2.6 / 0.0 [S] |
| Top language (share %) | english (35.3) [P] | schinese (48.7) [P] |
| China share of reviews % | 8.4 [P] | 48.7 [P] |
| SteamCharts all-time peak | 47,731 [T] | n/a [T] |
| Month-1 / month-6 avg players | 17,124 / 8,797 [T] | n/a / n/a [T] |
| m6/m1 | 0.51 [I] | n/a [I] |
| Current players (2026-11-10/11) | 2,877 [P] | 0 [P] |
| Steam news items (patch notes) | 72 / 20 [P] | 8 / 1 [P] |
| Top praise theme (% of codable positives) | value_price (22.2) [S] | fun_with_friends (20.0) [S] |
| Top complaint theme (% codable) | bugs_glitches (5.0) [S] | bugs_glitches (68.4) [S] |
| Technical-failure mentions % | 8.7 [S] | 71.0 [S] |
| Refund mentions % | 0.1 [S] | 0.0 [S] |
| Codable reviews (n) | 887 [S] | 38 [S] |
| Top Twitch clip views | 63,100 [P] | not collected |
| Top mod downloads | 29,262 [P] | not collected |
| Proximity voice | unknown [L1] | unknown [L1] |
| Solo | yes, hireable staff [P] | yes, added for release [P] |
| Public lobbies | yes, public servers [T] | unknown [L1] |
| Dead/waiting player | n/a; jailed player waits out a count [D] | not found |
| Interdependence / repeatability | medium / sandbox [I] | medium / finite [I] |

**Design**
- **Loop.** Supermarket Together: open-ended working days that grow one store and one money pool. There is no game-over; invoices and loans came later [D]. Out of Stock!: star-rated levels [P].
- **Interdependence.** Supermarket Together: a shared store, and demand scales with player count, up to 16 players [P]. Out of Stock!: task division and passing [P].
- **Readable goal.** In Supermarket Together's large-creator video the first ~11 min are toy-box play with brooms and cosmetics before the objective [T/M]: low pressure, high play value. No usable Out of Stock! video was found [T/M].
- **Dead players.** n/a in both; Supermarket Together has a "jail" for lazy friends [D].

**Execution.** This is the biggest execution gap in the study. Out of Stock! has 71.1% technical-failure mentions and bugs in 78.6% of its codable negatives [S]. Online play arrived only at release, with a "geographical restrictions" hotfix 2 days later [P]. Supermarket Together: 8.7% [S].

**Launch path**
- **Supermarket Together.** No demo or Next Fest [P]. Free at launch, with about 48k peak CCU within days [T]. Self-published by a 2-person team [D].
- **Out of Stock!** A 15-person Master-1 student project published by its school [D]. Demo Apr 2025, Next Fest June 2025 ("nearly 20k satisfied customers served" [D]), Debut Festival Aug 2025, launch 2025-10-31 at 35% off [P]. 48.7% of its reviews are Simplified Chinese [P].
- **Follower?** Yes. It launched 15 months after the hit [P], though its Overcooked-style design may not be a reaction to it [I].

**Price.** Free (with one $4.99 cosmetic DLC) vs $6.99 [P]. "Good value / free" is Supermarket Together's top praise (22.2% of codable positives [S]). Price is a real difference here.

**Updates.** A weekly patch cadence for over a year, 72 news items [D/P]; players stayed flat at 4.5k to 7k monthly average for 20 months [T]. Out of Stock!: 8 items [P]; negatives say "Dev has abandoned the game" [S quote].

**What reviewers say.** Supermarket Together: value and fun with friends; complaints are minor (bugs 5.0%, repetitive 4.3%) [S]. Out of Stock!: only 10 codable positives [S]. The negatives are about bugs and lag.

**What most plausibly made the difference**
1. **Broken online co-op at launch** (evidence-backed). 71% tech-failure mentions in a co-op game, with online play added only at release.
2. **Free vs paid** (evidence-backed as a difference; plausible as a cause). Free removed the "buy for each friend" barrier; value is the hit's top praise.
3. **Weekly updates** (evidence-backed for retention). Supermarket Together has the flattest long-run player curve of the hits [T].
4. **Student project with no post-launch team** (plausible).

**What cannot be separated.** Free-to-play and the press "surprise hit" wave arrived together.

---

## P06 Liar's Bar vs Bogos Binted? (hit vs MID)

**Shared idea.** Bluffing at twisted tabletop games around a table of 4, where losers die (revolver) or their heads explode. **This is hit vs mid, not flop:** Bogos Binted? sold 100,000 copies a week after 1.0 [D] and has 91.4% positive reviews [P]. The question here is why one reached 56k reviews and the other 1.4k, not why one failed.

| | Liar's Bar | Bogos Binted? |
|---|---|---|
| Stratum | hit | mid |
| Release (first) | 2024-10-02 [P] | 2025-07-24 [P] |
| Early Access (store lists EA now) | yes [P] | no [P] |
| Price (list, USD) | 6.99 [P] | 5.49 [P] |
| Max players | 4 [L1] | 4 [P] |
| Camera | first [I] | first [I] |
| Demo on store | no [P] | no [P] |
| Next Fest | none found | June 2025 [P] |
| Publisher | self [P] | GameDev.ist|underbadger|Gamersky Games [P] |
| Team | not found (animation studio, est. 2014) [T] | "small indie studio", size not found [D] |
| Reviews | 56,599 [P] | 1,448 [P] |
| % positive | 89.5 [P] | 91.4 [P] |
| Median h at review (all / pos / neg) | 4.1 / 4.2 / 3.4 [S] | 3.3 / 3.4 / 1.5 [S] |
| Reviews <2 h / >10 h / >50 h (%) | 24.8 / 22.0 / 3.5 [S] | 32.2 / 8.2 / 0.1 [S] |
| Top language (share %) | english (32.1) [P] | english (54.1) [P] |
| China share of reviews % | 23.5 [P] | 2.8 [P] |
| SteamCharts all-time peak | 109,419 [T] | 875 [T] |
| Month-1 / month-6 avg players | 19,758 / 1,589 [T] | 79 / 54 [T] |
| m6/m1 | 0.08 [I] | 0.69 [I] |
| Current players (2026-11-10/11) | 330 [P] | 12 [P] |
| Steam news items (patch notes) | 52 / 19 [P] | 15 / 1 [P] |
| Top praise theme (% of codable positives) | fun_with_friends (24.7) [S] | fun_with_friends (21.0) [S] |
| Top complaint theme (% codable) | connection_lobby_host (8.9) [S] | too_short_little_content (3.8) [S] |
| Technical-failure mentions % | 18.2 [S] | 5.0 [S] |
| Refund mentions % | 0.5 [S] | 1.1 [S] |
| Codable reviews (n) | 873 [S] | 872 [S] |
| Top Twitch clip views | not collected | not collected |
| Top mod downloads | not collected | not collected |
| Proximity voice | voice chat added 2024-10-08; proximity not stated [D] | unknown [L1] |
| Solo | unknown [L1] | Zogblorp solo vs AI (added post-1.0) [P] |
| Public lobbies | yes, from launch [D] | unknown [L1] |
| Dead/waiting player | spectate [D] | not found |
| Interdependence / repeatability | low / runs [I] | low / runs [I] |

**Design**
- **Loop.** Both are runs of short versus rounds with elimination [P].
- **Stakes and readability.** Liar's Bar puts a lethal, visible stake (Russian roulette) on every called bluff. In its first-session video the stakes hit within 1 min, and every round ends in a dramatic shot [T/M]. Bogos Binted? has 5 modes with invented names (Zogblorp, Beeble Meep, VORP...) [P]; in first-session videos the rules are learned over several minutes, and card-effect confusion persists [T/M] (11 confusion moments vs 4 for Liar's Bar [T/M]).
- **Interdependence.** Low in both; both are adversarial [I].
- **Dead players.** Liar's Bar: spectate [D]. Bogos Binted?: not found.

**Execution.** Liar's Bar has more technical failure (18.2% vs 5.1% [S]) and draws more cheating, connection and AI-voice complaints [S]. Execution favours the mid, not the hit.

**Launch path**
- **Liar's Bar.** No demo or Next Fest [P]. Launched in Early Access at about 2,000 CCU and grew "organically" through streamers to 113,798 on 2024-10-21, 19 days after release [T].
- **Bogos Binted?** Next Fest June 2025 demo [P], then EA 5 weeks later and 1.0 six months after that [P]. Its 1.0 bump explains its high m6/m1 of 0.69 [T/I]. Co-published by GameDev.ist and Gamersky [P].
- **Follower?** Yes. EA came 10 months after Liar's Bar [P].

**Price.** $6.99 vs $5.49 [P]. There is no material difference.

**Updates.** 52 vs 15 news items [P]. Liar's Bar keeps adding games and seasons; its July 2026 remaster triggered backlash (74% positive that month) [P].

**What reviewers say.** Liar's Bar: fun with friends 24.7%, deception/bluffing 18.5% [S]; negatives cite cheaters (18.4%), bugs, connection and AI-generated assets (12.1%) [S]. Bogos Binted?: fun with friends 22.7%, funny 8.3% [S]; negatives cite AI art (20.9%) and repetition (12.1%) [S].

**What most plausibly made the difference**
1. **One instantly readable, high-stakes image (the revolver)** (plausible, with supporting video evidence). It explains itself to a viewer in seconds, which suits clips.
2. **First-mover streamer wave** (evidence-backed as an event). 2k to 114k CCU in 19 days via streamers [T].
3. **Rule complexity** (plausible). Several invented card games against one simple bluff.
4. **Execution** (evidence against). The mid is more polished, so polish did not decide this pair.

**What cannot be separated.** Liar's Bar's streamer wave and first-mover position. Because Bogos Binted? is a mid, this pair shows a ceiling effect for a follower, not a failure mode.

---

## P07 Chained Together vs Don't Pull Me! (hit vs flop)

**Shared idea.** Players are physically chained or roped together and climb an obstacle course; one slip drags the team.

| | Chained Together | Don’t Pull Me! |
|---|---|---|
| Stratum | hit | flop |
| Release (first) | 2024-06-19 [P] | 2026-07-31 [P] |
| Early Access (store lists EA now) | no [P] | no [P] |
| Price (list, USD) | 4.99 [P] | 4.99 [P] |
| Max players | 4 [L1] | 4 [L1] |
| Camera | third [I] | third [I] |
| Demo on store | no [P] | yes [P] |
| Next Fest | none found | June 2026 (timing only) [I] |
| Publisher | Secret Mode [P] | self [P] |
| Team | not found (debut studio) [T] | not found |
| Reviews | 65,230 [P] | 78 [P] |
| % positive | 89.5 [P] | 74.4 [P] |
| Median h at review (all / pos / neg) | 5.2 / 5.3 / 4.2 [S] | 2.4 / 3.2 / 1.4 [S] |
| Reviews <2 h / >10 h / >50 h (%) | 16.8 / 17.7 / 0.7 [S] | 43.6 / 5.1 / 0.0 [S] |
| Top language (share %) | english (38.0) [P] | english (43.6) [P] |
| China share of reviews % | 21.5 [P] | 15.4 [P] |
| SteamCharts all-time peak | 92,186 [T] | n/a [T] |
| Month-1 / month-6 avg players | 27,947 / 2,216 [T] | n/a / n/a [T] |
| m6/m1 | 0.08 [I] | n/a [I] |
| Current players (2026-11-10/11) | 696 [P] | 29 [P] |
| Steam news items (patch notes) | 38 / 13 [P] | 0 / 0 [P] |
| Top praise theme (% of codable positives) | fun_with_friends (27.7) [S] | fun_with_friends (20.4) [S] |
| Top complaint theme (% codable) | bugs_glitches (3.0) [S] | bugs_glitches (16.7) [S] |
| Technical-failure mentions % | 6.5 [S] | 22.2 [S] |
| Refund mentions % | 0.5 [S] | 4.2 [S] |
| Codable reviews (n) | 866 [S] | 72 [S] |
| Top Twitch clip views | 130,679 [P] | not collected |
| Top mod downloads | 1,421 [P] | not collected |
| Proximity voice | unknown [L1] | unknown [L1] |
| Solo | yes [P] | yes [L1] |
| Public lobbies | yes, lobby browser at launch [P] | unknown [L1] |
| Dead/waiting player | n/a: nobody dies, fallen player climbs back [I] | not documented |
| Interdependence / repeatability | high / finite [I] | high / finite [I] |

**Design**
- **Loop.** Both are finite physics-parkour courses [P]. Chained Together: one vertical climb out of Hell with no checkpoints in Normal; checkpoints in Beginner; Lava mode [P]. Don't Pull Me!: levels of about 2.5 min (demo), with carrying objects and punching other players [P].
- **Readable goal.** Chained Together's goal is legible from the chain itself, and the first laugh comes at +20 to 60 s [T/M]. Don't Pull Me!'s first laugh comes at +328 s, with constant rope tangles and "who should do what?" confusion (9 confusion moments) [T/M; captions machine-translated].
- **Coordination tools.** Chained Together added a "3, 2, 1 Go!" jump-sync key after launch [P]. Don't Pull Me!: none found.
- **Dead players.** n/a in both.

**Execution.** Tech failure is 6.5% vs 22.2% [S]. Don't Pull Me! reviews: "4-player is literally unplayable", "super desyncd and laggy" [S quotes]; bugs are 44% of its codable negatives [S].

**Launch path**
- **Chained Together.** Store page by Sep 2023, demo Oct 2023, 40k wishlists by Nov 2023 [T/D], beta with streamers [D]. Launched at 1.0 in Jun 2024 [P], and big Twitch names played it in the first weeks [T]. Next Fest not found.
- **Don't Pull Me!** Demo 2026-06-14, timing consistent with the June 2026 Next Fest [I]. Released 2026-07-31 [P] with no developer posts (0 news items [P]).
- **Follower?** Yes, by 25 months [P]. It is effectively a late "Chained Together-like" [I].

**Price.** $4.99 vs $4.99 [P]. There is no difference.

**Updates.** 38 vs 0 news items [P]. Chained Together's Workshop update (Sep 2024) gave no lift [T]; paid DLC came only after the 2026 takeover [P].

**What reviewers say.** Chained Together: fun with friends 27.7%, "rage as part of the fun" 7.6%, funny 7.5% [S]. Don't Pull Me!: fun with friends 24.1%, funny 20.4% [S], so the comedy works when it works. The negatives are netcode.

**What most plausibly made the difference**
1. **Netcode and desync in a physics-coupled game** (evidence-backed). When players are physically coupled, desync breaks the core verb.
2. **Being 2 years late** (plausible). The format was already familiar, and reviewers frame it against Chained Together.
3. **Pre-launch audience building** (evidence-backed as a difference). 40k wishlists and streamer betas, against no posts at all.
4. **Readability of the rope vs the chain** (speculative). One first-session video per side.

**What cannot be separated.** The Chained Together streamer wave (Jynxzi, IShowSpeed, Kai Cenat [T]) and first-mover status.

---

## P08 Content Warning vs Backrooms: Extractions (hit vs MID)

**Shared idea.** Go into a horror space, film entities with a camera, survive and extract. **This is hit vs mid** (no eligible flop has a filming loop), and filming is a side system in Backrooms: Extractions, not its scoring core [I]. Weak on the filming mechanic; good on the extraction core.

| | Content Warning | Backrooms: Extractions |
|---|---|---|
| Stratum | hit | mid |
| Release (first) | 2024-04-01 [P] | 2025-04-30 [P] |
| Early Access (store lists EA now) | no [P] | yes [P] |
| Price (list, USD) | 7.99 [P] | 6.99 [P] |
| Max players | 4 [L1] | 6 [P] |
| Camera | first [I] | first [I] |
| Demo on store | no [P] | no [P] |
| Next Fest | none found | none found |
| Publisher | Evil Landfall? [P] | self [P] |
| Team | 5 [D] | not found (studio side project) [T] |
| Reviews | 164,372 [P] | 854 [P] |
| % positive | 93.7 [P] | 73.5 [P] |
| Median h at review (all / pos / neg) | 5.3 / 5.2 / 6.2 [S] | 4.3 / 5.0 / 2.6 [S] |
| Reviews <2 h / >10 h / >50 h (%) | 20.4 / 30.0 / 4.1 [S] | 21.0 / 14.8 / 0.9 [S] |
| Top language (share %) | english (45.9) [P] | english (41.0) [P] |
| China share of reviews % | 4.7 [P] | 14.1 [P] |
| SteamCharts all-time peak | 63,320 [T] | 368 [T] |
| Month-1 / month-6 avg players | 15,678 / 2,881 [T] | 90 / 49 [T] |
| m6/m1 | 0.18 [I] | 0.55 [I] |
| Current players (2026-11-10/11) | 472 [P] | 10 [P] |
| Steam news items (patch notes) | 41 / 13 [P] | 90 / 74 [P] |
| Top praise theme (% of codable positives) | fun_with_friends (22.6) [S] | fun_with_friends (22.3) [S] |
| Top complaint theme (% codable) | bugs_glitches (6.3) [S] | bugs_glitches (15.3) [S] |
| Technical-failure mentions % | 8.8 [S] | 22.4 [S] |
| Refund mentions % | 0.1 [S] | 0.9 [S] |
| Codable reviews (n) | 879 [S] | 745 [S] |
| Top Twitch clip views | 111,205 [P] | not collected |
| Top mod downloads | 1,346,156 [P] | not collected |
| Proximity voice | yes [L1] | unknown [L1] |
| Solo | weak but possible [S reviews] | yes [P] |
| Public lobbies | yes, matchmaking [P] | yes, lobby browser [D] |
| Dead/waiting player | not found | spectate; returned to lab when console armed [D] |
| Interdependence / repeatability | medium / runs [I] | medium / runs [I] |

**Design**
- **Loop.** Content Warning: 3 in-game days to film scary footage of monsters and friends, upload it, and hit a view quota [P]. The footage is the score, and the friends are the content [P]. Backrooms: Extractions: locate lost agents, solve puzzles, fill dossiers by filming, transmit data, and hold out for extraction. Gear is lost on failure [P].
- **Readable goal.** Content Warning's goal is diegetic (camera, SpöökTube); groups turn it into self-directed role-play [T/M]. Backrooms: Extractions has more objectives, and one early review says "The tutorial is also straight cheeks" [S quote].
- **Dead players.** Content Warning: not found. Backrooms: Extractions: spectate, returned to the lab when a player arms the console [D].

**Execution.** Tech failure is 8.8% vs 22.4% [S]. Backrooms: Extractions' complaints are bugs (15.3%), repetitive (9.1%) and too short (9.0%) [S]. Its May to June 2026 rework months fell to 61% and 54% positive [P].

**Launch path**
- **Content Warning.** Surprise-announced and launched the same day, free for 24 h on 2024-04-01: 6.2M claims and over 200k CCU [D]. Then $7.99 and 1M sold in about two weeks [T]. Landfall label [P].
- **Backrooms: Extractions.** EA 2025-04-30, no demo or Next Fest [P]. A side project of a small French studio [T]. About 30,000 copies in 2 months [T snippet].
- **Follower?** Yes: 13 months after Content Warning, and also one of many Backrooms-themed games [I].

**Price.** $7.99 vs $6.99 [P]. Not material.

**Updates.** 41 vs 90 news items [P]. The mid updated far more (about 35 patches in its first month) [D]. Content Warning's updates did not reverse its decay [T]. In this pair, updates do not explain the gap.

**What reviewers say.** Content Warning: fun with friends 22.7%, monsters 13.5%, "streamer / clip-worthy" 12.3% [S], the highest clip-worthy share among the pair games. Backrooms: Extractions: fun with friends 23.1%, then "potential" 14.9% and atmosphere 14.4% [S].

**What most plausibly made the difference**
1. **The free-day launch stunt** (evidence-backed). 6.2M claims seeded a viral weekend [D].
2. **A loop that makes clips by design** (plausible). Content Warning's output is a video of your friends; reviewers say so (12.3% clip-worthy [S]).
3. **Execution and scope** (evidence-backed as a difference). Bugs, repetition and short-content complaints [S].
4. **Theme saturation** (speculative). Backrooms is a crowded theme.

**What cannot be separated.** Landfall's brand and the free day came together with the design. Because this is hit vs mid with a side-system filming match, conclusions are weaker.

---

## P09 Mage Arena vs Super Shout Showdown (hit vs flop)

**Shared idea.** Shout spell incantations into the mic to cast spells in PvP.

| | Mage Arena | Super Shout Showdown |
|---|---|---|
| Stratum | hit | flop |
| Release (first) | 2025-07-24 [P] | 2026-08-06 [P] |
| Early Access (store lists EA now) | yes [P] | yes [P] |
| Price (list, USD) | 2.99 [P] | 7.99 [P] |
| Max players | 8 [L1] | 16 [L1] |
| Camera | first [I] | third [I] |
| Demo on store | no [P] | yes [P] |
| Next Fest | none found | June 2026 [D] |
| Publisher | self [P] | self [P] |
| Team | 1 (solo) [T] | ~1 (solo or very small) [I] |
| Reviews | 20,512 [P] | 152 [P] |
| % positive | 90.8 [P] | 86.2 [P] |
| Median h at review (all / pos / neg) | 2.3 / 2.6 / 1.2 [S] | 2.5 / 2.8 / 1.4 [S] |
| Reviews <2 h / >10 h / >50 h (%) | 44.4 / 10.6 / 1.0 [S] | 37.5 / 12.5 / 0.7 [S] |
| Top language (share %) | english (64.3) [P] | english (42.1) [P] |
| China share of reviews % | 0.8 [P] | 24.3 [P] |
| SteamCharts all-time peak | 17,126 [T] | 204 [T] |
| Month-1 / month-6 avg players | 4,843 / 161 [T] | 34 / n/a [T] |
| m6/m1 | 0.03 [I] | n/a [I] |
| Current players (2026-11-10/11) | 15 [P] | 6 [P] |
| Steam news items (patch notes) | 21 / 20 [P] | 34 / 4 [P] |
| Top praise theme (% of codable positives) | fun_with_friends (12.2) [S] | fun_with_friends (15.1) [S] |
| Top complaint theme (% codable) | bugs_glitches (4.9) [S] | connection_lobby_host (5.4) [S] |
| Technical-failure mentions % | 10.4 [S] | 15.7 [S] |
| Refund mentions % | 1.3 [S] | 0.7 [S] |
| Codable reviews (n) | 872 [S] | 147 [S] |
| Top Twitch clip views | 87,958 [P] | not collected |
| Top mod downloads | 28,758 [P] | not collected |
| Proximity voice | yes [T] | unknown [L1] |
| Solo | no, PvP only [P] | bots added 0.5.2 [D] |
| Public lobbies | yes, lobby finder [P] | yes, thin lobbies [D] |
| Dead/waiting player | respawn indicator [T] | spectator mode added 0.5.3 (2026-10) [D] |
| Interdependence / repeatability | medium / runs [I] | low / runs [I] |

**Design**
- **Loop.** Mage Arena: team capture-the-flag on an island, 4v4, voice-cast spells, proximity voice, and sudden death once your flag falls [P/T]. Super Shout Showdown: duels, team battles and 16-player FFA with custom chants, plus typing, Hand Seal and tapping modes for players without a mic [D].
- **Readable goal.** Both use voice mis-recognition as both the first laugh and the first failure (Mage Arena +184 s, Super Shout Showdown +20 s) [T/M]. There is no clear first-15 difference [T/M].
- **Dead players.** Mage Arena: a respawn indicator [T]. Super Shout Showdown: spectator mode added 2026-10-22 [D].

**Execution.** Tech failure is 10.4% vs 15.7% [S]. Mage Arena's negatives are dominated by "developer abandoned" (19.1% of codable negatives) [S], after a 6.5-month silence [P].

**Launch path**
- **Mage Arena.** No demo or Next Fest [P]. EA at $2.99, discounted "DUE TO A LARGE NUMBER OF BUGS" [P store text via T]. It went viral on TikTok in its first week [T]; the top Twitch clip has 87,958 views [P].
- **Super Shout Showdown.** Store page Nov 2025, two playtests, demo, Next Fest June 2026, EA 2026-08-07 at $7.99 with 20% off [D/P]. No viral moment; a clip contest [D].
- **Follower?** Yes, 12 months later [P].

**Price.** $2.99 vs $7.99 [P]. Polygon credited Mage Arena's "miniscule price point" [T]. This is the largest price gap among the paid pairs.

**Updates.** 21 vs 34 news items [P]. The flop updated about weekly [D] with no effect. Mage Arena's later updates did not lift players either [T]; it has the steepest decay of any hit (m6/m1 0.03 [I]).

**What reviewers say.** Both: fun with friends, funny, voice chat [S]. Mage Arena: 44% of reviews under 2 h [S], and "in 1-3 hours it gets boring" [S quote]. Super Shout Showdown: "potential" 10.3% [S]; complaints are connection problems and dead lobbies [S].

**What most plausibly made the difference**
1. **First mover on a novelty gimmick** (plausible, strongly suggested). The voice-cast idea is the whole hook; once seen, a second version is less shareable [I].
2. **Impulse price** (plausible). $2.99 against $7.99 for a game reviewers play for about 2 h (median 2.3 h vs 2.5 h [S]).
3. **Lobby liquidity** (evidence-backed for the flop). A PvP-only game needs strangers; the flop added bots to all modes 2 months in [D].
4. **Design depth** (evidence against). The flop has more modes and accessibility options and still lost.

**What cannot be separated.** TikTok luck and first-mover status. Note that the hit itself did not retain players, so neither game shows a durable design.

---

## P10 Demonologist vs Mortuar (hit vs flop)

**Shared idea.** Use ghost-hunting equipment to identify a ghost type, then banish it (the Phasmophobia formula). **Both are followers of Phasmophobia** (2020); this pair is "successful follower vs failed follower".

| | Demonologist | Mortuar |
|---|---|---|
| Stratum | hit | flop |
| Release (first) | 2023-03-27 [P] | 2024-07-09 [P] |
| Early Access (store lists EA now) | no [P] | no [P] |
| Price (list, USD) | 19.99 [P] | 0.00 [P] |
| Max players | 4 [L1] | 4 [L1] |
| Camera | first [I] | first [I] |
| Demo on store | yes [P] | no [P] |
| Next Fest | Feb 2023 (likely: demo released on day 1) [I] | none found |
| Publisher | self [P] | mortuargame [P] |
| Team | not found (second team exists) [D] | 3 named [P] |
| Reviews | 24,621 [P] | 89 [P] |
| % positive | 84.8 [P] | 37.1 [P] |
| Median h at review (all / pos / neg) | 9.4 / 9.2 / 9.7 [S] | 0.4 / 0.6 / 0.3 [S] |
| Reviews <2 h / >10 h / >50 h (%) | 11.7 / 48.2 / 10.4 [S] | 95.5 / 2.2 / 0.0 [S] |
| Top language (share %) | english (55.7) [P] | english (53.9) [P] |
| China share of reviews % | 2.3 [P] | 7.9 [P] |
| SteamCharts all-time peak | 8,693 [T] | n/a [T] |
| Month-1 / month-6 avg players | 3,839 / 1,045 [T] | n/a / n/a [T] |
| m6/m1 | 0.27 [I] | n/a [I] |
| Current players (2026-11-10/11) | 188 [P] | 0 [P] |
| Steam news items (patch notes) | 58 / 28 [P] | 1 / 1 [P] |
| Top praise theme (% of codable positives) | horror_tension (42.2) [S] | horror_tension (16.7) [S] |
| Top complaint theme (% codable) | bugs_glitches (12.6) [S] | bugs_glitches (17.5) [S] |
| Technical-failure mentions % | 18.5 [S] | 31.2 [S] |
| Refund mentions % | 3.0 [S] | 0.0 [S] |
| Codable reviews (n) | 919 [S] | 80 [S] |
| Top Twitch clip views | 74,300 [P] | not collected |
| Top mod downloads | 328 [P] | not collected |
| Proximity voice | yes since v2.1.0 [P] | unknown [L1] |
| Solo | yes [P] | yes [L1] |
| Public lobbies | yes (blacklist) [I] | unknown [L1] |
| Dead/waiting player | separate dead text channel (v2.1.0) [P] | not found |
| Interdependence / repeatability | medium / runs [I] | medium / runs [I] |

**Design**
- **Loop.** Demonologist: investigate, identify, exorcise; money upgrades a safe house; many maps; speech recognition ("one word you say can open a secret door") [P]. Mortuar: 2 locations; equipment, a journal and a ritual [P].
- **Readable goal.** Demonologist: the goal is found by reading the tablet about 2 to 4 min in [T/M]. Mortuar (solo videos only): "this game has not told me anything about what I'm meant to do", and the player quit after one round [T/M].
- **Dead players.** Demonologist: the dead can eliminate evidence on the tablet, and voice with the dead was cut and then restored via the Spirit Box [P]. Mortuar: not found.

**Execution.** Tech failure is 18.5% vs 31.3% [S]. Mortuar's median playtime at review is 0.4 h, with 95.5% of reviews under 2 h [S].

**Launch path**
- **Demonologist.** Announced Dec 2022 under another name [T]. Demo 2023-02-06, the first day of that Next Fest [P/I]. EA 2023-03-27; 1.0 2023-09-25 [P].
- **Mortuar.** Release 2024-07-09, free, 1 news post [P]. A likely student or hobby team of 3 [I].
- **Follower?** Both follow Phasmophobia by about 2.5 and 3.5 years. Mortuar launched 16 months after Demonologist [P].

**Price.** $19.99 vs free [P]. The expensive game won.

**Updates.** 58 vs 1 news items [P]. Demonologist kept adding maps; its 2026 v2.0.0 visual overhaul lifted players 65% [T].

**What reviewers say.** Demonologist: horror 42.2%, monsters 25.6%, atmosphere 18.7% of codable positives [S]. Its negatives are now dominated by AI art (34.6% of codable negatives) after a late disclosure on 2026-11-05 [P/S]. Mortuar: bugs 17.5% and performance 10.0% of codable [S]; "no tutorial" [S quote].

**What most plausibly made the difference**
1. **Production value and content volume** (evidence-backed). UE5 visuals, many maps and steady updates, against 2 locations and one patch.
2. **A readable goal** (evidence-backed, from weak solo videos plus reviews).
3. **Pre-launch path** (plausible). An announcement, a demo at Next Fest, then EA.
4. **Price** (evidence against).

**What cannot be separated.** Little luck is involved. Demonologist had no viral moment found [P]; it grew on genre demand. This pair shows that a follower can succeed with depth and polish.

---

## P11 WEBFISHING vs A Game About Penguins (hit vs flop)

**Shared idea.** A cute-animal hangout: friends fish, chat and play minigames with no fail state.

| | WEBFISHING | A Game About Penguins |
|---|---|---|
| Stratum | hit | flop |
| Release (first) | 2024-10-11 [P] | 2026-08-10 [P] |
| Early Access (store lists EA now) | no [P] | no [P] |
| Price (list, USD) | 4.99 [P] | 9.99 [P] |
| Max players | unknown [L1] | unknown [L1] |
| Camera | third [I] | unknown [I] |
| Demo on store | no [P] | no [P] |
| Next Fest | none found | Feb 2026 [D] |
| Publisher | self [P] | Ultimate Publishing|Ultimate Games S.A.|PlayWay S.A. [P] |
| Team | 1 (solo) [T] | ~3 named [D] |
| Reviews | 70,549 [P] | 52 [P] |
| % positive | 97.3 [P] | 94.2 [P] |
| Median h at review (all / pos / neg) | 14.2 / 14.8 / 10.2 [S] | 2.3 / 2.4 / 1.5 [S] |
| Reviews <2 h / >10 h / >50 h (%) | 6.2 / 60.3 / 15.1 [S] | 42.3 / 11.5 / 0.0 [S] |
| Top language (share %) | english (87.6) [P] | english (48.1) [P] |
| China share of reviews % | 0.5 [P] | 15.4 [P] |
| SteamCharts all-time peak | 23,966 [T] | n/a [T] |
| Month-1 / month-6 avg players | 9,960 / 809 [T] | n/a / n/a [T] |
| m6/m1 | 0.08 [I] | n/a [I] |
| Current players (2026-11-10/11) | 254 [P] | 0 [P] |
| Steam news items (patch notes) | 14 / 5 [P] | 41 / 9 [P] |
| Top praise theme (% of codable positives) | relaxing_chill (27.1) [S] | fun_with_friends (38.3) [S] |
| Top complaint theme (% codable) | dev_abandoned_no_updates (5.8) [S] | connection_lobby_host (6.0) [S] |
| Technical-failure mentions % | 12.9 [S] | 10.0 [S] |
| Refund mentions % | 0.1 [S] | 0.0 [S] |
| Codable reviews (n) | 890 [S] | 50 [S] |
| Top Twitch clip views | 17,700 [P] | not collected |
| Top mod downloads | 86,602 [P] | not collected |
| Proximity voice | no (mod adds it) [I] | unknown [L1] |
| Solo | yes, pointless [P] | yes; solo players nudged to online rooms [D] |
| Public lobbies | yes, by design [P] | yes [D] |
| Dead/waiting player | n/a; chat while waiting for a bite [T] | n/a |
| Interdependence / repeatability | low / sandbox [I] | low / sandbox [I] |

**Design**
- **Loop.** WEBFISHING: a small camp, a fishing minigame, cosmetics, chat, guitar and chalk; designed for strangers ("a chatroom-focused fishing game") [P]. A Game About Penguins: sliding, swimming, 98 fish, quests, house decorating, minigames, racing and arcade games [P]. That is more content and more systems.
- **Social density.** WEBFISHING lobbies hold up to about 12 [T] and are meant for strangers [P]. Penguins added a v1.0.3 system "that encourages players in solo sessions to join existing online rooms" [D], which signals empty lobbies [I].
- **Dead players.** n/a in both. WEBFISHING's wait for a bite is chat time [T].

**Execution.** Tech failure is 12.9% vs 10.0% [S]. Penguins is not worse built; its 52 reviews are 94.2% positive [P].

**Launch path**
- **WEBFISHING.** A remake of a 2022 itch.io jam game; Steam page in Aug 2024; release 2024-10-11; no demo or Next Fest [P/T]. It went viral within days on TikTok and Twitter (movement tech and guitar "concerts") [T]. Solo developer [T].
- **Penguins.** Made in Türkiye festival (Nov 2025), Next Fest Feb 2026, free prologue Jul 2026, 1.0 on 2026-08-10 via PlayWay's Ultimate Publishing [D/P]. Launch peak about 25 CCU [P].
- **Follower?** Yes, 22 months later [P].

**Price.** $4.99 vs $9.99 [P]. The flop costs twice as much, for a game whose value depends on other people being in the lobby [I]. Its free prologue may also have absorbed demand [I].

**Updates.** 14 vs 41 news items [P]. WEBFISHING stopped posting in Jan 2025 [P] and "developer abandoned" is now its top complaint (5.8% of codable) [S]. Penguins patched about 15 times in its first month with no lift [T].

**What reviewers say.** WEBFISHING: relaxing 27.1%, atmosphere 16.5%, fun with friends 14.4%, fun with strangers 12.2% of codable positives [S]; it is the only pair game where strangers are a top-5 praise. Penguins: fun with friends 40.4%, relaxing 31.9% [S]. Reviewers like it, but there are few of them.

**What most plausibly made the difference**
1. **A hangout needs a crowd: first mover took the crowd** (plausible, strongly suggested). WEBFISHING's value is the population; a later, emptier copy cannot offer that.
2. **Price for a social space** (plausible). $9.99 against $4.99.
3. **One readable, shareable gimmick** (plausible). Cat/dog avatars, a guitar and movement tech made clips; Penguins' feature list is broader but less distinct [I].
4. **Updates** (evidence against as a launch factor). The flop updated more.

**What cannot be separated.** WEBFISHING's organic TikTok wave and population advantage.

---

## Cross-pair synthesis: which differences recur

Counted over 11 pairs. Weak matches (P04) and hit-vs-mid pairs (P06, P08) are marked.

1. **The hit always launched first; every comparison game is a follower (11 of 11)** [P dates]. The gaps range from 3.5 months (Cargo Duty) to 25 months (Don't Pull Me!). In 2 cases the follower's concept predates the hit (Treasure Hunters [D]; Sunset Summit started in 2021 [D]), but both shipped after it. This is a selection artefact of building pairs around hits, so it **cannot be used as evidence that being first wins**. It does mean that design effects are always confounded with first-mover advantage. P10 is the counter-example: a follower (Demonologist) can win on depth.
2. **The hit had a dated viral moment the comparison game lacked (10 of 11; not P10)** [T/D]. Hits had none of the formal pre-launch route: no demo or Next Fest for PEAK, Lethal Company, R.E.P.O., RV, Supermarket Together, Liar's Bar, Content Warning, Mage Arena or WEBFISHING [P]. Only Demonologist shows a Next Fest-timed demo [I]. **Comparison games used festivals more:** Next Fest confirmed or likely for 7 of 11 (Treasure Hunters, Drive Together, Out of Stock!, Bogos Binted?, Super Shout Showdown, Penguins, Don't Pull Me! [P/D/I]). Festivals and demos did not substitute for a viral moment (evidence-backed). Three comparison games had real creator coverage that did not convert: Treasure Hunters at 1.29M YouTube views [P], Out of Stock!'s 20k Next Fest players [D], Drive Together's 20k wishlists [D].
3. **Execution failures cluster in the flops, especially online sync (8 of 11)** [S]. The comparison game has higher technical-failure mentions in 8 pairs: P01, P03, P04, P05, P07, P08, P09, P10. The exceptions are P02 (the flop is simply shallow), P06 (the mid is more polished) and P11 (both are fine). The worst cases are netcode in physics- or online-coupled games: Out of Stock! at 71% and Don't Pull Me!'s desync (evidence-backed).
4. **Readable goal and comedy from failure in the first minutes (strong in P02, P03, P07, P10; null in P09; untested in P01, P05, P11)** [T/M]. Hits make the first failure funny and legible: a valuable breaks, a friend drags you down, a revolver fires. Weak games leave players unsure of the point ("this can't be the whole game"; "has not told me anything"). This holds for the clearly weaker followers. In P09 it does not separate the games (plausible overall).
5. **Price is not a consistent lever (evidence against).** The cheaper game lost in P01, P02, P04 and P10. The pricier game lost in P05 (free vs $6.99), P09 ($2.99 vs $7.99) and P11 ($4.99 vs $9.99) [P]. Price seems to matter only where the hit was free or an impulse buy and the follower asked more for a thinner or emptier experience (plausible).
6. **Updates separate retention, not launch (evidence-backed for retention, against for launch).** The comparison game posted more updates in P08, P09 and P11 and still lost [P]. Among hits, updates lift players (PEAK, R.E.P.O., RV, Lethal Company, Supermarket Together [T]). Hits that stopped updating decay steepest (WEBFISHING 0.08, Mage Arena 0.03 m6/m1 [I]). See the Retention sheet in `Deep_study_comparison.xlsx`.
7. **Social failure states and something to do while dead (plausible).** PEAK, R.E.P.O. and Lethal Company give the dead or downed a role (carry, revive, possession, spectate and talk) [P/D/T]. Their comparison games mostly use instant respawn or "not found". The direction is consistent, but the data on dead-player activity is thin for flops.
8. **A single image that explains itself to a viewer (plausible).** Chain, revolver, fragile cart, voice spell, a camera filming your friends. The losing game often has more systems but a less instantly legible hook (Bogos Binted?, Penguins, Super Shout Showdown) [I].

**What the pairs cannot tell us.** Every hit benefited from first-mover advantage and at least one stroke of streamer or TikTok luck (or a stunt: Content Warning's free day, RV's leaked page). These cannot be separated from design in any pair. Flop samples are tiny (38 to 147 codable reviews [S]), and first-session videos are missing for 3 flops (P01, P05, P11) and solo-only for P10 [T/M]. **Weak matches:** P04 matches only the shared-vehicle mechanic. P06 and P08 are hit vs mid, so they show a follower's ceiling, not a failure. P08's filming is a side system in the mid. P05 differs in camera and pacing.
