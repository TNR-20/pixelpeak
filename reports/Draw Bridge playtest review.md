# Draw Bridge (3D build): playtest review

Build reviewed: `prototypes/draw_bridge/fps_iso_test.html`. It has a 3D driver view (chase or first person, with fog), a drawer view (side 2D with a top-view strip, or slanted 2.5D), free steering on a 360-wide track, ink drops and a pop-out driver window.
Date: 2026-11-11

> The truck physics (`carStep`) and the room layouts (`WORLDS`) are **identical** to `index.html`, so every physics finding from the 2D build applies here too. They are summarised under P0-4.

## Verdict

The 3D build is a real step forward on the 2D build's biggest problem. **Ink drops give the driver a job that matters.** In my runs, whether the drawer could build the second section depended entirely on whether the driver steered for drops in the first. That is the two-way dependence the 2D build lacked. The drawer's side view, with the top-view strip and the yellow "what the driver sees" fan, is also very good tooling.

But the 3D layer currently **hides the core fantasy from the driver**. In both cameras the driver can't actually see the line their friend drew: the truck covers the end of the bridge in chase view, and in first person the bridge isn't in frame at all. And because every line spans the full track width, steering never touches the drawing. The new axis (sideways position) is used only for drop pickup and falling off the edges, not for the bridges themselves.

**Score (prototype stage):** Hook 8/10 · Core loop 6/10 · Role balance 6/10 (was 3) · Driver readability 3/10 · Drawer tools 8/10 · Replay structure 4/10 · Performance 9/10.

## How this was tested

- I drove the game's own `update()` at a fixed 60 fps from script, drawing through real pointer events in the drawer's view, and rendered real frames of both views for screenshots. A bot driver used gas, hops and a steering controller that aims for the next ink drop.
- I ran about 15 scripted attempts in World 1 (First bridge, Island) plus camera checks in chase, first person, side view and slanted 2.5D. The physics findings are the ~45 attempts from the 2D review; the code is identical.
- This was not a session with two real people. It measures what is possible and what is visible, not fun or how players talk. Rendering cost is about 1.8 ms per frame for both views at 1.25× DPR, so performance is not a concern.

## What works: keep these

1. **Ink drops create two-way dependence.** On the same seed:
   - **Driver ignores drops:** the drawer reaches Island with **265–280 ink**. Island needs about 461 for straight planks; full planks ran dry mid-stroke and short planks crashed.
   - **Driver steers for drops:** collecting 3 of 4 drops in section 1 raises that to **475 ink**, which is enough for straight planks.
   
   The driver's play directly decides what the drawer can build. That is the coupling to build around.
2. **The drawer's information tools.** The "driver sees up to here" line, the yellow sight fan and the top-view strip, which shows drops, the truck's heading and ink bands, give the drawer a reason to call things out, and the driver a reason to listen.
3. **Information asymmetry as a design pillar.** A driver with a limited view (fog at 100–380) plus a drawer who sees everything is a proven recipe for shouting-at-each-other co-op. Keep the asymmetry, but see P0-1: it must hide *the road ahead*, not *your friend's work*.
4. **The slanted 2.5D drawer view** is the most readable view in the build. Bridges, gaps and the truck all read at a glance.
5. **Pop-out driver window.** Two screens, one per player, fixes the cramped "two people on one keyboard" problem. It is also the right stepping stone towards online play.
6. **The economy shape:** a full tank to start, +50% at each checkpoint, carry-over up to 1.5×, +25% per drop. Saving ink across sections creates real planning.

## P0: fix before building more

### P0-1. The driver can't see the drawer's work

- **Chase camera (default):** the truck sits dead centre and covers exactly the spot where the bridge ends. With a half-built bridge, the driver can't tell whether it continues. The far platform, about 200 units away, sits inside the fog band (100→380) and renders as a **translucent ghost box**, which reads as "not solid".
- **First person:** the hood fills the bottom of the frame, and the purple bridge the truck is driving on is **not visible at all**. The frame shows only the far platform's front face.
- The moment that should sell the game, "my friend's line appears in front of me just in time", currently happens only in the drawer's view.

