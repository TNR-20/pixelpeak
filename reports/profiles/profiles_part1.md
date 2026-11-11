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
