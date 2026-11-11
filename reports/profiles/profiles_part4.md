# Deep-study game profiles, part 4 (batches 7 and 8, 20 games)

Compiled 2026-11-11 from existing sources only (no new web research): `deep_profiles_batch_7.md`, `deep_profiles_batch_8.md`, `data\deep_study_numbers.csv`, `data\deep_study_selection.csv`, `data\deep\{appid}\summary.md` / `themes.md` / `themes.json`, `layer2_review_themes.md`, `layer2_tooling_method.md`.

**Tags.** [P] verified primary (Steam store/news/review API, review histogram, Steam current-player API, developer's own Steam post or store text as a record that it was posted). [D] developer claim (what the developer asserts: sales, wishlists, intentions). [T] third-party (SteamCharts, press, wikis, Wayback). [I] inference. [S] computed from the review sample (n given).

**Read these caveats before using the numbers.**
- Review sample: games with >1,000 reviews = 500 newest + 500 most-helpful (not random); smaller games = census. Playtime is *at review*, not session length. Helpful stratum leans to launch-window and joke reviews.
- Theme counts are multilingual keyword matches (micro precision about 0.77-0.86, recall 0.66-0.90). Complaint themes are counted on all reviews, so positives that *mention* a word (e.g. "bug and fossil hunting") inflate them; the "neg" count is the safer read. P09 Simple and P17 Unique over-count. German, French, Portuguese and Turkish recall is low. Jokes are coded literally.
- Review histogram counts are about 80-86% of the all-language total; use them for shape only. Games under about a year old come back in weekly buckets.
- SteamCharts month proxies (M1/M3/M6/M12) are the average of the calendar month(s) overlapping each window, not exact windows. "(missing)" means no row for that month.
- Price history is blocked for every game (SteamDB 403, ITAD client-side, gg.deals 403). Discounts come only from developer posts and Wayback.
- Late Nov 2025 review spikes (MIMESIS, Nine-Ball Roulette, Mage Arena) and Nov 2023 (Demonologist) fall in the Steam Awards nomination window with no player rise; treat them as a platform-prompt effect [I], not growth.

---

## 1. How to Fish (4001890)
**Stratum** hit | **Pair** none | **Release** 2026-08-20, full release, no EA [P] | **Price** $7.99 (38% launch discount to 2026-08-27) [P/D] | **Players** 1-4 per store; 8-player lobbies since 1.0.4 [P] | **Dev/Pub** Dazed Games, self-published [P] | **Core type** other (fish, kill, sell, upgrade, beat bosses to reach new islands) | **Reviews** 88,339, 95.1% positive [P]

| Metric | Value |
|---|---|
| Median h at review (all / pos / neg) | 6.68 / 6.73 / 5.82 [S, n=1000/951/49] |
| <2h / >10h / >50h | 6.3% / 28.0% / 0.8% [S, n=1000] |
| Top languages | English 39.1%, Simplified Chinese 17.5%, Russian 13.7% [P] |
| SteamCharts peak | 373,887 (2026-08) [T] |
| M1 / M3 / M6 / M12 proxy | 90,533 (Aug-Sep) / 17,952 (Oct) / not yet / not yet [T] |
| Current players | 3,297 (2026-11-11) [P] |

**Core loop & inputs.** Stranded on islands, players catch fish with physics rods, kill them with knives, guns, bows and explosives (trick shots on airborne fish pay bonuses), sell them, buy gear, and beat quests and bosses to unlock islands [P]. Cooking, carrying, an in-game roulette table, text and voice chat [P].
**Dependence.** One shared host save and shared progress; teammates carry and revive downed players (picked up and slapped awake) [P/T]. Money split not documented.
**Failure & dead players.** Downed then revive/self-revive; own explosives kill even with friendly fire off [P]. Dead players lie as bodies others carry; shown as turquoise radar dots (1.0.11) [P]. No spectate or run reset documented.

**What it gets right.** Fun with friends 188 (23.7% of codable positives), funny 79, monsters/bosses 73, good value 66, simple 43 [S, n=840 codable]. >20h reviewers also cite physics chaos (4/42) [S]. Quote: "every normal plan somehow ends with someone flying through the air" [S].

**Where players push back.** Complaints are thin: too short/one-time 50 (only 5 in negatives), repetitive 48 (7 neg), bugs 29 (5 neg), difficulty 21 [S]. "It's a shame it's only a one-time experience" (positive, 7.5h) [S]. <2h reviewers: repetition 6, bugs 3, tech mentions 14% [S, n=57]. >20h reviewers: zero negatives; bugs 3 and repetition 3 in passing [S, n=42].

**Sentiment over time.** Flat 93.6-95.4% every week from launch to Nov 2026 [P]. Weekly volume fell from 21,820 up to under 1,000; the Islet update bumped the week of 2026-10-01 to 4,903 up from 3,192 [P].

**What happened after launch.** Patches 1.0.4-1.0.12 within 15 days: 8-player lobbies, private lobbies, difficulty modes, anti-griefer chat change, Steam Deck Verified, cloud saves [P]. The Islet 1.1.0 (2026-09-28) first content update plus a PEAK bundle [P]. Players: Aug avg 148,647 -> Sep 32,419 (-78%) -> Oct 17,952 (-45%) [T]. Claimed 1M "fishermen" in 2 days and 10M players in under 2 months, "players" undefined [D]. Soundtrack DLC coming; Makeship plush; no cosmetics DLC [P].

**Launch path & team.** 2022 one-month jam game ("shoreline" theme), shelved about 3 years, revived after Out of Hand: Deluxe did poorly [D]. Viral X trailer 2025-11-27, about 9 months before release [D/I]; steady TikTok posting raised wishlists [D]; release date announced a week out added "tens of thousands" of wishlists [D]. No demo, playtest or Next Fest [P]. About 90k wishlists (estimate) [T]. Two Swedish co-founders plus music and sound; Unity, Steam P2P [D]. Possible Landfall support, single source [T]. Developer: "What we care most about in game-making is play feel" [D, translated].

**Unknowns.** Session length, money split, price history, real sales (player milestone undefined), Landfall's role, whether public lobbies were griefed (only implied) [I].

---

## 2. Demonologist (1929610)
**Stratum** hit | **Pair** P10 (Phasmophobia-like investigation) | **Release** EA 2023-03-27, 1.0 2023-09-25 (unannounced) [P] | **Price** $19.99 (EA price not found) [P] | **Players** 1-4 [P] | **Dev/Pub** Clock Wizard Games (Istanbul), self-published [P/T] | **Core type** investigation | **Reviews** 24,621, 84.8% [P]; last 30 days 61% of 210 [P]

| Metric | Value |
|---|---|
| Median h at review (all / pos / neg) | 9.37 / 9.23 / 9.67 [S, n=1000/767/233] |
| <2h / >10h / >50h | 11.7% / 48.2% / 10.4% [S] |
| Top languages | English 55.7%, Russian 10.9%, German 6.8% [P] |
| SteamCharts peak | 8,693 (2023-04) [T] |
| M1 / M3 / M6 / M12 proxy | 3,839 / 1,527 / 1,045 / 419 [T] |
| Current players | 188 [P] |

**Core loop & inputs.** Investigate a cursed location with ghost tools (EMF, ESG, Ouija, voodoo doll, salt, cameras, tarot), identify the spirit type, exorcise it; money upgrades the safe house [P]. Speech recognition reacts to spoken words ("manifest", "show yourself"); proximity voice since v2.1.0; emotes [P].
**Dependence.** Shared evidence and a ghost-type vote; timed exorcism sequences [P].
**Failure & dead players.** Ghost kills during hunts; only revive is the Angel tarot card [T]. Dead players can open the tablet and eliminate evidence but not pick the ghost [P]. Dead-living voice: added 2023, cut June 2026, restored via Spirit Box Oct 2026 [P].

**What it gets right.** Horror/tension 295 (42.2% of positives), monsters 179, atmosphere 131, fun with friends 124, value 50 [S, n=919 codable]. "Playing with friends is like watching Scary Movie 2." (44.5h) [S].

**Where players push back.** Bugs 116 (49 neg), repetitive 92 (35 neg), AI-generated art 81 (76 neg), clone/asset-flip 52 (32 neg), performance 47 [S]. Tech mentions 18.5%, refund mentions 28 [S]. "Use of AI art for a lot of 2D art" [S]. <2h: asset-flip 8 and AI art 6, nearly all negative [S, n=104]. >20h: bugs 48 (18.5%), AI art 30, crashes 20; "The game also is almost unplayable in multiplayer." (103h) [S, n=259].

**Sentiment over time.** 91-93% in spring 2023, dipping to 69-70% in Dec 2023-Jan 2024 around Nightmare difficulty [P]. Nov 2023 spike (2,025 up) is the awards-window pattern [I]. Mostly 75-85% through 2025-26 [P]. Nov 2026 (to the 11th) 35 up / 52 down, 40.2%, the first net-negative month, after a 2026-11-05 "Regarding AI Usage" disclosure [P].

**What happened after launch.** Steady content: maps (Kurosawa, Bedlam, Deadwood, Haunted School, Funeral Home), hiding, Nightmare mode [P]. Players halved by May 2023 then decayed; recurring July and October bumps align with Summer Sale and Halloween [I]; Jan 2025 +78% unexplained [T]. v2.0.0 (UE 5.6, Jan 2026, +65%), v2.1.0 (Oakville, emotes, outfits for purchase, likely in-game currency [I]), v2.3.0 Halloween [P]. Makeship plush [P].

**Launch path & team.** Announced 2022-12 as "The Shivers" [T]. Demo 2023-02-06, likely Feb Next Fest [P/I]. EA about 8,000 concurrent in week 1 [T]. Founders Furkan Sak and Volkan Demir; founding date conflicting (2021 vs 2014) [T]. UE5. A second team makes Night Club Simulator [D]. On voice tech: "there are some technical limitations with current solutions" [D].

**Unknowns.** Wishlists, viral moment, EA price, discount history, team size, dev time, interviews, cause of Jan 2025 rise.

---

## 3. MIMESIS (2827200)
**Stratum** hit | **Pair** none | **Release** EA 2025-10-27, still EA [P] | **Price** $9.99 [P] | **Players** 4 recommended (tested 2-5) [P/D] | **Dev/Pub** ReLU Games (KRAFTON subsidiary) / ReLU + KRAFTON [P] | **Core type** extraction | **Reviews** 10,887, 84.5% [P]

| Metric | Value |
|---|---|
| Median h at review (all / pos / neg) | 4.43 / 4.62 / 2.97 [S, n=1000/822/178] |
| <2h / >10h / >50h | 19.3% / 20.7% / 1.4% [S]; 37.1% of negatives <2h |
| Top languages | Russian 34.5%, English 25.0%, Korean 7.8% [P] |
| SteamCharts peak | 8,254 (2025-11) [T] |
| M1 / M3 / M6 / M12 proxy | 2,688 / 2,050 / 867 / 435 [T] |
| Current players | 254 [P] |

**Core loop & inputs.** Ride a tram into buildings, grab scrap, return before midnight rain; AI "Mimesis" copy teammates' looks, behaviour and voice lines [P]. Microphone required; compass, paint gun, puppy, recording device; host kick [P].
**Dependence.** Shared tram, quota, host save and trust. Solo survival 6.6% vs 53.6% with four [D]; 63,142 teammate kills "on suspicion" [D].
**Failure & dead players.** Since 2026-06-15 all four down = game over, no next day [P]. Dead players spectate and, since 2026-03/06, possess a nearby Mimesis and speak through it [P].

**What it gets right.** Fun with friends 198 (27.4%), monsters 148, horror 89, funny 85, potential 61 [S, n=893]. "Me and my friends used a jump and an emote to spot the fake." [S].

**Where players push back.** Repetitive 71 (25 neg), bugs 41 (24 neg), asset-flip 41, too short 38, AI art 36 (25 neg), difficulty 34 [S]. "becomes extremely stale fast" (1.2h) [S]. <2h: bugs, repetition, AI art and asset-flip 11 each [S, n=176]. >20h: "update made it worse" 5 is top, tied to scrap changes [S, n=53].

**Sentiment over time.** Launch weeks 73-79% [P]. Week of about 2025-11-24: 2,064 up / 70 down, the awards-window pattern [P/I]. 75-89% through 2026; Off the Rails week 126/16 (89%), early Nov 2026 91-100% [P].

**What happened after launch.** Save/load (11-12) and public lobby with join-in-progress (11-27) were the top requests [P]. Two 20% sales in Dec; Japanese Hololive streams late Nov-Dec [T]; Japan top streaming and sales country [D]. Feb 2026 -45%; rises in Mar (+23%, Lab/possession), Jun (+62%, rework and 30% sale), Oct (+42%, "Off the Rails", peak 3,604) [T/P]. Sales over 1M by 2025-12-19 [D], 2.1M by Aug 2026 [T]. No paid cosmetics; KADOKAWA merch [P].

**Launch path & team.** Pivoted from a 3v3 extraction prototype that "wasn't fun"; pivot driven by data that co-op was 6% of 2023 releases but 36% of units [D]. Wishlists 10k to 100k in 40 days [D]; June 2025 Next Fest, 4th most-played demo [D]. Developer: "brutal feedback… it stung. A lot." [D]. ReLU has 51 staff [D]; small in-house neural nets, not an LLM [D]. Likely Unity [I]. On EA: "content was not sufficient" [D, translated].

**Unknowns.** MIMESIS team size, engine (confirmed), total dev time, KRAFTON marketing role, session length (about 22 min per demo tram is [I]), 1.0 date.

---

## 4. Nine-Ball Roulette (3376250)
**Stratum** mid | **Pair** none | **Release** EA 2025-01-14, 1.0 2025-12-05 [P] | **Price** $3.99 [P] | **Players** 2-4 [P] | **Dev/Pub** WaveBox Labs, self-published [P] | **Core type** versus | **Reviews** 2,482, 88.2% [P]

| Metric | Value |
|---|---|
| Median h at review (all / pos / neg) | 5.69 / 6.11 / 3.06 [S, n=1000/878/122] |
| <2h / >10h / >50h | 17.6% / 31.3% / 6.1% [S]; 44.3% of negatives <2h |
| Top languages | Simplified Chinese 41.7%, English 21.0%, Brazilian 20.8% [P] |
| SteamCharts peak | 2,146 (2025-02) [T] |
| M1 / M3 / M6 / M12 proxy | 442 / 369 / 165 / 347 [T] |
| Current players | 148 [P] |

**Core loop & inputs.** Turn-based pool; a foul sends you to a revolver (Russian roulette), last alive wins; 9/6/4-ball and 8-ball arena [P]. Aim, power, spin, jump and masse shots, walking, voice and text chat, table ping, emotes [P].
**Dependence.** One table: your shot sets up the next player [P].
**Failure & dead players.** Elimination by revolver. Developer: "some players are very bored during the long wait after premature death" [D]; answered with First Blood mode (Mar 2025) and ghost spectators who can mark the table (Sep 2025) [P].

**What it gets right.** Fun with friends 131 (20.3%), potential 34, value 32, visuals 30, funny 27 [S, n=748]. "for the price being offered, this is an excellent multiplayer pool game" [S].

**Where players push back.** Low complaint load: bugs 36 (12 neg), performance 26, repetition 16, difficulty 11, crashes 10 [S]. "Super buggy." (0.2h) [S]. <2h: bugs 14, performance 7, tech 14.8% [S, n=162]. >20h: lobby-join bugs and dead-time; "Please add something for dead players" (27.3h) [S, n=113].

**Sentiment over time.** 71-82% in launch weeks, rising to 86-100% by Mar-Jul 2025 with near-daily patches [P]. Aug 2025 dip to 55-57% on tiny volume [P]. Week of about 2025-11-24: 274 up / 2 down, awards-window pattern [P/I]. 1.0 weeks 67/14, 55/8 [P].

**What happened after launch.** About 100 developer posts in 22 months [P]. Players: 505 in Feb 2025, -51% in Apr, slide to 115 by Nov; 1.0 lifted Dec 2025 to 382 (+232%); Mar 2026 341 [T]. VAC after cheaters, reporting after abuse [P]. 1.0 free with no price rise at launch [D]. Bundle with Soccer in a Box; cue skins earned in-game [P]. Next game Mafia Deal announced 2026-11-06 [P].

**Launch path & team.** Pre-EA test phase, EA announced only 5 days ahead [P]. Prior game Soccer in a Box [D]. Possibly China-based [I, weak].

**Unknowns.** Team size, location, engine, wishlists, Next Fest, viral cause of the Chinese and Brazilian audience, session length.

---

## 5. BACKROOMS NO RETURN: Prologue (2866360)
**Stratum** mid | **Pair** none | **Release** 2024-08-09 [P] | **Price** free (prologue to unreleased paid game, app 2216840) [P] | **Players** single-player and co-op; max not found [P] | **Dev/Pub** FriedGPU [P] | **Core type** escape_survival | **Reviews** 1,232, 32.2% [P]

| Metric | Value |
|---|---|
| Median h at review (all / pos / neg) | 0.43 / 0.48 / 0.43 [S, n=1000/353/647] |
| <2h / >10h / >50h | 97.3% / 0.3% / 0% [S] |
| Top languages | Russian 63.4%, English 24.9%, Ukrainian 2.1% [P] |
| SteamCharts peak | not found (no page) |
| M1 / M3 / M6 / M12 proxy | not found |
| Current players | 3 [P] |

**Core loop & inputs.** Scientists explore the Poolrooms, solve puzzles, escape creatures [P]. Proximity voice, host/join lobbies [P]. Other inputs not documented.
**Dependence.** not found. **Failure & dead players.** not found.

**What it gets right.** Horror 51 (17.2% of positives), atmosphere 43, potential 33, fun with friends 31 [S, n=880]. "creates fear through atmosphere and uncertainty" [S].

**Where players push back.** Performance 159 (112 neg), bugs 88, too short 81, lag 44, controls 27 [S]. Tech mentions 30.6% [S]. "CHANGING THE SOUND BROUGHT MY GAME TO 5 FRAMES A SECOND" [S]. "no gameplay, no atmosphere, and only one cheap jump scare" [S]. Almost every reviewer is <2h (n=858 codable); no >20h reviews.

**Sentiment over time.** Launch month 131/476 (21.6%) [P]. Never sustainably above 50% except Nov 2024 (48/23) and Dec 2025 (10/5) [P].

**What happened after launch.** Two developer posts: 2024-08-11 apology ("this is not the final version") and a performance fix [D/P]. No further updates. Forum mostly Russian teammate searches [P].

**Launch path & team.** Main-game demo 2023-03-10; prologue 2024-08-09; full game "coming soon", planned EA [P/T]. UE5 [P].

**Unknowns.** Player history, player cap, team, location, Next Fest, wishlists, conversion to the main game.

---

## 6. The Anomaly Project (2960770)
**Stratum** mid | **Pair** none | **Release** EA 2024-07-24, 1.0 2024-11-21 [P] | **Price** $7.99 [P] | **Players** 1-8 [P] | **Dev/Pub** Kekdot (solo), self-published [D/P] | **Core type** asymmetric_information (spot anomalies) | **Reviews** 658, 81.2% [P]

| Metric | Value |
|---|---|
| Median h at review (all / pos / neg) | 3.23 / 3.46 / 1.58 [S, census n=658/534/124] |
| <2h / >10h / >50h | 26.1% / 5.0% / 0% [S]; 57.3% of negatives <2h |
| Top languages | English 71.1%, Turkish 14.1%, German 2.9% [P] |
| SteamCharts peak | 195 (2025-08) [T] |
| M1 / M3 / M6 / M12 proxy | not found (Jul-Aug 2024 missing) / 3.2 / 16.1 / 17.9 [T] |
| Current players | 7 [P] |

**Core loop & inputs.** Walk a level, find the anomaly, everyone picks Red or Green tube; wrong resets to level 1, escape at level 10 [P]. Proximity voice and text chat, magnifier, lobby Plinko, outfit shop [P].
**Dependence.** One group decision per level from pooled observations [I].
**Failure & dead players.** Reset to level 1; chasing-clown maps exist [P]. Dead players not documented.

**What it gets right.** Fun with friends 133 (28.8%), horror 102, value 42, potential 42, funny 24 [S, n=581]. "works really well whether you're jumping in with friends or playing with strangers" [S].

**Where players push back.** Too short 65 (13 neg), repetitive 37 (20 neg), asset-flip/lazy 21 (20 neg), AI art 16 (15 neg), price 10 [S]. Tech mentions only 3.3% [S]. "only has four maps… all of which get very repetitive" [S]. <2h: repetitive 11, asset-flip 9 [S, n=159]. >20h: 2 reviews; "the story mode is so short" [S].

**Sentiment over time.** 91% Aug 2024, 61-62% Nov-Dec 2024, back to 88-90% Jan-Feb 2025, then 72-100% on small monthly volume [P].

**What happened after launch.** Maps every few weeks in 2024 (Stairs map later demoted as unenjoyed [D]); shop and visual overhaul; 1.0; leaderboards; Storage map; Barny's Playground Ch. 2 [P]. Sales 15-25% [D]. Players rose to 24 (Feb 2025) after 1.0 and sales; Aug 2025 46.5 (+233%) with no update, maybe a YouTuber video [T/I]. 2026 decline as the developer moved to Anomaly Company [P]. "In-App Purchases" category listed, real-money status unclear [P/I].

**Launch path & team.** Big YouTubers on the store list (SMii7Y, VanossGaming, Forsen, Yogscast); "over 40 million views combined" [D]. Likely Unreal [I].

**Unknowns.** Creator video dates, Next Fest/demo, wishlists, location, dead-player rules, Aug 2025 spike cause.

---

## 7. WHERE the F$CK is my BITCOIN (4705620)
**Stratum** flop | **Pair** none | **Release** 2026-06-13 [P] | **Price** $6.99, 40% off ($4.19) on 2026-11-11 [P] | **Players** solo or co-op; max not found [P] | **Dev/Pub** Bin Juice Games / Vibes Only Interactive [P] | **Core type** other (dig trash, sell, upgrade) | **Reviews** 120, 58.3% [P]

| Metric | Value |
|---|---|
| Median h at review (all / pos / neg) | 1.37 / 1.97 / 0.74 [S, census n=120/70/50] |
| <2h / >10h / >50h | 65.8% / 0.8% / 0% [S]; 88% of negatives <2h |
| Top languages | English 62.5%, Russian 13.3%, German 6.7% [P] |
| SteamCharts peak / proxies | not found (no page) |
| Current players | 1 [P] |

**Core loop & inputs.** Dig trash piles by hand, sort and sell, upgrade hands, bags and stamina to reach dirtier dumps while hunting a lost Bitcoin; "Split the loot, or 'accidentally' grab the shiny thing first" [P]. Inputs not documented.
**Dependence.** Loot split only [P]. Players report no save; each co-op session restarts [P forum]. **Failure & dead players.** none documented.

**What it gets right.** Progression/upgrades 10 (14.5% of positives), value 9, visuals 6, fun with friends 5 [S, n=118]. "I traded a bag of tin cans to upgrade my shovel" [S].

**Where players push back.** Too short 16 (11 neg), repetitive 9, bugs 7, price 7, asset-flip 6 (all neg) [S]. "Not enough content, 100% solo in 38 minutes." [S]. "Lazy & buggy asset flip and copying another game" [S]. All reviewers are <2h or a little more; none >20h. Forum: "AI Asset Flip" accusation naming a near-identical dump game [P player claim, unverified].

**Sentiment over time.** Launch week 70/19 (79%), then 1/6, 0/2 and near-zero weekly volume, mostly negative [P].

**What happened after launch.** Only the launch post; no patches [P]. 40% discount by Nov 2026 [P].

**Launch path & team.** Publisher is the only effort signal [P]. No web presence found for either company.

**Unknowns.** Team, engine, announcement, demo, player cap, sales, player history.

---

## 8. Don't Pull Me! (4423110)
**Stratum** flop | **Pair** P07 (Chained Together-like) | **Release** 2026-07-31 [P] | **Price** $4.99 [P] | **Players** 1-4 online [P] | **Dev/Pub** Komplo Games, self-published [P] | **Core type** climbing_traversal | **Reviews** 78, 74.4% [P]

| Metric | Value |
|---|---|
| Median h at review (all / pos / neg) | 2.36 / 3.18 / 1.41 [S, census n=78/58/20] |
| <2h / >10h / >50h | 43.6% / 5.1% / 0% [S]; 75% of negatives <2h |
| Top languages | English 43.6%, Simplified Chinese 14.1%, Turkish 10.3% [P] |
| SteamCharts peak / proxies | not found (no page) |
| Current players | 29 [P] |

**Core loop & inputs.** Players tied by rope climb, swing and carry objects through physics parkour maps; one bad move drags the team [P]. Move, climb, swing, grab, punch, voice chat, customization; level-time leaderboards [P].
**Dependence.** The rope is the physical link. **Failure & dead players.** not documented (falling presumably drags the team back [I]).

**What it gets right.** Fun with friends 13 (24.1%), funny 11, value 7, rage-as-fun 4 [S, n=72]. "I haven't laughed this hard at a game in a long time." [S].

**Where players push back.** Bugs 12 (8 neg), lag/desync 3, difficulty 2 [S]; tech mentions 22.2% [S]. "4-player is literally unplayable." [S]. "the Desyncing is very bad" [S]. <2h: bugs 5, all negative [S, n=29]. No >20h reviews. Forum: unmet local couch co-op demand; friend-invite failures [P].

**Sentiment over time.** Weekly 25-100% on single-digit volume in Aug 2026, about 50% in September, fewer than 7 a week since [P].

**What happened after launch.** No developer posts [P]. On couch co-op the developer said "i dont think i can :(" [D]. DLC count 1 (content not described) [P].

**Launch path & team.** Demo 2026-06-14, consistent with June Next Fest [P/I]. 16 languages [P].

**Unknowns.** Team, location, engine, wishlists, failure rules, DLC content, player history.

---

## 9. Co-op Kaiju Horror Cooking (3139570)
**Stratum** flop | **Pair** none | **Release** 2025-07-29 [P] | **Price** $7.99 (40% launch discount, $4.79) [P/D] | **Players** 2-4 "or more"; solo and strangers supported [P] | **Dev/Pub** Strange Scaffold / Strange Scaffold + Frosty Pop [P] | **Core type** shared_object | **Reviews** 43, 74.4% [P]

| Metric | Value |
|---|---|
| Median h at review (all / pos / neg) | 2.13 / 2.73 / 1.28 [S, census n=43/32/11] |
| <2h / >10h / >50h | 46.5% / 7.0% / 0% [S] |
| Top languages | English 90.7%, Russian 2.3%, Polish 2.3% [P] |
| SteamCharts peak / proxies | not found (no page) |
| Current players | 0 [P] |

**Core loop & inputs.** Monk-chefs gather ingredients in a shifting labyrinth, avoid enemies, cook and catapult food into a kaiju's jaws; 13 levels, 10 minutes each [P]. Pick up/throw, traps, molotovs, proximity voice, Gregorian chanting with selectable voices [P].
**Dependence.** One meal, shared ingredients and timer; dynamic difficulty by player count [P].
**Failure & dead players.** Failed level; dead players leave a recoverable "heart" (implies revive [I]) [P].

**What it gets right.** Fun with friends 13 (44.8%), monsters 5, potential 5, funny 3 [S, n=40]. "10/10 game, would sacrifice my friends again" [S].

**Where players push back.** Bugs 8 (5 neg), difficulty 3, crashes 2, too short 2 [S]; tech mentions 30% [S]. "too easy to get one shot or obliterated, pinned against a wall" [S]. Playtest pair found the timer too tight: "It often felt like we were just barely scraping by" [P forum]. Forum: co-op and proximity voice broken threads [P]. No >20h reviews.

**Sentiment over time.** Launch week 12/1, then 0-3 a week, negative-leaning in Sep 2025 [P]. No update moved reviews.

**What happened after launch.** Weekly content to Oct 2025: tools, levels, endless mode, Versus mode; "Play with the devs" Jun 2026 [P].

**Launch path & team.** Announced and open playtest 2025-07-16, release 13 days later [P/T]. Strange Scaffold's first co-op game, part of a rapid release cadence; founder Xalavier Nelson Jr. [T]. Probably Unity [T, not confirmed].

**Unknowns.** Team size, dev time, sales, Frosty Pop's role, why it underperformed (no postmortem), player history.

---

## 10. We Escape Together (3762430)
**Stratum** flop | **Pair** none | **Release** 2026-01-19 [P] | **Price** $0.99 [P] | **Players** exactly 2, co-op only, microphone required [P] | **Dev/Pub** 1 bit dreams [P] | **Core type** puzzle_platformer | **Reviews** 13, 0% [P]

| Metric | Value |
|---|---|
| Median h at review (all / pos / neg) | 0.68 / none / 0.68 [S, census n=13/0/13] |
| <2h / >10h / >50h | 84.6% / 0% / 0% [S] |
| Top languages | English 69.2%, Russian 30.8% [P] |
| SteamCharts peak / proxies | not found (no page) |
| Current players | 0 [P] |

**Core loop & inputs.** Two kidnapped players solve communication puzzles and parkour through a construction site, island and cave [P]. Communication device, dance emote [P].
**Dependence.** Communication puzzles need both players [P]. **Failure & dead players.** not found.

**What it gets right.** No positive reviews [P].

**Where players push back.** Bugs 4, crash 1, price 1, unclear clues 1, missing settings 1 [S, n=13]. "it softlocks on the second level with the lever" [S]. "after 15 minutes we gave up" (unclear clues) [S]. Nearly all reviewers <2h.

**Sentiment over time.** 1-2 negative reviews per week from Jan to Sep 2026 [P].

**What happened after launch.** No developer posts [P]. Forum: menu and level-2 bugs, missing key bindings [P].

**Launch path & team.** Demo 2025-05-26, release 2026-01-19 [P]. Seven languages including Turkish [P].

**Unknowns.** Everything else: team, engine, session length, sales.

---

## 11. WEBFISHING (3146520)
**Stratum** hit | **Pair** P11 (hangout, vs A Game About Penguins) | **Release** 2024-10-11, full release, no EA [P] | **Price** $4.99, launch and now, no discount found [P/T] | **Players** about 1-12 per server [T] | **Dev/Pub** lamedeveloper (solo "West"), self-published [P/T] | **Core type** hangout_no_fail | **Reviews** 70,549, 97.3% [P]

| Metric | Value |
|---|---|
| Median h at review (all / pos / neg) | 14.22 / 14.78 / 10.2 [S, n=1000/908/92] |
| <2h / >10h / >50h | 6.2% / 60.3% / 15.1% [S] |
| Top languages | English 87.6%, Russian 3.1%, Brazilian 2.5% [P] |
| SteamCharts peak | 23,966 (2024-11) [T] |
| M1 / M3 / M6 / M12 proxy | 9,960 / 3,013 / 809 / 412 [T] |
| Current players | 254 [P] |

**Core loop & inputs.** Wander a small island camp, fish (cast, then a click-mash minigame), sell, buy rods, bait and cosmetics [P/T]. Text chat, emote keys (meow, bark, kiss), guitar with chord pages, chalk drawing, punching, metal detector [P/T]. No built-in voice; a proximity-voice mod exists [I].
**Dependence.** None mechanically; co-presence only (show-off catches, guitar "concerts", chalk art) [T]. Hosts kick, ban, block and approve joins [P].
**Failure & dead players.** No fail state, no death [P].

**What it gets right.** Relaxing/cozy 217 (27.1% of positives), visuals/audio 132, fun with friends 115, fun with strangers/community 98, potential 65 [S, n=890 codable]. "As I entered my first public lobby, I was warmly greeted with an invitation to a wedding" [S].

**Where players push back.** Developer abandoned 52 (21 neg), bugs 50 (18 neg), cheaters/hackers 36 (20 neg), griefers 35, too short 32 [S]. "it has a TON of safety issues now" [S]. Reviewers say the developer was harassed off the internet and security went unpatched (player claims, unverified) [S]. <2h: griefers 5, repetitive clicking 4 [S, n=56]. >20h: abandonment 26 is the top complaint; "no more updates… no more security updates" (118h) [S, n=353].

**Sentiment over time.** 98.5% in Oct 2024 and 98.2% in Nov 2024 (26,532 reviews, the record month) [P]; slid to the high 80s and low 90s through 2026 (88.6% Nov 2026) [P].

**What happened after launch.** Patches 1.06-1.12 up to 2025-01-01: Housecleaning Update (new items, 18+ lobbies, a "Straight" title priced at $9,999 in-game cash that drew press), Block/Boot player, Lobby Update with private lobbies and request-to-join [P/T]. Makeship plush in Jan 2025, then no developer posts [P]. Players: 10,084 in Nov 2024, -65.7% in Dec, smooth decline to 175 by Oct 2026 with no rebound [T]. The developer closed the 17k-member Discord: "I'd rather have no server, than a bad one." [D via T].

**Launch path & team.** Remake of an 8-day 2022 itch.io jam game; Steam page announced 2024-08-14 [T]. No demo or Next Fest found. Went viral within days through TikTok and Twitter clips and word of mouth [T]. Solo developer, Godot, 4-5 months of development (claims differ) [D/T]. "I figured MAYBE like 100 people would play it ever" [D via T]. "The launch product was rushed and a bit of a mess" [D].

**Unknowns.** Sales (a 1.5M claim is unsourced [T]), location, session length, wishlists, whether development has formally ended.

---

## 12. Mage Arena (3716600)
**Stratum** hit | **Pair** P09 (voice-spell versus, vs Super Shout Showdown) | **Release** EA 2025-07-24, still EA [P] | **Price** $2.99 (planned $4.99; cut "due to a large number of bugs", the raise never happened) [P/T] | **Players** up to 4v4; cap 10 since 2026-03-30; 1v1 duel mode [P] | **Dev/Pub** jrsjams (solo), self-published [P/T] | **Core type** versus | **Reviews** 20,512, 90.8% [P]

| Metric | Value |
|---|---|
| Median h at review (all / pos / neg) | 2.32 / 2.56 / 1.22 [S, n=1000/836/164] |
| <2h / >10h / >50h | 44.4% / 10.6% / 1.0% [S]; 60.4% of negatives <2h |
| Top languages | English 64.3%, Russian 9.8%, Brazilian 5.1% [P] |
| SteamCharts peak | 17,126 (2025-08) [T] |
| M1 / M3 / M6 / M12 proxy | 4,843 / 447 / 161 / 39 [T] |
| Current players | 15 [P] |

**Core loop & inputs.** Team capture-the-flag on a shuffled island: capture biomes, craft at base, find spellbook pages, take the enemy flag [P/T]. Spells are cast by speaking their names into the mic; proximity voice; WASD, sprint, crouch, recall; no controller [T].
**Dependence.** Team respawn depends on holding your flag; biome captures feed team resources [P/T].
**Failure & dead players.** Respawn while your flag stands; once it is captured, sudden death [P]. A respawn indicator exists; spectating after permanent death not found. Hot Potato mode swaps teams on death [P].

**What it gets right.** Fun with friends 87 (12.2%), funny 54, proximity/voice chat 39, unique concept 31 (upper bound), value 25 [S, n=872]. Praise shares are low because reviews are short [I]. "wizards clash by voice alone" [S].

**Where players push back.** Bugs 43 (25 neg), crashes 33, repetitive 33, developer abandoned 33 (30 neg), too short 29, dead game 24 [S]. "the game crashes every time I try to join a lobby" [S]. "in 1-3 hours it gets boring" [S]. <2h: crashes 22 lead [S, n=387]. >20h: toxicity and cheaters; "the occasional racial slur in proximity chat, and randoms making nazi flags" (99h) [S, n=30].

**Sentiment over time.** 95.3% launch week, 86-90% in Aug 2025, 75-84% by Oct [P]. Weeks of 2025-11-20/27: 1,342 and 1,023 up at 97.7% with no player rise, the awards-window pattern (later nominated "Most Innovative Gameplay") [P/T/I]. Mostly 65-90% on tiny volume through 2026 [P].

**What happened after launch.** Six patches in four days, an anti-cheat that kicked friends by mistake, the DOOM spell update (an 8.2M-view clip) [P/T]. Players: Jul 5,681, Aug 4,006, Sep 623 (-84.5%), Oct 271 [T]. Then 6.5 months of silence; the Mar 2026 update (spell pool, lobby rework, cap 10) cancelled other promised items and brought no player rise [P/T]. Aug 2026 modes "might be buggy i didnt test them that much yet" [D].

**Launch path & team.** No demo, playtest or Next Fest [P]. Viral within days on TikTok; Twitch clips (sodapoppin 88K views) [T/P]. Solo, Unity, about 18 months of development, first game [D via T]. Earns about "$1 per sale" after cuts [D].

**Unknowns.** Location, session length, wishlists, sales, Discord-only announcements, cause of the Nov 2025 review spike.

---

## 13. YAPYAP (3834090)
**Stratum** hit | **Pair** none | **Release** 2026-02-03, full release, no EA [P] | **Price** $9.99 (20% launch discount) [P] | **Players** 1-6 [P] | **Dev/Pub** Maison Bap (Vancouver), self-published [P/T] | **Core type** extraction | **Reviews** 10,494, 83.0% [P]

| Metric | Value |
|---|---|
| Median h at review (all / pos / neg) | 4.03 / 4.46 / 3.26 [S, n=1000/726/274] |
| <2h / >10h / >50h | 22.5% / 19.0% / 1.7% [S] |
| Top languages | English 46.7%, Russian 25.1%, Simplified Chinese 5.7% [P] |
| SteamCharts peak | 14,719 (2026-02) [T] |
| M1 / M3 / M6 / M12 proxy | 3,174 / 752 / 459 / not yet [T] |
| Current players | 180 [P] |

**Core loop & inputs.** Minions enter a procedural rival-wizard tower over three nights (about 8 min each, +3 min since Feb 2026), vandalise to a "Chaos" quota, avoid monsters, extract; hub shop between nights [P/T]. Spells cast by voice ("enunciation matters"), a text-wheel alternative, a hold-to-cast option; proximity chat; potions, compass, physics carrying [P/T].
**Dependence.** Shared quota and gold; leaving a body behind costs money; revive item; Lost and Found [P/T].
**Failure & dead players.** Missed quota: the giant wizard squishes everyone; a run reset is implied [T]. Dead players ragdoll and spectate; since Mar 2026 they can be heard by the player they spectate [P].

**What it gets right.** Fun with friends 169 (26.2%), monsters 83, funny 71, potential 68, visuals 64 [S, n=915]. "10 bucks for an adorable hilarious wizard game with friends?" (55h) [S].

**Where players push back.** Repetitive 118 (73 neg), too short 106 (50 neg), bugs 62, developer abandoned 57 (52 neg), price 21 [S]. "the gameplay loop itself is incredibly stale" (1.5h) [S]. <2h: repetition 31 leads [S, n=215]. >20h: the same pair; "it does get quite boring after awhile due to the lack of content" (116h) [S, n=55].

**Sentiment over time.** 80.9% launch week, rising to 84-92% by Mar-Apr with hotfixes [P]. Then 75-83% mid-year, 61-72% in Oct 2026 and 45.8% in the first Nov 2026 week [P], while the promised big update has not shipped.

**What happened after launch.** Hotfixes 1-5 in two weeks (compass, timer, save system, new-player guidance); Mandarin and Japanese voice casting; soundtrack DLC $2.99 [P]. 500K copies by 2026-02-10 and "1M players" by 2026-03-18 [D]. 2026-04-22 "Words From a Raven": "we are not content with the amount of agency players currently have" [D]; no posts since [P]. Players -65.5% in Mar and -51.5% in Apr; the Jul +32% and early-Sep daily peaks are unexplained [T/I]. Cross-promo bundles with other co-op games [P].

**Launch path & team.** October 2025 Next Fest demo; PC Gamer called it "The next great co-op horror game" [T]; release 3.5 months later [I]. Launch-week streamers (SMii7Yplus videos at 1.9-3.1M views) [P]. No in-game matchmaking at launch [T]. "Way more of you showed up than we ever expected" [D].

**Unknowns.** Team size, engine, dev time, wishlists, announcement date, post-launch discounts, cause of the Jul and Sep 2026 bumps.

---

## 14. Sinister Night 2 (2761670)
**Stratum** mid | **Pair** none | **Release** EA 2024-04-04 (store 1.0 date 2025-08-31, announced 2025-10-01) [P] | **Price** $9.99 [P]; EA 9.75 EUR [T] | **Players** 9-10 [P] | **Dev/Pub** Bug Inventors, self-published, China [P/I] | **Core type** versus (social deduction) | **Reviews** 2,059, 87.0% [P]

| Metric | Value |
|---|---|
| Median h at review (all / pos / neg) | 81.15 / 96.13 / 27.7 [S, n=1000/832/168] |
| <2h / >10h / >50h | 5.2% / 81.4% / 57.5% [S] |
| Top languages | Simplified Chinese 98.0%, Traditional Chinese 1.4%, English 0.5% [P] |
| SteamCharts peak | 2,450 (2024-06) [T] |
| M1 / M3 / M6 / M12 proxy | 376 / 715 / 402 / 297 [T] |
| Current players | 20 [P] |

**Core loop & inputs.** Nine "streamer" characters in a Chinese mansion (plus church-school and Shanghai lane maps); two hidden possessed players kill during "Crimson Night"; survivors gather offerings and clues, then vote [P]. Items (Zhong Kui statues, EMF, peach-wood sword), role abilities, transform and self-destruct keys, distorted ghost proximity voice [P].
**Dependence.** Faction win; survivors must pool information in a game built on lying [P].
**Failure & dead players.** Killed players are out. Two spectator slots per room since 2026-01 and a "Last Words" mechanic [P]; what dead players do in-round not found.

**What it gets right.** Deception/social deduction 264 (36.9%), horror 186, fun with friends 150, visuals 127, potential 103 [S, n=873]. >20h reviewers say the same (deception 220) [S, n=639]. From an English sample review: "refining its social deduction mechanics and atmospheric tension" [S].

**Where players push back.** Toxic players 70 (31 neg), bugs 45, performance 44, dead game 31, connection 26, abandonment 23 [S]. A <1h Chinese review warns that veterans mock and abuse newcomers, so avoid it without friends [S, translated]. >20h: toxicity 47 leads; a 198h reviewer alleges moderators side with streamers [S, translated]. A 373h reviewer says updates are now mostly skin DLC [S, translated]. <2h n=48 codable only.

**Sentiment over time.** 77% launch month, 69-70% Aug-Sep 2024, then Oct 2024 397/6 (98.5%) while players fell, cause unknown [P/I]. 84-95% through mid-2025, 50-69% Aug-Dec 2025, Oct 2026 37/4 (90.2%) with the Possessed Enhancement Project and newcomer fixes [P].

**What happened after launch.** 71 posts, weekly balance patches in 2024; DDoS on servers in Apr 2024 [P]. The Church School map lifted Jun 2024 to 679 (+78.5%), Jul 752 [T]. Characters based on real Chinese streamers; Huya streamer recruitment with gift cards; a Douyin tournament [P]. Eight $8.99 character DLCs, a Deluxe bundle, a "historically lowest" 20% sale [P]. Players slid to about 80-100 in 2026 [T]. Room level gates removed Oct 2026: "Please give newcomers a little patience" [D].

**Launch path & team.** Predecessor "Sinister Night" (2022, dev "zstar") [T]; same team not confirmed [I]. "just a small indie game team" [D, translated]. No English at EA [T]. Free demo from 2025-10 [P].

**Unknowns.** Engine, dev time, team size, Next Fest, wishlists, Oct 2024 review spike cause, session length.

---

## 15. Darkwater (619540)
**Stratum** mid | **Pair** none | **Release** EA 2025-04-22, 1.0 2026-03-26 [P] | **Price** $9.99, no rise at 1.0 [P] | **Players** 1-4 [P] | **Dev/Pub** Targon Studios / Playstack [P] | **Core type** shared_object (submarine) | **Reviews** 1,210, 77.9% [P]

| Metric | Value |
|---|---|
| Median h at review (all / pos / neg) | 5.15 / 5.83 / 1.62 [S, n=1000/771/229] |
| <2h / >10h / >50h | 20.5% / 26.7% / 3.0% [S]; 54.1% of negatives <2h |
| Top languages | English 61.5%, Russian 17.9%, Korean 3.7% [P] |
| SteamCharts peak | 768 (2026-03) [T] |
| M1 / M3 / M6 / M12 proxy | 79 (Apr missing) / 28 / 28 / 96 [T] |
| Current players | 13 [P] |

**Core loop & inputs.** Crew one submarine under Enceladus ice: pilot, fire weapons, read sonar, repair leaks; dock at procedural outposts for fuel and loot, fight infected divers, upgrade the sub [P/T]. Melee and guns, parry, stealth, inventory slots, emotes [P].
**Dependence.** One shared sub, fuel, storage and carrying capacity [P].
**Failure & dead players.** Dead players become mice ("mouse mode") with places to hang out; respawn at outposts [P]. Whole-run failure not found.

**What it gets right.** Fun with friends 178 (25.5%), potential 118, monsters 84, horror 61, value 58 [S, n=914]. "a torpedo-laden kraken… and boarding parties trying to take our sub" [S].

**Where players push back.** Bugs 216 (23.6% of codable; 70 neg), too short 88, repetitive 66, performance 41, crashes 32, connection 29 [S]. Tech mentions 29.2% [S]. "it desperately needs to be redeveloped, polished, and most importantly bug fixed" [S]. <2h: bugs 43 and performance 18, tech mentions 35% [S, n=190]. >20h: bugs still 32.7%; "Bugs galore." (25.8h) [S, n=104].

**Sentiment over time.** 81% and 76% in the first two weeks [P]. Noisy 50-100% weekly on small volume through 2025; a Feb 2026 dip (30-33% in two weeks) [P]. 1.0 weeks 41/16 and 56/18 (72-76%) [P].

**What happened after launch.** Community updates, Invasion (Aug 2025, +72.6% players), Brimstone, and Fire and Brimstone with endless mode [P/T]. 30% sales in Autumn, Winter and at 1.0 [P]. 1.0 lifted Mar 2026 to 80 (peak 768) and Apr to 113, then May 41 (-64%) [T]. $4.99 Supporter's Pack cosmetic DLC; Steam Workshop in Oct 2026 [P].

**Launch path & team.** Store page by Jun 2024; PC Gaming Show reveal and Playstack signing in Dec 2024; closed playtest Feb 2025; Feb 2025 Next Fest, "one of the most played demos" [P/D]. Developer at 1.0: "PRICE INCREASE? Nope!" [D].

**Unknowns.** Team size, location, engine, start of development (appid suggests about 2017 [I]), wishlists, viral moment, session length.

---

## 16. Backrooms Media (2714970)
**Stratum** mid | **Pair** none | **Release** EA 2024-09-10, 1.0 2025-12-16 [P] | **Price** $7.99 [P]; EA launch 6.99 EUR with 20% off [T] | **Players** 1-4, online and LAN [P] | **Dev/Pub** NPK Games (solo "Patrik"), self-published [P/D] | **Core type** escape_survival | **Reviews** 651, 40.2% [P]

| Metric | Value |
|---|---|
| Median h at review (all / pos / neg) | 1.57 / 1.95 / 1.3 [S, census n=651/262/389] |
| <2h / >10h / >50h | 63.3% / 0.9% / 0.2% [S]; 87.6% written during EA |
| Top languages | Simplified Chinese 28.3%, English 26.3%, Russian 24.3% [P] |
| SteamCharts peak / proxies | not found (HTTP 500) |
| Current players | 0 [P] |

**Core loop & inputs.** Explore "hyper-realistic" Backrooms levels, evade entities, find notes and solve puzzles to find exits; "The Hunt" mode flips it to capturing an entity with gadgets [P]. Five gadgets, proximity voice, Workshop and level editor [P].
**Dependence.** The store says "You cannot make it alone" (traps and puzzles), yet single-player is listed [P].
**Failure & dead players.** not found.

**What it gets right.** Potential 56 (24.0% of positives), atmosphere 39, monsters 38, horror 35, fun with friends 28 [S, n=580]. "Excited for more to come." [S].

**Where players push back.** Bugs 92 (66 neg), repetitive 47, too short 44, crashes 37, performance 37, connection 24 [S]. Tech mentions 27.2%, refund mentions 22 [S]. "Monsters are buggy and often break the experience." [S]. "The walking speed is painfully slow" [S]. <2h reviewers dominate (n=364 codable); >20h has 2 reviews.

**Sentiment over time.** Launch month 123/198 (38.3%), the bulk of all reviews [P]. 64% in Oct 2024 after the camera fix, about 50-55% through Jan 2025, mostly under 40% since; 1.0 did not help (Jan 2026 1/9) [P].

**What happened after launch.** Weekly devlogs Oct 2024-Mar 2025; Level 0 rework; Hunt mode; procedural mode; 1.0 with a new Hunt level [P]. "My main focus right now is fixing and polishing" [D]. Apr 2025 apology for a missed update: challenges "way more complex (and time-consuming) than I expected" [D]. Scream Fest 20% [P].

**Launch path & team.** Feb 2024 Next Fest most-played list [T]; beta playtests Jul 2024; a content-creator call before EA [P]. Solo developer [D]. Deku Deals lists a different publisher [T, conflicts with Steam].

**Unknowns.** Player history, location, engine, dev time, wishlists, failure and dead-player rules.

---

## 17. SpyHunt (formerly SpyFall) (3334280)
**Stratum** flop | **Pair** none | **Release** EA 2025-02-11, 1.0 2026-01-06 [P] | **Price** $9.99 list, 40% off ($5.99) on 2026-11-11 [P]; EA CDN$6.99 [T] | **Players** 1v1 up to 8 with 2 detectives [P] | **Dev/Pub** Mamkalo / MKL Studios (probably the same entity [I]) [P] | **Core type** versus (hidden role) | **Reviews** 118, 81.4% [P]

| Metric | Value |
|---|---|
| Median h at review (all / pos / neg) | 3.83 / 3.93 / 2.57 [S, census n=118/96/22] |
| <2h / >10h / >50h | 33.1% / 7.6% / 0.8% [S] |
| Top languages | English 74.6%, French 11.9%, German 4.2% [P] |
| SteamCharts peak / proxies | not found (HTTP 500) |
| Current players | 0 [P] |

**Core loop & inputs.** Spies blend in among NPCs and do secret tasks; one or two Detectives watch for player-like behaviour and shoot [P]. Detective weapons with ammo (the reload is audible to spies), potions, a task-location key, role select, proximity voice (Apr 2025) [P].
**Dependence.** Spies share a goal and can see teammates [P].
**Failure & dead players.** Shot spies are out; the Detective loses if tasks complete [P]. Dead players not found.

**What it gets right.** Fun with friends 34 (41.0%), potential 12, funny 11, value 6, deception 6 [S, n=105]. "getting caught creates a lot of tense and funny moments with friends" (97h) [S].

**Where players push back.** Bugs 12 (4 neg), too short 12, performance 9 (8 neg), crashes 4 [S]. "this game has some of the worst optimization ive ever seen" (0.1h) [S]. A LAN-party review reports crashes on several machines [S]. <2h: bugs and performance 4 each [S, n=37]. Only 1 codable >20h review.

**Sentiment over time.** Mostly positive on 1-6 reviews a week through 2025; Jan 2026 (1.0) was the weakest month at about 40-50% [P]. About 1 review a month since [P].

**What happened after launch.** Silent West map and 8-player custom settings (Apr 2025); 1.0 with 4 maps and Detective weapons, demo cut to one map and 2 players; DLSS; renamed SpyHunt (May 2026); The Bar map (Jul 2026) [P]. The EA Q&A promised a price rise at 1.0 [P]. Claimed "more than 30,000 players", hard to square with 118 reviews; possibly demo players [D/I].

**Launch path & team.** Renamed because "searching for 'Spyfall' often led players to the popular board game" [D]. Free demo [P].

**Unknowns.** Team, location, engine, announcement, Next Fest, wishlists, player history, session length.

---

## 18. Drive Together (4117320)
**Stratum** flop | **Pair** P04 (shared vehicle, vs RV There Yet?) | **Release** 2026-05-15, full release (EA had been planned) [P/D] | **Price** $4.49 list; 30% Summer Sale [P] | **Players** 1-4 per car; Race up to 8 [P] | **Dev/Pub** Otakumi Games / TARK Future Heroes [P] | **Core type** shared_object | **Reviews** 73, 68.5% [P]

| Metric | Value |
|---|---|
| Median h at review (all / pos / neg) | 1.03 / 1.29 / 0.87 [S, census n=73/50/23] |
| <2h / >10h / >50h | 82.2% / 0% / 0% [S]; 91.3% of negatives <2h |
| Top languages | English 43.8%, Turkish 27.4%, Japanese 5.5% [P] |
| SteamCharts peak / proxies | not found (HTTP 500) |
| Current players | 0 [P] |

**Core loop & inputs.** Players share one car on obstacle courses (ramps, narrow bridges, fans on ice, launch pads); each controls one function: throttle, brake/reverse, left or right [P/T]. With fewer players, each holds two functions [T]. Keyboard-only option; voice is external ("Communication is the most important skill") [P].
**Dependence.** Total: every move needs another player's input [P].
**Failure & dead players.** Falling off restarts at a generous checkpoint [T]. No death.

**What it gets right.** Fun with friends 16 (34.0%), funny 5, visuals 5, value 5, rage-as-fun 5 [S, n=69]. "another chained together with your friends… with driving instead" [S]. One reviewer says most maps take about 30 minutes [S].

**Where players push back.** Bugs 14 (8 neg), too short 9, price 4, difficulty 4 [S]. Tech mentions 26.1% [S]. "Very buggy and makes you rage, try playing it when it gets fixed" [S]. "too expensive for unreal slop" [S]. Almost all reviewers <2h; no >20h reviews.

**Sentiment over time.** Launch week 17/8 (68%), then 0-2 a week; Jul-Oct 2026 mostly single negative reviews [P].

**What happened after launch.** A leaderboard fix and a Route 66 map within 3 days; Summer Sale 30% (2026-06-26); no posts since [P]. Five bundles with other "Together"-style games [P].

**Launch path & team.** Demo Jan 2026 with Japanese press coverage [T]; wishlists 5K -> 10K ("officially trending") -> 15K in about 3 weeks, 20K by 2026-05-09 [D]. GG Con booth and a Feb 2026 Next Fest livestream [P]. About 20K wishlists became fewer than 100 reviews [I]. Possibly Turkey-based [I].

**Unknowns.** Launch price, team, engine, publisher role, sales, player history, session length.

---

## 19. Tentacle Tango (3253920)
**Stratum** flop | **Pair** none | **Release** 2025-11-20 (local co-op only; online added 2026-01-22; Switch 2026-09-24) [P] | **Price** $14.99 [P] | **Players** 2 (one player can control both) [P] | **Dev/Pub** Cable Nest, self-published, Sweden [P/D] | **Core type** climbing_traversal | **Reviews** 39, 100% [P]

| Metric | Value |
|---|---|
| Median h at review (all / pos / neg) | 1.98 / 1.98 / none [S, census n=39/39/0] |
| <2h / >10h / >50h | 51.3% / 12.8% / 0% [S] |
| Top languages | English 82.1%, Swedish 7.7%, Russian 5.1% [P] |
| SteamCharts peak / proxies | not found (HTTP 500) |
| Current players | 0 [P] |

**Core loop & inputs.** Two tethered octopuses revolve, swing and jump with momentum through 4 worlds with bosses [P]. Move, swing, jump, arm length; full controller support; leaderboards and a speedrun timer; no in-game voice [P].
**Dependence.** A physical tether: each player's movement moves the other [P].
**Failure & dead players.** Frequent death ("Prepare to die—a lot"), checkpoints, a death counter; both respawn together [P/I].

**What it gets right.** Fun with friends 12 (30.8%), visuals 9, simple 7, teamwork 7, also good solo 7 [S, n=39]. "A cute, but quite challenging game due to the movement and control mechanics." [S].

**Where players push back.** Almost nothing coded: difficulty 2, bugs 1, too short 1, controls 1, all in positive reviews [S]. "the difficulty is like night and day when you don't have to tell someone else" [S]. The developer cut World 1 difficulty as "more difficult than intended" [D]. The problem was reach, not sentiment [I].

**Sentiment over time.** Launch week 13/0, then 0-2 a month [P].

**What happened after launch.** World 1 made easier, online beta, free demo and Steam Deck Verified (Dec 2025); online co-op with 25% off (Jan 2026); repeated sales from 25% to 50% ($7.49, "lowest price to date") [P]. Bundle with Brave Escape [P].

**Launch path & team.** Demo from Oct 2024 and a long run of themed festivals (Difficult Game Bash, Six One Indie, Made in Sweden, Debut, Animal Fest) instead of Next Fest [P]. "our small team" [D].

**Unknowns.** Engine, team size, dev time, wishlists, player history, session length.

---

## 20. Keep It Contained (4251090)
**Stratum** flop | **Pair** none | **Release** EA 2026-08-07 (missed its planned window) [P/D] | **Price** $5.99; may rise about 25% after EA [P] | **Players** 2+ required; only one copy needed, others use the free Protocol Book [P] | **Dev/Pub** Triarch Interactive, self-published [P] | **Core type** asymmetric_information | **Reviews** 12, 100% [P]

| Metric | Value |
|---|---|
| Median h at review (all / pos / neg) | 3.17 / 3.17 / none [S, census n=12/12/0] |
| <2h / >10h / >50h | 33.3% / 8.3% / 0% [S] |
| Top languages | Turkish 50.0%, English 41.7%, Simplified Chinese 8.3% [P] |
| SteamCharts peak / proxies | not found (HTTP 500) |
| Current players | 0 [P] |

**Core loop & inputs.** Keep Talking-style: one "scientist" works facility modules and an organism containment; the others hold only the Protocol Book and guide by voice [P]. Free-look camera, mouse-only option, custom level creator; voice through Discord or in person [P].
**Dependence.** A total information split; everything depends on communication [P].
**Failure & dead players.** The organism breaks containment; retry rules not found [P]. No dead state.

**What it gets right.** Fun with friends 12 (all 12), potential 5, funny 4, physics/chaos 3 [S, n=12]. "My friend and I literally argued our way through the levels" [S].

**Where players push back.** Bugs 2 and connection 2, all in positive reviews [S]. The two "connection" hits are Turkish jokes about friends who cannot describe a cable, not network faults [I]. One reviewer says reported bugs were fixed quickly [S]. No >20h reviews.

**Sentiment over time.** Launch week 10/0, then 1 review after mid-August [P].

**What happened after launch.** Fixes, mouse sensitivity and a "Distortion & Stability" update by 2026-09-02 [P]. No discounts found.

**Launch path & team.** Demo in the Feb 2026 Next Fest (30+ languages, new art and tutorial); release planned for April, then July 2026 [P/T]. "Rather than rushing the game out, we decided to spend the extra time" [D]. Unity [D].

**Unknowns.** Team, location, dev time, wishlists, session length, player history, why the store lists Single-player.