**Fixes to try:**
- Raise the chase camera and pitch it further down, or fade the truck to ~40% opacity when a line end is within 150 units.
- Exclude ink lines from fog, or give them an emissive top surface and a bright end-cap. Your own lines should be the most visible thing on screen.
- Draw gaps as dark voids and solid ground as solid. Keep fog for "how far ahead", never for "is this solid".
- Add a "road ends" marker (a red lip or a flag) at every line end and ledge.

> **Status (2026-11-11): first pass done in `fps_iso_test.html`.** Ink lines ignore fog and glow slightly, and are culled beyond the driver's view distance so the limit still holds. Open line ends get a yellow and black hazard lip (not where a line meets ground or another stroke). Fog now covers only the last ~40% of the view. The driver view adds a dark void under the track and darker pit walls. The cameras are retuned in `DCAM`: chase 140 back, 135 up, pitch −0.42; first person 22 above the head, pitch −0.42, at least 48° vertical field of view. Screenshots confirm the lip at the end of a half bridge is visible in both cameras. It is not yet checked with human drivers or in the pop-out window. Ledges themselves still have no marker.

### P0-2. The drawing ignores steering

`viewLevel()` treats every level piece and every ink line as spanning the full 360-wide track. So the drawer still draws in 1D, and steering only matters for drops and edges. This is the biggest opportunity in the build:
- **Give lines a width.** The drawer places a plank in a lane, using the top-view strip or the 2.5D view, and the driver has to steer onto it. Then a failure tells you whose fault it was: "you drew it in the wrong lane" or "you missed my bridge". And the driver's steering becomes part of the shared object.
- Start wide (half the track) in World 1 and narrow it in later worlds. Narrow lines also cost less ink, which ties into the economy.

### P0-3. The driver still dies at spawn

Holding gas with no lines: the first death at **1.2 s**, then a death every **0.9 s**. The drops don't help here, because there's nothing to collect before the first gap. The title screen still promises "No waiting".
- Put 1–2 drops in the area before the first gap of each section, so the driver's first job is to fetch ink while the drawer plans.
- Or start each section with a short "drawer's lead" window, like a gate that opens when the drawer finishes the first stroke.

### P0-4. Physics surprises (shared with the 2D build) — fixed in `fps_iso_test.html`

Measured with a scripted suite in the 3D build, before and after. The before numbers come from the backup `fps_iso_v1_before_physics.html`.

| Issue | Before | After | What changed |
|---|---|---|---|
| A spring drawn like a ramp throws the truck **backwards** | speed +244 became **−110**; 0/2 ramp springs passed Up! | speed +243 becomes **+665**; 2/3 pass (the miss is a spring right against the ledge) | `springDir()`: a floor-like spring never pushes backwards and adds a little forward carry |
| In Up! (the spring tutorial), a flat spring only works close to the ledge | passed only at **420–480** (~60 px band) | passes at **340–470** (~130 px band) | forward carry, and incoming speed is cancelled before the launch so every bounce is the same height |
| Driving off a ledge or over a crest tips the truck into a nose-dive | The wall ramp **0/3** (bonk every time); The drop ended wedged on its belly or bonked (**0/4**) | The wall **3/3**; The drop **5/6** (the miss is a ramp starting 90 px out from the cliff with the truck rolling from a standstill) | uncommanded spin is capped at 1.3 rad/s while a wheel is off the ground; leaning on gas or brake still allows 6 rad/s, so flips stay possible; gentle self-levelling in the air when the driver isn't leaning |
| Landing on the start tip of a drawn ramp bounces the truck backwards | wheel hit the tip, speed +246 became −129, then a bonk | the wheel is pushed off the line's surface instead ("ramp catch") | only on the end the truck is driving onto, so drive-off ends and gap sizes are unchanged |
| Beached on its belly (wheels in the air, body on a line) is a silent soft-lock | stuck forever, no prompt, no fail | "Stuck! (Space)", Space kicks it, auto-reset after 2 s | the existing flip timer and kick also cover the beached state |
| Flip prompt said "(W)", but W is gas in this build | — | says "(Space)" | text fix |
| Long jump | booster + hop + rocket **4/6** hop timings; booster + hop **0/4** | **5/6** and **2/4** | side effect of the spin cap. *Correction:* the earlier "1 of 6" came from a test driver that held gas through the whole flight and backflipped itself |

