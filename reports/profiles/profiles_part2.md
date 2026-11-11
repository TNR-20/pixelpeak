# Friendslop deep-study game profiles - part 2 (batches 3 and 4, 20 games)

Sources: deep_profiles_batch_3.md / deep_profiles_batch_4.md, data/deep_study_numbers.csv, data/deep_study_selection.csv, data/deep/{appid}/summary.md + themes.md, layer2_review_themes.md, layer2_tooling_method.md. No new web research.

Tags: [P] verified primary (Steam) | [D] developer claim | [T] third-party (SteamCharts etc.) | [I] inference | [S] computed from review sample (n=...).
Method caveats: review samples are 500 newest + 500 most-helpful for games with >1,000 reviews (census otherwise), so they are not random. Theme counts come from keyword coding (codebook v1) and include some false positives, which are flagged where spotted. Month-N player figures are SteamCharts calendar-month proxies. Price history was blocked for all games.

Order: batch 3 (PEAK, One-armed robber, Jump Space, Roadside Research, Scam Line, Backrooms: Extractions, EXPEDITION TO THE BACKROOMS, Cargo Duty, OCTOPinbs, RADIOACTIVE INC.), then batch 4 (Content Warning, Big Walk, PANICORE, Sledding Game, Mama's Sleeping Angels, Chained Wheels, Innchanted, Treasure Hunters: Raid Together, Servonauts, Nightfall Secrets).

---

## PEAK (appid 3527290)
**Stratum:** hit | **Pair:** P01 (vs Sunset Summit) | **Release:** 2025-06-16 | **Price:** $7.99 list, $4.95 (−38%) at launch and on 2026-11-11 [P] | **Players:** 1-4, friends-only [P] | **Dev/Pub:** Team PEAK / Aggro Crab, Landfall [P] | **Core type:** climbing_traversal | **Reviews:** 385,690 total, 94.4% positive [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 14.1h / 14.3h / 12.3h [S] (n=1000 / 921 / 79) |
| <2h / >10h / >50h (all) | 3.7% / 61.6% / 16.5% [S] (n=1000) |
| Top 3 languages | English 47.6%, Russian 18.1%, Brazilian 6.2% [P] (schinese 6.1% at 83.7% positive, lowest big language) |
| SteamCharts all-time peak | 169,910 (2025-08) [T]; SteamDB press feed: 170,759 on 2025-08-17 |
| Month 1 / 3 / 6 / 12 avg proxies | 57,223 / 46,535 / 25,161 / 13,901 [T] |
| Current players | 13,304 (2026-11-11) [P] |

### Core loop & inputs
- Up to 4 scouts climb a procedurally laid-out island mountain that changes every 24h, through 4+ biomes, managing a shared stamina/injury bar, food and items [P].
- Inputs: move/jump/sprint/climb (lunge), "Helping Hand" pull-up, throw/drop, ping, emote, backpack slot, proximity voice; rebinding added 2025-09-23 [D].

### Interdependence & failure
- Players depend on each other for help-ups, ropes/spikes, carrying downed friends, food/healing sharing, shared campfires (checkpoints) [P/T].
- Status effects fill stamina → unconscious → death timer (paused while carried) → ghost + skeleton [T]. Ghosts spectate and still talk; revival at Ancient Statue / Scout Effigy, Book of Bones, or entering Nadir [T]. Run fails if everyone dies; campfire saves added 2026-03-30 [D].

### What it gets right
- Praise among codable positives [S] (n=783): fun with friends 304 (38.8%), funny 83, visuals/audio 69, simple to pick up 63, teamwork 46, value 44, relaxing 43, also good solo 37.
- >20h reviewers add physics/chaos (22) and rage-as-fun (22) [S] (n=324 pos).
- "You can scream when someone falls, and laugh at a friend slipping on a banana."

### Where players push back
- Complaints, all codable [S] (n=858): bugs 60, connection/lobby 44, repetitive 42, needs friends 30, difficulty/balance 29, lost progress 28, too short 27, performance 26. Among negatives (n=75): connection 23 (30.7%), bugs 16, balance 11, lost progress 11; technical failure in 54.7% of codable negatives. Keyword coding inflates some counts ("disconnect" metaphors, "plane crash") [I].
- "The player is nerfed in ways that are unfun: Increased heat gain over hot rocks in the kiln."
- "given the artstyle and gameplay not sure why this game is 16GB nor why it needs a whole new gen GPU."
- <2h: only 31 codable reviews [S]; thin signal (friends, connection, performance, 2 each). >20h (n=353 codable): bugs 36, repetitive 22, connection 20, needs friends 20; technical failure in 62% of their negatives [S].

### Sentiment over time
- Weekly histogram [P]: launch week 89.9%, then 92-94% throughout. Mesa week (2025-08-11) 15,623 reviews at 92.4%. Week of 2025-11-24: 53,367 reviews at 99.2% with no player spike; coincides with Steam Awards campaign post, likely sale/awards review activity [I]. Final Ascent week (2026-08-10) 7,158 at 90.4%. Recent weeks 92-94%.

### What happened after launch
- 2M copies in 9 days [D]; 11M sold cited by Aggro Crab [D via T]; 20M players headline seen only as snippet [T].
- Players [T]: Jun 62,045 → Aug 64,798 (Mesa biome) → Sep −56%, Oct −39% → Nov +66% (Roots biome) → Dec −25% despite bbno$ concert "DOUBLED" weekend [D] → Aug 2026 +212% (Final Ascent, peak 122,714) → Oct 2026 −34% despite console launch with crossplay (console players not counted [I]).
- Many patches; cannibalism added then toned down; zombie nerf; Ascent 7 rule softened as "not in the spirit of the game" [D]; host kick, anti-grief, longer room codes.
- Monetisation: no DLC [P]; Points Shop items, merch (Makeship, Fangamer/Youtooz); creator cosmetics temporary by policy [D]; bundles at −10% [P].

### Launch path & team
- Teaser April 2025; announced 2025-06-12, released 4 days later; no demo/playtest/Next Fest found; launch discount "so that you can get PEAK for a friend too" [D].
- Virality via Twitch/TikTok/YouTube; "99% of the marketing... word of mouth or from content creators" (Kaman) [D].
- Landfall (Sweden) + Aggro Crab (~13 devs) [T/D]; born in a 4-week jam in Seoul [T]; Unity [I]. "neither of us being live service studios" [D]; "I can't say with confidence that the success is easily replicable" (Kaman) [D].

### Unknowns
- Session length, PEAK-specific headcount, wishlists, price history (blocked), revenue, console player counts, cause of Nov 2025 review spike and early-Mar 2026 lift, RPS "not a forever game" article body, behaviour with exactly 2 players or weaker players.

---

## One-armed robber (appid 2551020)
**Stratum:** hit | **Pair:** none | **Release:** 2023-12-15 | **Price:** free-to-play; some maps paid via in-app purchase [P] | **Players:** 1-5 (5 per TechRadar [T]; store does not state) | **Dev/Pub:** Duhndal / Duhndal [P] | **Core type:** extraction | **Reviews:** 54,546 total, 91.3% positive [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 5.1h / 5.4h / 3.1h [S] (n=1000 / 924 / 76) |
| <2h / >10h / >50h (all) | 23.4% / 30.6% / 3.3% [S] (n=1000); 46.1% of negatives are <2h |
| Top 3 languages | English 41.4%, Russian 18.6%, Polish 7.5% [P] |
| SteamCharts all-time peak | 10,993 (2023-12) [T] |
| Month 1 / 3 / 6 / 12 avg proxies | 3,259 / 1,439 / 1,474 / 1,047 [T] |
| Current players | 348 (2026-11-11) [P]; last-30-day avg 659 [T] |

### Core loop & inputs
- 1-5 one-armed robbers plan stealth or loud heists, fill duffel bags from vaults, carry loot to the truck, spend the take on guns, tools and skills [P/T].
- Inputs: move, shoot (attachments), lock-pick, powerbox sabotage, carry bag, tow car, grenades/C4, pager answering; one arm for everything [P/D/T]. Voice/ping/emotes not found.

### Interdependence & failure
- "Grab a friend and you'll have two arms in total"; friends carry out loot [P]; role split (guard killer, bag carrier, lookout) per TechRadar [T].
- Alarm → police waves → SWAT [T]; civilian casualties cut the take [D]. Death handling and what dead players do: not found.

### What it gets right
- Praise among codable positives [S] (n=764): fun with friends 115, good value/free 94, funny 32, visuals 29, potential 17, unique 16.
- Free price is the top praise among >20h reviewers (16 of 103 codable positives) [S].
- "Better than PAYDAY 3 and it's FREE!"

### Where players push back
- Complaints, all codable [S] (n=829): bugs 31, repetitive 27, too short 25, monetisation/paid content 25 (9 of 65 negatives, 13.9%), grind 14, performance 13, needs friends 13, missing translation 10 (Chinese requests), price 9 (6 in negatives). Technical failure only 6.2% of codable [S].
- "EVERYTHING IS A PAYWALL PAY FOR SKINS PAY FOR THIS PAY FOR NOTHING"
- "nearly half of this games heists (5 out of 11) are locked behind a paid currency system"
- <2h (n=211 codable, 33 negative): bugs 9, monetisation 6, crashes 5, boredom 5 [S]. >20h (n=106 codable, only 3 negative): monetisation 7, repetitive 5, grind 4 — long players stay positive but name paywalls and grind [S].

### Sentiment over time
- Monthly histogram [P]: launch month 5,862 reviews at 86.4% (lowest), rising to 90-93% through 2024. Nov 2024 spike to 4,412 at 95.1% with no player rise; cause unknown, sale/Steam Awards activity is an inference [I]. Since 2025 a flat 88-92%; no update visibly moved sentiment.

### What happened after launch
- Players [T]: Dec 2023 4,269 avg → Jan −47% → Feb −35%, then a slow slide from ~1,500 to ~700. Lifts: May 2024 +21% (Casino map), Jan 2025 +45% (Mansion + weapons update), Jan 2026 +26% (Harbour Heist + server browser) [D].
- Updates: new maps roughly 1-3 per year (Lundenburg, Casino, Mansion, Harbour, Data Center, Halloween map), skills research, sound/music pass, grenades [D].
- Monetisation: paid maps with recurring 25% map sales; weekly cosmetic shop cut to 2 items because "spending too much of our time making skins" [D]; daily weapon-skin crates tradeable on Community Market (2026-08-21); Halloween cases [D].

### Launch path & team
- Announcement, trailer, demo, Next Fest, wishlists and viral moment: not found. Direct free launch, self-published [P].
- Duhndal, Denmark; "a small team" [D]; Unreal Engine 4/5 [D]; sibling game One-Armed Cook [D]; studio-wide claim "13,812,000+ Players" across both games [D].

### Unknowns
- Team size, dev time, map prices, revenue split, launch driver, death/spectate rules, session length, party-size behaviour, cause of Nov 2024 review spike. No interviews or postmortems found.

---

## Jump Space (appid 1757300)
**Stratum:** hit | **Pair:** none | **Release:** 2025-09-19 (Early Access; Xbox Game Preview same day) | **Price:** $19.99 [P]; Supporter Upgrade DLC $9.99 [P] | **Players:** 1-4 [D] | **Dev/Pub:** Keepsake Games / Keepsake Games [P] | **Core type:** shared_object | **Reviews:** 13,494 total, 85.0% positive [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 14.0h / 15.5h / 9.5h [S] (n=1000 / 732 / 268); sample 73.2% positive, so negatives over-weighted |
| <2h / >10h / >50h (all) | 7.6% / 60.4% / 10.8% [S] (n=1000) |
| Top 3 languages | English 73.3%, Russian 7.5%, German 5.2% [P] |
| SteamCharts all-time peak | 21,933 (2025-09) [T] |
| Month 1 / 3 / 6 / 12 avg proxies | 4,665 / 839 / 404 / 881 [T] |
| Current players | 348 (2026-11-11) [P] |

### Core loop & inputs
- Crew a ship through mission sectors (pilot, turrets, power routing, repairs, firefighting), then go on foot/spacewalk to board, salvage and fight; extract loot to upgrade ship, weapons and character [P].
- Inputs: move/jetpack, pilot, turrets, reroute power, airlocks, extinguisher, multi-tool, guns, melee (2025-10-27), deployables [D]. No in-game voice chat yet; planned for Dec 2026 [D].

### Interdependence & failure
- Shared hull and ship roles; "no set classes" [P]. Losing the ship fails the mission.
- Downed players are revived by teammates [D]; inventory loss on failure removed 2026-03-27 [D]; AI Director eases spawns after a teammate death to avoid a "death spiral" [D]. What dead players do: not found.

### What it gets right
- Praise among codable positives [S] (n=682): fun with friends 143, potential 143, enemies 80, visuals 78, progression 75, content variety 65, also good solo 47, active developer 42.
- "enemies can often board the player ship and you theirs which really changes the dynamic"

### Where players push back
- Complaints, all codable [S] (n=947): bugs 151, repetitive 147, performance 114, too short 69, difficulty/RNG 68, grind 50, controls 46, crashes 39, connection 35. Technical failure in 28.2% of codable reviews [S].
- "All mission objectives revolves around the same thing : "do that before timer off", "extract this", "kill that"."
- <2h (n=72 codable, 46 negative, 4 refund mentions): repetitive 11, performance 10, bugs 9, AI-generated voices 5 — "This game uses AI voices and they honestly sound like sh*t." [S].
- >20h (n=371 codable, 90 negative): bugs 76, repetitive 56, performance 50, difficulty/RNG 47 (27.8% of their negatives), grind 32, "update made it worse" 18 (14 negative) [S]. "The progression system still feels unnecessarily grindy."

### Sentiment over time
- Weekly histogram [P]: launch week 3,716 reviews at 88.8%, sliding to ~81% by mid-Oct 2025; brief 95-97% weeks from 2025-11-21 (cause not found); Dec 2025-Jan 2026 75-80%.
- Update weeks dip: Heated (2026-03-27) 75.3%; early May 62.7-66%; Weapons Update week (2026-06-19) 63.0% after MK3 component conversion [D]; Free Weekend week (2026-09-18) 345 reviews at 89.9%.

### What happened after launch
- 130k players in 24h, 250k by 2025-09-23 across Steam + Xbox [D]; "over 430,000 copies in its first three weeks" (snippet only) [T].
- Players [T]: Sep 2025 7,613 avg → Oct 1,717 (−77%) → Nov 769 → Feb 2026 322 → each content update lifts (Mar +51%, Jun +53%, Jul +75%) → Sep 2026 1,295 (+177%, Free Weekend + Anniversary update, peak 9,256) → Oct 580.
- Developers admitted crashes and broken multiplayer "still all too frequent" (2025-11-07), hired a programmer; networking rewrite, DX12, Unity 6 (Mar 2026); difficulty "a little overtuned" [D]; one-time "Ingot Compensation" after MK3 backlash [D]; non-hosts lacked progression [D].
- Pricing: 20% seasonal sales, 40% Sep 2026, free weekend 2026-09-17-21; price "may increase" at 1.0 [D].

### Launch path & team
- Hobby project from 2012; 2019 tech demo drew "Thousands" into Discord [D]. Store reveal Apr 2024, 100k wishlists in week 1 [D]; closed beta Jan-Apr 2025; Next Fest June 2025 as "Jump Ship": 500k+ demo players, top-3 demo, 950k wishlists [D]; renamed for trademark reasons, 1M wishlists (2025-08-05) [D].
- Keepsake Games, Stockholm, founded 2021 by 5 veterans (Mojang, Hazelight, Coffee Stain, Toca Boca) [T]; ~16 employees [D]; private investor [D]; Unity 6 + Epic Online Services [D]. Planned "two years... just the five of us founders" [D]; EA came ~4.5 years after founding.

### Unknowns
- Typical mission/session length, dead-player activity, behaviour with exactly 2 players, 1.0 date, price history, verified sales total, cause of late-Nov 2025 positive spike.

---

## Roadside Research (appid 3643170)
**Stratum:** mid | **Pair:** none | **Release:** 2026-02-12 (Early Access; 1.0 planned 2027 [D]) | **Price:** launched at $12.99 with 10% launch discount [D]; now $14.99 [P] | **Players:** 1-4 [D] | **Dev/Pub:** Cybernetic Walrus / Oro Interactive [P] | **Core type:** job_simulation | **Reviews:** 5,015 total, 85.7% positive [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 5.8h / 6.9h / 2.6h [S] (n=1000 / 820 / 180) |
| <2h / >10h / >50h (all) | 14.8% / 30.9% / 0.8% [S] (n=1000); 42.2% of negatives are <2h |
| Top 3 languages | English 58.4%, Russian 12.5%, German 7.1% [P] |
| SteamCharts all-time peak | 9,171 (2026-02) [T] |
| Month 1 / 3 / 6 / 12 avg proxies | 2,384 / 1,055 / 425 / not yet reached [T] |
| Current players | 236 (2026-11-11) [P] |

### Core loop & inputs
- Aliens disguised as humans run a gas station: by day restock, refuel, cook, clean, work the register while scanning, stealing from and testing customers without filling a suspicion meter; at night buy station and alien-tech upgrades [P].
- Inputs: physics carry/place, shelves, pumps, register, cooking, cleaning, scanner, DNA puzzle, tractor-beam abduction (2026-08-18), self-drawn face masks [D]. Voice/text chat, ping: not found.

### Interdependence & failure
- Chores vs research split; 4-player cap "based on the roles for each player" [D].
- Too much suspicion brings government agents and mini-games; "they will turn you into goo" [P]. Customer-satisfaction score [D]. Run reset, permadeath and dead-player activity: not found.

### What it gets right
- Praise among codable positives [S] (n=694): fun with friends 176, funny 80, potential 74, progression 54, unique concept 40, value 32, active developer 29.
- >20h positives (n=84) stress friends 27, humour 12, active developer 8, addictive 8 [S].
- "I played this game coop with my wife and we had a ton of fun and some good laughs."

### Where players push back
- Complaints, all codable [S] (n=867): bugs 101, repetitive 89, too short 55, performance 31, needs friends 30, connection 20, lag 19, price 17 (14 in negatives). Technical failure in 29.5% of codable negatives [S].
- "The constant unloading and endlessly restocking shelves and fuel becomes incredibly repetitive"
- "whoever is the host seems to get good connection but anybody else gets stuttering / rubber banding issues"
- <2h (n=136 codable, 72 negative): bugs 16, repetitive 14, performance 7, bad solo 7, price 6, "clone/slop" 6 [S]. >20h (n=92 codable, only 8 negative): bugs 11, repetitive 8, thin content 4; "Was fun before the battery update." [S].

### Sentiment over time
- Weekly histogram [P]: launch week 760 reviews at 86.4%; 85-88% through early Apr; gradual drift to low 80s with small-n dips (75.0% week of 2026-04-30, 73.3% 2026-06-11).
- Abduction Update week (2026-08-13): 63.2% (57 reviews) after unpopular battery system and F.A.R.T. robot; next-day apology/hotfix [D], then 83.3% and 98.0% (51 reviews) in following weeks [P]. Volumes now <30/week.

### What happened after launch
- 150k players by 2026-02-16; "over 400,000 copies sold in just the first month"; "over 730K copies sold" by 2026-05-19 [D]. Photon blog the same day says "330K Players" — conflict unresolved.
- Players [T]: Feb 3,337 avg → Mar 1,432 (−57%) → Apr 1,245 → May 865 → Jul 383 → Aug 467 (+22%, Abduction Update) → Oct 226.
- Launch hotfixes eased solo load (dirt −50%, customers −33%) [D]; Automation (Mar), Easter (Apr), "More Alien, More Sim" (May), Abduction (Aug), Autumn Update with Steam-Xbox crossplay (Nov, "final major update before... 1.0") [D].
- Monetisation: price rose $12.99 → $14.99 (date not found); no DLC [P]; free cosmetics; Shlorp plushie merch [D].

### Launch path & team
- 100k wishlists 2025-06-18; closed playtest autumn 2025 (~1,000 testers); demo ~Sep 2025: 114k players, 250k wishlists; by 2025-12-15 700k demo players, 430k wishlists, demo median 1h12m [D]. Next Fest participation not confirmed; cause of the Oct-Dec 2025 "blow-up" not stated.
- Lobbies friends/friend-of-friend only, no public matchmaking [D].
- Cybernetic Walrus, Belgium; co-founder Mike Coeck [T]; prior Antigraviator, Order 13 [T/D]; Photon Fusion [D], Unity [I]. "we released three patches in the first week of the demo alone" [D]; publisher Oro Interactive's role not described.

### Unknowns
- Team size, dev time, announcement/trailer date, viral driver, price-increase date, full-game session length, failure/reset rules, month-12 players (not yet reached), reconciling 730K copies vs 330K players.


---

## Scam Line (appid 2794590)
**Stratum:** mid | **Pair:** none | **Release:** EA 2026-01-10, 1.0 2026-11-03 [P] | **Price:** $6.99 (launch and current) [P] | **Players:** 4-8, no solo [P] | **Dev/Pub:** RavenJm / RavenJm + GAZE IN GAMES [P] | **Core type:** versus (social deception party rounds) | **Reviews:** 1,413 total, 84.3% positive (Very Positive) [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 2.09h / 2.31h / 1.13h [S] (n=1000 / 846 / 154) |
| <2h / >10h / >50h (all) | 46.7% / 3.4% / 0.2% [S] (n=1000) |
| Top 3 languages | Russian 34.0%, Turkish 22.6%, English 21.3% [P] |
| SteamCharts all-time peak | 2,155 (2026-03) [T] |
| Month 1 / 3 / 6 / 12 avg proxies | 205 / 312 / 101 / not yet (window starts 2026-12) [T] |
| Current players | 71 (2026-11-11) [P] |

### Core loop & inputs
- 4-8 players in separate rooms, unable to see each other, talk only through an in-game phone; short psychological rounds (Prisoner's Dilemma, room-number hunts, Russian roulette); "only one of you will win" [P store].
- Inputs: voice via phone (mic settings/mute added 2026-01-22 [D]), in-room movement, round-specific codes/numbers/words; 1.0 Roles mode (e.g. eavesdropping CIA Agent) [D].

### Interdependence & failure
- Players depend on each other for information and deals; most rounds score cooperation or deception between pairs [D].
- Failure = lost per-round points; Anonymous Mode hides scores until the end (0.7 [D]). What waiting/eliminated players do: not found.

### What it gets right
(n=748 codable positives) [S]
- Fun with friends 164; deception/bluffing 86; potential 54; good value 34; funny 32; unique concept 27; betraying friends 25.
- "10/10 if you want to develop trust issues, lose your friends, and question every decision"

### Where players push back
(n=892 codable) [S]
- Repetitive 43 (20 in negatives); too little content 39; bugs 31; needs friends 26; connection/lobby 23; "abandoned" 17; crashes 15; performance 12. Tech-failure mentions: 20.8% of codable negatives.
- "with less than 5 players this game is incredibly boring" / "No updates or communication since March and seems to be abandoned"
- <2h (n=418 codable): same mix; repetition (26) and crashes (7 of 9 in negatives) lead; 74% of negatives are <2h. >20h: only 10 codable reviews, mostly Russian/Turkish, citing a dead online and repetition [S]. Caveat: keyword coding misfires on Russian "скам" (scam) words for C15 [I].

### Sentiment over time
- Weekly histogram 85-91% positive Jan-Feb 2026; dip to 74% week of 2026-02-28; volume +81% week of 2026-03-21 (0.7 update) at 84% [P].
- Drift to ~67-78% Aug-Oct 2026 during the no-update gap; 1.0 week (2026-10-31) 31 reviews, 74% [P].

### What happened after launch
- 0.5.2 (2026-01-22: lobby list, mic settings, FR/KO/ES/PT) → Feb avg 240 (+41%) [T]; 0.7 (2026-03-19: 10 rounds, Anonymous Mode, ban list, GPU fix) → Mar 316, peak 2,155 [T].
- No updates May-Oct; avg fell 308 (Apr) → 66 (Oct) [T].
- 1.0 (2026-11-03: 40 rounds, Roles, pets, BepInEx mod support, DX11) → last 30 days 111 avg (+68%), week of 2026-11-05 +114% [T].
- Price unchanged; a reported 1.0 price rise not seen on store [P/T]. Paid OST $1.50 (2026-10-19); bundles incl. "Inspired by Buckshot" [P].

### Launch path & team
- No demo [P]; announcement/Next Fest not found. EA → 1.0 in ~10 months [D].
- RavenJm writes in first person, later "The team and I"; likely solo plus helpers [I]. Engine likely Unity (BepInEx) [I].
- "I spent a long time thinking about whether I should launch the game in Early Access." (2026-01-10 [D]); "we've delivered on every promise, 100%" (1.0 [D]).

### Unknowns
Session length; dead/waiting-player activity; cause of the Feb-Mar growth (streamers?); role of GAZE IN GAMES; location; prior games; discount and price history (blocked); wishlists.

---

## Backrooms: Extractions (appid 2835530)
**Stratum:** mid | **Pair:** P08 (vs Content Warning; filming-as-loot extraction) | **Release:** EA 2025-04-30, no 1.0 [P] | **Price:** $6.99 current; launch price not confirmed [P] | **Players:** 1-6 [P] | **Dev/Pub:** Headlight Studio (self-published) [P] | **Core type:** extraction | **Reviews:** 854 total, 73.5% positive (Mostly Positive) [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 4.31h / 4.97h / 2.59h [S] (census n=854 / 628 / 226) |
| <2h / >10h / >50h (all) | 21.0% / 14.8% / 0.9% [S] |
| Top 3 languages | English 41.0%, Russian 16.4%, Simplified Chinese 13.0% [P] |
| SteamCharts all-time peak | 368 (2025-05) [T] |
| Month 1 / 3 / 6 / 12 avg proxies | 90 / 52 / 49 / 31 [T] (Apr 2025 not tracked) |
| Current players | 10 [P] |

### Core loop & inputs
- M.E.G. agents enter Backrooms levels: find lost agents, solve instability puzzles, film entities for dossiers, transmit beacon data, hold out until extraction [P store].
- Inputs: move/sprint/crouch/mantle, hide spots, radial items, detector/PDA/paint gun/glowsticks/camera; voice-recording Fog Horn; built-in proximity-style voice plus radios that entities "listen" to [P/D].

### Interdependence & failure
- Shared: radio/voice comms (radios die in blackouts), signal transmission by any player, holding position together [P/D]. Smiler count scales with player count and difficulty [D].
- Failure: "the Backrooms keep what you brought" (gear permadeath); rank/storage persist; dead player's inventory drops for others [P/D].
- Dead players spectate (incl. late joiners) and return to the Lab when a living player arms the console [D].

### What it gets right
(n=542 codable positives) [S]
- Fun with friends 125; potential 81; atmosphere/visuals 78; monsters 77; horror 74; unique 30; value 28.
- "What really sold me was the atmosphere."

### Where players push back
(n=745 codable) [S]
- Bugs 114; repetitive 68; too little content 67; performance 33; crashes 32; connection/lobby 21; no tutorial 21. Tech-failure mentions 22.4% of codable, 37.4% of negatives.
- "Multiplayer Host gets disconnected 30% of the time and will collapse the whole session." / "The same monsters appear on every level, with no real evolution"
- <2h (n=159, 86 negative): bugs, boredom, crashes, "not scary" (5). >20h (n=35, 29 positive): potential and atmosphere praised; bugs (9) and thin content (5) still the top complaints [S].

### Sentiment over time
- Launch weeks 67-71% positive [P]; Jul 2025 update ~72-79%; Nov 2025 (stress-triggered entity) 88-100% [P].
- Rework months May-Jun 2026 fell to 61% / 54% (week of 2026-06-03: 40%) [P]; recovered to 75-91% after Aug 2026 voice/photo updates [P].

### What happened after launch
- ~35 patches in May 2025; 90 news items (74 patch notes) overall [P].
- Avg players: May 2025 90 → Jun 43 (−52%) → Jul 61 (+41%, sale + major update) [T/D]; Endless Loop mode (Sep 2025); update gap Dec 2025-Feb 2026 ("We're back!") [D].
- "Something Has Changed" rework (2026-05-04) with sentiment dip [P/I]; 30% off + double XP tied to Kane Pixels' Backrooms film (2026-05-27) gave no June lift [D/T].
- Aug 2026 +54% (peak 123) after Found Footage/voice updates, then Sep −54% [T]. Cosmetic M.E.G. Credits earned in-game; no paid DLC; cross-bundles with other indies [P].

### Launch path & team
- No demo [P]; announcement/Next Fest not found. Store uses YouTuber gameplay videos as trailers [P]. "sold over 30,000 copies in its first two months" [T, snippet].
- Headlight Studio, Castelnau-le-Lez, France; side project/"testing ground" for its main game Rooted [T]; Unreal Engine [I].

### Unknowns
Launch price; session length; team size and dev time; price history (blocked); cause of the Jan 2026 +24% bump; wishlists; developer interviews.

---

## EXPEDITION TO THE BACKROOMS (appid 3038290)
**Stratum:** flop | **Pair:** none | **Release:** EA 2025-07-20 [P] | **Price:** launch $7.99 → $4.79 (2025-07-25) [D]; current $5.99 [P] | **Players:** 1-6 (plus LAN co-op) [P] | **Dev/Pub:** 1_Cutter_1 (self-published) [P] | **Core type:** investigation | **Reviews:** 186 total, 66.1% positive (Mixed) [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 1.83h / 2.25h / 1.37h [S] (census n=186 / 123 / 63) |
| <2h / >10h / >50h (all) | 52.7% / 5.9% / 0.0% [S] |
| Top 3 languages | English 61.8%, Russian 25.3%, German 5.4% [P] |
| SteamCharts all-time peak | not found (SteamCharts HTTP 500, not tracked) |
| Month 1 / 3 / 6 / 12 avg proxies | not found |
| Current players | 0 [P] |

### Core loop & inputs
- Team wanders large liminal Backrooms levels, searching for clues and anomalies while avoiding 3 entities; two endings [P/D]. Developer framing: "a CO-OP WALKING SIMULATOR, with a bit of puzzles and entities" [D].
- Inputs: movement (overhauled 2025-07), interact, camera with flashlight, inventory and saves (2026-05), VOIP [D]; others not found.

### Interdependence & failure
- "Work together to navigate... search for clues" [P]; what exactly players depend on each other for: not found.
- Failure states and dead-player activity: not found. Demo ~45 min of play [D]; EA criticised as "very short compared to the DEMO" [D, quoting players].

### What it gets right
(n=121 codable positives) [S]
- Atmosphere/visuals 44 (36% of positives); horror 30; fun with friends 22; monsters 20; potential 18; value 12.
- "Playing with friends adds a layer of paranoia: we kept yelling each other's names"

### Where players push back
(n=181 codable) [S]
- Bugs 30; performance 22; too short 20; crashes 12; repetitive 12; lag 8; price not worth it 8 (7 in negatives); controls 7. Tech-failure mentions 28.2% of codable.
- "And the frame rate is terrible, you can't even see or move due to the lag." / "entirely too short and empty."
- <2h (n=94 codable, 41 negative): negatives led by performance (9), crashes (6), price (4). >20h: 1 review only, no pattern [S].

### Sentiment over time
- Launch week 63% (19 reviews), then 50% [P].
- Week of 2025-08-24: 46 reviews, 45 positive (97.8%), after the price cut; then near-zero, mostly negative weeks Sep-Oct 2025 [P]. Cause of the one-week burst not found [I: price cut or a community push].
- Rebuild weeks (late May-Jun 2026) 0-25% positive on small n [P].

### What happened after launch
- Day-1 crash hotfix and small fixes (2025-07-20/23) [P]; price cut 2025-07-25 "SO EVERYONE CAN PLAY... WITH FRIENDS!" [D].
- No updates Aug 2025-Jan 2026 (personal issues; "almost completely paused") [D]. Jan 2026 roadmap; 2 developers join [D].
- 2026-05-23 "completely rebuilt": character rework, voice actors, inventory/save [D]; sentiment fell [P]. Minor updates 06-04 and 06-22, then nothing [P].
- Current $5.99: date of rise from $4.79 not found. No DLC [P].

### Launch path & team
- Discord Jan 2025 → free demo 2025-02-15 (5 levels, 1 entity) → EA 2025-07-20 adding multiplayer [D]. Next Fest participation not confirmed.
- Solo lead "1_Cutter_1" plus "Abstract and Risensy" from 2026-01 [D]. "I want to sincerely apologize for the long silence and lack of updates." [D]

### Unknowns
Player counts (untracked); demo player numbers; wishlists; engine; location; failure/death design; reason for the Aug 2025 review burst; price history (blocked).

---

## Cargo Duty (appid 2766480)
**Stratum:** flop | **Pair:** P02 (vs Lethal Company; moon cargo runs) | **Release:** 2024-02-03 (full release, no EA) [P] | **Price:** A$3 (~US$2) at launch [D]; free since 2024-04-18 [D/P] | **Players:** up to 6, solo supported [P] | **Dev/Pub:** Carrot Studios (self-published) [P] | **Core type:** extraction | **Reviews:** 103 total, 68.9% positive (Mixed) [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 0.63h / 0.73h / 0.45h [S] (census n=103 / 71 / 32) |
| <2h / >10h / >50h (all) | 86.4% / 4.9% / 1.0% [S] |
| Top 3 languages | English 68.0%, Russian 6.8%, Polish 5.8% [P] |
| SteamCharts all-time peak | not found (HTTP 500, not tracked) |
| Month 1 / 3 / 6 / 12 avg proxies | not found |
| Current players | 0 [P] |

### Core loop & inputs
- Crew flies moon to moon collecting cargo, keeping creatures out of the ship with on-board countermeasures: "goofy horror resource management" [P store]. Framed as "How long will you survive?" [P].
- Inputs: not found beyond store text. One review mentions route planning, fuel and ship-state factors [S, untranslated Russian; I].

### Interdependence & failure
- What crewmates depend on each other for: not found.
- Failure and dead-player activity: not found; survival-length framing implies a run ends on crew death [I].

### What it gets right
(n=61 codable positives) [S]
- Very thin: fun with friends 4; atmosphere 3; free/value 3; monsters 3; funny 2; physics/chaos 2. Many positives are meme reviews (the "Throngle" creature).
- "0 issues loading in with a friend and tbh, throngler has changed my life."

### Where players push back
(n=89 codable) [S]
- Bugs 4; repetitive 4; no tutorial 3 (all negatives); performance 2; price 2 (ironic). Tech-failure mentions 6.7% of codable.
- "The player is given no guidance whatsoever in what they must do." / "it was fun for an hour then i got bored"
- <2h: 88 of 103 reviews, so the whole picture is first-session; >20h: 1 review only [S]. 96.9% of negatives were written under 2h [S].

### Sentiment over time
- Feb 2024: 6 reviews, 100% [P]. After going free: Apr 2024 15 reviews, 47%; May 18, 67%; Jun 8, 38% [P] — more players, lower sentiment [I].
- From Jul 2024: 1-7 reviews/month, mixed; last review 2026-08 [P].

### What happened after launch
- 2024-04-12 "LET ME BE FREE": switched from A$3 to free from 2024-04-18 [D]; the only monthly review peak followed [P].
- 2024-05-04 tiny update removed a ~1-in-a-million RNG achievement that "was going to be a setup for a sequel if the game did well" [D].
- No further posts; 2 news items total [P]. No DLC or monetisation [P].

### Launch path & team
- Announcement, demo, Next Fest, wishlists: not found. Self-published [P].
- Carrot Studios, contact "thatcarrotfella"; reads as solo [I]; Australia inferred from AUD pricing [I].
- "I have made the decision to switch the game from $3 AUD to absolutely free." [D]

### Unknowns
Player counts (untracked); core inputs and failure design; engine; team size; prior games; whether a sequel was made; price history (blocked).


---

## OCTOPinbs (appid 2660510)
**Stratum:** flop (corporate-backed) | **Pair:** none | **Release:** 2026-05-11 [P] | **Price:** $9.99 (20% off at launch) [P/D] | **Players:** 3-10 [P] | **Dev/Pub:** tri-Ace + Lasengle / Aniplex [P] | **Core type:** versus (wordless social deduction + action) | **Reviews:** 57 total, 71.9% positive [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 2.05 h / 2.42 h / 0.45 h [S] (n=57 census; 41 pos, 16 neg) |
| <2h / >10h / >50h (all) | 49.1% / 1.8% / 1.8% [S] (n=57); 93.8% of negatives <2h |
| Top 3 languages | Japanese 61.4%, English 17.5%, Korean 12.3% [P] |
| SteamCharts peak | not found (SteamCharts HTTP 500, not tracked) |
| Month 1/3/6/12 avg proxies | not found |
| Current players | 0 (2026-11-11) [P] |

### Core loop & inputs
- Octopus firefighters douse spreading fires on collapsing floors and stuff suspects into Octojars; squid "Hidden Artists" set fires while pretending to help and can reveal/transform for a comeback power-up. Ends at 0%/100% incineration or when one side is jarred [P store].
- Inputs: move, spray, attack/push, jar, escape restraint, peek into adjacent rooms, throw colour balls to mark suspects, emotes/stamps [D]. No meeting/discussion phase: cut because it "didn't pair well with fast-paced action" [D]. Voice chat: not found.

### Interdependence & failure
- Team fire containment; reading each other's behaviour instead of talking [D].
- 0 HP: become a "powerless, helmeted form" and run to the fire truck for a new body; jarred players are out but can spectate others' perspectives [P store]. Emotes usable while incapacitated (v1.3.0.0) [D].

### What it gets right
- Social deduction / bluffing 20, simple/easy to pick up 13, fun with friends 10, visuals/audio 6, monsters/enemies 5, fun with strangers 5 [S] (n=40 codable positives).
- "VERY FUN and also extremely easy to get into." (English review)
- Several reviewers specifically praise the no-meeting, no-voice design (theme quotes) [S].

### Where players push back
- Performance/FPS 10 (5 of 16 negatives), connection/lobby 5, lag/desync 3, dead game/no players 3, controls 3 [S] (n=56 codable). Technical-failure mentions in 43.75% of codable negatives [S]. C12 "price" hits (4) look like keyword false positives on inspection [I].
- "I can't find any matches, even after trying incessantly all these days."; "The game is capped at 60 FPS at most and keeps lagging." (English rendering in the review dataset).
- <2h (n=28, 15 neg): performance 6, connection 4, lag 3. >20h: only 1 review (positive) [S].

### Sentiment over time
- Week of 2026-05-12: 33 reviews, 60.6% positive [P histogram]; afterwards 0-3 reviews/week, mostly positive; last bucket 2026-08-25 [P]. The launch-week negatives (mostly <1h, tech) set the score [I].

### What happened after launch
- Matchmaking post at launch (region/language first, Auto Match ignores filters) [D]; 06-02/06-10 beginner defaults and room list showing in-progress rooms [D]; from 06-03 scheduled "OCTOPinbs TIME" JST evening sessions to get matches going [D] (low-concurrency signal [I]).
- Free costume DLC 2/3/4 (05-22, 06-26, 07-10); paid ARTIST COSTUME $2.99, COSTUME1 $4.99; Starter Bundle; trading cards [P/D]. Sales 30% x4 (Jun-Aug), 35% Autumn (10-01) [D].
- Solo Practice Mode 07-22 [D]; official Discord closed 08-31 [D]; last patch v1.3.2.1 on 10-29 [P].

### Launch path & team
- Store page 2026-03-09 (Gematsu/Automaton coverage [T]) -> AnimeJapan, INDIE Live Expo (date reveal 04-25), BitSummit PUNCH -> launch 05-11; two-month store-to-launch gap; no demo [P/D].
- Four developer Q&A posts. Director: wanted "to remove as many barriers as possible" of social deduction [D]. Team "youth-centered production structure" at tri-Ace [D]; Lasengle is an Aniplex subsidiary [T].

### Unknowns
- Concurrent players history, wishlists, Next Fest, team size, engine, dev time, session length, voice chat, sales/price history (blocked).

---

## RADIOACTIVE INC. (appid 3879670)
**Stratum:** flop | **Pair:** none | **Release:** 2025-09-19 [P] | **Price:** $1.99 (unchanged) [P] | **Players:** 1-4 (solo, online, LAN co-op) [P] | **Dev/Pub:** 45DK / Devotıon Labs [P] | **Core type:** escape_survival | **Reviews:** 30 total, 56.7% positive [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 0.99 h / 1.5 h / 0.93 h [S] (n=30 census; 17 pos, 13 neg) |
| <2h / >10h / >50h (all) | 73.3% / 3.3% / 0% [S] (n=30); 92.3% of negatives <2h |
| Top 3 languages | English 86.7%, Russian 6.7%, Turkish 6.7% [P] |
| SteamCharts peak | not found (HTTP 500, not tracked) |
| Month 1/3/6/12 avg proxies | not found |
| Current players | 0 (2026-11-11) [P] |

### Core loop & inputs
- Escape a deserted nuclear complex across 20 PS1-style horror levels: hide, collect clues, solve puzzles, find the exit [P store]. One reviewer describes light puzzles with machinery and locked areas [S].
- Inputs: not found (store text only).

### Interdependence & failure
- What players share, failure state and dead-player behaviour: not found. Reviews stress that fun "depends on who you're playing with" [S].

### What it gets right
- Good value/cheap 6, fun with friends 4, progression 2 [S] (n=16 codable positives). Most other praise hits come from one long descriptive review and look like keyword false positives [I].
- "Perfect for having fun with friends at a very cheap price fmo" (English review)

### Where players push back
- AI-generated art/code accusations 4 (all in negatives; 36% of codable negatives), not worth $2 2, clone/cash grab 2, unclear mechanics 2, bugs/connection/controls 1 each [S] (n=27 codable).
- "Also probably used ai for some in-game pictures and steam arts."; "Multiplayer doesn't seem to work, couldn't even get into a game."
- <2h (n=22): the same AI/low-effort/value complaints; positives cite price and friends. >20h: 0 reviews [S].

### Sentiment over time
- Launch week (2025-09-19): 15 histogram reviews, 80% positive; week of 10-03: 3 reviews, 0% [P]. Thereafter 1-2 reviews per bucket, mixed; last 2026-06-26 [P]. The slide from launch-week friends' reviews to strangers' negatives produced "Mixed" [I].

### What happened after launch
- No developer posts at all (GetNewsForApp 0 items) [P]. No DLC, no demo, price never changed (history blocked) [P]. Bundle "Party & Radioactive Pack" $5.38 at 10% off [P].

### Launch path & team
- Release 2025-09-19, no pre-launch posts found [P]. Developer 45DK; publisher Devotıon Labs (dotless ı suggests Turkish [I]); publisher role not found. A related app 3956540 surfaced but was not checked.

### Unknowns
- Inputs, co-op mechanics, failure, team size/location, engine, marketing, player counts, wishlists, any developer statement.

---

## Content Warning (appid 2881650)
**Stratum:** hit | **Pair:** P08 (vs Backrooms: Extractions; filming-as-loot extraction) | **Release:** 2024-04-01 [P] | **Price:** $7.99 (free first 24 h) [P/D] | **Players:** 2-4 (offline/single-player mode exists) [P] | **Dev/Pub:** five Landfall developers / "Evil Landfall?" [P] | **Core type:** extraction | **Reviews:** 164,372 total, 93.7% positive [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 5.27 h / 5.21 h / 6.22 h [S] (n=1000; 916 pos, 84 neg) |
| <2h / >10h / >50h (all) | 20.4% / 30.0% / 4.1% [S] (n=1000) |
| Top 3 languages | English 45.9%, Russian 25.9%, Simplified Chinese 4.3% [P] |
| SteamCharts peak | 63,320 (2024-04) [T]; dev claims >200K concurrent on free day [D] |
| Month 1/3/6/12 avg proxies | 15,678 / 7,257 / 2,881 / 2,334 [T] |
| Current players | 472 (2026-11-11) [P] |

### Core loop & inputs
- Dive into the "Old World" with a camcorder, film monsters and friends over 3 in-game days, upload to SpöökTube, hit the view quota to continue [P store].
- Inputs: move/sprint/crouch, working camera recording real footage, 3 item slots (flashlight, Reporter Mic, rescue hook, Sketch Pad, defibrillator), emotes, sit, ASCII face customiser, in-game voice captured in the footage [P patches].

### Interdependence & failure
- One camera per team; the footage is the shared score; shared ad money and view quota; everyone returns to the diving bell. Friends are the content [P].
- Missing the quota after 3 days ends the run [P]. Dying can lose the camera (permanently on day 3) [T]; one-use Defibrillator revives [T]. Dead-player activity: not found.

### What it gets right
- Fun with friends 181, monsters 108, streamer/clip-worthy 98, horror 84, funny 70, value 52 [S] (n=799 codable positives).
- "1000000000/10 i filmed my friends dying while laughing hysterically."

### Where players push back
- Bugs 55, repetitive 32, too short 25, needs friends/bad solo 25, dev abandoned 17, connection 13 [S] (n=879 codable). Technical failure in 32.5% of codable negatives [S].
- "It gets old quick"; "its a single player experience masquerading as…" (negative)
- <2h (n=192, 180 pos): praise dominated by friends and clip-worthiness; few complaints (repetitive 6, price 6). >20h (n=126): mods/workshop praise appears (6); bugs 12, too short 7, bad solo 7 [S].

### Sentiment over time
- Apr 2024 92.4% (11,556 histogram reviews); May-Jul ~93.5-94.6%; Nov 2024 97.3% (volume +182%, cause unknown; PANICORE shows the same jump [I]); slides to 88.6% (Jun 2025) and lows of 87.3%/85.8% (Nov/Dec 2025); 89.3% after console launch (Apr 2026), 89.5% Oct 2026 [P].

### What happened after launch
- Free-day virality, then decay: Apr 2024 avg 15,678 -> May 9,467 -> Jun 5,048 -> Oct 2,115 [T]; the 2024-05-02 big update did not reverse it.
- 2024-07-29 "last patch for a while" [D]; 2024-12-11 Workshop mods + controller + ping matchmaking (Dec +45%, also Winter Sale [I]); 2025-11-17 achievements, lobby codes, mute; 2026-04-01 console launch + crossplay = only post-launch spike >50% (Apr 1,687, +77%) [T/P]; 2026-10-19 Workshop disabled over "potentially malicious content" [D].
- No DLC; hats bought with in-game MC; bundles at 10% off [P]. Sales: 6.2M free claims in 24 h [D], 1M sold in ~2 weeks [T].

### Launch path & team
- Surprise-announced and launched the same day, 2024-04-01, free for 24 h; no demo, playtest or Next Fest [P/T]. Viral on TikTok/YouTube/Twitch during the free day [T]. PR: Future Friends, Popagenda [D].
- Five devs, Stockholm; built Feb-Apr 2024, mostly in a month-long game jam in Seoul [D]; Unity [P-derived]. "not a live-service or early access game ... any additional updates are a bonus" [D].

### Unknowns
- Real minutes per dive, dead/spectator behaviour, wishlists, discount history, exact free-day peak on SteamCharts (month-only data).

---

## Big Walk (appid 1478500)
**Stratum:** hit | **Pair:** none | **Release:** 2026-08-04 [P] | **Price:** $19.99 (25% launch discount to ~08-18) [P/D/T] | **Players:** 2-12, no solo [D] | **Dev/Pub:** House House / Panic [P] | **Core type:** hangout_no_fail | **Reviews:** 47,512 total, 94.7% positive [P] (Metacritic 91 [P])

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 11.57 h / 12.33 h / 6.82 h [S] (n=1000; 773 pos, 227 neg; sample 77.3% positive, skewed by 11-10 review bomb [I]) |
| <2h / >10h / >50h (all) | 11.2% / 56.9% / 0.5% [S] (n=1000) |
| Top 3 languages | English 72.8%, Simplified Chinese 8.8%, French 2.9% [P] |
| SteamCharts peak | 46,224 (2026-08) [T] |
| Month 1/3/6/12 avg proxies | 10,882 (Aug-Sep) / 4,721 (Oct) / not yet / not yet [T] |
| Current players | 2,271 (2026-11-11) [P] |

### Core loop & inputs
- Walk a big open world with friends solving communication puzzles; no fail state; "An Ending" [P store].
- Inputs: walk, "Arms!!" point/wave/gesture, distance-faded proximity voice and range-limited text chat, walkie-talkies, laser pointers, binoculars, megaphones, flares, whiteboards, cowbells, map, kick and carry other players [P/D]. Some segments remove speech.

### Interdependence & failure
- Puzzles need split roles and in-game communication; FAQ asks players not to use Discord or share a room [D].
- No failure state; challenges skippable [D]. Dead/waiting player: not applicable.

### What it gets right
- Fun with friends 342, visuals/atmosphere 156, teamwork/coordination 147, unique concept 87, proximity voice 81, simple 72, relaxing 72 [S] (n=750 codable positives).
- "This was a love letter to playing games with friends and being able to enjoy your time with them"

### Where players push back
- AI use 187 (130 in negatives = 58.3% of codable negatives, almost all from 11-10), bugs 109, repetitive 44, low effort 31, connection 30 [S] (n=973 codable). Refund mentions 47 [S].
- "This game had no notification on its store page that it used AI in its development."; "Big Walk has puzzles, and not much else."
- <2h (n=105, 39 neg): AI 19, bugs 14, missing settings 7. >20h (n=175): fun with friends 85, teamwork 39; AI 35, repetitive 13 [S].

### Sentiment over time
- Launch week 92.1% (voice-volume complaints) -> 95.7-98.0% after the 1.4.8 quiet-voice fix (Aug-Sep) [P].
- 10-13 week 91.5% after the BDS/Microsoft-boycott statement (49 negatives on 10-15 vs ~5/day) [P/T].
- 11-10 week 54.2%: review bomb (+426/-366 in a day) after LLM use disclosure ("well under 0.1%" of code) [P/T].

### What happened after launch
- Patches 1.4.8-1.5.1 (voices, networking, session passwords, volume sliders), 1.6.0 (alphanumeric codes, anti-modded clients, echo cancellation) [P].
- Players: Aug avg 15,720 -> Sep 6,044 (-62%, normal decay [I]); early-Oct daily peaks 12-19k, cause unknown (China Golden Week fits [I]).
- 1M copies first week [T]. No DLC/cosmetics; Big Walk + PEAK bundle 10% off [P].

### Launch path & team
- Announced 2023-12-07 [T]; trailer at Summer Game Fest 2025-06-06, slipped to 2026 [T]; press-only demo; no public demo/Next Fest [P]; date revealed in Nintendo Direct 2026-06-09 [T]; launch on PC/Mac/PS5/Switch 2 with crossplay, PS Plus [T]; #1-2 global top seller first two weeks [P].
- Five full-time staff, ~6 years, from a lockdown prototype [T]. "Goose Game has meant that we can afford a flop." [T, paraphrase risk]. Admitted proximity volume made it "easy to have a bad experience" [T].

### Unknowns
- Engine, wishlists, discount history, cause of the October spike, real effect of the AI disclosure on sales and players.


---

## PANICORE (appid 2695940)
**Stratum:** hit (random draw) | **Pair:** none | **Release:** 2024-05-31 (1.0, no EA) [P] | **Price:** $9.99 now; launched at $4.99 [T] | **Players:** 1-5 (4 in demo) [P] | **Dev/Pub:** ZTEK Studio / ZTEK Studio (self-published) | **Core type:** escape_survival | **Reviews:** 13,110 total, 78.8% positive (Mostly Positive) [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review, all / pos / neg | 4.36 h / 5.23 h / 1.6 h [S] (n=1000 / 763 / 237) |
| <2h / >10h / >50h (all) | 25.8% / 22.2% / 1.1% [S] (n=1000); negatives: 56.1% under 2 h |
| Top 3 languages | English 41.7%, Russian 21.7%, Turkish 4.3% [P] |
| SteamCharts all-time peak | 3,491 (2024-06) [T] |
| Month 1 / 3 / 6 / 12 avg proxies | 1,335 / 698 / 572 / 181 [T] (release month May 2024 missing) |
| Current players | 50 (2026-11-11) [P] |

### Core loop & inputs
- Urban explorers trapped in a building find items and use them at escape routes while an AI entity hunts by footsteps and real microphone voice [P store].
- Inputs: move/sprint (stamina)/crouch, hide in cabinets and shadows, throw objects, 1 flashlight per player ("due to trolls") [P 1.0.7], TAB inventory, medkit revive, proximity voice the monster hears (reworked 1.4), walkie-talkies (beta 2026-08), noise meter and "Voice Reuse" playback [P 1.4.9].

### Interdependence & failure
- Players split item-finding across the map, revive each other, and share risk: your voice endangers everyone [P].
- Permadeath within a round; "Try to escape alone or together" [P store]. Money bags unlock maps/skins; PAINCORE/PAINCORE+ difficulties [P].
- Dead players could talk before 1.4; a review asks to "go back to were you could talk while you are dead" [P review]. Spectating: not found.

### What it gets right
- Horror/tension 154, monsters 153, fun with friends 149, atmosphere 65, funny 51, proximity voice 49 [S] (n=676 codable positives).
- Voice-as-threat is the signature: "Whispering to your team so the AI does not hear you, then screaming..." [S].

### Where players push back
- Bugs 75, repetitive 35, too little content 29, connection/lobby 21, needs friends 19, unfair difficulty 18 [S] (n=894 codable). Technical-failure mentions in 22.0% of codable negatives [S].
- "Really unplayable past easy mode but on easy mode it's extremely boring." [S]
- <2h (n=228 codable, ~half negative): bugs 26, repetitive 11, price 7, clone/asset-flip 6. >20h (n=61, 55 positive): praise horror/monsters 16 each; few complaints (bugs 6) [S].

### Sentiment over time
- Jun 2024 80.2% (2,086 histogram reviews) → Jul 75.1% [P].
- Nov 2024 spike: 1,367 reviews at 90.5%, cause unknown [P/I].
- Long slide from 2025-07 (68.4%) to lows of 66.4% (Dec 2025, Snowbound 1.3) and 60.6% (Jul 2026) before the 1.4 AI/voice rewrite; Sep 2026 75.3%, Oct 68.5% [P].

### What happened after launch
- Ten patches in 11 days post-launch [P]. Maps: Submarine 1.1 (2024-10), Military Base 1.2 (2025-10), Snowbound 1.3 (2025-12), Ashmore Prison 1.5 announced for Nov 2026 [D].
- Monthly avg fell 1,335 (Jun 24) → 774 → 273 (Mar 25, despite 33% Spring Sale) → ~100 (2026) [T]. Content plus seasonal sales gave bumps (Oct 25 +48%, Dec 25 +32%) [T/I].
- 1.4 (2026-08-18) rewrote entity AI and voice "from scratch" [D]; with a Daily Deal, week of 08-20 +112% [P] — "highest player numbers this game has seen all year" [D].
- List price doubled $4.99 → $9.99 between Mar and Jul 2026 [T/I]; no dev post found. Supporter Pack $11.98; no paid cosmetics [P].

### Launch path & team
- Demo by early March 2024 (UE5 Nanite removed in performance patch) [T/P]; 1.0 three months later. Next Fest, wishlists, viral moment: not found.
- "Your two brothers at ZTEK Studio" [D]; first helper dev for 1.3 [D]; Unreal Engine 5 [I from patch notes]; prior game The Devourer: Hunted Souls [D/T]. Console (Xbox, PS5) confirmed for 2026 [D].
- "(I wish we could at least once do an update where everything works)" [D 1.2.0.1].

### Unknowns
Session length, spectator system, wishlists, announcement date, Next Fest participation, cause of Nov 2024 review spike, reason for price increase, console launch date, team location, sales.

---

## Sledding Game (appid 3438850)
**Stratum:** mid (random draw) | **Pair:** none | **Release:** 2026-04-30 (Early Access; Xbox/Game Pass day one [T]) | **Price:** $7.99 [P]; launch discount below $5 to May 14 [T] | **Players:** public/private lobbies "up to 50*" [P]; 30 per third parties [T] | **Dev/Pub:** The Sledding Corporation (solo dev "Max") / self-published | **Core type:** hangout_no_fail | **Reviews:** 3,472 total, 96.1% positive (Overwhelmingly Positive) [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review, all / pos / neg | 4.55 h / 4.72 h / 1.42 h [S] (n=1000 / 949 / 51) |
| <2h / >10h / >50h (all) | 24.6% / 24.5% / 4.0% [S] (n=1000) |
| Top 3 languages | English 81.5%, Russian 4.0%, Korean 2.6% [P] |
| SteamCharts all-time peak | 3,213 (2026-05) [T] |
| Month 1 / 3 / 6 / 12 avg proxies | 803 / 182 / 87 / not reached [T] (April release month folded into May) |
| Current players | 109 [P] |

### Core loop & inputs
- Sled down a social hill, do tricks and races, play minigames, earn points for cosmetics, hang out in proximity chat [P store].
- Inputs: sled/steer/tricks, build ramps, ragdoll, shove, snowballs, darts, curling, bowling, s'mores, fishing, lanterns/binoculars, hide-and-seek and Infection Tag (Oct 2026), radio/party chat, customizable animals [P/D].

### Interdependence & failure
- Nothing obligatory; races and minigames are optional; some sleds seat more than one player [S quote].
- No failure state: the yeti kicks wanderers back onto the course [P]. Dead player: not applicable.

### What it gets right
- Fun with friends 235, relaxing/cozy 169, visuals/audio 118, potential 57, value 49, funny 47 [S] (n=837 codable positives); strangers/community also coded.
- "30 player lobbies for under $10." [S]

### Where players push back
- Bugs 58, too little content 21, repetitive 21, performance 18, needs friends 15, lag 14 [S] (n=886 codable). Technical failure in 46.9% of codable negatives (n=49) [S].
- "There has still not been a bugfix patch more than 3 MONTHS after release." [S]; "Barebones Unity sloppa." [S]
- <2h (n=214): performance 12, bugs 11, controls 6. >20h (n=101, 96 positive): fun with friends 35, cozy 31, community 11; complaints only bugs 7, repetitive 6 [S].

### Sentiment over time
- Weekly buckets: launch week 1,517 reviews at 97.8%; volume fell -66%, -60%, -54% over the next three weeks [P].
- By month: May 96.2% → Jun 91.6% → Jul 92.3% → Sep 90.9% → Oct 92.4% [P]. Dip coincides with the 4+ month gap before the first fixes update [I].

### What happened after launch
- "100,000 copies sold ... in 5 days" [D 2026-05-05].
- Jun avg 216 (-73%) after discount end and decay [T/I]; Sep 82.
- 2026-09-21 fixes/QoL (save slots, ban notices); 2026-10-23 night mode, Halloween map, minigames, fishing: week of 10-22 +198% [P], Oct 91 (+11%) [T].
- Paid DLC: Supporter Pack $2.99, Soundtrack $4.99 [P]; cosmetics earned through play [S quote]. Game Pass likely diverted players off Steam [I].

### Launch path & team
- Social-video virality (Instagram/TikTok, Dec 2024-Jan 2025) before the Steam page [D]; 530k+ Instagram followers [T].
- Page 2025-01-09: 15k wishlists day one, 100k in ~9 days, 200k by Jul 2025 [D]. Demo Sep 2025 (public lobbies pulled, then demo removed), withdrew from Oct 2025 Next Fest, joined Feb 2026 Next Fest, Triple-i date reveal [D].
- Solo US dev, Unity, "my first ever video game", ~1.3 years to EA, planned 12 months EA [D/T]. Turned down publishers: calls cost "long, focused work sessions" [D].

### Unknowns
Real lobby cap, session length, Xbox player numbers, launch-discount depth (sources differ), wishlist count at launch, cross-play status (a review says Steam/Xbox cannot play together), sales after day 5.

---

## Mama's Sleeping Angels (appid 2918310)
**Stratum:** mid (random draw) | **Pair:** none | **Release:** 2026-03-11 (1.0) [P] | **Price:** $9.99 [P] | **Players:** 1-4; uncapped via experimental host launch option [P] | **Dev/Pub:** itamu (solo) / Oro Interactive | **Core type:** escape_survival | **Reviews:** 1,378 total, 93.6% positive (Very Positive) [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review, all / pos / neg | 3.45 h / 3.68 h / 0.85 h [S] (n=1000 / 938 / 62) |
| <2h / >10h / >50h (all) | 31.9% / 19.4% / 0.3% [S] (n=1000); negatives: 80.6% under 2 h |
| Top 3 languages | English 72.7%, Russian 17.6%, Brazilian Portuguese 2.4% [P] |
| SteamCharts all-time peak | 476 (2026-03) [T] |
| Month 1 / 3 / 6 / 12 avg proxies | 85 / 31 / 17 / not reached [T] |
| Current players | 14 [P] |

### Core loop & inputs
- Enter procedural Y2K dream worlds, collect cursed objects to a team quota, fight monsters with guns, then "feed Mama" against a timer to clear the layer [P store/patches].
- Inputs: sprint/crouch/jump, sniper/FAMAS/chainsaw/rocket launcher (rocket-jump), pogo stick, flip phone (analyse curses, ping to Mama, call numbers), masks, kiss-to-heal, proximity VOIP plus radio, text chat [P].

### Interdependence & failure
- Shared quota, timed group feeding stage, healing by kissing [P].
- Failing to feed Mama loses the run; since 2.0 only progress toward waking new friends is lost [P/S quote]. Full playthrough ~14 h (one review) [S].
- Dead players become invincible ghosts that cannot carry items, can draw aggro and are revived for feeding [S quotes].

### What it gets right
- Visuals/audio/atmosphere 204, fun with friends 132, horror 83, unique concept 76, monsters 65, progression 41 [S] (n=864 codable positives); "also good solo" coded too.
- "If you had a Tumblr in the 2010s you will probably vibe with this game's aesthetic." [S]

### Where players push back
- Too little content 40, bugs 35, unclear/no tutorial 28, repetitive 20, performance 16, needs friends 13 [S] (n=923 codable); clone complaints ("quota slop") appear among negatives (5 of 59) [S].
- "It's just another lethal-company-like with slightly interesting visuals." [S]
- <2h (n=301, mostly positive): repetitive 13, bugs 11, unclear 10. >20h (n=33, all positive): aesthetic 13, friends 10; asks for more content (4) [S].

### Sentiment over time
- Monthly (weekly buckets rolled): Mar 94.0% (485) → Apr 91.8% → Jun 94.1% (2.0 bump, 119) → Aug low 83.7% (43) → Sep 93.3% [P]. Stable high; volume decay is the main signal.

### What happened after launch
- Daily patches first week: lobby joining, solo-scaled feed timer, text chat, uncapped lobbies [P].
- Apr: seeded runs, story-mode difficulty (damage -99%), quota fix [P].
- 2026-06-05 MSA 2.0 (broken dream worlds, modifiers, new monster, Doll, softer loss): Jun avg 34 (+21%) [T/P]. No posts since; dev reply quoted: "no concrete plans" for more content [S].
- Players: Mar 128 → Apr 41 (-68%) → Oct 17 [T]. No paid cosmetics; Soundtrack $8.99; Oro bundles [P].

### Launch path & team
- Kickstarter Nov-Dec 2024 ($15k goal [T]; 40% funded at one point, video 255k views [D]); outcome not verified.
- Playtest Nov 2025 → demo Jan 2026 → Feb 2026 Next Fest → 1.0; wishlists 8k → 50k in two months [D].
- Solo self-taught dev, ~3 years of work [D]; music by crisp and Gecko Afterlife [D]. "I don't think I have this dog in me" [D launch post].

### Unknowns
Kickstarter result, publisher's role, launch discount, engine, location, normal round length, sales, public-lobby health beyond one review ("kinda dead"), cause of Sep 2026 +66% week.

---

## Chained Wheels (appid 4243690)
**Stratum:** mid (random draw) | **Pair:** none | **Release:** 2026-03-27 (1.0, no EA) [P] | **Price:** $4.99, no DLC [P] | **Players:** exactly 2, no single-player [P]; local co-op added May 2026 [P] | **Dev/Pub:** Karga Games / Teneke Kafalar Spotlight, Karga Games | **Core type:** climbing_traversal | **Reviews:** 792 total, 70.3% positive (Mostly Positive) [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review, all / pos / neg | 3.1 h / 3.33 h / 1.85 h [S] (census n=792 / 557 / 235) |
| <2h / >10h / >50h (all) | 29.0% / 2.5% / 0.0% [S] (n=792) |
| Top 3 languages | English 33.2%, Russian 28.8%, Turkish 15.3% [P] |
| SteamCharts all-time peak | 847 (2026-04) [T] |
| Month 1 / 3 / 6 / 12 avg proxies | 107 / 39 / 13 / not reached [T] (March release month missing) |
| Current players | 1 [P] |

### Core loop & inputs
- Two players each drive an off-road car permanently chained to the other through physics obstacle courses and weather biomes; one mistake costs both [P store].
- Inputs: throttle/brake/steer, the chain, gamepad (May 2026), colour choice; voice not listed on store [P/I].

### Interdependence & failure
- The chain is the entire interdependence; clutch plays like wrapping the chain round a tree [S quote].
- Game Over screen, sparse checkpoints on map 1, easy/normal/hard, leaderboards [P/S]. Both respawn together; no dead-player state [S].
- Runs are short: one map ~1 h; "5-6 hours of fun" overall [S].

### What it gets right
- Fun with friends 118, good value 81, funny 73, physics chaos 66, rage-as-fun 38 [S] (n=503 codable positives).
- "This game had the perfect amount of janky physics that just made it a laughing fest with friends." [S]

### Where players push back
- Bugs 107, too short 59, performance 25, crashes 22, price 21, repetitive 20; checkpoint/progress loss 13 among negatives [S] (n=717 codable). Technical failure in 37.4% of codable negatives [S].
- "physics are random and the little car gets thrown randomly" [S]
- <2h (n=213, majority negative): bugs 28, crashes 15, performance 14, price 12 — "a 10 minute disaster, even for $5" [S]. >20h: one review, no codable content [S].

### Sentiment over time
- Monthly (weekly buckets rolled): Mar 68.3% (227) → Apr 66.4% (lowest weeks 59.3%) → May-Jul ~67-69% → Aug 87.5% (n=16) → Oct 80.0% (40) [P]. Small-n recovery after content updates [I].

### What happened after launch
- 2026-04-03 fixes; 05-04 "Play Together" (gamepad, local co-op): May avg 40 (-63%) [T].
- 06-25 MOON map (week 76.9% positive); 07-23 rejoin last session, trading cards, physics; 08-14 backend moved Steamworks → EOS for consoles/crossplay [P/D].
- 10-01 Pirate Island: week +137%, Oct avg 15 (+36%) [T/P].
- Price unchanged; label cross-promo bundles at 10% [P/I].

### Launch path & team
- Demo app exists (third-party snapshot "Very Positive (64)") [T]; Next Fest flagged but edition not verified; no EA.
- Turkish studio of three childhood friends founded 2022, prior mobile games, first PC title [T].
- Only statement: EOS move "prepares Chained Wheels for its upcoming console versions" [D].
- No matchmaking described; a player found a partner via Reddit [S].

### Unknowns
Demo dates, Next Fest edition, wishlists, announcement, viral moment, engine, sales, console dates, why the review mix is weighted to Russian/Turkish.


---

## Innchanted (appid 1369720)
**Stratum:** flop (random draw) | **Pair:** none | **Release:** 2023-03-28 [P] | **Price:** $19.99, 0% discount on 2026-11-11 [P] | **Players:** 1-4, online + local split-screen, AI companion for solo [P] | **Dev/Pub:** DragonBear Studios / Twin Sails Interactive [P] (some listings say Asmodee Digital [T conflict]) | **Core type:** job_simulation (magical inn) | **Reviews:** 175 total, 82.3% positive (Very Positive) [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review, all / pos / neg | 4.03 h / 4.53 h / 1.63 h [S] (census n=175; 144 pos, 31 neg) |
| <2h / >10h / >50h (all) | 29.1% / 18.3% / 0.6% [S] (n=175); negatives 58.1% under 2 h |
| Top 3 languages | English 72.0%, Simplified Chinese 9.7%, Korean 5.1% [P] |
| SteamCharts all-time peak | 124 (2023-04) [T] |
| Month 1 / 3 / 6 / 12 avg proxy | 20.5 / 5.2 / 6.0 / 5.9 [T] (calendar-month proxies; Mar-2023 row missing) |
| Current players | 0 (2026-11-11) [P] |

### Core loop & inputs
- Overcooked-like inn management over 50+ daily levels: serve food and potions, fish, cook, defend from monsters, upgrade with shells; evenings are a calm hub with 5 night activities [P store].
- Inputs: carry and throw items, brew, cook, fish, fight; decorate the inn (60+ items) [P]. Voice/text chat: not found.

### Interdependence & failure
- Shared stations and orders in a kitchen-rush format; inn layout changes daily [P]. One reviewer: higher difficulties feel "made to play with 4 people" [S].
- Failure: not found (probably a star/score fail per level [I, unverified]). Dead-player behaviour: not found.

### What it gets right
- Praise (codable positives n=140) [S]: Fun with friends 50; visuals/audio/atmosphere 44; funny 18; unique concept 12; relaxing/cozy 12; lots of content 11.
- Quote: "The cute story is definitely worth hearing and I think the characters are easy to fall in love with" (EN).

### Where players push back
- Complaints (all codable n=171) [S]: bugs 13 (7 of 31 negatives); too short 9 (all in positives); repetitive 9; needs friends/bad solo 9; controls 9 (6 in negatives); lag/desync 7; performance 6. Technical failure in 35.5% of codable negatives.
- "In it's current state, the game has a lot of bugs." / "the controls are just floaty and unrefined." (EN negatives)
- <2h (n=50 codable, 18 neg): controls 6, bugs 5, lag 5, needs friends 5, price too high 3 (all negatives), refund mentions 4. >20h (n=10, all positive): visuals 5, funny 3; complaint is "too short" 3 [S].

### Sentiment over time
- Histogram [P]: launch month 90.6% (32), Apr 84.2% (19), then single-digit monthly volumes, mostly positive; Jun-Jul 2023 dip to 75%/67%. Histogram sums 121 vs 175 total (Steam-purchase subset). No clear cause-linked shift [I].

### What happened after launch
- 2023-05-22 bug fixes; 2023-08-17 desync rollback, QoL, early-game difficulty; 2023-11-21 Steam Awards "Better With Friends" vote push [D]. No developer posts after Nov 2023.
- SteamCharts [T]: May 2023 -74% (20.5 to 5.3); Sep 2023 8.6 (cause unknown, possibly a sale [I]); Mar 2024 8.0 then -62%; under 4 avg from Apr 2024; last 30 days 0.74. 19 months missing in table.
- Price unchanged at $19.99; Soundtrack DLC $9.99 (2023-12-15) [P]. Discount history blocked.

### Launch path & team
- Shown at PAX Australia 2019 as "Chaos Tavern"; ACMI X residency / Audience Lab; Steam teaser Jul 2020; publisher partnership Jun 2021; release Mar 2023 (~3.5 years public-to-release) [T/D]. No demo, no Next Fest [P].
- Melbourne, 8 people in 2020 [T]; "our first game" [D]; Indigenous cultural advisor [T].
- On renaming: "We stripped every single type of connotation of alcohol out due to feedback" [T Byteside].

### Unknowns
- Engine, session length, failure state, dead-player state, voice chat, discount/price history, wishlists, sales, cause of Sep 2023 / Mar 2024 bumps, publisher identity conflict.

---

## Treasure Hunters: Raid Together (appid 2835460)
**Stratum:** flop (deliberate pair) | **Pair:** P03 (R.E.P.O.-like) | **Release:** 2026-03-11 [P] | **Price:** $9.99 list, $6.49 (-35%) on 2026-11-11 [P] | **Players:** 1-4, online + LAN co-op [P] | **Dev/Pub:** Biax (solo) / PlayWay S.A. [P] | **Core type:** extraction | **Reviews:** 98 total, 85.7% positive (Very Positive) [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review, all / pos / neg | 1.69 h / 1.88 h / 1.35 h [S] (census n=98; 84 pos, 14 neg) |
| <2h / >10h / >50h (all) | 53.1% / 7.1% / 1.0% [S] (n=98) |
| Top 3 languages | English 46.9%, Turkish 20.4%, Russian 6.1% (French also 6.1%) [P] |
| SteamCharts all-time peak | 46 (2026-03) [T] |
| Month 1 / 3 / 6 / 12 avg proxy | 7.2 / 2.8 / not found (Aug-Sep 2026 rows missing) / window not yet reached [T] |
| Current players | 4 (2026-11-11) [P] |

### Core loop & inputs
- Indiana Jones-style co-op raid of procedural dungeons: grab the main artifact and valuables, sell for gear, unlock larger dungeons [P].
- Inputs: sprint/jump (stamina), slide, crouch, vault, lean, whip and swing, kick, pistol, sword, dynamite, torches, throwable backpack; heavy treasure slows you; bandage/revive; proximity voice; controller only from v1.2 (2026-11-10) [P].

### Interdependence & failure
- Co-op puzzles "that require cooperation", shared loot value, reviving teammates [P]. Enemy credits scale with player count [P 1.0.1].
- Failure: death with ragdoll and revive; respawn with "adrenaline effect" (v1.1); money carries over; leaderboards [P]. Dead players: free-movement spectator plus spectating others [P]; a bug let "Players could hear dead players" (fixed 1.0.4) [P].

### What it gets right
- Praise (codable positives n=83) [S]: fun with friends 38; visuals/atmosphere 13; potential 10; funny 9; monsters 9; good value 7.
- Quote: "And yet… somehow… it's stupidly fun with friends." (EN)

### Where players push back
- Complaints (codable n=97) [S]: bugs 8; performance 4; too short 4; repetitive 4; controls 4; connection 3; lag 2 (both negative, Chinese). Technical failure in 42.9% of codable negatives.
- "The animations however are clunky, the physics are questionable" / "need more work especially in performance" (EN).
- <2h (n=52, 9 neg): controls 3, performance 3, too short 2, repetitive 2. >20h (n=5, all positive): fun with friends 4, relaxing 2; "too short" 2, grindy 1 [S].

### Sentiment over time
- Launch week 93.1% (29), week 2 88.9% (9), then 1-3 reviews/week, increasingly mixed: Apr-Oct weeks often 0-50% [P histogram]. Decline coincides with shrinking, later-arriving audience and netcode complaints [I].

### What happened after launch
- 9 patches 2026-03-12 to 03-26 incl. economy rework (items unlocked by money, "Thanks to Tomato on Twitch") [D].
- 2026-03-28: "The sales are way below my expectations" [D]. v1.1 (05-10): character creator, leaderboards, promotion system, "no microtransactions" [D]. 08-01: "reached 5000 copies" [D]. 09-27: next game announced. v1.2 (11-10): controller, netcode/desync fixes.
- SteamCharts: Apr -68.6% (11.0 to 3.5), May 3.3, Jun 2.4; later months missing [T].
- Bundles with PlayWay sims at 10%; free Prologue (Jul 2025); no DLC [P/D].

### Launch path & team
- Announced ~early 2024; demo Nov 2024; Four is a Party (Dec 2024), Couch Co-op Fest (Feb 2025, PlayWay publishing announced), Next Fest Jun 2025 (15 languages), Prologue Jul 2025, Discord beta Oct 2025, 1.0 Mar 2026 after "3 years"; no EA [D].
- Solo dev, likely Turkey and Unreal [I]. "I started this journey as an Indiana Jones fan" [D].

### Unknowns
- Wishlists, session length, weaker-player handling, publisher's marketing role, price/discount history, m6/m12 player data.

---

## Servonauts (appid 2514400)
**Stratum:** flop (random draw) | **Pair:** none | **Release:** 2024-11-21, PC + Switch [P/T] | **Price:** $14.99 [P] | **Players:** 1-4, local couch co-op; online only via Steam Remote Play Together [P] | **Dev/Pub:** MAXART Games / Untold Tales, GamerSky [P] | **Core type:** job_simulation (space gas station) | **Reviews:** 54 total, 81.5% positive (Very Positive) [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review, all / pos / neg | 2.94 h / 3.13 h / 0.87 h [S] (census n=54; 44 pos, 10 neg) |
| <2h / >10h / >50h (all) | 40.7% / 1.9% / 0.0% [S] (n=54); negatives 80% under 2 h |
| Top 3 languages | Simplified Chinese 55.6%, English 35.2%, Traditional Chinese 3.7% [P] |
| SteamCharts all-time peak | not found (steamcharts HTTP 500; likely untracked [I]) |
| Month 1 / 3 / 6 / 12 avg proxy | not found |
| Current players | 0 (2026-11-11) [P] |

### Core loop & inputs
- Overcooked-like levels: refine fuel, connect wobbly physics pipes, mix colour-coded fuels to serve space cars; aim for 3 Gold Stars [P].
- Inputs: move, grab/carry/throw, plug/swap pipes, build menu (pipes, drills, refineries, orbital laser), hats; controller-first [P]. No built-in voice/text [I].

### Interdependence & failure
- Shared pipes and machines; teammates can help or sabotage [T 80.lv]. Solo gets a helper vacuum and shorter builds [P/T].
- Failure: per-level star rating; players can "die hilariously" (lava, explosions) [P]. Respawn and waiting-player behaviour: not found. About 3 h to 3-star everything (one review) [S].

### What it gets right
- Praise (codable positives n=44) [S]: fun with friends 20; funny 9; teamwork 8; potential 7; simple to pick up 6; visuals 5.
- Quote: "It's like a mix of Overcooked and Moving Out, but with its own unique puzzle twists" (EN).

### Where players push back
- Complaints (codable n=54) [S]: performance 6; too short 5; bugs 3; repetitive 3; lag 2; no tutorial 2 (Chinese reviews). Technical failure in 30% of codable negatives.
- "Multiplayer relies on Remote play which is a dealbreaker for me" (EN, from batch profile); "a single player with added lazy multiplayer aspects." (EN).
- <2h (n=22, 8 neg): lag 2, performance 2, repetitive 2. >20h: no reviews [S].

### Sentiment over time
- Launch week 28 up / 1 down (96.6%); afterwards 0-3 reviews per week, scattered negatives (Dec 2024, Jan 2026, Sep 2026) [P histogram]. No meaningful later trend; the game stopped generating reviews [I].

### What happened after launch
- No developer patches: all 44 news items are publisher sale/bundle/festival posts (Winter Sale 2 weeks after launch, Couch Co-op Fest Feb 2025, up to -85% catalogue Oct 2025, Steam Awards nomination push) [P].
- DLC: Soundtrack $1.99, Artbook $4.99; Deluxe and Untold Tales bundles [P]. 60% off snapshot ($5.99) [T]. 11.1% of sample received the game free [S]; Remote Play lets one copy cover 4 players, likely suppressing sales [I].

### Launch path & team
- Announced Feb 2024; Feb 2024 Next Fest with Twitch creators; World 3 playtest; Gamescom and PAX Aus 2024; publisher signed 2024-10-01 (7 weeks before launch); demo overhaul 9 days pre-launch [P/T].
- Brisbane; serious-games studio since 2016, first entertainment title; ~2 years dev; possible Screen Australia funding [T].
- "One of our goals with Servonauts was to create a couch co-op experience" [T Qualbert].

### Unknowns
- Player counts, engine, sales, wishlists, respawn rules, exact discount history, why no native online was built.

---

## Nightfall Secrets (appid 3356970)
**Stratum:** flop (random draw) | **Pair:** none | **Release:** 2025-06-11 [P] | **Price:** $5.99 (earlier $6.99 per SteamDB snippet [T]) | **Players:** 1-4, solo allowed [P] | **Dev/Pub:** Lonely Horror (self-published) [P] | **Core type:** escape_survival | **Reviews:** 27 total, 29.6% positive (Mostly Negative) [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review, all / pos / neg | 0.57 h / 0.95 h / 0.37 h [S] (census n=27; 8 pos, 19 neg) |
| <2h / >10h / >50h (all) | 88.9% / 7.4% / 0.0% [S] (n=27) |
| Top 3 languages | English 40.7%, Korean 22.2%, Russian 18.5% [P] |
| SteamCharts all-time peak | not found (HTTP 500; not tracked) |
| Month 1 / 3 / 6 / 12 avg proxy | not found |
| Current players | 0 (2026-11-11) [P] |

### Core loop & inputs
- "4v1" PvE: up to 4 players complete randomised objectives (e.g. levers) to open an escape route before a sound-reactive AI entity catches them [P store].
- Inputs: move, sprint, item slots (keybinds added by hotfix), flashlight, droppable noisy items, proximity voice that the AI hears [P/S].

### Interdependence & failure
- Split objectives and shared escape route; voice is both coordination and risk ("sensitive the monster is to your voice") [S].
- Failure: caught means death; difficulty levels ("Medium" renamed "Nightmare" and toned down) [P]. Run reset assumed [I]. Dead-player behaviour: not found.

### What it gets right
- Praise (codable positives n=8) [S]: fun with friends 3; horror/tension 3; good value 2; monsters 2.
- Quote: "Screamed, panicked, and laughed with my squad." (EN)

### Where players push back
- Complaints (codable n=24) [S]: bugs 4; price not worth it 2; asset flip 2; one each for performance, too short, repetitive, mic/voice, missing settings. Technical failure in 31% of codable negatives.
- "This game is literally unplayable." / "You die within the first 10 seconds due to the entity spawning next to players" (EN).
- Russian review notes "only 2 maps" and a 30-minute game [batch profile translation]. <2h covers 24 of 27 reviews, so it is effectively the whole picture; >20h: no reviews [S].

### Sentiment over time
- Histogram weeks Jun-Jul 2025: 0 up / 9 down; first positives only in Nov-Dec 2025; then ~1 review/month, mostly negative [P]. Launch-day positives in the sample (5, some "Got it for free") do not appear in the histogram, consistent with it counting Steam purchases only [I].

### What happened after launch
- Hotfixes 06-13 (menu, lobby overhaul, tips), 06-14 (keybinds, difficulty), 06-15 (enemy spawn moved "to give players more time"), 06-27 AI hearing/footstep balancing; no posts since (abandoned 16 days after launch) [P].
- Price $5.99; -80% ($1.19) snapshot [T]; demo app 3432730 [P]; no DLC.

### Launch path & team
- Demo before launch; no Next Fest found; self-published [P]. "Lonely Horror Studio" [D]; nothing else known.

### Unknowns
- Team location/size, engine, prior games, demo dates, announcement date, wishlists, player counts, matchmaking for strangers, session length (only reviewer estimates), price history.
