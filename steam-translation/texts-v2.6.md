# Kayak Photography Sim — Steam Store Page Localization (v2)

Full rewrite of all 15 languages. This supersedes the earlier file.

## What changed and why

A Russian-speaking reader found the first Russian version poor and hard to follow. On re-inspection it had real errors, not style quibbles — an idiom missing its required preposition (`никто не гонится` with no `за тобой`), an English-style compound that Russian doesn't form (`каяк-игра`), a broken reflexive (`где ничего не отсчитывается`), and a term borrowed from mechanical engineering by accident (`свободный ход`).

The cause was the same across the whole set: the first pass mapped English sentence structures onto each language instead of writing in that language's own idiom. Every text here was rebuilt on the second approach. Concretely, that means:

- **"Nowhere you have to be"** means freedom from obligation, not absence of company. An earlier pass rendered it as "nobody is waiting for you anywhere" in ten languages; a Russian reader flagged that this reads as rejection. It is now phrased as having no schedule to keep — *aucun horaire à tenir*, *и никуда не надо успевать*, *żadnych terminów*, *急ぐ理由はどこにもありません*.
- **The paddle-audio section states the mechanic plainly** — each stroke is processed separately, and the sound comes from the side you pull on. The earlier "built stroke by stroke" phrasing said nothing concrete and translated badly.
- **Nautical terms come from each language's own sailing vocabulary** — *sur sa lancée*, *per abbrivio*, *in seiner eigenen Fahrt*, *op eigen vaart*, *по инерции*.
- **Idioms are complete.** Verbs that require a preposition or object have one.
- **Antecedents are explicit.** "A few will end up in your wallpapers" now points at photos, not at places, in every language.
- **No gendered forms addressed to the player** in Polish, Russian, or Ukrainian.

## Honest status

This is a better second draft. It is not a verified translation.

**Russian is the exception** — it was written by a native speaker rather than translated, so it is the one entry here that is confirmed. Turkish has been read by Hasan and corrected. Everything else is unverified.

Two rounds of native review have now happened, and both found real errors that the self-review passes missed. The errors that survive self-review are tonal, not grammatical: phrasing that parses correctly but lands wrong. When asking a native reader to check one of these, the useful question is "does anything here sound unkind or off," not "is this correct."

Recommended order if native review is available for only some:

1. **Simplified Chinese** — largest non-English Steam market, so the stakes are highest even where confidence is decent.
2. **Thai** — lowest confidence in this set.
3. **Korean, Japanese** — the register choices (해요체, です/ます) are defensible but are taste calls in tone-sensitive markets.
4. Everything else. (Russian is done — a native speaker wrote it.)

A missing language is neutral: those players see the English page and nothing is lost. A broken language is worse than nothing, because it gets quoted in reviews and forums.

## Before pasting

- **Short description cap is 300 characters per language.** All verified below.
- **BBCode and image paths stay untranslated.** `[p]`, `[h2]`, `[list]`, `[b]` and `{STEAM_APP_IMAGE}/extras/...` are identical in every language.
- **Chinese is two separate fields.** Simplified → 简体中文, Traditional → 繁體中文. They are not conversions of each other; the vocabulary differs (皮划艇/獨木舟, 壁纸/桌布, 文件/檔案, 相册/相簿, 硬盘/硬碟, 界面/介面, 打印/列印). A Simplified reader never sees the Traditional field, and vice versa.
- **Spanish is Spain only. Portuguese is Brazil only.** Other locales need separate versions.
- **The Languages table on the store page is a different thing** — it declares what the build supports, not what the store page is translated into.

## Character counts (short descriptions)

| Language | Steam field | Chars |
|---|---|---|
| French | french | 286 |
| Italian | italian | 270 |
| German | german | 276 |
| Spanish (Spain) | spanish | 270 |
| Dutch | dutch | 269 |
| Japanese | japanese | 116 |
| Korean | koreana | 138 |
| Polish | polish | 232 |
| Portuguese (Brazil) | brazilian | 257 |
| Russian | russian | 266 |
| Simplified Chinese | schinese | 86 |
| Thai | thai | 207 |
| Traditional Chinese | tchinese | 88 |
| Turkish | turkish | 264 |
| Ukrainian | ukrainian | 299 |

## Form of address

| Language | Choice |
|---|---|
| French | vous |
| Italian, German, Spanish, Dutch, Polish, Turkish, Ukrainian, Chinese (both) | informal singular |
| Russian | formal **вы** — the native writer's choice, normal for a Russian store page |
| Portuguese (BR) | você |
| Japanese, Korean, Thai | no second-person pronoun at all |

Japanese uses です/ます, Korean uses 해요체, Thai omits the ครับ/ค่ะ politeness particles (they are speaker-gendered and not used in written marketing).

---

# English

Updated to match the translations — the four edits below were applied here too.

**Short**

```
A meditative kayaking and photography sim. Open water, a slow boat, and nowhere you have to be. Paddle until you feel like stopping, photograph whatever catches your eye, dive underwater to explore what's down there. Nothing chases you. Nothing is timed. You're just chilling and exploring.
```

**Full**

```
[p][b]Kayak Photography Sim[/b] is a first-person kayaking game about going wherever you want on the water and photographing what you find there — even underwater pictures.[/p][p]Get in, push off, pick a direction. The water is clear enough to see the bottom, so what's below you is as much of the world as what's around you.[/p][h2]Nothing will disturb you[/h2][p]No timers. No stamina bar. No scoreboards. No pace to keep.[/p][p]Just keep paddling and enjoy the journey.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_paddle"][/img][/p][p] [/p][h2]Camera in hand[/h2][p]Raise the camera and everything slows down. Zoom in and the background softens. Press the shutter and hear it click.[/p][p]Every shot stays in a gallery between sessions and saves to your PC as a real file. Print it, post it, send it to a friend. The places you paddle are cinematic enough that a few will end up in your wallpapers folder.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_photo2"][/img][/p][p] [/p][h2]Go under[/h2][p]The water isn't scenery. Half of what's out there is underneath it, and you can reach all of it — slip out of the kayak whenever you want. No gear screen, no dive timer, no oxygen gauge.[/p][p]A sailing ship lying on its side. A passenger plane broken across the sand. Nothing marks them and nothing points you there — you find them because you looked down at the right moment.[/p][p]Down there the fish carry on without you. Get close enough for the shot without scattering them, then float back up whenever you feel like it.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_diveandexploreunderwater"][/img][/p][p] [/p][h2]The sound of the paddle[/h2][p]Each stroke is processed separately. Pull on the right and the sound comes from the right; pull on the left and it comes from the left.[/p][p]Ease off entirely and the paddle comes up. The boat keeps gliding on its own momentum until you dip back in.[/p][h2]Features[/h2][list][*][p][b]A kayak with real momentum.[/b][/p][/*][*][p][b]Open water to roam.[/b] No route, no waypoints, no wrong direction. Paddle out and see where you end up.[/p][/*][*][p][b]A real-time in-game camera.[/b] 28–70mm, background softening on zoom, a shutter that clicks. Works above and below the water.[/p][/*][*][p][b]Photos saved locally.[/b] A gallery that persists between sessions, image files written straight to your PC.[/p][/*][*][p][b]Dive anywhere, any time.[/b] Leave the kayak for warm, clear water — no oxygen gauge, no time limit.[/p][/*][*][p][b]Unmarked wrecks to find.[/b] A sunken sailing ship, a fallen plane, and the rare fish living around them — none of it flagged on a map.[/p][/*][*][p][b]Water audio for every stroke.[/b] Each one sounds different, and comes from the side you pull on.[/p][/*][/list]
```

---

# French — `french`

**Short** (286)

```
Un simulateur de kayak et de photographie, tout en douceur. De l'eau à perte de vue, un bateau qui prend son temps, aucun horaire à tenir. Pagayez tant que ça vous chante, photographiez ce qui vous plaît, plongez voir ce qu'il y a dessous. Rien ne vous poursuit, rien n'est chronométré.
```

**Full**

