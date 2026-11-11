# Deep-study game profiles (80 games)

Parts 1-4 combined. Tag key: [P] verified primary, [D] developer claim, [T] third-party estimate, [I] inference, [S] computed from review sample (n given).

# Friendslop deep-study game profiles - part 1 (batches 1 and 2, 20 games)

Sources: deep_profiles_batch_1.md / deep_profiles_batch_2.md, data/deep_study_numbers.csv, data/deep_study_selection.csv, data/deep/{appid}/summary.md + themes.md, layer2_review_themes.md, layer2_tooling_method.md. No new web research.

Tags: [P] verified primary (Steam) | [D] developer claim | [T] third-party (SteamCharts, press, wikis) | [I] inference | [S] computed from review sample (n=...).

Method caveats (apply to every profile):
- Review sample: games with >1,000 reviews use 500 newest + 500 most-helpful (not random; helpful stratum over-represents launch-era, long, joke and negative reviews; recent stratum over-represents late/sale buyers). Games with <=1,000 reviews are a census. Sample % positive can therefore differ from the store figure.
- Theme counts are multilingual keyword matches (codebook v1). Praise is counted on codable positive reviews, complaints on all codable reviews. Overall precision about 0.77-0.86; P17 "unique" and P09 "simple" over-count; German/French/Portuguese/Turkish recall is low; sarcasm is coded literally. Obvious false positives are flagged.
- Month-N players = SteamCharts calendar-month average(s) overlapping the window (proxy, not an exact window average). Monthly % positive comes from the Steam review histogram (about the Steam-purchase subset; compare months with each other).
- Price history was blocked for every game (SteamDB 403, gg.deals 403, IsThereAnyDeal client-side).