No regressions on the World 1 obvious solutions: First bridge, the short-plank star trick, The climb, Low ceiling, Two gaps and Island all still pass. Spring pit passes 3/3 with plank + spring.

**Follow-up (2026-11-11): special inks are now placed pads, not drawn lines.** Spring and booster are clicked onto a surface: ground, a hill, or a drawn plank.
- **Springs:** drag while placing to aim, up to 60° from vertical; a longer drag gives more power, costing 35–80 ink. A dotted preview arc tracks the real flight within 5–9 px over the first 0.6 s.
- **Boosters:** 60 ink each; drag left or right to set the direction.
- **Visibility:** both carry white arrows or chevrons that the driver sees too.
- **Measured:** a plain click clears Up! from 360 to 480. Aimed from further back, using only the preview to choose, it passed 3/3, and the preview correctly showed when the ledge was out of reach. Spring pit (plank + pad) passes. Long jump with one 60-ink booster pad, hop and rocket passes 3/3 (it needed 195 ink of drawn booster before).
- **Removal:** pads on an erased plank are removed and refunded.

The previous version is `fps_iso_v2_before_pads.html`.

**Follow-up: driver-triggered springs (on by default; test key G switches back to fire on contact).** A spring pad only arms when touched, and "Jump!" flashes on the driver's view; the driver must press Space to fire the aimed launch.
- **No press:** nothing happens.
- **Armed window:** about 0.63 s at cruising speed (on the pad, plus 0.15 s after leaving it). A hop pressed just before the pad is held back and fires on contact instead of being a normal hop.
- **Measured on Up!:** with a pad 140 px from the ledge, a press anywhere from 340 to 420 works and reactions of 0.05–0.3 s after "Jump!" work. With an aimed pad placed further back, reactions of 0.05–0.55 s work. So the drawer's placement decides how much timing slack the driver gets.
- **Drawer preview:** the main arc assumes a press mid-pad, and faint arcs show the earliest and latest launch.
- **Regressions:** fire-on-contact mode, Spring pit and normal hops all still pass.

The previous version is `fps_iso_v3_before_trigger.html`.

**Follow-up: spring pads now render as an in-ground trampoline** instead of a yellow slab: a black mat level with the road, blue frame padding and silver springs, keeping the white aim arrows. The mat glows orange while the pad is armed and bounces after a launch. This is visual only; the physics is unchanged. The previous version is `fps_iso_v4_before_trampoline.html`.

**Follow-up: booster pads now render as an in-ground conveyor speed strip:** a dark belt, pink side rails, and striped steel end rollers that spin the way it pushes, with three rows of glowing chevrons streaming in the push direction. While the truck is on it, the belt glows magenta and the chevrons turn white and speed up. This is visual only; the booster regression (one pad, hop and rocket on Long jump) still passes 3/3. The previous version is `fps_iso_v5_before_booster_model.html`.

**Not done yet:**
- Retuning the World 1 copy that mentions wall-jumping.
- A check with humans that the 1.3 rad/s cap doesn't make the truck feel floaty off big drops. All the values are in `K` (`wFree`, `wCmd`, `level`, `springJ`, `springFwd`).

The steering projection still stretches gaps when driving at an angle: at ψ ≈ 0.6, a 220 gap behaves like ~265.

## P1: major

### P1-1. The ink economy can soft-lock