```
[p][b]Kayak Photography Sim[/b] est un jeu de kayak à la première personne : vous naviguez où bon vous semble et vous photographiez ce que vous croisez en chemin, y compris sous l'eau.[/p][p]Vous embarquez, vous poussez au large, vous choisissez un cap. L'eau est si limpide qu'on voit le fond : ce qui se trouve sous la coque fait autant partie du monde que ce qui vous entoure.[/p][h2]Personne ne viendra vous déranger[/h2][p]Ni chrono, ni barre d'endurance, ni classement. Aucun rythme à tenir.[/p][p]Continuez à pagayer, et savourez le trajet.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_paddle"][/img][/p][p] [/p][h2]L'appareil photo à la main[/h2][p]Vous levez l'appareil, tout ralentit. Vous zoomez, l'arrière-plan part dans le flou. Vous appuyez sur le déclencheur, vous entendez la mécanique claquer.[/p][p]Chaque cliché reste dans la galerie, même après avoir quitté le jeu, et se retrouve sur votre disque en fichier image ordinaire. À imprimer, à publier, à envoyer à un ami. Les paysages que vous traversez sont assez cinématographiques pour que deux ou trois de vos photos finissent en fond d'écran.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_photo2"][/img][/p][p] [/p][h2]Sous la surface[/h2][p]L'eau n'est pas un décor. La moitié de ce qu'il y a à voir se trouve dessous, et rien n'est hors d'atteinte : quittez le kayak dès que l'envie vous prend. Ni écran d'équipement, ni minuteur de plongée, ni jauge d'oxygène.[/p][p]Un voilier couché sur le flanc. Un avion de ligne brisé en deux sur le sable. Rien ne les signale, rien ne vous y mène : vous tombez dessus parce que vous regardez vers le fond au bon moment.[/p][p]En bas, les poissons vaquent à leurs occupations. Approchez-vous assez près pour le cliché sans faire fuir le banc, puis remontez quand ça vous chante.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_diveandexploreunderwater"][/img][/p][p] [/p][h2]Le son de la pagaie[/h2][p]Chaque coup de pagaie est traité séparément. Vous tirez à droite, le son vient de droite ; à gauche, il vient de gauche.[/p][p]Arrêtez-vous complètement, la pagaie se relève. Le bateau continue de glisser sur sa lancée jusqu'à ce que vous replongiez la pale.[/p][h2]Caractéristiques[/h2][list][*][p][b]Un kayak qui garde son élan.[/b][/p][/*][*][p][b]De l'eau libre, sans limites.[/b] Ni itinéraire, ni points de passage, ni mauvaise direction. Partez, et voyez où ça vous mène.[/p][/*][*][p][b]Un appareil photo intégré, en temps réel.[/b] 28-70 mm, flou d'arrière-plan au zoom, un déclencheur qui claque. Fonctionne au-dessus comme au-dessous de l'eau.[/p][/*][*][p][b]Des photos enregistrées sur votre disque.[/b] Une galerie qui subsiste après avoir quitté le jeu, et des fichiers image bien réels.[/p][/*][*][p][b]Plongez où vous voulez, quand vous voulez.[/b] Laissez le kayak et descendez dans une eau chaude et claire, sans jauge d'oxygène ni limite de temps.[/p][/*][*][p][b]Des épaves que rien ne signale.[/b] Un voilier coulé, un avion tombé, et les poissons rares qui vivent autour. Rien de tout cela n'apparaît sur une carte.[/p][/*][*][p][b]Un son d'eau propre à chaque coup.[/b] Chaque coup de pagaie sonne différemment, du côté où vous tirez.[/p][/*][/list]
```

---

# Italian — `italian`

**Short** (270)

```
Un simulatore di kayak e fotografia da prendere con calma. Acque libere, una barca che va con calma e nessun orario da rispettare. Pagaia finché ne hai voglia, fotografa quello che ti colpisce, immergiti a vedere cosa c'è sotto. Niente ti insegue, niente è cronometrato.
```

**Full**

```
[p][b]Kayak Photography Sim[/b] è un gioco di kayak in prima persona: navighi dove ti pare e fotografi quello che incontri lungo la strada, anche sott'acqua.[/p][p]Sali, stacchi da riva, scegli una direzione. L'acqua è così limpida che si vede il fondo: quello che hai sotto lo scafo è parte del mondo quanto quello che ti sta intorno.[/p][h2]Nessuno verrà a disturbarti[/h2][p]Niente timer, niente barra della stamina, niente classifiche. Nessun ritmo da tenere.[/p][p]Continua a pagaiare e goditi la strada.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_paddle"][/img][/p][p] [/p][h2]La fotocamera in mano[/h2][p]Alzi la fotocamera e tutto rallenta. Zoomi e lo sfondo va fuori fuoco. Premi il pulsante di scatto e senti il clic.[/p][p]Ogni foto resta nella galleria anche dopo aver chiuso il gioco e finisce sul disco come un normale file immagine. Stampala, pubblicala, mandala a qualcuno. I posti che attraversi sono abbastanza cinematografici da far finire due o tre di quelle foto tra i tuoi sfondi.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_photo2"][/img][/p][p] [/p][h2]Sotto la superficie[/h2][p]L'acqua non è scenografia. Metà di quello che c'è da vedere sta lì sotto, e niente è fuori portata: esci dal kayak appena ti va. Niente schermata dell'equipaggiamento, niente timer di immersione, niente indicatore dell'ossigeno.[/p][p]Un veliero coricato su un fianco. Un aereo di linea spezzato in due sulla sabbia. Niente li segnala e niente ti ci porta: ci finisci sopra perché guardi verso il fondo al momento giusto.[/p][p]Laggiù i pesci si fanno gli affari loro. Avvicinati quanto basta per lo scatto senza disperdere il branco, poi risali quando ti va.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_diveandexploreunderwater"][/img][/p][p] [/p][h2]Il suono della pagaia[/h2][p]Ogni pagaiata è trattata a sé. Tiri a destra e il suono arriva da destra, tiri a sinistra e arriva da sinistra.[/p][p]Smetti del tutto e la pagaia si solleva. La barca continua per abbrivio finché non rimetti la pala in acqua.[/p][h2]Caratteristiche[/h2][list][*][p][b]Un kayak che conserva l'abbrivio.[/b][/p][/*][*][p][b]Acque libere, senza confini.[/b] Nessun percorso, nessun waypoint, nessuna direzione sbagliata. Parti e vedi dove finisci.[/p][/*][*][p][b]Una fotocamera integrata, in tempo reale.[/b] 28-70 mm, sfondo fuori fuoco con lo zoom, uno scatto che si sente. Funziona sopra e sotto la superficie.[/p][/*][*][p][b]Foto salvate sul tuo disco.[/b] Una galleria che resta anche dopo aver chiuso il gioco, e file immagine veri e propri.[/p][/*][*][p][b]Immergiti dove vuoi, quando vuoi.[/b] Lascia il kayak e scendi in acqua calda e limpida, senza indicatore dell'ossigeno né limiti di tempo.[/p][/*][*][p][b]Relitti che nessuno segnala.[/b] Un veliero affondato, un aereo caduto e i pesci rari che ci vivono intorno. Niente di tutto questo compare su una mappa.[/p][/*][*][p][b]Un suono d'acqua per ogni pagaiata.[/b] Ognuna suona diversa, dal lato da cui tiri.[/p][/*][/list]
```

---

# German — `german`

**Short** (276)

```
Ein meditativer Kajak- und Fotografie-Simulator. Offenes Wasser, ein gemächliches Boot, und kein Termin, den du einhalten musst. Paddle, solange du Lust hast, fotografiere, was dir auffällt, tauch ab und schau, was da unten liegt. Nichts jagt dich, nichts läuft gegen die Uhr.
```

**Full**