Order: batch 1 (Lethal Company, Chained Together, LOCKDOWN Protocol, Fast Food Simulator, Bogos Binted?, Doll Impostor, Dumb Ways to Build, S.E.M.I., OK Boomer, Out of Stock!), then batch 2 (R.E.P.O., Liar's Bar, Nuclear Nightmare, Sneak Out, Hospital 666, Backroom Company, Airport Security Sucks!, Foodslingers, Cafe Crew Simulator: Prologue, Lamentations).

---

## Lethal Company (appid 1966720)
**Stratum:** hit | **Pair:** P02 (vs Cargo Duty) | **Release:** EA 2023-10-23, still EA [P] | **Price:** $9.99 [P] | **Players:** 4 official [T], mods to 32 [T headline] | **Dev/Pub:** Zeekerss / Zeekerss [P] | **Core type:** extraction | **Reviews:** 511,826, 96.9% positive [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 13.98h / 13.52h / 23.36h [S] (n=1000 / 944 / 56) |
| <2h / >10h / >50h (all) | 8.2% / 57.6% / 23.7% [S] |
| Top 3 languages | English 67.6%, Russian 8.7%, Simplified Chinese 3.5% (92.8% pos, lowest big language) [P] |
| SteamCharts all-time peak | 239,369 (2023-12) [T] |
| Month 1 / 3 / 6 / 12 avg proxies | 20,005 (Oct-Nov 23) / 101,205 (Dec 23-Jan 24) / 25,326 (Mar-Apr 24) / 14,714 (Sep-Oct 24) [T] |
| Current players | 2,778 (2026-11-10) [P] |

### Core loop & inputs
- Crew lands on moons, loots scrap from facilities while avoiding creatures, carries it to the ship and sells it to meet a rising quota every 3 in-game days [P store; T].
- Inputs: proximity voice/text [T], 4 scrap slots plus a utility slot (V80) [T/P], typed ship-terminal commands (radar, doors, turrets) [P], store tools (flashlight, shovel, walkie, stun grenade), bestiary scanning [P].

### Interdependence & failure
- The "computer guy" on the ship guides the team by radar and unlocks doors remotely [P store]; V70 explicitly buffed that role [D]. Scrap only counts once it reaches the ship [T].
- A dead player stays dead for the day; a full wipe loses the day's scrap; a missed quota ejects the crew and resets the run [T]. Dead players spectate (widely reported, not verified from a primary source); no mini-game found.

### What it gets right
- Praise among codable positives [S] (n=846): fun with friends 150, monsters 107, horror/tension 103, funny 93, progression/quota 62, atmosphere 55, value 52, proximity voice 51, mods 48.
- "I love watching my friends turn into 5 star voice actors."

### Where players push back
- Complaints, all codable [S] (n=898): bugs 45, needs friends 29, "abandoned" 26 (mostly false positives: "abandoned buildings/facilities" [I]), repetitive 24, too short 18, connection 17, performance 17. Negatives (n=52): bugs 9, crashes 9, cheaters/hackers 8, RNG/balance 6.
- "love this game so much but hackers and modders are ruining it."
- <2h (n=79 codable): needs friends 6, missing translation 6; technical failure 3.8%. >20h (n=357): bugs 35, repetitive 13, cheaters 12; technical failure 14.6% [S]. Negatives have the longer median (23.4h): long-term players souring, not quick refunders [I].

### Sentiment over time
- 98.5-98.7% in Oct-Nov 2023 (93,694 reviews in Nov), easing to about 95% through 2024; Nov 2024 bump to 97.0% (cause unknown; Lethal and others show November review bumps [I]); 92-94% through 2025; Oct 2026 89.7%, the lowest month [P]. Cause of the slide not established; recent negatives cite cheaters and lobby crashes [S].

### What happened after launch
- Big, infrequent updates: V40 Autumnal (Nov 2023), V45 Frosty (Dec 2023, all-time peak), V47 Challenge Moons, V50, V55 Cruiser, V60, V64 Bag, V69, V70 (Jun 2025, +60% CCU), V73, V80 Blooming (Apr 2026, +92% CCU) [P posts; T CCU].
- Viral explosion mid-Nov 2023 via Twitch/YouTube clips; "passed 100,000 concurrent players" [T]; Nov +3,664% avg CCU [T]. Feb-Mar 2024 -46%/-48% is post-viral decay [I]. Mar-Apr 2025 -43%/-50%, cause unknown; R.E.P.O. launch is a candidate [I].
- Price: $9.99 since launch; first sale -30% Feb 2024 [T]; -35% to $6.49 Jan 2025 (CCU +34%) [T]. No DLC, no paid cosmetics [P].

### Launch path & team
- Patreon dev logs from 2022-05-11, teaser 2022-07-08, small playtests from Aug 2023; no demo or Next Fest found; self-published EA [T/P].
- Solo US developer, age 21 in Jan 2024, Unity, about 19 prior small titles [T]. Statements: updates "bigger and less frequent" [T]; "I'm just not working like I have a quota" (V50) [D]; "I started losing steam" (V64) [D].

### Unknowns
- Real-time session length; primary confirmation of spectating; wishlists; sales; exact viral trigger streamer; price history; cause of the 2025-2026 sentiment slide.

---

## Chained Together (appid 2567870)
**Stratum:** hit | **Pair:** P07 (vs Don't Pull Me!) | **Release:** 2024-06-19, straight to 1.0 [P] | **Price:** $4.99 [P] | **Players:** 1-4 [P] | **Dev/Pub:** Anegar Games + Lab42 (since 2026) / Secret Mode [P] | **Core type:** climbing_traversal | **Reviews:** 65,230, 89.5% positive [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 5.22h / 5.28h / 4.22h [S] (n=1000 / 886 / 114) |
| <2h / >10h / >50h (all) | 16.8% / 17.7% / 0.7% [S] |
| Top 3 languages | English 38.0%, Simplified Chinese 19.6%, Russian 11.5% (Turkish 6.2% at 82.1% pos) [P] |
| SteamCharts all-time peak | 92,186 (2024-06) [T] |
| Month 1 / 3 / 6 / 12 avg proxies | 27,947 (Jun-Jul 24) / 5,920 (Aug-Sep 24) / 2,216 (Nov-Dec 24) / 1,417 (May-Jun 25) [T] |
| Current players | 696 (2026-11-11) [P] |

### Core loop & inputs
- Players chained together climb a vertical obstacle course out of Hell; one fall drags the team down [P store].
- Inputs: move, jump, secondary jump (1.7.9), "3, 2, 1 Go!" countdown key added 1.8.0 to sync jumps [P]; fully simulated chain that wraps platforms [P]; wing power-ups [T]. No built-in voice found [I].

### Interdependence & failure
- Everything runs through the shared chain [P]. Falling costs the whole team height; Normal has no checkpoints, Beginner does; Lava mode resets on contact [P store].
- Nobody "dies": a fallen player stays chained and climbs back [I].

### What it gets right
- Praise [S] (n=765 codable positives): fun with friends 212, rage-as-fun 58, funny 57, simple 35 (upper bound), teamwork 34, value 31, betraying/trolling 21.
- "it's better to play with friends, so if u fall u can always blame them."

### Where players push back
- Complaints [S] (n=866 codable): bugs 26, needs friends 17, too short 15, repetitive 12, toxic randoms 12, lost progress/saves 12, translation 11. Negatives (n=101): bugs 7, repetitive 4, clone/low effort 4, difficulty 3 (mostly Chinese "too hard").
- "secret mode made the game buggy and unplayable." / "I hoped on the slop train and got burned."
- <2h (n=153): translation 5, repetitive 3, needs friends 3, clone 3. >20h is thin (n=24): bugs 2 [S]. Negatives skew short (28.9% <2h) [S].

### Sentiment over time
- Jun 2024 90.2%, Jul 88.6%, Aug 87.6%; Nov 2024 best month 96.6% on 8,310 reviews with falling CCU (candidates: Golden Joystick award, Steam Awards/Autumn Sale [I]); 2025 84.6-90%; 2026 drifts to 81-86%, with Sep 2026 81.0% the low after the takeover and paid cosmetics (cause not established) [P/I].

### What happened after launch
- Launch day lobby failure ("impossible to join their friends") fixed with Steam invites; rapid patches 1.7.6-1.8.3 (quality settings, host cap, leaderboards, 7 languages, countdown key) [P].
- Workshop/map editor Sep 2024: no CCU lift [P/T]. Film adaptation news Nov 2025: CCU +51% [T].
- 2026-06-02 Secret Mode takes over, Lab42 developing; 2v2 Race Mode (Sep 2026); Gang Beasts bundle, Triple-i reveal, Autumn Sale -20% (Oct, CCU +11%); new map moved from Nov 12 to December [P].
- Monetisation: paid cosmetics only after takeover. Store lists Supporter Pack $2.99 (2026-09-01) and Restless Souls Pack $4.99 (2026-10-27) [P]; dev post named a $3.99 Golden Chain on 2026-09-01 (not reconciled with the store list).

### Launch path & team
- Steam page by Sep 2023 as an "Only Up!-style" climber; demo with chain physics Oct 2023, then pitched as 2-5 players [T]; 40k wishlists by 2023-11-15 [D]; beta testers and streamers before launch [D].
- Launch-week Twitch: DisguisedToast, LilyPichu; Kai Cenat and IShowSpeed on 2024-07-21 [T]. Viral gap about 0 days [I].
- Anegar Games debut, Unreal [T]; team size/location not found. "we've decided it's time for us to move on" (takeover post) [D].

### Unknowns
- Team size and location; session length; Next Fest; discount history; interviews or postmortem; why Sep 2026 sentiment fell.

---

## LOCKDOWN Protocol (appid 2780980)
**Stratum:** hit | **Pair:** none | **Release:** EA 2024-07-22 [T/P], 1.0 2025-11-18 [P] | **Price:** $9.99 [P] | **Players:** 1-16 (store), balanced for 5-8 [P/D] | **Dev/Pub:** Mirage Creative Lab / same [P] | **Core type:** versus | **Reviews:** 20,134, 85.9% positive [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 12.19h / 11.70h / 14.96h [S] (n=1000 / 742 / 258) |
| <2h / >10h / >50h (all) | 10.3% / 55.4% / 18.1% [S] |
| Top 3 languages | English 57.5% (82.8% pos), Russian 15.1%, Brazilian 4.8% [P] |
| SteamCharts all-time peak | 9,318 (2024-09) [T] |
| Month 1 / 3 / 6 / 12 avg proxies | 694 (Jul-Aug 24) / 3,663 (Sep-Oct 24) / 2,038 (Dec 24-Jan 25) / 518 (Jun-Jul 25) [T] |
| Current players | 218 (2026-11-11) [P] |

### Core loop & inputs
- First-person social deduction: employees do timed tasks while hidden "dissidents" sabotage and kill [P store]. Proximity voice is the core channel [T].
- Inputs: move/sprint on stamina, melee and guns, item slots and bag, hands-up gesture, separate wink keys per eye "so you can communicate" (0.6.0), tablet, cassettes, defibrillator [P].

### Interdependence & failure
- Some tasks need two people [T]; testimony and defibrillator revives [P]. Per-match win/loss; session length is a host setting up to 60 min [P].
- Dead players become ghosts who follow survivors [T]; ghosts can blink (0.14.2) [P]. Reviewers still find it dull: "Being dead in game is boring AF because there's nothing to do but watch the others" [S].

### What it gets right
- Praise [S] (n=646 codable positives): deception/bluffing 130, fun with friends 121, fun with strangers 46, atmosphere 45, potential 43, funny 42, betraying 37.
- "Its like amongus but you dont HAVE to lie to win as the killer."

### Where players push back
- Complaints [S] (n=893 codable): monetisation/DLC 62, repetitive 56, cheaters 52, too short 49, abandoned 47, bugs 45, price too high 38. Negatives (n=247): monetisation 51, abandoned 43, price 35, repetitive 31.
- "the creators just released a DLC where you pay $10 to be a woman." / "Abandonware, Greedy Devs and Horrible game management."
- <2h (n=94): repetitive 10, connection 5, toxic randoms 5, price 4. >20h (n=314): cheaters 40, abandoned 31, bugs 23, repetitive 21 [S]. Long-term players carry the anger: negatives' median is 15h [S].

### Sentiment over time
- 95% Jul 2024 and 94% Aug, 90% Sep; Dec 2024 82.1% (cosmetic DLC packs dated 2024-12-18 [P] line up with the DLC complaints [I]); 2025 slides to 76.6% in Jul during the content freeze; 1.0 month Nov 2025 82.5% on 1,000 reviews; Oct 2026 75.4%, the low [P]. Sample is only 74.2% positive vs 85.9% store, because the helpful stratum holds the angry reviews [S/I].

### What happened after launch
- EA patching (lobbies, kick/ban, tutorial, difficulty presets) [P]; Aug 2024 +5,502% and Sep +209% CCU, trigger not found (likely streamers; ChilledChaos top launch-week streamer [T]).
- 0.2.0 weapon crates were "a big mistake", rushed before a Steam sale [D]. Jan-Mar 2025 content freeze for a UE 5.2 to 5.5 rebuild: CCU -22%, -40%, -32% [T/D]. 16-player lobbies, 60-min sessions (Sep 2025); 1.0 lifted reviews, not CCU [P/T]; team then moved "main focus to a new game project" [D].
- Monetisation: 3 cosmetic DLCs (Holidays $4.99, Characters $9.99, Contrast $4.99) [P]; dev promised they "will remain the only 3 DLCs" with new skins at no extra cost [D]; Kickstarter backer rewards; Makeship plushie [P].

### Launch path & team
- Kickstarter by Feb 2024 (about €10k from 141 backers, unverified [T]); self-published EA; viral moment 1-2 months after EA [T].
- 3 siblings in Corsica, France, later friends hired; "only one has the skills to work on internal game structure" [D/T]; Unreal 5 [D].

### Unknowns
- Launch price and discounts; the Aug-Sep 2024 trigger; prior games; demo/Next Fest; whether ghosts got further tools after 1.0.

---

## Fast Food Simulator (appid 2916430)
**Stratum:** hit | **Pair:** none | **Release:** EA 2024-12-10, still EA [P] | **Price:** $14.99 [P] | **Players:** 1-6 [P] | **Dev/Pub:** No Ceiling Games / same [P] | **Core type:** job_simulation | **Reviews:** 10,075, 86.2% positive [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 10.22h / 9.70h / 10.83h [S] (n=1000 / 551 / 449) |
| <2h / >10h / >50h (all) | 4.8% / 51.1% / 3.5% [S] |
| Top 3 languages | English 51.7%, German 11.5%, French 7.3% [P] |
| SteamCharts all-time peak | 6,154 (2024-12) [T] |
| Month 1 / 3 / 6 / 12 avg proxies | 2,438 (Dec 24-Jan 25) / 1,262 (Feb-Mar 25) / 663 (May-Jun 25) / 471 (Nov-Dec 25) [T] |
| Current players | 131 (2026-11-11) [P] |

### Core loop & inputs
- First-person co-op burger restaurant: take orders, grill and fry, run the drive-thru, restock via the market computer, renovate and expand [P store].
- Inputs: move/sprint, hold-and-flip tools, burger labelling, computer apps, voice and text chat, player-collision toggle, interaction permissions for joiners [P]; full controller support only in a playtest branch [P].

### Interdependence & failure
- Station division; AI restocker and cashier were added for solo players after "intense demand" [D]. Day-based with adjustable day length and Easy-Nightmare tiers [P]. No fail state found; no death, so no waiting-player issue.

### What it gets right
- Praise [S] (n=475 codable positives): fun with friends 90, potential 34, progression 21, funny 19, simple 19, relaxing 19, value 18.
- "My friend and I would blast the 2000's pop, burn patties, run out of stock, and lose our minds."

### Where players push back
- Complaints [S] (n=914 codable): developer abandoned 269 (251 of them in negatives), bugs 64, repetitive 42, dead game 42, too short 30, clone/AI assets 30, price 25.
- "No updates, not posts, absolute dead silence." / "Abandoned cash grab that I regret buying, on top of the AI-generated assets."
- <2h (n=45): abandoned 10, bugs 4. >20h (n=171): abandoned 55, bugs 13, repetitive 13, too short 11 [S]. Negatives played a median 10.8h: they liked it, then ran out of content [I].

### Sentiment over time
- Weekly 94-97% Dec 2024-Mar 2025; 83-89% Apr-Aug 2025; monthly Jan 2026 82%, Feb 75%, Mar 72%, May 55%, Sep 47% [P]. Cause: no main-branch content for 16+ months (Jun 2025 to Nov 2026) [P]; the clearest neglect signal in the set [I]. One Nov 2025 week at 94.2% on 207 reviews (cause unknown). The sample is 55.1% positive [S].

### What happened after launch
- Updates 0.2.0 (Normal difficulty, anti-griefing), 0.3.0 AI restocker, 0.4.0 AI cashier and customisation, 0.5.0 trash/order monitor (Jun 2025), then a status post (Sep 2025: UE 5.3 to 5.5, EOS matchmaking, mini open world) and 0.5.2 [P]. Oct 2025 +84% CCU, cause unknown [T].
- 2026-10-20 playtest branch: re-migration to UE 5.8 after "persistent, game breaking engine level problems" [D].
- Monetisation: no DLC; bundles with Wrap House, Restaurats [P]. AI Steam art was "because of financial impossibility" [D]. Sales estimate 916.7k units / $11.45M gross [T, weak method].

### Launch path & team
- Free Prologue page Jul 2024, released 2024-10-07 (possibly during Oct 2024 Next Fest [T]); EA announced citing "incredible interest... in our game demo" [D]. Self-published; viral trigger not found.
- "Newly founded" Turkish studio [D/T]; Unreal. "December was spent resting and company work" [D].

### Unknowns
- Launch price; discount history; team size and city; viral trigger; fail state; Oct 2025 spike cause.

---

## Bogos Binted? (appid 3588490)
**Stratum:** mid | **Pair:** P06 (vs Liar's Bar) | **Release:** EA 2025-07-24, 1.0 2026-01-28 [P] | **Price:** $5.49 [P] | **Players:** up to 4 [P] | **Dev/Pub:** underbadger / GameDev.ist, underbadger, Gamersky Games [P] | **Core type:** versus | **Reviews:** 1,448, 91.4% positive [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 3.26h / 3.42h / 1.49h [S] (n=1000 / 902 / 98) |
| <2h / >10h / >50h (all) | 32.2% / 8.2% / 0.1% [S] |
| Top 3 languages | English 54.1%, Turkish 18.9%, Russian 7.7% [P] |
| SteamCharts all-time peak | 875 (2026-01) [T] |
| Month 1 / 3 / 6 / 12 avg proxies | 78.8 (Jul-Aug 25) / 28.5 (Sep-Oct 25) / 54.3 (Dec 25-Jan 26) / 43.2 (Jun-Jul 26) [T] |
| Current players | 12 (2026-11-11) [P] |

### Core loop & inputs
- Up to 4 aliens at a table play twisted bluffing/counting/word games (Zogblorp, Beeble Meep, Zinky Zoogle, VORP, Zoggy); losers' heads inflate and explode [P store].
- Inputs: card selection, calling bluffs, typed clues and voting (VORP), a Deadeye gun card, microphone [P]. Seated; no movement found.

### Interdependence & failure
- Adversarial versus play; elimination per match ("off to meet your alien god") [P]. Quick Mode (week 1 after 1.0) shortens matches [P]. What eliminated players do: not found.

### What it gets right
- Praise [S] (n=781 codable positives): fun with friends 177, funny 65, value 52, potential 29, bluffing 27, content variety 22.
- "Funny game, great price."

### Where players push back
- Complaints [S] (n=872 codable): too short 36, AI-generated art 23, bugs 22, repetitive 17, needs friends 12, dead game 9. Negatives (n=91): AI art 19, repetitive 11, bugs 8, dead game 7.
- "once we noticed the ai generated content it turned us off the whole experience." / "Game is dead; no public community servers."
- <2h (n=282): too short 15, AI art 14, repetitive 10. >20h only 16 codable [S]. Negatives decide fast: median 1.49h, 61.2% under 2h [S].

### Sentiment over time
- EA launch week 96.7% (120 reviews), next week 79.2%; tiny but near 100% Sep-Oct 2025; Nov 2025 week 98.3% (60, cause unknown); 1.0 week 86.0% on 228 reviews during the AI-art backlash; Feb 2026 92-97% after the art was replaced; mid-2026 weeks 70-100% on single-digit counts [P].

### What happened after launch
- Updates: VORP turn order (Aug 2025), trading cards, holiday cosmetics, 1.0 with Zoggy mode and map, week-1 Quick Mode, Day-10 solo mode vs AI, deck customisation (May 2026) [P].
- 1.0 + sale drove the spike: Jan-Feb 2026 avg 80 then 207, peaks 875/820 [T]; 50,000 copies at 1.0, 100,000 a week later [D]. Mar 2026 -64% [T].
- AI placeholders "unintentionally overlooked"; replaced; "We do not support AI generation in any form" [D].
- Monetisation: Fashion Pack DLC $0.99 [P]; bundles (Dripped Out Edition, with Pogo Together, Cheater's Table) [P]; 50% off May and Jun 2026, "we're risking rent here" [D].

### Launch path & team
- Game-jam side project [D]; Next Fest June 2025 demo, extended a week [P]; EA about 5 weeks later; 1.0 six months after EA [P].
- "A small indie studio", "quite frankly, exhausting" [D]. Turkish link inferred from publisher and review share [I].

### Unknowns
- Team size, location, engine; launch price; wishlists; viral trigger; co-publishers' roles; session length; eliminated-player experience.

---

## Doll Impostor (appid 2882870)
**Stratum:** mid | **Pair:** none | **Release:** 2024-03-28, full release [P] | **Price:** $11.99 [P] | **Players:** 1-4 (multiplayer from Nov 2024) [P] | **Dev/Pub:** David Gallardo / HeadArrow [P] | **Core type:** investigation | **Reviews:** 1,091, 92.0% positive [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 3.67h / 3.77h / 2.47h [S] (n=1000 / 915 / 85) |
| <2h / >10h / >50h (all) | 29.1% / 17.9% / 1.4% [S] |
| Top 3 languages | Russian 46.4%, English 32.8%, Spanish 7.5% [P] |
| SteamCharts all-time peak | 150 (2024-06) [T] |
| Month 1 / 3 / 6 / 12 avg proxies | 16.7 (Apr 24; Mar missing) / 30.5 (May-Jun 24) / 7.1 (Aug-Sep 24) / 10.8 (Feb-Mar 25) [T] |
| Current players | 5 (2026-11-11) [P] |

### Core loop & inputs
- 1-4 "guardians" watch possessed dolls through a night, study clues, likes, enmities and movement, use traps and stimuli, and must name the impostor before 9 AM [P store].
- Inputs: move, interact, traps, doors, craft/equip, career shop and safehouse; VR (OpenXR/Quest) and controller support [P].

### Interdependence & failure
- Shared deduction; wrong accusation or no answer by 9 AM brings "dire consequences" [P]. Career mode has a killer robot and loot drops so teammates can recover a fallen player's gear [D]. Dead-player activity: not found.

### What it gets right
- Praise [S] (n=839 codable positives): horror/tension 259, potential 109, atmosphere 94, unique 77 (upper bound), deduction 77, value 63.
- "i really hate dolls in real life and this game made me hate them more scary as hell."

### Where players push back
- Complaints [S] (n=922 codable): bugs 62, repetitive 42, too short 37, performance 24, balance 24, crashes 22, no tutorial 21. Negatives (n=83): bugs 23, repetitive 15, crashes 9, performance 7 (mostly Russian); technical failure in 37% of negatives.
- "My friend and I consistently crash after finishing one round on any map."
- <2h (n=271): bugs 17, too short 15, repetitive 12. >20h (n=55): bugs 9, no tutorial 3 [S].

### Sentiment over time
- 94-100% Apr-Sep 2024 (peak month Jun: 259 reviews, 95.4%); dips on small counts: Oct 2024 70%, Jan 2025 83.7%, Nov 2025 75%; 2026 mostly 70-82% on 7-23 reviews a month, May 2026 69.6% during a player spike [P]. Slow erosion; multiplayer errors were a long-running dev admission [D/I].

### What happened after launch
- Many updates (300+ posts, mostly hotfixes): Mommy, Circus, Daycare (Jun 2024, CCU +158% [T]), Career mode, Multiplayer (Nov 2024, beta to Jan 2025), VR (Mar 2025), matchmaking/Elo (Apr 2025), free demo (May 2025), Impostor mode (Nov 2025), Carnival, Madness mode (Apr 2026, "puts an end to the multiplayer errors... after 1 year") [P/D].
- Jun 2024 spike: likely Russian YouTube (Kuplinov, ViteC added to credits 2024-05-31) [I]. May 2026 +276% cause unknown [T].
- Monetisation: soundtrack DLC $0.99 [P]; Patreon-funded updates [D]; bundles with 8AM, Door Factory, others [P]; news feed used to advertise other HeadArrow games [P]. 40k copies by Nov 2025, 50k by Jun 2026 [D].

### Launch path & team
- Free itch.io demo [T]; Steam demo only 13 months after launch [P]. Launched as full release; "it was more of an Early Access than a finished game" [D].
- Solo dev who owns HeadArrow (8AM, The Last Stop, Floors, Doll INC); two outside devs joined in 2025 [D].

### Unknowns
- Engine, location; Next Fest; wishlists; session length; what dead players do; causes of the Jun 2024 and May 2026 spikes.

---

## Dumb Ways to Build (appid 4412320)
**Stratum:** mid | **Pair:** none | **Release:** 2026-09-10, PC/PS5/Xbox, crossplay [P/T] | **Price:** $7.99 [P] | **Players:** 1-4; 8-player lobbies in beta [P] | **Dev/Pub:** Dumb Ways to Die (PlaySide Studios) [P/T] | **Core type:** job_simulation | **Reviews:** 596, 87.9% positive [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 3.52h / 3.64h / 1.82h [S] (census n=596 / 524 / 72) |
| <2h / >10h / >50h (all) | 22.8% / 12.8% / 1.7% [S] |
| Top 3 languages | English 52.7%, Russian 12.8%, Simplified Chinese 6.9% (58.5% pos) [P] |
| SteamCharts all-time peak | not found (not tracked, 404); PlaySide claims Steam peak >1,600 [D] |
| Month 1 / 3 / 6 / 12 avg proxies | not found |
| Current players | 100 (2026-11-11) [P] |

### Core loop & inputs
- 1-4 "Beans" grab, rotate, throw and nail-gun materials into sketchy bridges, ramps and structures across hazardous "Crisis Jobs" [P store].
- Inputs: grab/rotate/throw, nail gun, tool belt, lunchbox consumables, proximity chat, ping system and expressions (v2.0), full controller support [P].

### Interdependence & failure
- Players build paths for each other; sabotage is part of it ("launch your buddy off a roof") [P]. Death by hazards; respawn rules and dead-player activity not found.

### What it gets right
- Praise [S] (n=422 codable positives): fun with friends 120, funny 50, potential 36, value 27, physics/chaos 20.
- "Fun friendslop, potential for very funny moments without having to force it."

### Where players push back
- Complaints [S] (n=490 codable): too short 53, bugs 28, connection 16, performance 16, repetitive 16, lag 11, crashes 9. Negatives (n=68): bugs 16, repetitive 8, connection 7, crashes 6; technical failure in 45.6% of negatives.
- "It took me and my friends less than 2 hours to finish the levels, twice."
- <2h (n=121): bugs 11, too short 11, connection 9, repetitive 8; technical failure 22.3%. >20h only 10 codable [S]. Negatives are quick (median 1.82h, 51.4% <2h) [S].

### Sentiment over time
- Weekly 82-95% since launch; Sep 87%, Oct 88% [P]. Chinese reviews 58.5% positive [P], matching Chinese connection complaints and a China hotfix that "may disable voice chat for some players" [P/S].

### What happened after launch
- Four free content updates in 6 weeks: v1.3.0 (Master Builder mode), v2.0 Power Tools & Packed Lunches, v3.0 Beach Breach level, v4.0 8-player lobbies and costumes; connection fixes for Japan and Russia [P]. Weekly reviews still fell from 157 to about 11-23 [P].
- Monetisation: no DLC; four bundles at an extra 10% off (DUMBANANA!, Shady Builders, Ribbits & Rivets, Gamble With Your Friends) [P].

### Launch path & team
- Announced 2026-08-19, 22 days before launch; creator keys via Keymailer and Dare Drop [P]. No demo or Next Fest found.
- PlaySide figures [D]: about 100k wishlists at launch, >80% of Steam buyers had not wishlisted, about 150k units in month 1 (two-thirds Steam), US$1.0M gross, >2,600 creators, 57k peak Twitch viewers, 36M views.
- PlaySide Studios, ASX-listed; owns the Dumb Ways to Die IP [T]. CEO: aim was "a strongly reviewed, enjoyable experience" [D]. Plans: UGC levels, more than 4 players [D].

### Unknowns
- CCU history; team size and engine; session length; respawn and dead-player rules; demo/Next Fest.

---

## S.E.M.I. - Side Effects May Include... (appid 3957560)
**Stratum:** flop | **Pair:** none | **Release:** EA 2025-11-20, 1.0 2026-01-23 [P] | **Price:** $7.99, EA launch -15% [P] | **Players:** 1-4 [P] | **Dev/Pub:** Two Horn Unicorn / same [P] | **Core type:** puzzle_platformer | **Reviews:** 113, 85.8% positive [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 2.07h / 2.30h / 0.94h [S] (census n=113 / 97 / 16) |
| <2h / >10h / >50h (all) | 46.0% / 1.8% / 0.9% [S] |
| Top 3 languages | Russian 49.6%, English 27.4%, Simplified Chinese 13.3% [P] |
| SteamCharts all-time peak | not found (HTTP 500) |
| Month 1 / 3 / 6 / 12 avg proxies | not found |
| Current players | 0 (2026-11-11) [P] |

### Core loop & inputs
- 1-4 patients escape a clinic through procedurally assembled rooms (traps, gravity shifts, puzzles), fighting staff; pills grant random "syndrome" powers and a madness meter makes them uncontrollable [P store].
- Inputs: move/jump, melee, pick up and throw, weapon durability, pills, candy currency, carry-and-aim a teammate (Meatball), pull stuck teammates out of walls, reworked voice chat and emotes at 1.0 [P].

### Interdependence & failure
- Pulling teammates out, passing fire/electricity by touch, puzzle rooms [P]; "a single wrong move can knock out the entire squad" [P store]. Dead-player rules not found; a negative review complains of spending a round bored, stuck upside down watching teammates [S].

### What it gets right
- Praise [S] (n=94 codable positives): fun with friends 40, funny 25, atmosphere 17, potential 17, physics/chaos 14, teamwork 12.
- "Hilarious Platformer puzzle game!"

### Where players push back
- Complaints [S] (n=108 codable): bugs 13, too short 13, connection 3, lag 3, repetitive 3, price 3. Negatives (n=14): bugs 4.
- "Bit too buggy and unbalenced to enjoy right now." / co-op called "just for show" in a release-era negative.
- <2h (n=49): too short 5, price 3. >20h: 1 review [S]. Note: 26.5% of reviewers received the game free (key distribution) and only 41.6% bought on Steam [S].

### Sentiment over time
- First EA week 53.8% (13 reviews), next week 100% (11); Jan 2026 week 50% (6); essentially no reviews after Feb 2026 [P].

### What happened after launch
- Therapy Course mode (Dec 2025), Christmas event, last EA update (Jan 2026), 1.0 with Stage 3, enemies, voice rework and low-end optimisation, then achievements/cards (Feb 2026); no posts after [P].
- Funnel: 11k demo players in week 1; >50k demo players and 25k wishlists by late Oct; >75k demo players by EA [D], ending in 113 reviews [P]. A severe demo-to-purchase gap [I].
- Monetisation: 3 DLC (two soundtracks $1.99/$0.99, digital artbook $1.99) and a Deluxe bundle [P]; EA-exclusive skin bought with in-game currency [P].

### Launch path & team
- Demo from 2025-09-26 with solo mode and public lobbies added after feedback ("assembling a full team... could be challenging") [D]; window overlaps Oct 2025 Next Fest, participation not confirmed. EA lasted 2 months [P].
- Two Horn Unicorn, also making "Life Slash Death" [T]; Russian-speaking team inferred [I].

### Unknowns
- CCU; team size, location, engine; Next Fest participation; run structure and death rules; session length; why the demo audience did not convert.

---

## OK Boomer (appid 4162290)
**Stratum:** flop | **Pair:** none | **Release:** EA 2026-06-25 [P] | **Price:** $7.99, launch discount % not stated [P/D] | **Players:** 4 [P] | **Dev/Pub:** Pugsy Studios / GameDev.ist [P] | **Core type:** escape_survival | **Reviews:** 70, 71.4% positive [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 1.01h / 1.15h / 0.77h [S] (census n=70 / 50 / 20) |
| <2h / >10h / >50h (all) | 85.7% / 2.9% / 0.0% [S] |
| Top 3 languages | English 50.0% (57.1% pos), Turkish 24.3% (94.1% pos), Polish 5.7% [P] |
| SteamCharts all-time peak | not found (404) |
| Month 1 / 3 / 6 / 12 avg proxies | not found |
| Current players | 0 (2026-11-11) [P] |

### Core loop & inputs
- 4-player co-op survival horror inside a procedurally generated "internet": analog-tech boomers purge glitches, hack traps and survive monsters; a sanity system makes players hallucinate footsteps or see friends as enemies [P store].
- Inputs: equipment, trap hacking, platform-specific weapons, customisation, push-to-talk voice, ping display, captcha mechanics [P/S].

### Interdependence & failure
- Shared survival with trust undermined by hallucinations [P]. Death means "log off forever"; sessions end in a server disconnect with a 1:30 warning [P]. Dead players spectate with auto-switch to survivors (demo update) [P].

### What it gets right
- Praise [S] (n=48 codable positives): fun with friends 15, monsters 7, potential 7, atmosphere/value/streamer/unique 4 each.
- "We had a really fun time with my friends."

### Where players push back
- Complaints [S] (n=67 codable): bugs 10, repetitive 10, too short 7, too easy/balance 5, clone 3, price 3. Negatives (n=19): repetitive 8, bugs 6; refund mentions in 21% of negatives.
- "Unity slop game, played with friends for around 43 minutes we all ended up refunding it." / "still feels like a demo at best."
- <2h covers 57 of 67 codable reviews: bugs 9, repetitive 9, too short 7. No reviews over 20h [S].

### Sentiment over time
- Launch week 84.2% (38), next week 84% (25), then weeks of 0% (1 and 5 reviews) and one negative in Aug [P]. Content-thinness complaints set in after the first sessions [I].

### What happened after launch
- One update: 2026-08-13 "Smoother, Faster and More Fun!" (pacing, balance, "more comedic and playful elements") [P]. Nothing after.
- Monetisation: no DLC; bundles with Gamble With Your Friends, Bogos Binted?, Don't Panic! It is Just Turbulence [P].

### Launch path & team
- Demo, then Next Fest June 2026 (demo closed 2026-06-05 before the fest), EA 10 days later; launch slipped one day for a store-page re-review [P].
- "We built OK Boomer because we wanted a co-op game that's easy to jump into with friends" [D]. Team not found; Turkish publisher inferred [I].

### Unknowns
- Team and engine; wishlists; launch discount %; CCU; total session length; any roadmap after Aug 2026.

---

## Out of Stock! (appid 1938750)
**Stratum:** flop | **Pair:** P05 (vs Supermarket Together) | **Release:** 2025-10-31 [P] | **Price:** $6.99, -35% for 10 days at launch [P] | **Players:** 1-4, local or online (not combined) [P] | **Dev/Pub:** Studio Maxi Mini / Rubika Supinfogame [P] | **Core type:** job_simulation | **Reviews:** 39, 28.2% positive [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 2.62h / 1.32h / 3.03h [S] (census n=39 / 11 / 28) |
| <2h / >10h / >50h (all) | 35.9% / 2.6% / 0.0% [S] |
| Top 3 languages | Simplified Chinese 48.7% (15.8% pos), English 33.3% (23.1%), French 15.4% (66.7%) [P] |
| SteamCharts all-time peak | not found (HTTP 500) |
| Month 1 / 3 / 6 / 12 avg proxies | not found |
| Current players | 0 (2026-11-11) [P] |

### Core loop & inputs
- Top-down, fixed-camera, Overcooked-style store chaos: order stock, restock, clean spills, run checkouts and keep trait-driven customers happy across star-rated levels [P store; T].
- Inputs: move, pick up, throw boxes, pass to teammates (minimum pass distance removed in 1.0.1), stun other players, cashier mini-game; controller or keyboard [P/T]. No voice found.

### Interdependence & failure
- Task division and passing [P]; star score per level, thresholds tuned separately for 2 and 3-4 players [P]. No death.

### What it gets right
- Praise is thin [S] (n=10 codable positives): fun with friends 2, music/visuals 2, potential 2.
- "Also, the music is great."

### Where players push back
- Complaints [S] (n=38 codable): bugs 26, lag 3, "abandoned" 3, toxic/kicked 2, price 2. Technical failure in 71% of codable reviews and 82% of negatives.
- "the game is so laggy its impossible to play." / "Dev has abandoned the game and isn't planning to fix issues, confirmed on discord" (player claim).
- <2h (n=13): bugs 8. No >20h reviews. Negatives played longer than positives (3.0h vs 1.3h), so they tried and hit netcode problems [S/I].

### Sentiment over time
- Launch month 30.8% (13 reviews); a few mixed weeks in Nov 2025; almost only negative singles after Dec 2025 [P]. Chinese reviewers, half the total, were 15.8% positive [P].

### What happened after launch
- 2025-11-02: hotfix for "geographical restrictions" on online play, patch 1.0.1 lowering star thresholds, new demo [P]; 2025-12-03: two GWB Game Awards (Tencent student awards) [P]. No later updates in the feed [P].
- Dev-side data: median playtime 13 min for the demo (>4,000 players) and 49 min for the full game (>1,000 players) by Nov 2025 [D].
- Monetisation: no DLC, no bundles found [P].

### Launch path & team
- Demo Apr 2025; Next Fest Jun 2025 ("nearly 20k satisfied customers served") and Debut Festival Aug 2025; roadmap promised online play, solo, 4 worlds and 80 cosmetics; online play only arrived with the full release [P/D].
- 15-person student team (Master 1, Rubika Supinfogame), 12 months (9 half-time, 3 full-time), Unity [D].

### Unknowns
- CCU; exact team location; voice; whether online play was ever fixed after Nov 2025.


---

## R.E.P.O. (appid 3241660)
**Stratum:** hit | **Pair:** P03 (vs Treasure Hunters: Raid Together) | **Release:** EA 2025-02-26, still EA; 1.0 planned for 2026 [P/D] | **Price:** $9.99; launch -20% to $7.99 [P/T] | **Players:** up to 6 [P] | **Dev/Pub:** semiwork / semiwork [P] | **Core type:** extraction | **Reviews:** 435,350, 96.0% positive [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 22.41h / 23.80h / 9.23h [S] (n=1000 / 923 / 77) |
| <2h / >10h / >50h (all) | 4.0% / 69.0% / 28.1% [S] |
| Top 3 languages | English 41.1%, Russian 25.4%, Spanish 7.6% [P] |
| SteamCharts all-time peak | 266,908 (2025-03) [T]; SteamDB press post "peaks at 271k" [P feed] |
| Month 1 / 3 / 6 / 12 avg proxies | 105,384 (Mar 25; Feb missing) / 82,089 (Apr-May 25) / 27,694 (Jul-Aug 25) / 31,853 (Jan-Feb 26) [T] |
| Current players | 22,496 (2026-11-11) [P] |

### Core loop & inputs
- Robots search procedurally assembled haunted levels for physics-simulated valuables, carry them unbroken to extraction to meet the quota, then spend surplus on upgrades [D store; T].
- Inputs: move/sprint/crouch/jump, Tumble ragdoll, physics grab beam with rotate and push/pull, item slots, map, typed "Truck Chat" spoken by your robot, proximity voice with push-to-talk, walkie item, expressions, gamepad from 0.5.0 [D/T].

### Interdependence & failure
- Heavy and fragile objects need several carriers and lose value when damaged; one shared quota and money pool [D/T]. A full wipe loses the run (save backups since 0.3.0) [D].
- Dead players spectate; since 0.3.0 they can possess their own head on a recharging battery to interact with the living, and from 0.5.0 find valuables; revival by carrying the head back (not read in a primary source) [D/T].

### What it gets right
- Praise [S] (n=784 codable positives): fun with friends 260, horror 153, monsters 148, funny 134, physics/chaos 56, atmosphere 45, value 42.
- "You can hear your friends whispering in real time as you creep through a dark mansion."

### Where players push back
- Complaints [S] (n=855 codable): repetitive 39, bugs 31, connection 31, needs friends 27, difficulty 24, performance 19, toxic randoms 18. Negatives (n=71): connection 13, repetitive 8, missing translation 8 (Chinese demands), bugs 7.
- "matches have been closing on their own due to server timeout issues."
- <2h (n=35): translation 3, connection 2, repetitive 2, controls 2. >20h (n=468): repetitive 23, needs friends 16, bugs 15, connection 14 [S]. Negatives stop much earlier (median 9.2h vs 23.8h) [S].

### Sentiment over time
- Weekly 95-97% Feb-May 2025; Jun 2025 dip to 92-94% around the Museum update; free-weekend week (late Oct 2025) 92.4% on 5,837 reviews; late-Nov 2025 weeks of 21,383 and 29,935 reviews at 98.7-98.9% (Steam Awards / Autumn Sale window, link not proven [I]); 2026 steady 93-96% [P].

### What happened after launch
- v0.2.0 Museum (Jun 2025: server list, matchmaking, kick, region picker) did not reverse decay (Jun -37%) [P/T]. v0.3.0 Monster Update + free weekend (Oct 30): Oct peak 118,994, Nov avg +164% to 53,071 [T]. Devlog-only Dec 2025-Apr 2026; Jan 2026 +34% unexplained [T]. v0.4.0 Cosmetic Update (May 2026, 500+ earned cosmetics): +105% [T]. v0.5.0 Sunstone (Oct 2026: map, gamepad, 21 languages): Oct peak 71,168 [T].
- Monetisation: no DLC, cosmetics earned in-game [P/D]; "If you happen to love microtransactions, I am going to disappoint you deeply" [D via T headline]; price raise planned at 1.0 [D via T snippet]; Summer Sale -20%; all-time low $6.49, date unknown [T]; merch [D].

### Launch path & team
- No demo or Next Fest found; viral in launch week; top-grossing paid Steam game 11-18 Mar 2025 [T]; Zeekerss shout-out [T].
- semiwork, Uppsala, Sweden, under 10 staff [T]; first Unity game, Photon networking [D/T]; prior game Voidigo (about 6 years, "wasn't a big seller") [D/T]. "Let's just fail quickly this time" [D]; began as a solo cleaning-horror game, dropped because co-op cleaning split players up [D].

### Unknowns
- Wishlists; announcement date; dev time; session length; exact revive rules; date of the all-time-low price; cause of the Jan 2026 lift.

---

## Liar's Bar (appid 3097560)
**Stratum:** hit | **Pair:** P06 (vs Bogos Binted?) | **Release:** EA 2024-10-02, still EA [P] | **Price:** $6.99 [P] | **Players:** tables of 4; 100-player mode announced [D] | **Dev/Pub:** Curve Animation / same [P] | **Core type:** versus | **Reviews:** 56,599, 89.5% positive [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 4.10h / 4.22h / 3.40h [S] (n=1000 / 798 / 202) |
| <2h / >10h / >50h (all) | 24.8% / 22.0% / 3.5% [S] |
| Top 3 languages | English 32.1%, Russian 22.8%, Simplified Chinese 22.4% (82.9% pos) [P] |
| SteamCharts all-time peak | 109,419 (2024-10) [T]; 113,798 on 2024-10-21 [T GWO] |
| Month 1 / 3 / 6 / 12 avg proxies | 19,758 (Oct 24) / 4,734 (Dec 24) / 1,589 (Mar 25) / 1,088 (Aug-Oct 25) [T] |
| Current players | 330 (2026-11-11) [P] |

### Core loop & inputs
- Four players at a bar table bluff in Deck/Dice/Poker/Slots; a caught liar faces Russian roulette, poison or a death spin until one remains [D store].
- Inputs: play cards/dice/bids, call "Liar" or "Spot On", once-per-game abilities, text chat, voice chat (added 2024-10-08) with per-player volume, emotes, gamepad (Apr 2026); seated, no movement [D].

### Interdependence & failure
- No co-op dependency: PvP bluffing where voice reads are the core [I]. Elimination within a match; ranked points since Dec 2024 [D].
- Eliminated players watch in spectator mode (a hotfix stopped them seeing others' cards) [D].

### What it gets right
- Praise [S] (n=683 codable positives): fun with friends 169, bluffing 126, potential 68, funny 56, visuals 54, simple 46 (upper bound), fun with strangers 45.
- "This game is hilarious with friends and fun as hell."

### Where players push back
- Complaints [S] (n=873 codable): connection/host 78, bugs 77, cheaters 64, too short 40, AI voices/art 38, repetitive 36, toxic randoms 31. Negatives (n=190): cheaters 35, bugs 34, connection 32, AI 23.
- "The host leaving issue is bad, game killing bad." / "Negative review until they stop using AI voices and hire actual voice actors."
- <2h (n=226): bugs 23, connection 20, cheaters 19, too short 13; technical failure 19.9%. >20h (n=88): connection 15, bugs 12, cheaters 12, toxic 6; technical failure 27.3% [S].

### Sentiment over time
- Oct 2024 86.3% (lobby bugs), Nov 96.0%, Dec 93.3%; slide to 75.6% by Apr 2025; Jul 2025 77.4% after Poker/matchmaking (cheat fixes followed [I]); Nov 2025 91.3% (cause unknown); Jul 2026 73.9%, the low, after Deck Remastered removed Deck 2 (hotfix "DECK 2 RETURNS BETTER") [P/D].

### What happened after launch
- October 2024 fix run: lobby fixes, voice chat, Chinese/Russian, quick join, new rulesets, Spot On [D]. Nov 2024 Arcade Bar and host migration beta; Dec matchmaking and ranked; Steam Award "Most Innovative Gameplay" [D/P].
- Mode updates as seasons: Deck 2 (Mar 2025), Poker + Season 1 (Jun 2025, with Summer Sale: Jun +45%, Jul +82%), ban system (Aug), Dice Remastered (Sep; Oct +30%), Slots (Dec, +34%), Season 4 with anti-cheat and gamepad (Apr 2026, -26%), Deck Remastered (Jul 2026, +17%), "100 LIARS WALK INTO A BAR" teaser (Nov 2026) [D/T].
- Monetisation: no DLC, no IAP category [P]; wardrobe store since Mar 2025 (paid items not stated) [D]; free skin sets; 1.0 expected to add "in-game monetization" [T]; Youtooz figures [D]; Android version [T].

### Launch path & team
- No demo or Next Fest found; launch CCU about 2,000, grew "organically" through streamers to a peak 19 days after release [T].
- Curve Animation, Ankara, Turkey, founded 2014 as an animation studio; first full video game [T]. "As a small indie studio with a limited team, it took us a bit longer" [D].

### Unknowns
- Launch price and discounts; team size, engine; session length; whether the store sells paid items; Velvet Room 2-player mode status.

---

## Nuclear Nightmare (appid 2909110)
**Stratum:** hit | **Pair:** none | **Release:** EA 2024-10-20, moving to 1.0 via 8.x [P/D] | **Price:** $6.99 [P] | **Players:** 8-player lobbies [D] | **Dev/Pub:** BG Productions / same [P] | **Core type:** escape_survival | **Reviews:** 19,898, 81.2% positive [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 6.03h / 6.46h / 3.69h [S] (n=1000 / 848 / 152) |
| <2h / >10h / >50h (all) | 13.5% / 32.6% / 2.9% [S] |
| Top 3 languages | English 59.9%, Russian 26.3% (77.8% pos), Polish 1.9% [P] |
| SteamCharts all-time peak | 10,404 (2024-12) [T] |
| Month 1 / 3 / 6 / 12 avg proxies | 305 (Oct-Nov 24) / 1,815 (Dec 24-Jan 25) / 122 (Mar-Apr 25) / 415 (Sep-Oct 25) [T] |
| Current players | 340 (2026-11-11) [P] |

### Core loop & inputs
- Team flies into an open Arctic map, gathers classified materials, drives snowmobiles/Snowcats or flies helicopters, tests each other for black-goo infection and reaches the evac chopper before the nuke timer ends [D store].
- Inputs: move/sprint/crouch, vehicles, 5 item slots, emote/point/whistle, ping, husky commands, infection kit and vaccine, proximity voice with occlusion, radios, death voice chat, proximity text, ammo drop, horn; chess/pool during whiteouts (V8.2) [D].

### Interdependence & failure
- Infection testing, reinforcement tokens to respawn the dead, shared vehicles; anyone outside the evac circle at the timer "fail[s] the match" [D].
- Dead players spectate, use death voice chat, and can be reinforced back in; optional "playable enemy" spawn on death [D].

### What it gets right
- Praise [S] (n=776 codable positives): fun with friends 215, horror 195, monsters 169, atmosphere 129, value 113, potential 65, funny 55.
- "There is tension in the group between those who wish to extract early and those who wish to complete research."

### Where players push back
- Complaints [S] (n=922 codable): bugs 227, performance 78, crashes 49, repetitive 43, too short 38, controls 28, lag 26; technical failure in 32% of codable reviews and 63% of negatives. Negatives (n=146): bugs 70, performance 25, crashes 23, price 14.
- "After the last patch, the game became unplayable, with few frames and a huge number of bugs."
- <2h (n=127): bugs 24, performance 11, no tutorial 6, translation 6. >20h (n=135): bugs 45, performance 15, repetitive 9, crashes 8; technical failure in 88% of >20h negatives [S].

### Sentiment over time
- 87-88.5% Oct-Dec 2024; then 81.4% Jan, 67.1% Feb, 63.0% Mar, 61.2% Apr, 58.8% May 2025 while the lead developer could not work and a broken update stayed live [P; forum relay]. Recovery to 78.9% in Jun 2025 with the Resurrection updates; 73-80% through 2025-2026; Aug 2026 86.5%, Nov 2026 87.8% during V8.x [P].

### What happened after launch
- 30+ hotfixes Oct-Nov 2024 (8-player lobbies, reinforcements, ammo, new voice system) [D].
- Breakout was a sale, not an update: Autumn Sale "well under $2" (Nov +266%, Dec +438%, peak 10,404) [T/D]; "the exploding popularity ever since the sale" [D]; a third-party listing shows $1.04 (-85%), date unconfirmed [T].
- Base Update (Jan 2025, -59% post-sale); Feb-May 2025 collapse to 64 avg during a development halt [T/D]; Resurrection parts 1-5 (Jun 2025, +385%); Forest; Tower Island ("for those with smaller friend groups"); Remaster V5.0; Imposter Mode (Mar 2026, +130%); Crevasse (Jul 2026, +50%); V8.0-8.2 (Oct 2026, +68%) [D/T].
- Monetisation: no DLC; skins and perks bought with in-game points [P/D].

### Launch path & team
- Store page public by Mar 2024 [T]; no demo, Next Fest or wishlists found; viral via the sale 5-6 weeks after EA [T/D]. Self-published.
- BG Productions; lead dev "Benjamin"; first-person dev posts suggest a near-solo developer [I]; Unreal inferred from patch terms [I]. "My goal... was to have everything driven by the community" [D].

### Unknowns
- Team size, location, prior games; confirmed engine; launch price; sale discount %; session length; causes of Feb 2026 -59% and the Nov 2025 peak.

---

## Sneak Out (appid 2410490)
**Stratum:** mid | **Pair:** none | **Release:** 2024-06-06, free to play [P] | **Price:** free; 6 paid packs $4.99-$99.99 [P] | **Players:** 6 (5 hiders vs 1 hunter) [D] | **Dev/Pub:** Kinguin Studios / Kinguin [P] | **Core type:** versus | **Reviews:** 6,720, 69.0% positive [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 2.02h / 2.75h / 0.70h [S] (n=1000 / 623 / 377) |
| <2h / >10h / >50h (all) | 49.5% / 14.1% / 1.8% [S] |
| Top 3 languages | Russian 22.9% (81.0% pos), Simplified Chinese 21.6% (34.6% pos), English 21.0% (72.3% pos) [P] |
| SteamCharts all-time peak | 5,322 (2024-06) [T] |
| Month 1 / 3 / 6 / 12 avg proxies | 781 (Jun-Jul 24) / 230 (Aug-Sep 24) / 128 (Nov-Dec 24) / 36.8 (May-Jun 25) [T] |
| Current players | 0 (2026-11-11) [P] |

### Core loop & inputs
- 5v1 horror hide-and-seek in a haunted castle: hiders do tasks to earn coins and open the escape portal while a random player hunts as a monster [D store].
- Inputs: move/sprint/crouch, tasks and mini-games, traps, items (banana peel, broom, hoverboard), prop disguise, revives; hunter abilities and skill cards; ghost toolkit; emotes; full controller support [D/P]. Voice/text chat not found.

### Interdependence & failure
- Joint task progress opens the portal; revives [D]. Caught hiders become ghosts who possess armour, slime floors and throw chairs at the Hunter: a strong answer to the waiting player [D/I].

### What it gets right
- Praise [S] (n=535 codable positives): fun with friends 150, free/value 50, visuals 43, monsters 39, funny 38, simple 30.
- "Some bugs/server issues, but the game is fun enough with friends that it is all worth it."

### Where players push back
- Complaints [S] (n=887 codable): connection/lobby 184, bugs 86, lag 54, crashes 47, dead game 47, balance 40, monetisation 33; technical failure in 33% of codable. Negatives (n=352): connection 121, bugs 44, dead game 34, crashes 29.
- "Actually unplayable without 5 more friends Why launch a game that you can't match make?" / "Playtest was fun, game is dead now."
- <2h (n=444, the bulk): connection 98, bugs 40, crashes 30, dead game 29. >20h (n=59): connection 9, lag 8, repetitive 6 [S]. Negatives quit fast: median 0.7h, 68.2% <2h [S].

### Sentiment over time
- Launch Jun 2024 51.1% on 2,699 reviews (servers, China connectivity, pay-to-win criticism [T]); Jul 70.8%, Aug 82.6%; review spikes Nov 2024 (90.3%, 834) and Jan 2025 (94.0%, 571) far above player levels, cause unknown (Kinguin code promotion a candidate [I]); Mar 2026 27.3% during the matchmaking outage; Oct 2026 41.2% (17) [P].

### What happened after launch
- Resource economy removed a day after launch [D]; streamer contest with €1,000 prize [D]; free Season Pass (Jul 2024), Premium Shop (Aug), Battle Pass, Capture the Crown and School map (Sep): no lift [D/T].
- No posts for 16 months (Nov 2024-Mar 2026); online play broke (Jan 2026 avg 3.4); private matches restored Mar 2026, public still impossible in Apr [D]. Region-locked matchmaking, then fewer regions "to improve matchmaking density", then bots fill quiet public matches (Sep 2026) [D].
- Monetisation: F2P with 6 DLC packs (Founders $11.99, Starter Iron to Diamond $4.99-$99.99) [P], Premium Shop, free battle passes [D].

### Launch path & team
- Next Fest June 2023 demo, playtests Oct 2023 and Feb 2024, influencer stress test Mar 2024; date announced Apr 2024 [D].
- Kinguin Studios (the key marketplace's own studio); press release datelined Hong Kong [T]; CGO Michał Kaczmarek [D].

### Unknowns
- Team size, engine, location; wishlists; session length; outage start date; cause of the Nov 2024 / Jan 2025 review spikes.

---

## Hospital 666 (appid 2774380)
**Stratum:** mid | **Pair:** none | **Release:** 2024-03-05, full release [P] | **Price:** $7.99, -20% launch week [P/D] | **Players:** 1-4 [D] | **Dev/Pub:** Lokin / Lokin [P] | **Core type:** investigation | **Reviews:** 1,424, 71.9% positive [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 3.62h / 3.85h / 1.77h [S] (n=1000 / 731 / 269) |
| <2h / >10h / >50h (all) | 24.2% / 4.0% / 0.0% [S] |
| Top 3 languages | English 26.5% (80.1% pos), Russian 18.0% (72.3%), Simplified Chinese 16.6% (49.8%) [P] |
| SteamCharts all-time peak | 1,028 (2024-03) [T] |
| Month 1 / 3 / 6 / 12 avg proxies | 122 (Mar-Apr 24) / 67.3 (May-Jun 24) / 30.1 (Aug 24) / 17.8 (Jan-Mar 25) [T] |
| Current players | 2 (2026-11-11) [P] |

### Core loop & inputs
- "Exit 8"-style anomaly game: on each hospital floor decide whether something is abnormal and take the front or rear elevator; wrong choices or bosses kill you, over 100+ floors, 85 anomalies and 5 bosses [D store].
- Inputs: mouse and keyboard, move, look, interact, choose elevator; friendly sabotage ("Stab your friend in the back") [D]. Voice/text/emotes not found.

### Interdependence & failure
- Joint anomaly spotting and boss escapes; several traps changed from "kill everyone" to "players in range" after launch [D]. Death means respawn with per-floor autosave and checkpoints; Easy/Normal/Hell [D]. Dead-player activity beyond respawn: not found.

### What it gets right
- Praise [S] (n=622 codable positives): fun with friends 140, horror 108, monsters/bosses 44, funny 36, atmosphere 29, unique 24.
- "great game for shoving your friends into sawblades."

### Where players push back
- Complaints [S] (n=864 codable): bugs 75, repetitive 71, performance 42, crashes 35, too short 31, not scary 23, price 19. Negatives (n=242): repetitive 38, bugs 34, performance 18, crashes 17; 14 refund mentions.
- "No good jumpscares and boring ass rooms." / "its fun to play with friends but the constant crashes make it hard to play in multiplayer."
- <2h (n=217, 124 of them negative): bugs 23, repetitive 21, crashes 15, performance 15. >20h: 1 review [S]. Negatives quit early (median 1.77h, 51.7% <2h); 4.6% of the sample refunded [S].

### Sentiment over time
- Launch Mar 2024 67.8% (289; black-screen saves, multiplayer desyncs, 27 hotfixes); Apr-May 74.5%; Jun 2024 54.8% (93, cause unknown); Oct 2024 81.2%; later months swing 37-100% on 6-35 reviews [P].

### What happened after launch
- About 27 hotfixes in 3 weeks, then v1.1 optimisation ("Around Double Game's Frame Rate", Apr 2024), the last content patch [D].
- Sequel School 666 announced Aug 2024, demo and Next Fest Oct 2024 (small Oct-Nov rises, cross-promotion plausible [I]); School 666 release Jun 2025 lifted Hospital 666 CCU +144% [P/T].
- Monetisation: no DLC; a second "Commercial License" package at $7.99 (purpose not stated); bundle "Anomalies 666" [P].

### Launch path & team
- 9 numbered teaser trailers; free creator keys via a form (Jan 2024); launch slipped to Mar 5 [P/D]. No demo or Next Fest for this game [P].
- Solo developer "Lokin", Unreal 5.3 [D]; "I need money to make games T_T" (2025) [D]. Chinese-speaking inferred [I]. School 666: 703 reviews, Very Positive [P].

### Unknowns
- Location; viral moment; wishlists; real session length (store "666 minutes" is a joke); Jun 2024 dip cause.

---

## Backroom Company (appid 3010460)
**Stratum:** mid | **Pair:** none | **Release:** EA 2024-10-28, 1.0 2025-07-29/30 [P/D] | **Price:** $8.99 (adjusted 2025-04-18) [P/D] | **Players:** up to 8 [T] | **Dev/Pub:** Hypercent Inc. / same [P] | **Core type:** extraction | **Reviews:** 923, 85.4% positive [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 3.58h / 4.00h / 2.48h [S] (census n=923 / 788 / 135) |
| <2h / >10h / >50h (all) | 17.8% / 8.1% / 0.2% [S] |
| Top 3 languages | English 32.4%, Simplified Chinese 31.4%, Korean 23.7% [P] |
| SteamCharts all-time peak | 2,444 (2026-01, inside an unexplained flat plateau) [T] |
| Month 1 / 3 / 6 / 12 avg proxies | 16.2 (Nov 24; Oct missing) / 11.9 (Dec 24-Jan 25) / 9.4 (Mar-Apr 25) / 33.2 (Sep-Oct 25) [T] |
| Current players | 8 (2026-11-11) [P] |

### Core loop & inputs
- Up to 8 test subjects explore Backrooms levels (hotel, pool, parking, sewer, school, office), collect strange items and film entities to meet a research quota, hide and stay silent, then extract [D store; T].
- Inputs: move/sprint/crouch/jump, carry items and carts, camera filming, lockers, hold breath, push teammates, voice chat with voice-control mechanics, walkie-talkies, controller support [D/P].

### Interdependence & failure
- Team quota; revival by inserting a dead player's ID card into a dumbwaiter; missed quota triggers game over [D]. Dead players roam as ghosts and can disrupt the living ("Ghost Path Disruption") [D].

### What it gets right
- Praise [S] (n=747 codable positives): fun with friends 202, horror 174, monsters 135, atmosphere 108, potential 82, value 60, content variety 53.
- "Dropped a chicken to distract the creatures, and honestly, best decision ever!"

### Where players push back
- Complaints [S] (n=873 codable): bugs 87, too short 60, repetitive 53, performance 46, difficulty 21, lag 19, needs friends 19. Negatives (n=126): bugs 19, performance 18, repetitive 18, lag 9.
- "Gets boring after 3-4 runs, nothing really exciting." / "Voice chat has a 4-5 second delay which really ruins the mood."
- <2h (n=149): bugs 11, performance 10, repetitive 8, lag 5. >20h only 20 codable (bugs 4) [S].

### Sentiment over time
- EA Oct 2024 91.5% (47), Nov 66.7%; small-count swings through mid-2025; 1.0 month Aug 2025 71.5% on 179; Dec 2025 94.4%; Jul 2026 55.6% (engine update + supporter DLC); Aug-Nov 2026 94-98% on 71-144 reviews a month while CCU sat near 14, cause unknown [P].

### What happened after launch
- Weekly patches v92-v106 through EA (ghost mode, quota game-over, revival, voice control) with CCU at 4-18 [D/T]. 1.0 (Jul 2025): Aug +639%, peak 1,185, then -70% [T]; roadmap admitted "Lack of creatures with diverse mechanics... Monotony" [D].
- Nov 2025-Mar 2026 plateau: avg 152, 913, 896, 877, 848 with flat peaks near 2,440 and tiny review counts, then Apr -92%; no matching update; possibly non-organic concurrency [I]. Later: hotel revamp, Tech Tree (beta), UE 5.5 to 5.7 [D].
- Monetisation: IAP category, supporter DLC skin, bundles (Supporter's Edition, Hyper, Horror) [P/D]; planned DLC packs and skin sales [T].

### Launch path & team
- Development from Apr 2024 [T]; demo Sep 2024; EA delayed two weeks, launched with a Scream Fest discount [D]; "over 110,000 downloads... including its demo" [D via T].
- Hypercent, Pangyo, South Korea, "21 developers in their mid-20s", first title, KOCCA support and a 2026 seed round [T]; an explicit trend play mixing Lethal Company elements with Backrooms [T]. "development progress was only 10-20% during early access" [T].

### Unknowns
- Session length; direction of the Apr 2025 price adjustment; causes of the plateau and the 2026 review surge; strangers/2-player evidence.

---

## Airport Security Sucks! (appid 4285690)
**Stratum:** mid | **Pair:** none | **Release:** 2026-06-05, full release [P] | **Price:** $7.99 [P] | **Players:** "as large as your PC can handle" [D] | **Dev/Pub:** JakeHub, Metater / Jatater Worldwide [P] | **Core type:** versus | **Reviews:** 591, 84.8% positive [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 3.40h / 3.87h / 0.84h [S] (census n=591 / 501 / 90) |
| <2h / >10h / >50h (all) | 35.2% / 16.1% / 2.0% [S] |
| Top 3 languages | English 50.9%, Russian 32.8%, Simplified Chinese 9.6% [P] |
| SteamCharts all-time peak | 685 (2026-06) [T] |
| Month 1 / 3 / 6 / 12 avg proxies | 127 (Jun-Jul 26) / 42.9 (Aug-Sep 26) / not yet available / not yet available [T] |
| Current players | 12 (2026-11-11) [P] |

### Core loop & inputs
- Round-based asymmetric hide-in-the-crowd: smugglers blend with NPC travellers to get contraband onto the plane; TSA agents arrest them without hurting innocents using voice commands, a K9 dog and a parrot; plus an air-marshal "Hijacked" mode [D store].
- Inputs: move/jump/crouch, voice commands in 13 languages, gadgets and weapons (arrest gun, shrink ray, drones, helicopters), disguises, punching, emotes, lobby mini-games; proximity voice [D/T].

### Interdependence & failure
- Smugglers coordinate distractions; agents share CCTV lockdown [D/T]. Arrest/elimination per round; one-time parachute rescue in Hijacked [D]. What eliminated players do: not found.

### What it gets right
- Praise [S] (n=398 codable positives): fun with friends 56, funny 44, value 17, physics/chaos 14, potential 13, fun with strangers 12.
- "Critically speaking this is a terrible game, but its an absolute gem with a group of friends."

### Where players push back
- Complaints [S] (n=483 codable): bugs 25, toxic randoms 20, connection 14, lag 11, performance 10, too short 10, repetitive 10. Negatives (n=85): bugs 15, connection 7, lag 7, toxic 7.
- "this game is riddled to the brim with slur bots, griefers, and overall horrible people."
- <2h (n=185): bugs 17, connection 11, toxic 9. >20h (n=22): toxic 3, lag 2 [S]. Negatives quit in under an hour (median 0.84h, 71.1% <2h) [S].

### Sentiment over time
- Launch week 84.2% (177); weekly 70-100% Jun-Sep; Oct 2026 weeks 50-80% on 4-12 reviews [P].

### What happened after launch
- Jun 2026 update: level progression with cosmetics, lobby mini-games, balance; "more than 50,000 people have played the full game" in 2 weeks [D]. Jul -69% CCU [T].
- Sep 2026 major update (helicopters, shrink ray, host item toggles, fix for lag "that could drop the game to 1 FPS", fairer team randomisation): Sep -30% anyway [D/T].
- The team then released Scam With Your Friends (2026-10-15, 5,527 reviews) [P].
- Monetisation: no DLC; cosmetics earned; bundles with Asian Parents and Scam With Your Friends; direct key sales and Ko-fi [P/D].

### Launch path & team
- Demo by Feb 2026 ("Half of those people played at least 30 minutes") [D]; public lobbies added to the demo; creator waves from SMii7Y and friends (Mar 2026) and SMii7Y + Daukey (May) [D].
- Wishlists 420 → 1,000 → 86k → 100k → 131k at launch [D]; 591 reviews per 131k wishlists ≈ 0.45% [I]. No Next Fest found.
- Two developers, JakeHub and Metater: "We wouldn't have gotten here without them" (about SMii7Y's group) [D].

### Unknowns
- Location, engine, dev time; session length; eliminated-player experience; launch discount; month 6/12 players.

---

## Foodslingers (appid 2145460)
**Stratum:** flop | **Pair:** none | **Release:** EA 2025-06-20, 1.0 2026-03-18 [P/D] | **Price:** $9.99 [P] | **Players:** 1-4; levels scale to 1/2/4, trio logic added later [D] | **Dev/Pub:** Ardent Games / Kenny Doan [P] | **Core type:** job_simulation | **Reviews:** 106, 97.2% positive [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 4.50h / 4.58h / 3.23h [S] (census n=106 / 103 / 3) |
| <2h / >10h / >50h (all) | 16.0% / 29.2% / 1.9% [S] |
| Top 3 languages | English 91.5%, Russian 2.8%, French 1.9% [P] |
| SteamCharts all-time peak | 13 (2026-07) [T] |
| Month 1 / 3 / 6 / 12 avg proxies | 2.03 (Jul 25; Jun missing) / 1.9 (Sep 25; Aug missing) / not found / not found [T] |
| Current players | 3 (2026-11-11) [P] |

### Core loop & inputs
- First-person Overcooked-style co-op kitchen: cook, parkour and physically throw food and dishes to serve timed orders across 21 levels plus Endless and Food Fight modes [D store].
- Inputs: move/run/jump/crouch, ladders, grab and throw, station interactions, perks, Polaroid camera, voice and text chat, emotes, Endless voting, mouse-only and keyboard-only options [D/P].

### Interdependence & failure
- Kitchen labour division and throwing food to each other, built to require "strong teamwork" [D]. Score thresholds and stars; Endless has an error limit and Ascension 1-5; no death; knocked-out players cannot pick up items [D].

### What it gets right
- Praise [S] (n=100 codable positives): fun with friends 39, progression/cosmetics 14, unique 13 (upper bound), physics/chaos 11, funny 10, active developer 8.
- "This game's a lot of fun and puts a nice twist on the Overcooked formula."

### Where players push back
- Complaints [S] (n=103 codable): bugs 19 (many inside positives praising same-day fixes), difficulty 8, performance 5, repetitive 4, crashes 3. Only 3 negatives: multiplayer crashes and price.
- "Every time I join with friends or have friends join with me all of our games crash."
- <2h (n=17): one each of crash, too short, difficulty. >20h (n=11): all positive [S].

### Sentiment over time
- Near 100% weekly through 2025 (14/0 in the first EA week); a few negative singles Jan-Apr 2026; 75-100% since on 1-6 reviews a week [P]. Satisfied but tiny audience.

### What happened after launch
- Frequent patches: Day-1, QoL, perks, trios support ("trios is too difficult"), cosmetic variants, Chip and challenge maps, Crumbs (Dec 2025), 1.0 with Foodlabs and Celeri (no visible player change), Spring Fling, Endless Cooking (Jun 2026), 1.2 fixes [D/P].
- Monetisation: no DLC; in-game currency cosmetics; bundle "Explosive Eats" [P/D].

### Launch path & team
- No announcement, demo, Next Fest or wishlist data found; straight to EA [P].
- Kenny Doan ("Tinfoil") with friends, part-time: made "on our free time over the past year" [D]. Prior free game Smithworks drew about 22x the reviews (2,330) [P/I]. Aim: "create core memories between friends" [D].

### Unknowns
- Engine, location; any marketing or creator outreach; session length; discount history.

---

## Cafe Crew Simulator: Prologue (appid 3723430)
**Stratum:** flop | **Pair:** none | **Release:** 2026-05-08 free prologue; full game (app 3816420) 2026-06-03 at $9.99, -20% launch [P/D] | **Price:** free [P] | **Players:** up to 3 (store) vs up to 4 (PlayWay press release) [D] | **Dev/Pub:** Woo Game Studio / PlayWay S.A. [P] | **Core type:** job_simulation | **Reviews:** 64, 82.8% positive [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 0.96h / 1.00h / 0.43h [S] (census n=64 / 53 / 11) |
| <2h / >10h / >50h (all) | 84.4% / 3.1% / 1.6% [S] |
| Top 3 languages | English 29.7%, Russian 28.1%, Simplified Chinese 9.4% (tied with Turkish) [P] |
| SteamCharts all-time peak | not found (404) |
| Month 1 / 3 / 6 / 12 avg proxies | not found |
| Current players | 0 (2026-11-11) [P] |

### Core loop & inputs
- Free prologue covering the first 4 in-game days of running a café: brew coffee, clean, serve, renovate; in multiplayer players run rival cafés and can sabotage each other [D store].
- Inputs: grinder mini-game, coffee machine, syrups, trays, cleaning, renovation, sabotage, football between cafés (World Cup event) [D]. Voice/text chat not found.

### Interdependence & failure
- Co-op inside a café or PvP between cafés ("Cooperate... or create chaos") [D]. Lost customers and reputation; no fail state or death found.

### What it gets right
- Praise [S] (n=42 codable positives): potential 8, free/value 5, relaxing/cozy 4, fun with friends 3, progression 3.
- "The game is very relaxing and I certainly enjoyed it."

### Where players push back
- Complaints [S] (n=52 codable): bugs 8, too short 2, single mentions of connection, repetitive, toxic, difficulty, camera. Negatives (n=10): bugs 4, connection 1, controls 1.
- "Only played for 20 minutes and had to completely restart twice because of bugs."
- Almost all reviews are <2h (45 of 52 codable; bugs 7); one >20h review. A Japanese reviewer found the café work dull but loved the side football game [S].

### Sentiment over time
- Launch week 80% (15); week of 05-29 100% (13) in the run-up to the full game; 33-100% on 1-4 reviews a week since [P].

### What happened after launch
- Lighting overhaul and a spawn system that "adapts to your pace" for solo (May 14), fixes (May 18), full-game launch with progress carry-over (Jun 3), World Cup event (Jun 15) [D]. Full game: 89 reviews, 81% positive [P].
- Monetisation: prologue free; the full game is the product; bundled with "The Walking Trade" [T].

### Launch path & team
- PlayWay press release with free keys, "no embargo restrictions" and an open invitation to streamers [T]; prologue used as a wishlist funnel [D]. No Next Fest or viral moment found.
- Woo Game Studio: location, size, engine and prior games not found.

### Unknowns
- CCU; team; definitive player cap; prologue-to-full-game conversion.

---

## Lamentations (appid 3191800)
**Stratum:** flop | **Pair:** none | **Release:** 2025-02-21, full release [P] | **Price:** $4.99 [P] | **Players:** solo, 3-player co-op, 1v1 PvP [D] | **Dev/Pub:** Yooper Game Studios LLC / same [P] | **Core type:** escape_survival | **Reviews:** 34, 61.8% positive [P]

### Snapshot
| Metric | Value |
|---|---|
| Median playtime at review (all / pos / neg) | 0.70h / 0.63h / 0.70h [S] (census n=34 / 21 / 13) |
| <2h / >10h / >50h (all) | 79.4% / 0.0% / 0.0% [S] |
| Top 3 languages | English 85.3%, French 5.9%, Simplified and Traditional Chinese 2.9% each [P] |
| SteamCharts all-time peak | not found (HTTP 500) |
| Month 1 / 3 / 6 / 12 avg proxies | not found |
| Current players | 0 (2026-11-11) [P] |

### Core loop & inputs
- Backrooms PvE dungeon-crawl FPS: buy a loadout, descend by elevator, solve key/lever puzzles, fight or avoid monsters and bosses, restore the elevator and extract; PvPvE "Wager Extraction" pools wagers, one life each [D store].
- Inputs: move/sprint with stamina, jump, swim, shoot, reload, grenades, knife, abilities, flashlight, proximity voice and lobby text chat, gamepad beta [D].

### Interdependence & failure
- Keys are needed to finish levels (dead players now drop keys to prevent soft-locks); the team must restore the elevator [D]. Death means "become another casualty"; one life in PvP [D].
- Dead players get a spectate camera; a revive station planned for v1.1.0 apparently never shipped [D/I].

### What it gets right
- Praise [S] (n=20 codable positives): fun with friends 9, horror 6, monsters 6, atmosphere 5, value 4.
- "pretty fun with friends and was a pretty good deal for 5 bucks."

### Where players push back
- Complaints [S] (n=32 codable): bugs 6, performance 3, too short 3, too punishing 2; technical failure in 67% of the 12 codable negatives.
- "Beat the game in like 40 minutes while not having any idea of what is happening." / "No randomness to level layout or enemy spawns."
- <2h (n=25): bugs 4, too short 2, difficulty 2. No >20h reviews [S]. Minimum spec is an RTX 2070 [P], high for a $4.99 game.

### Sentiment over time
- Launch Feb 2025 70% (20 reviews); 0/2 and 0/2 in the next two weeks; 8 reviews in total after March 2025 [P].

### What happened after launch
- Hotfixes #1-3 (Feb 2025), a release stream with streamer Croakitoad, Dev Update #1 (2025-03-01) planning v1.1.0 (grenade launcher, revive station, procedural spawns, horde mode, new map); no posts after [D/P].
- Monetisation: no DLC; 40 unlockable weapon skins [D].

### Launch path & team
- Press-preview demo Oct 2024, demo v2.0.0 with PvP and voice, Next Fest Oct 2024, INDIE Live Expo Dec 2024, one partner streamer [D]. Full release, self-published.
- Solo developer ("As a solo dev/publisher") [D]; Unreal 5 inferred from "lumen lighting" [I]; prior game Super Battle PolyCars; next project Exodus of Descent on Kickstarter [D].

### Unknowns
- CCU; location; demo player and wishlist numbers; whether v1.1.0 was ever made; session length.


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