- Drops stay collected after a death and never come back, and nothing else adds ink within a section. If the team arrives short, its only outs are partial-plank tricks or **Restart level**.
- In my seed, the only drop that would have rescued the "ignored drops" run was **behind the respawn point**, so the driver had to reverse to reach it, and nothing tells them that.
- **Fixes:** give each checkpoint a floor (top up to at least the section's minimum need); respawn drops on death; or add a slow trickle when the tank is nearly empty.

### P1-2. Drops spawn behind the truck

`makeBlots` starts placing drops at x = 70–160, but the level spawn is at x = 240. So **the first drop of every level is always behind the truck**. On this seed, two more sat between a section's start and its spawn point, which also puts them behind the respawn point.
- Start placement at spawn + 60, and skip the range [x0, start.x + 40] in every section.

### P1-3. Shuffling breaks the difficulty curve (same as 2D)

In this seed World 1 ran First bridge → **Island** → The wall → **The climb** → Two gaps → The drop → Low ceiling. The easiest room after the tutorial came fifth. Shuffle within difficulty tiers. The Sky shelf and Backwards rooms still never appear.

### P1-4. One shared screen is a compromise

The default stacked layout splits one monitor and one keyboard and mouse between two people. The pop-out is the real layout, so treat "two windows" (and later online) as the target and the stacked view as a dev tool. The netcode case is good: lines are small events, and only the truck needs authoritative physics.

## P2: polish and bugs

- ~~**Wrong key in the flip prompt:** it said "(W)", but W is gas in this build and the kick is Space.~~ Fixed.
- The World 1 intro and the Plank tool tip still mention wall-jumping, which the truck can't do.
- A held steer from the centre reaches the track edge in about 1.2 s at top speed, with no rails, warning or edge rumble. Add an edge highlight or a shoulder strip so falling off the side feels like a fair mistake.
- **Dark mode:** panel text is #9c9a92 on cream, about 2.6:1 contrast (same CSS as the 2D build).
- Fogged platforms looked semi-transparent: the fog colour is the paper colour, so they faded into the background. Addressed by the fog change in P0-1.

## Against your own design requirements

| Requirement (from *Friendslop coop game gaps*) | 3D build |
|---|---|
| Hook readable in 10 s | ✅ From the drawer's view · ❌ from the driver's (P0-1) |
| Each mistake has a visible author | ⚠️ Physics surprises remain, and full-width lines remove lane-based blame |
| No idle player | ⚠️ Better: the driver hunts drops. Still idle or dying before the first gap |
| Every seat has a continuous, distinct job | ✅ Mostly: the driver steers for ink, the drawer spends it |
| Difficulty from coordination | ✅ The drop call-outs are coordination · ⚠️ steering doesn't touch the bridges yet |
| Run-to-run variation through systems | ⚠️ Drop placement is seeded, but rooms are still a thin shuffle |
| Tuned for 2, scales to 4 | ❌ Exactly 2 |
| Comfortable camera, no motion sickness | ⚠️ First person with a limited view and a fixed pitch is fine, but untested with humans |
| Online is reliable | Pop-out is a good step · online not started |

## Next 3 experiments (in this order)

1. **Make lines visible to the driver** (fog-exempt lines, end-caps, camera pitch, truck fade). Then check: can the driver tell from their own view alone whether the bridge ahead is complete?
2. **Lines with lane width.** Prototype a plank half the track wide that the drawer positions in the top strip or 2.5D view. Measure: does steering failure now get blamed on the right person?
3. **Fix the economy edges.** Add a checkpoint ink floor, respawn drops on death, and drops in front of the spawn instead of behind it. Re-run the "driver ignores drops" scenario: the team should be slower and miss stars, not get stuck.

## Human playtest protocol

- 5 or more pairs, using the **pop-out on two screens**. Run one pair in chase camera and one in first person per session.
- Measure: time to the first death; the share of drops collected; how often the driver asks "is it there?" (a P0-1 signal); restarts caused by running out of ink (a P1-1 signal); deaths off the track edge.
- Code the audio for **call-outs** (good: "drop on your left!") versus **blame** (bad when it is about physics surprises).
- Ask after each world: "Driver, did you ever see your friend's bridge appear?" If the answer is no, P0-1 isn't solved yet.