```
[p][b]Kayak Photography Sim[/b] ist ein Kajakspiel aus der Ego-Perspektive: Du fährst über das Wasser, wohin du willst, und fotografierst, was dir unterwegs begegnet — auch unter der Oberfläche.[/p][p]Einsteigen, vom Ufer abstoßen, eine Richtung wählen. Das Wasser ist so klar, dass man den Grund sieht: Was unter dem Boot liegt, gehört genauso zur Welt wie das, was dich umgibt.[/p][h2]Niemand wird dich stören[/h2][p]Keine Timer, keine Ausdauerleiste, keine Bestenlisten. Kein Tempo, das du halten müsstest.[/p][p]Paddle einfach weiter und genieß die Strecke.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_paddle"][/img][/p][p] [/p][h2]Die Kamera in der Hand[/h2][p]Du hebst die Kamera, alles wird langsamer. Du zoomst heran, der Hintergrund geht ins Unscharfe. Du drückst ab und hörst den Auslöser klicken.[/p][p]Jede Aufnahme bleibt in der Galerie, auch nachdem du das Spiel beendet hast, und landet als ganz normale Bilddatei auf deiner Festplatte. Ausdrucken, posten, jemandem schicken. Die Gegenden, durch die du paddelst, sind kinoreif genug, dass zwei, drei deiner Fotos als Hintergrundbild enden.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_photo2"][/img][/p][p] [/p][h2]Unter die Oberfläche[/h2][p]Das Wasser ist keine Kulisse. Die Hälfte von allem, was es zu sehen gibt, liegt darunter, und nichts davon ist unerreichbar: Steig aus dem Kajak, sobald dir danach ist. Kein Ausrüstungsmenü, kein Tauchtimer, keine Sauerstoffanzeige.[/p][p]Ein Segelschiff, das auf der Seite liegt. Ein Passagierflugzeug, im Sand entzweigebrochen. Nichts markiert sie, nichts führt dich hin — du stößt auf sie, weil du im richtigen Moment nach unten schaust.[/p][p]Da unten gehen die Fische ihren eigenen Sachen nach. Komm nah genug für die Aufnahme, ohne den Schwarm zu verscheuchen, und lass dich wieder nach oben treiben, wann immer du magst.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_diveandexploreunderwater"][/img][/p][p] [/p][h2]Der Klang des Paddels[/h2][p]Jeder Paddelschlag wird einzeln berechnet. Ziehst du rechts, kommt der Ton von rechts; ziehst du links, von links.[/p][p]Hörst du ganz auf, kommt das Paddel hoch. Das Boot läuft in seiner eigenen Fahrt weiter, bis du das Blatt wieder eintauchst.[/p][h2]Features[/h2][list][*][p][b]Ein Kajak mit echtem Schwung.[/b][/p][/*][*][p][b]Offenes Wasser ohne Grenzen.[/b] Keine Route, keine Wegpunkte, keine falsche Richtung. Fahr los und schau, wo du herauskommst.[/p][/*][*][p][b]Eine Kamera im Spiel, in Echtzeit.[/b] 28-70 mm, unscharfer Hintergrund beim Zoomen, ein Auslöser, der klickt. Funktioniert über und unter Wasser.[/p][/*][*][p][b]Fotos auf deiner Festplatte.[/b] Eine Galerie, die nach dem Beenden erhalten bleibt, und echte Bilddateien.[/p][/*][*][p][b]Tauch, wo und wann du willst.[/b] Lass das Kajak zurück und geh in warmes, klares Wasser, ohne Sauerstoffanzeige und ohne Zeitlimit.[/p][/*][*][p][b]Wracks, die niemand markiert hat.[/b] Ein gesunkenes Segelschiff, ein abgestürztes Flugzeug und die seltenen Fische, die dort leben. Nichts davon steht auf einer Karte.[/p][/*][*][p][b]Wasserklang für jeden Schlag.[/b] Jeder Schlag klingt anders, von der Seite, an der du ziehst.[/p][/*][/list]
```

---

# Spanish (Spain) — `spanish`

**Short** (270)

```
Un simulador de kayak y fotografía para tomárselo con calma. Aguas abiertas, una embarcación sin prisa y ningún horario que cumplir. Rema mientras te apetezca, fotografía lo que te llame la atención, sumérgete a ver qué hay abajo. Nada te persigue, nada va contrarreloj.
```

**Full**

```
[p][b]Kayak Photography Sim[/b] es un juego de kayak en primera persona: navegas a donde quieras y fotografías lo que te encuentras por el camino, también bajo el agua.[/p][p]Te subes, te separas de la orilla, eliges un rumbo. El agua es tan clara que se ve el fondo: lo que hay bajo el casco forma parte del mundo tanto como lo que te rodea.[/p][h2]Nadie va a molestarte[/h2][p]Ni temporizadores, ni barra de resistencia, ni clasificaciones. Ningún ritmo que mantener.[/p][p]Sigue remando y disfruta del camino.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_paddle"][/img][/p][p] [/p][h2]La cámara en la mano[/h2][p]Levantas la cámara y todo se ralentiza. Haces zoom y el fondo se va de foco. Pulsas el disparador y oyes el clic.[/p][p]Cada foto se queda en la galería incluso después de cerrar el juego y acaba en tu disco como un archivo de imagen normal y corriente. Imprímela, publícala, mándasela a alguien. Los sitios por los que remas son lo bastante cinematográficos como para que dos o tres de esas fotos acaben de fondo de escritorio.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_photo2"][/img][/p][p] [/p][h2]Bajo la superficie[/h2][p]El agua no es un decorado. La mitad de lo que hay que ver está debajo, y nada queda fuera de tu alcance: sal del kayak en cuanto te apetezca. Ni pantalla de equipo, ni temporizador de inmersión, ni medidor de oxígeno.[/p][p]Un velero tumbado de costado. Un avión de pasajeros partido en dos sobre la arena. Nada los señala y nada te lleva hasta ellos: das con ellos porque miras hacia el fondo en el momento justo.[/p][p]Ahí abajo los peces van a lo suyo. Acércate lo justo para la foto sin dispersar el banco y sube de nuevo cuando te apetezca.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_diveandexploreunderwater"][/img][/p][p] [/p][h2]El sonido de la pala[/h2][p]Cada palada se procesa por separado. Si tiras a la derecha, el sonido llega por la derecha; si tiras a la izquierda, por la izquierda.[/p][p]Para del todo y la pala se levanta. El bote sigue avanzando por inercia hasta que vuelves a meterla en el agua.[/p][h2]Características[/h2][list][*][p][b]Un kayak que conserva el impulso.[/b][/p][/*][*][p][b]Aguas abiertas sin límites.[/b] Ni ruta, ni puntos de paso, ni dirección equivocada. Sal a remar y mira dónde acabas.[/p][/*][*][p][b]Una cámara integrada, en tiempo real.[/b] 28-70 mm, fondo desenfocado al hacer zoom, un disparador que suena. Funciona por encima y por debajo del agua.[/p][/*][*][p][b]Fotos guardadas en tu disco.[/b] Una galería que se conserva al cerrar el juego, y archivos de imagen de verdad.[/p][/*][*][p][b]Bucea donde quieras y cuando quieras.[/b] Deja el kayak y baja a un agua cálida y transparente sin medidor de oxígeno ni límite de tiempo.[/p][/*][*][p][b]Restos que nadie ha señalado.[/b] Un velero hundido, un avión caído y los peces raros que viven alrededor. Nada de eso aparece en un mapa.[/p][/*][*][p][b]Un sonido de agua por cada palada.[/b] Cada una suena distinta, desde el lado del que tiras.[/p][/*][/list]
```

---

# Dutch — `dutch`

**Short** (269)

```
Een rustige simulator over kajakken en fotograferen. Open water, een boot die de tijd neemt, en geen agenda om je aan te houden. Peddel zolang je zin hebt, fotografeer wat je opvalt, duik onder om te zien wat daar ligt. Niets zit je achterna, niets loopt tegen de klok.
```

**Full**

```
[p][b]Kayak Photography Sim[/b] is een kajakspel vanuit de eerste persoon: je vaart waarheen je wilt en fotografeert wat je onderweg tegenkomt, ook onder water.[/p][p]Instappen, afzetten van de kant, een richting kiezen. Het water is zo helder dat je de bodem ziet: wat onder de boot ligt hoort net zo goed bij de wereld als wat om je heen is.[/p][h2]Niemand komt je storen[/h2][p]Geen timers, geen uithoudingsbalk, geen ranglijsten. Geen tempo dat je moet bijhouden.[/p][p]Peddel gewoon door en geniet van de tocht.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_paddle"][/img][/p][p] [/p][h2]De camera in je hand[/h2][p]Je tilt de camera op en alles vertraagt. Je zoomt in en de achtergrond gaat uit focus. Je drukt af en hoort de sluiter klikken.[/p][p]Elke foto blijft in de galerij staan, ook nadat je het spel hebt afgesloten, en komt als een gewoon beeldbestand op je schijf terecht. Printen, posten, naar iemand sturen. De plekken waar je langs peddelt zijn filmisch genoeg dat een paar van je foto's als bureaubladachtergrond eindigen.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_photo2"][/img][/p][p] [/p][h2]Onder de oppervlakte[/h2][p]Het water is geen decor. De helft van alles wat er te zien valt ligt eronder, en niets is onbereikbaar: stap uit de kajak zodra je daar zin in hebt. Geen uitrustingsscherm, geen duiktimer, geen zuurstofmeter.[/p][p]Een zeilschip dat op zijn zij ligt. Een passagiersvliegtuig dat doormidden in het zand ligt. Niets markeert ze en niets wijst je de weg — je stuit erop omdat je op het juiste moment naar beneden kijkt.[/p][p]Daar beneden gaan de vissen hun eigen gang. Kom dicht genoeg voor de foto zonder de school uiteen te jagen, en drijf weer omhoog wanneer je wilt.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_diveandexploreunderwater"][/img][/p][p] [/p][h2]Het geluid van de peddel[/h2][p]Elke peddelslag wordt apart berekend. Trek je rechts, dan komt het geluid van rechts; trek je links, van links.[/p][p]Stop je helemaal, dan komt de peddel omhoog. De boot loopt op eigen vaart door tot je het blad weer in het water zet.[/p][h2]Kenmerken[/h2][list][*][p][b]Een kajak die zijn vaart houdt.[/b][/p][/*][*][p][b]Open water zonder grenzen.[/b] Geen route, geen waypoints, geen verkeerde richting. Vaar weg en zie waar je uitkomt.[/p][/*][*][p][b]Een camera in het spel, in realtime.[/b] 28-70 mm, onscherpe achtergrond bij inzoomen, een sluiter die klikt. Werkt boven en onder water.[/p][/*][*][p][b]Foto's op je eigen schijf.[/b] Een galerij die blijft bestaan na het afsluiten, en echte beeldbestanden.[/p][/*][*][p][b]Duik waar en wanneer je wilt.[/b] Laat de kajak achter en ga het warme, heldere water in, zonder zuurstofmeter of tijdslimiet.[/p][/*][*][p][b]Wrakken die niemand heeft gemarkeerd.[/b] Een gezonken zeilschip, een neergestort vliegtuig en de zeldzame vissen die eromheen leven. Niets ervan staat op een kaart.[/p][/*][*][p][b]Watergeluid bij elke slag.[/b] Elke slag klinkt anders, vanaf de kant waar je trekt.[/p][/*][/list]
```

---

# Japanese — `japanese`

**Short** (116)

```
カヤックと写真の、のんびりしたシミュレーターです。開けた水面と、ゆっくり進む舟。急ぐ理由はどこにもありません。止まりたくなるまで漕いで、目に留まったものを撮って、水に潜って底をのぞく。追われることも、時間を計られることもありません。
```

**Full**

```
[p][b]Kayak Photography Sim[/b]は、水の上を好きな方へ進みながら、道すがら出会ったものを撮っていく一人称視点のカヤックゲームです。水中の景色も撮れます。[/p][p]舟に乗り、岸を蹴り、進む向きを決める。水は底まで見通せるほど澄んでいて、足元に広がるものも、まわりの景色と同じくらいこの世界の一部です。[/p][h2]邪魔をするものは何もありません[/h2][p]タイマーもスタミナゲージもランキングもなし。合わせるべきペースもありません。[/p][p]ただ漕ぎ続けて、その道のりを味わってください。[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_paddle"][/img][/p][p] [/p][h2]手にはカメラ[/h2][p]カメラを構えれば、まわりの動きがゆるやかになります。ズームすれば背景がぼけ、シャッターを切れば、カシャッと音が返ってきます。[/p][p]撮った写真はゲームを終了したあともギャラリーに残り、ふつうの画像ファイルとしてPCに保存されます。印刷しても、投稿しても、誰かに送っても構いません。漕いでいく景色はどれも絵になるので、何枚かは壁紙フォルダに落ち着くはずです。[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_photo2"][/img][/p][p] [/p][h2]水面の下へ[/h2][p]水はただの背景ではありません。見どころの半分は水面の下にあって、どこにも手が届きます。その気になったら、いつでもカヤックを降りてください。装備画面も、潜水時間の制限も、酸素ゲージもありません。[/p][p]横倒しになった帆船。砂の上で二つに折れた旅客機。目印もなければ、案内もありません。ちょうどいいときに下を見ていたから行き当たる、それだけです。[/p][p]水の底では、魚たちがこちらに構わず暮らしています。群れを散らさない距離まで近づいて一枚撮り、気が済んだら浮かび上がってください。[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_diveandexploreunderwater"][/img][/p][p] [/p][h2]パドルの音[/h2][p]ひと漕ぎごとに別々に処理されます。右で漕げば音は右から、左で漕げば左から返ってきます。[/p][p]漕ぐのをやめれば、パドルは水から上がります。次にひと掻きするまで、舟は惰性のまま進み続けます。[/p][h2]主な特徴[/h2][list][*][p][b]しっかり慣性の効くカヤック。[/b][/p][/*][*][p][b]果てのない開けた水面。[/b]決まった道も、ウェイポイントも、間違った方角もありません。漕ぎ出して、行き着いた先を眺めてください。[/p][/*][*][p][b]ゲーム内のリアルタイムカメラ。[/b]28〜70mm、ズームに応じた背景のボケ、音の返るシャッター。水上でも水中でも使えます。[/p][/*][*][p][b]手元に残る写真。[/b]終了後も消えないギャラリーと、PCに書き出される本物の画像ファイル。[/p][/*][*][p][b]どこでも、いつでも潜れます。[/b]カヤックを離れて、暖かく澄んだ水の中へ。酸素ゲージも制限時間もありません。[/p][/*][*][p][b]誰も印をつけていない残骸。[/b]沈んだ帆船、墜ちた飛行機、その周りに棲む珍しい魚。どれも地図には出てきません。[/p][/*][*][p][b]ひと漕ぎごとの水音。[/b]一回ごとに響きが違い、力を入れた側から返ってきます。[/p][/*][/list]
```

---

# Korean — `koreana`

**Short** (138)

```
카약과 사진의 느긋한 시뮬레이터. 탁 트인 물, 천천히 나아가는 배, 그리고 서둘러야 할 이유는 어디에도 없어요. 멈추고 싶어질 때까지 젓고, 눈에 들어오는 걸 찍고, 물속으로 내려가 아래를 들여다보세요. 쫓아오는 것도, 시간을 재는 것도 없어요.
```

**Full**

```
[p][b]Kayak Photography Sim[/b]은 물 위를 원하는 방향으로 나아가며 가는 길에 마주친 것들을 찍는 1인칭 카약 게임이에요. 물속 풍경도 담을 수 있어요.[/p][p]배에 올라 기슭에서 밀어내고, 방향을 정하세요. 물이 바닥까지 들여다보일 만큼 맑아서, 발밑에 펼쳐진 것도 주변 풍경만큼이나 이 세계의 일부예요.[/p][h2]방해하는 것은 아무것도 없어요[/h2][p]타이머도, 스태미나 게이지도, 순위표도 없어요. 맞춰야 할 속도도 없고요.[/p][p]그냥 계속 저으면서 그 길을 즐기면 돼요.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_paddle"][/img][/p][p] [/p][h2]손에는 카메라[/h2][p]카메라를 들면 주변이 천천히 흘러가요. 줌을 당기면 배경이 흐려지고, 셔터를 누르면 찰칵 소리가 돌아와요.[/p][p]찍은 사진은 게임을 끄고 나서도 갤러리에 남고, 평범한 이미지 파일로 PC에 저장돼요. 인쇄하든 올리든 누군가에게 보내든 마음대로예요. 지나온 풍경이 워낙 그림 같아서, 그중 몇 장은 배경화면 폴더에 자리 잡게 될 거예요.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_photo2"][/img][/p][p] [/p][h2]수면 아래로[/h2][p]물은 배경이 아니에요. 볼거리의 절반은 수면 아래에 있고, 닿지 못할 곳은 없어요. 내키면 언제든 카약에서 내려가면 돼요. 장비 화면도, 잠수 시간 제한도, 산소 게이지도 없어요.[/p][p]옆으로 누운 범선. 모래 위에서 두 동강 난 여객기. 표시된 것도 없고 안내해 주는 것도 없어요. 알맞은 순간에 아래를 보고 있었기 때문에 마주치게 되는 거예요.[/p][p]물 아래에서 물고기들은 제 할 일을 해요. 무리를 흩뜨리지 않을 만큼만 다가가 한 장 찍고, 마음이 내키면 다시 떠오르세요.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_diveandexploreunderwater"][/img][/p][p] [/p][h2]패들 소리[/h2][p]한 번 젓는 동작마다 따로 처리돼요. 오른쪽으로 저으면 소리가 오른쪽에서, 왼쪽으로 저으면 왼쪽에서 들려요.[/p][p]젓기를 멈추면 패들이 물 위로 올라와요. 다시 물에 담글 때까지 배는 관성으로 계속 나아가요.[/p][h2]주요 특징[/h2][list][*][p][b]진짜 관성이 있는 카약.[/b][/p][/*][*][p][b]끝이 없는 탁 트인 물.[/b] 정해진 경로도, 웨이포인트도, 틀린 방향도 없어요. 저어 나가서 어디에 닿는지 보세요.[/p][/*][*][p][b]게임 안의 실시간 카메라.[/b] 28~70mm, 줌에 따라 흐려지는 배경, 소리가 돌아오는 셔터. 물 위에서도 아래에서도 써요.[/p][/*][*][p][b]내 컴퓨터에 남는 사진.[/b] 게임을 꺼도 사라지지 않는 갤러리와 진짜 이미지 파일.[/p][/*][*][p][b]어디서든 언제든 잠수.[/b] 카약을 두고 따뜻하고 맑은 물속으로. 산소 게이지도 제한 시간도 없어요.[/p][/*][*][p][b]아무도 표시해 두지 않은 잔해.[/b] 가라앉은 범선, 떨어진 비행기, 그 주변에 사는 희귀한 물고기. 지도에는 하나도 나오지 않아요.[/p][/*][*][p][b]한 번 저을 때마다 달라지는 물소리.[/b] 매번 다르게 들리고, 힘을 준 쪽에서 나요.[/p][/*][/list]
```

---

# Polish — `polish`

**Short** (232)

```
Spokojny symulator kajaka i fotografii. Otwarta woda, niespieszna łódka i żadnych terminów. Wiosłuj, dopóki masz ochotę, fotografuj to, co wpadnie ci w oko, zanurkuj i zobacz, co jest na dole. Nic cię nie goni, nic nie mierzy czasu.
```

**Full**

```
[p][b]Kayak Photography Sim[/b] to kajakowa gra z perspektywy pierwszej osoby: płyniesz, gdzie chcesz, i fotografujesz to, co spotkasz po drodze — również pod wodą.[/p][p]Wsiadasz, odbijasz od brzegu, wybierasz kierunek. Woda jest tak przejrzysta, że widać dno: to, co pod kadłubem, należy do świata tak samo jak to, co dookoła.[/p][h2]Nikt ci nie przeszkodzi[/h2][p]Żadnych timerów, żadnego paska wytrzymałości, żadnych rankingów. Żadnego tempa, które trzeba utrzymać.[/p][p]Po prostu wiosłuj dalej i ciesz się drogą.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_paddle"][/img][/p][p] [/p][h2]Aparat w dłoni[/h2][p]Podnosisz aparat i wszystko zwalnia. Przybliżasz i tło rozmywa się. Naciskasz spust i słyszysz migawkę.[/p][p]Każde zdjęcie zostaje w galerii nawet po wyłączeniu gry i trafia na dysk jako zwykły plik graficzny. Wydrukuj, wrzuć w sieć, wyślij komuś. Miejsca, przez które płyniesz, są na tyle filmowe, że dwa czy trzy z tych zdjęć wylądują w folderze z tapetami.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_photo2"][/img][/p][p] [/p][h2]Pod powierzchnię[/h2][p]Woda nie jest tłem. Połowa tego, co jest do zobaczenia, leży pod spodem i nic nie jest poza zasięgiem: wyjdź z kajaka, kiedy tylko przyjdzie ci ochota. Żadnego ekranu ekwipunku, żadnego licznika nurkowania, żadnego wskaźnika tlenu.[/p][p]Żaglowiec leżący na boku. Samolot pasażerski przełamany na pół na piasku. Nic ich nie oznacza i nic do nich nie prowadzi — trafiasz na nie, bo patrzysz w dół w odpowiednim momencie.[/p][p]Na dole ryby zajmują się swoimi sprawami. Podpłyń na tyle blisko, żeby zrobić zdjęcie i nie rozproszyć ławicy, a potem wypłyń, kiedy przyjdzie ci ochota.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_diveandexploreunderwater"][/img][/p][p] [/p][h2]Dźwięk wiosła[/h2][p]Każde pociągnięcie wiosłem jest liczone osobno. Ciągniesz z prawej — dźwięk idzie z prawej; z lewej — z lewej.[/p][p]Przestaniesz całkiem — wiosło idzie w górę. Łódka płynie dalej rozpędem, dopóki znowu nie zanurzysz pióra.[/p][h2]Najważniejsze cechy[/h2][list][*][p][b]Kajak z prawdziwym rozpędem.[/b][/p][/*][*][p][b]Otwarta woda bez granic.[/b] Żadnej trasy, żadnych punktów nawigacyjnych, żadnego złego kierunku. Wypłyń i zobacz, gdzie wylądujesz.[/p][/*][*][p][b]Aparat w grze, w czasie rzeczywistym.[/b] 28-70 mm, tło rozmywane przy zbliżeniu, migawka, którą słychać. Działa nad wodą i pod wodą.[/p][/*][*][p][b]Zdjęcia na twoim dysku.[/b] Galeria, która zostaje po wyłączeniu gry, i prawdziwe pliki graficzne.[/p][/*][*][p][b]Nurkuj gdzie chcesz i kiedy chcesz.[/b] Zostaw kajak i wejdź do ciepłej, przejrzystej wody, bez wskaźnika tlenu i bez limitu czasu.[/p][/*][*][p][b]Wraki, których nikt nie oznaczył.[/b] Zatopiony żaglowiec, rozbity samolot i rzadkie ryby, które żyją wokół. Nic z tego nie jest na mapie.[/p][/*][*][p][b]Dźwięk wody przy każdym pociągnięciu.[/b] Każde brzmi inaczej, od strony, po której ciągniesz.[/p][/*][/list]
```

---

# Portuguese (Brazil) — `brazilian`

**Short** (257)

```
Um simulador tranquilo de caiaque e fotografia. Águas abertas, um barco sem pressa e nenhum horário para cumprir. Reme enquanto tiver vontade, fotografe o que chamar sua atenção, mergulhe para ver o que tem lá embaixo. Nada te persegue, nada é cronometrado.
```

**Full**

```
[p][b]Kayak Photography Sim[/b] é um jogo de caiaque em primeira pessoa: você navega para onde quiser e fotografa o que encontra pelo caminho, inclusive debaixo d'água.[/p][p]Você entra, se afasta da margem, escolhe uma direção. A água é tão limpa que dá para ver o fundo: o que está embaixo do casco faz parte do mundo tanto quanto o que está em volta.[/p][h2]Ninguém vai te incomodar[/h2][p]Sem cronômetros, sem barra de estamina, sem placares. Nenhum ritmo para acompanhar.[/p][p]É só continuar remando e aproveitar o caminho.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_paddle"][/img][/p][p] [/p][h2]A câmera na mão[/h2][p]Você levanta a câmera e tudo desacelera. Dá zoom e o fundo sai de foco. Aperta o disparador e ouve o clique do obturador.[/p][p]Cada foto continua na galeria mesmo depois de fechar o jogo e vai parar no seu disco como um arquivo de imagem comum. Imprima, poste, mande para alguém. Os lugares por onde você rema são cinematográficos o bastante para que duas ou três dessas fotos acabem virando papel de parede.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_photo2"][/img][/p][p] [/p][h2]Embaixo da superfície[/h2][p]A água não é cenário. Metade do que há para ver está lá embaixo, e nada fica fora do seu alcance: saia do caiaque assim que der vontade. Sem tela de equipamento, sem cronômetro de mergulho, sem medidor de oxigênio.[/p][p]Um veleiro deitado de lado. Um avião de passageiros partido ao meio na areia. Nada os marca e nada te leva até eles — você esbarra neles porque olhou para o fundo na hora certa.[/p][p]Lá embaixo os peixes seguem a vida deles. Chegue perto o bastante para o clique sem espalhar o cardume e volte à superfície quando der vontade.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_diveandexploreunderwater"][/img][/p][p] [/p][h2]O som do remo[/h2][p]Cada remada é processada separadamente. Se você puxa pela direita, o som vem da direita; pela esquerda, vem da esquerda.[/p][p]Pare de vez e o remo sobe. O barco segue por inércia até você colocar a pá na água de novo.[/p][h2]Características[/h2][list][*][p][b]Um caiaque que mantém o impulso.[/b][/p][/*][*][p][b]Águas abertas sem limites.[/b] Sem rota, sem waypoints, sem direção errada. Reme e veja onde você vai parar.[/p][/*][*][p][b]Uma câmera no jogo, em tempo real.[/b] 28-70 mm, fundo fora de foco no zoom, um obturador que soa. Funciona acima e abaixo da água.[/p][/*][*][p][b]Fotos no seu disco.[/b] Uma galeria que continua depois de fechar o jogo, e arquivos de imagem de verdade.[/p][/*][*][p][b]Mergulhe onde e quando quiser.[/b] Deixe o caiaque e desça para uma água quente e transparente sem medidor de oxigênio nem limite de tempo.[/p][/*][*][p][b]Destroços que ninguém sinalizou.[/b] Um veleiro afundado, um avião caído e os peixes raros que vivem em volta. Nada disso aparece em um mapa.[/p][/*][*][p][b]Um som de água para cada remada.[/b] Cada uma soa diferente, do lado em que você puxa.[/p][/*][/list]
```

---

# Russian — `russian`

Written by a native speaker (a friend of Hasan's), not translated. Uses formal **вы**, unlike the informal address in the other European languages — that is a normal register choice for a Russian store page and does not need to match the rest.

**Short** (266)

```
Медитативное путешествие на каяке с фотографией и исследованием мира. Впереди — бескрайняя гладь воды, за спиной — суета. Никаких маршрутов, заданий и дедлайнов. Гребите туда, куда ведёт любопытство, фотографируйте что понравится, ныряйте и смотрите, что там на дне.
```

**Full**

```
[p][b]Kayak Photography Sim[/b] — медитативное путешествие на каяке с исследованием мира и фотографией.[/p][p]Впереди — бескрайняя гладь воды. За спиной — суета. Здесь нет маршрутов, заданий и дедлайнов. Просто садитесь в каяк, выберите направление и отправляйтесь туда, куда вас приведёт любопытство.[/p][p]Фотографируйте живописные пейзажи, исследуйте прозрачные глубины и наслаждайтесь путешествием в собственном ритме. Никто не будет вас торопить.[/p][h2]Полная свобода[/h2][p]Никаких таймеров. Никакой выносливости. Никаких очков, заданий или обязательных целей.[/p][p]Только вы, каяк и открытая вода. Гребите столько, сколько захотите, остановитесь, когда почувствуете, что пора, и наслаждайтесь моментом.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_paddle"][/img][/p][p] [/p][h2]Запечатлейте путешествие[/h2][p]Поднимите камеру — и мир словно замедлится.[/p][p]Используйте зум, ловите идеальный кадр и наслаждайтесь приятным щелчком затвора. Каждый снимок автоматически сохраняется в игровой галерее и одновременно записывается на ваш компьютер как обычный файл изображения.[/p][p]Поделитесь лучшими фотографиями с друзьями или украсьте ими рабочий стол — окружающий мир создан для красивых кадров.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_photo2"][/img][/p][p] [/p][h2]Исследуйте мир под водой[/h2][p]Самое интересное скрывается под поверхностью.[/p][p]В любой момент можно покинуть каяк и отправиться исследовать тёплую прозрачную воду. Без ограничений по времени. Без запаса кислорода. Без специального снаряжения.[/p][p]На дне вас ждут забытые истории: затонувший парусник, обломки пассажирского самолёта, косяки рыб и другие тайны, которые никто не отметил на карте.[/p][p]Их можно найти только одним способом — внимательно смотреть вокруг.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_diveandexploreunderwater"][/img][/p][p] [/p][h2]Почувствуйте каждое движение[/h2][p]Каждый гребок сопровождается объёмным звуком.[/p][p]Гребёте справа — всплеск слышен справа. Гребёте слева — звук приходит слева. Перестаньте грести, и каяк продолжит плавно скользить по воде благодаря естественной инерции.[/p][p]Простые детали складываются в по-настоящему расслабляющее путешествие.[/p][h2]Особенности игры[/h2][list][*][p]Медитативный симулятор каякинга от первого лица.[/p][/*][*][p]Большой открытый водный мир без маршрутов и ограничений.[/p][/*][*][p]Реалистичная физика движения каяка и естественная инерция.[/p][/*][*][p]Полноценная игровая камера с фокусным расстоянием 28–70 мм и эффектом глубины резкости.[/p][/*][*][p]Возможность фотографировать как над водой, так и под водой.[/p][/*][*][p]Все фотографии сохраняются на вашем компьютере как обычные изображения.[/p][/*][*][p]Свободные погружения без таймеров, шкалы кислорода и ограничений.[/p][/*][*][p]Затонувшие объекты и редкие обитатели подводного мира, которые предстоит найти самостоятельно.[/p][/*][*][p]Пространственный звук каждого гребка для полного погружения в атмосферу.[/p][/*][/list][p]Иногда лучшее приключение — это просто выбрать направление и позволить воде вести вас дальше.[/p]
```

---

# Simplified Chinese — `schinese`

**Short** (86)

```
一款慢下来的皮划艇与摄影模拟游戏。开阔的水面，一条不赶路的船，没有非去不可的地方。想划多久就划多久，看到什么就拍什么，潜进水里看看底下有什么。没有东西追你，也没有东西计时。
```

**Full**

```
[p][b]Kayak Photography Sim[/b] 是一款第一人称皮划艇游戏：想往哪儿划就往哪儿划，把一路上遇到的东西拍下来，水底下的也一样。[/p][p]上船，蹬开岸边，挑个方向。水清得能一眼看到底，船下的世界和身边的景色一样，都是这片天地的一部分。[/p][h2]没有什么会来打扰你[/h2][p]没有计时，没有体力条，没有排行榜。也没有需要跟上的节奏。[/p][p]只管一直划，享受这一路。[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_paddle"][/img][/p][p] [/p][h2]手里握着相机[/h2][p]举起相机，周围就慢了下来。推近镜头，背景开始虚化。按下快门，能听见咔嚓一声。[/p][p]拍下的照片会一直留在相册里，关掉游戏也还在，还会以普通图片文件的形式存进你的硬盘。想打印、想发帖、想发给朋友，都随你。你划过的地方够有电影感，其中几张多半会进你的壁纸文件夹。[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_photo2"][/img][/p][p] [/p][h2]潜到水面以下[/h2][p]水不只是背景。能看的东西有一半在水面之下，而且没有一处够不着——什么时候想离开皮划艇都行。没有装备界面，没有潜水计时，也没有氧气条。[/p][p]一艘侧翻的帆船。一架断成两截、卧在沙上的客机。没有标记，也没有指引——你能撞见它们，只是因为在对的时候低头看了一眼。[/p][p]水底下的鱼自顾自地过日子。靠近到能拍得到、又不惊散鱼群的距离，拍完再慢慢浮上去。[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_diveandexploreunderwater"][/img][/p][p] [/p][h2]划桨的声音[/h2][p]每一桨都单独处理。右边划，声音就从右边来；左边划，就从左边来。[/p][p]完全停下，桨就抬起来。船靠着惯性继续往前滑，直到你把桨重新放进水里。[/p][h2]主要特色[/h2][list][*][p][b]有真实惯性的皮划艇。[/b][/p][/*][*][p][b]一望无际的开阔水面。[/b]没有路线，没有路径点，也没有走错的方向。划出去，看看会到哪儿。[/p][/*][*][p][b]游戏里的实时相机。[/b]28-70mm，随变焦而来的背景虚化，会响的快门。水上水下都能用。[/p][/*][*][p][b]存在自己硬盘上的照片。[/b]关掉游戏也还在的相册，还有实实在在的图片文件。[/p][/*][*][p][b]想在哪潜就在哪潜，什么时候都行。[/b]离开皮划艇，进到温暖清澈的水里，没有氧气条，也没有时间限制。[/p][/*][*][p][b]没人标注过的残骸。[/b]一艘沉没的帆船、一架坠落的飞机，还有在它们周围生活的稀有鱼类。地图上一个都找不到。[/p][/*][*][p][b]每一桨都有自己的水声。[/b]每一下听起来都不一样，从你发力的那一侧传来。[/p][/*][/list]
```

---

# Thai — `thai`

**Short** (207)

```
เกมจำลองการพายคายัคและถ่ายภาพแบบเนิบช้า ผืนน้ำกว้าง เรือที่ไปช้า ๆ และไม่มีอะไรที่ต้องไปให้ทัน พายไปเรื่อย ๆ จนกว่าจะอยากหยุด ถ่ายสิ่งที่สะดุดตา แล้วดำลงไปดูว่าข้างล่างมีอะไร ไม่มีอะไรไล่ตาม ไม่มีอะไรจับเวลา
```

**Full**

```
[p][b]Kayak Photography Sim[/b] คือเกมพายคายัคมุมมองบุคคลที่หนึ่ง พายไปทางไหนก็ได้บนผืนน้ำ แล้วถ่ายภาพสิ่งที่พบระหว่างทาง รวมถึงสิ่งที่อยู่ใต้น้ำ[/p][p]ลงเรือ ถีบออกจากฝั่ง เลือกทิศทาง น้ำใสจนมองเห็นพื้นข้างล่าง สิ่งที่อยู่ใต้ท้องเรือก็เป็นส่วนหนึ่งของโลกใบนี้ไม่ต่างจากสิ่งที่อยู่รอบตัว[/p][h2]ไม่มีอะไรมารบกวน[/h2][p]ไม่มีการจับเวลา ไม่มีหลอดพลัง ไม่มีตารางอันดับ ไม่มีจังหวะที่ต้องไล่ให้ทัน[/p][p]พายต่อไปเรื่อย ๆ แล้วเพลิดเพลินกับเส้นทาง[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_paddle"][/img][/p][p] [/p][h2]กล้องอยู่ในมือ[/h2][p]ยกกล้องขึ้น ทุกอย่างรอบตัวก็ช้าลง ซูมเข้าไป ฉากหลังก็เบลอ กดชัตเตอร์ แล้วได้ยินเสียงคลิกกลับมา[/p][p]ภาพที่ถ่ายจะอยู่ในแกลเลอรีต่อไปแม้ปิดเกมแล้ว และถูกบันทึกลงเครื่องเป็นไฟล์ภาพธรรมดา จะพิมพ์ จะโพสต์ จะส่งให้ใครก็ได้ สถานที่ที่พายผ่านสวยพอที่ภาพสองสามใบจะไปอยู่ในโฟลเดอร์วอลเปเปอร์[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_photo2"][/img][/p][p] [/p][h2]ลงไปใต้ผิวน้ำ[/h2][p]น้ำไม่ใช่แค่ฉากหลัง ครึ่งหนึ่งของสิ่งที่มีให้ดูอยู่ข้างล่าง และไม่มีตรงไหนที่ไปไม่ถึง อยากออกจากคายัคเมื่อไหร่ก็ได้ ไม่มีหน้าจออุปกรณ์ ไม่มีการจับเวลาดำน้ำ ไม่มีหลอดออกซิเจน[/p][p]เรือใบลำหนึ่งนอนตะแคง เครื่องบินโดยสารหักเป็นสองท่อนอยู่บนพื้นทราย ไม่มีเครื่องหมาย ไม่มีอะไรชี้ทาง เจอเพราะก้มมองลงไปในจังหวะที่พอดีเท่านั้น[/p][p]ข้างล่างนั้น ฝูงปลาใช้ชีวิตของมันไปตามปกติ เข้าใกล้พอที่จะถ่ายได้โดยไม่ทำให้ฝูงแตก แล้วค่อยลอยขึ้นมาเมื่ออยากขึ้น[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_diveandexploreunderwater"][/img][/p][p] [/p][h2]เสียงของใบพาย[/h2][p]แต่ละจังหวะพายประมวลผลแยกกัน พายทางขวา เสียงมาจากขวา พายทางซ้าย เสียงมาจากซ้าย[/p][p]หยุดพายไปเลย ใบพายก็ยกขึ้น เรือยังไหลต่อด้วยแรงส่งของมันเอง จนกว่าจะจุ่มใบพายลงไปอีกครั้ง[/p][h2]คุณสมบัติเด่น[/h2][list][*][p][b]คายัคที่มีแรงส่งจริง[/b][/p][/*][*][p][b]ผืนน้ำกว้างไร้ขอบเขต[/b] ไม่มีเส้นทาง ไม่มีเวย์พอยต์ ไม่มีทิศที่ผิด พายออกไปแล้วดูว่าจะไปจบที่ไหน[/p][/*][*][p][b]กล้องในเกมแบบเรียลไทม์[/b] 28-70 มม. ฉากหลังเบลอตามการซูม ชัตเตอร์ที่มีเสียง ใช้ได้ทั้งเหนือน้ำและใต้น้ำ[/p][/*][*][p][b]ภาพถ่ายเก็บไว้ในเครื่องของคุณเอง[/b] แกลเลอรีที่ยังอยู่หลังปิดเกม และไฟล์ภาพจริง ๆ[/p][/*][*][p][b]ดำน้ำที่ไหนเมื่อไหร่ก็ได้[/b] ทิ้งคายัคไว้แล้วลงไปในน้ำอุ่นใส ไม่มีหลอดออกซิเจน ไม่มีการจำกัดเวลา[/p][/*][*][p][b]ซากที่ไม่มีใครทำเครื่องหมายไว้[/b] เรือใบที่จม เครื่องบินที่ตก และปลาหายากที่อาศัยอยู่รอบ ๆ ไม่มีอะไรอยู่บนแผนที่[/p][/*][*][p][b]เสียงน้ำในทุกจังหวะพาย[/b] แต่ละครั้งฟังไม่เหมือนกัน มาจากฝั่งที่ออกแรง[/p][/*][/list]
```

The spaces inside the Thai text are intentional — Thai does not separate words with spaces, so they act as clause breaks.

---

# Traditional Chinese — `tchinese`

**Short** (88)

```
一款讓人慢下來的獨木舟與攝影模擬遊戲。開闊的水面、一艘不趕路的船，沒有非去不可的地方。想划多久就划多久，看到什麼就拍什麼，潛進水裡看看底下有什麼。沒有東西追你，也沒有東西計時。
```

**Full**

```
[p][b]Kayak Photography Sim[/b] 是一款第一人稱獨木舟遊戲：想往哪划就往哪划，把一路上遇到的東西拍下來，水底下的也一樣。[/p][p]上船，蹬開岸邊，挑個方向。水清得能一眼看到底，船下的世界和身邊的景色一樣，都是這片天地的一部分。[/p][h2]沒有什麼會來打擾你[/h2][p]沒有計時，沒有體力槽，沒有排行榜。也沒有需要跟上的節奏。[/p][p]只管一直划，享受這一路。[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_paddle"][/img][/p][p] [/p][h2]手裡握著相機[/h2][p]舉起相機，周圍就慢了下來。推近鏡頭，背景開始虛化。按下快門，能聽見喀嚓一聲。[/p][p]拍下的照片會一直留在相簿裡，關掉遊戲也還在，還會以普通圖片檔的形式存進你的硬碟。想列印、想發文、想傳給朋友，都隨你。你划過的地方夠有電影感，其中幾張多半會進你的桌布資料夾。[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_photo2"][/img][/p][p] [/p][h2]潛到水面以下[/h2][p]水不只是背景。能看的東西有一半在水面之下，而且沒有一處到不了——什麼時候想離開獨木舟都行。沒有裝備介面，沒有潛水計時，也沒有氧氣條。[/p][p]一艘側翻的帆船。一架斷成兩截、臥在沙上的客機。沒有標記，也沒有指引——你能撞見它們，只是因為在對的時候低頭看了一眼。[/p][p]水底下的魚自顧自地過日子。靠近到能拍得到、又不驚散魚群的距離，拍完再慢慢浮上去。[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_diveandexploreunderwater"][/img][/p][p] [/p][h2]划槳的聲音[/h2][p]每一槳都單獨處理。右邊划，聲音就從右邊來；左邊划，就從左邊來。[/p][p]完全停下，槳就抬起來。船靠著慣性繼續往前滑，直到你把槳重新放進水裡。[/p][h2]主要特色[/h2][list][*][p][b]有真實慣性的獨木舟。[/b][/p][/*][*][p][b]一望無際的開闊水面。[/b]沒有路線，沒有導航點，也沒有走錯的方向。划出去，看看會到哪。[/p][/*][*][p][b]遊戲裡的即時相機。[/b]28-70mm，隨變焦而來的背景虛化，會響的快門。水上水下都能用。[/p][/*][*][p][b]存在自己硬碟上的照片。[/b]關掉遊戲也還在的相簿，還有實實在在的圖片檔。[/p][/*][*][p][b]想在哪潛就在哪潛，什麼時候都行。[/b]離開獨木舟，進到溫暖清澈的水裡，沒有氧氣條，也沒有時間限制。[/p][/*][*][p][b]沒人標註過的殘骸。[/b]一艘沉沒的帆船、一架墜落的飛機，還有在它們周圍生活的稀有魚類。地圖上一個都找不到。[/p][/*][*][p][b]每一槳都有自己的水聲。[/b]每一下聽起來都不一樣，從你出力的那一側傳來。[/p][/*][/list]
```

---

# Turkish — `turkish`

**Short** (264)

```
Dingin bir kano ve fotoğraf simülasyonu. Açık su, ağır ağır ilerleyen bir tekne ve gitmen gereken hiçbir yer yok. Canın istediği kadar kürek çek, gözüne çarpanı fotoğrafla, suyun altına dalıp aşağısını keşfet. Kovalayan yok, süre tutan yok. Sadece takıl ve keşfet.
```

**Full**

```
[p][b]Kayak Photography Sim[/b], suda canının çektiği yere gittiğin ve orada bulduğun her şeyi fotoğrafladığın birinci şahıs bir kano oyunu — su altı kareleri dahil.[/p][p]Kanoya bin, kıyıdan uzaklaş, bir yön seç. Su, dibi görebileceğin kadar berrak; altında kalanlar da en az etrafındakiler kadar bu dünyanın parçası.[/p][h2]Kimse seni rahatsız etmeyecek[/h2][p]Süre yok. Stamina barı yok. Skor tablosu yok. Yetişilecek bir tempo yok.[/p][p]Kürek çekmeye devam et, yolculuğun tadını çıkar.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_paddle"][/img][/p][p] [/p][h2]Elinde kamera[/h2][p]Kamerayı kaldır, her şey yavaşlar. Yakınlaştır, arka plan yumuşar. Deklanşöre bas ve o tık sesini duy.[/p][p]Çektiğin her kare galeride kalır, oyunu kapatsan bile; ayrıca bilgisayarına gerçek bir dosya olarak kaydedilir. Yazdır, paylaş, bir arkadaşına gönder. Kürek çektiğin yerler öyle sinematik ki birkaç kare duvar kâğıdı klasörüne girecek.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_photo2"][/img][/p][p] [/p][h2]Suya dal[/h2][p]Su sadece dekor değil. Görülecek şeylerin yarısı yüzeyin altında ve hepsine ulaşabilirsin — istediğin an kanodan kayıp suya gir. Ekipman ekranı yok, dalış süresi yok, oksijen göstergesi yok.[/p][p]Yan yatmış bir yelkenli. Kuma saplanmış, ikiye ayrılmış bir yolcu uçağı. Hiçbiri işaretli değil, kimse seni oraya yönlendirmiyor — doğru anda aşağı baktığın için buluyorsun.[/p][p]Aşağıda balıklar sen yokmuşsun gibi kendi işlerine bakar. Onları ürkütmeden karene girecek kadar yaklaş, sonra canın ne zaman isterse yüzeye çık.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_diveandexploreunderwater"][/img][/p][p] [/p][h2]Kürek sesi[/h2][p]Her kürek çekişi ayrı ayrı işleniyor. Sağa çektiğinde ses sağdan, sola çektiğinde soldan geliyor.[/p][p]Çekmeyi tamamen bıraktığında kürek yukarı kalkar. Sen yeniden suya daldırana kadar tekne kendi hızıyla süzülmeye devam eder.[/p][h2]Özellikler[/h2][list][*][p][b]Gerçek bir süzülme hissi olan kano.[/b][/p][/*][*][p][b]Gezilecek açık su.[/b] Rota yok, işaret yok, yanlış yön yok. Kürek çek ve nereye varacağını gör.[/p][/*][*][p][b]Gerçek zamanlı oyun içi kamera.[/b] 28–70mm, yakınlaştırdıkça yumuşayan arka plan, tıklayan bir deklanşör. Su üstünde de altında da çalışır.[/p][/*][*][p][b]Yerel olarak kaydedilen fotoğraflar.[/b] Oyunu kapatsan da duran bir galeri, doğrudan bilgisayarına yazılan görüntü dosyaları.[/p][/*][*][p][b]İstediğin yerde, istediğin zaman dalış.[/b] Kanoyu bırak, ılık ve berrak suya gir; oksijen göstergesi yok, süre sınırı yok.[/p][/*][*][p][b]İşaretlenmemiş enkazlar.[/b] Batık bir yelkenli, düşmüş bir uçak ve çevrelerinde yaşayan nadir balıklar — hiçbiri haritada belirtilmiyor.[/p][/*][*][p][b]Her darbe için ayrı su sesi.[/b] Her kürek darbesi farklı duyulur, kullandığın taraftan gelir.[/p][/*][/list]
```

Unchanged from the corrected version you already reviewed. Note that "kayak" means *ski* in Turkish and the store name field is not localized, so both texts name the boat as a **kano** early.

---

# Ukrainian — `ukrainian`

Reviewed and largely rewritten by a native speaker. His notes were made against the first draft, so where he fixed something that had already been changed, his idiom was carried over to the current wording rather than reverting.

**Short** (299)

```
Медитативний симулятор плавання на каяку та фотографування. Відкрита вода, повільний човен і нікуди не потрібно поспішати. Греби, доки не захочеться зупинитися, фотографуй усе, що приверне твою увагу, пірнай під воду, щоб дослідити, що ж під нею є. Ніхто тебе не переслідує. Немає обмежень за часом.
```

**Full**

```
[p][b]Kayak Photography Sim[/b] — це гра про плавання на каяку від першої особи, у якій ти мандруєш по воді куди захочеш і фотографуєш те, що знаходиш, — зокрема й під водою.[/p][p]Сідай, відштовхуйся від берега, обирай напрямок. Вода достатньо прозора, щоб бачити дно: те, що під тобою, — така сама частина світу, як і те, що навколо.[/p][h2]Тебе ніхто не потурбує[/h2][p]Ні таймерів, ні шкали витривалості, ні таблиць рекордів. Жодного темпу, за яким треба встигати.[/p][p]Просто греби далі й тішся дорогою.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_paddle"][/img][/p][p] [/p][h2]Камера в руках[/h2][p]Підніми камеру — й усе сповільниться. Наближ — тло розмиється. А як натиснеш спуск — почуєш клацання затвора.[/p][p]Кожен знімок лишається в галереї навіть після виходу з гри й зберігається на комп'ютері справжнім файлом. Ти можеш роздрукувати, викласти в інтернет чи надіслати свої знімки друзям. Місця, повз які ти пливеш, достатньо кінематографічні, щоб кілька твоїх знімків осіли в теці зі шпалерами.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_photo2"][/img][/p][p] [/p][h2]Занурися[/h2][p]Вода — не просто гарний вид. Половина всього, що тут є, лежить під її поверхнею, і ти можеш туди дістатися — вислизнути з каяка коли завгодно. Без екрана зі спорядженням, без таймера занурення, без шкали кисню.[/p][p]Вітрильник, що лежить на боці. Пасажирський літак, переламаний навпіл на піску. Їх ніщо не позначає й ніщо до них не веде — ти натрапляєш на них просто тому, що вчасно дивишся вниз.[/p][p]Унизу риби живуть своїм життям. Підберися ближче для кадру, але так, щоб не розполохати зграю, — а потім спливай, коли захочеться.[/p][p][img src="{STEAM_APP_IMAGE}/extras/gif_diveandexploreunderwater"][/img][/p][p] [/p][h2]Звук весла[/h2][p]Кожен гребок обробляється окремо. Тягнеш праворуч — звук іде праворуч, ліворуч — ліворуч.[/p][p]Зовсім перестанеш гребти — весло підійметься. Човен далі ковзатиме за інерцією, доки ти знову не опустиш весло у воду.[/p][h2]Особливості[/h2][list][*][p][b]Каяк зі справжньою інерцією.[/b][/p][/*][*][p][b]Відкрита вода для вільного руху.[/b] Жодних маршрутів, контрольних точок чи неправильних напрямків. Відпливай і побачиш, куди дістанешся.[/p][/*][*][p][b]Ігрова камера, що працює в реальному часі.[/b] 28–70 мм, розмиття тла при наближенні, затвор, який клацає. Працює над водою і під водою.[/p][/*][*][p][b]Знімки зберігаються локально.[/b] Галерея, що лишається після виходу з гри, і файли зображень, які відразу ж зберігаються на комп'ютері.[/p][/*][*][p][b]Пірнай де завгодно й коли завгодно.[/b] Залиш каяк і йди в теплу прозору воду: без шкали кисню, без обмежень за часом.[/p][/*][*][p][b]Непозначені уламки, що варто знайти.[/b] Затонулий вітрильник, впалий літак і рідкісні риби, що живуть навколо, — нічого з цього не позначено на карті.[/p][/*][*][p][b]Звук води, який чути гребок за гребком.[/b] Кожен з них звучить по-своєму й іде з того боку, яким гребеш.[/p][/*][/list]
```
