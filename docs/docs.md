# RE_iO Script: documentation

> **Work in progress (v0.0.1).** Unreviewed draft; labels, codes and layout may change or be wrong. No licence has been chosen yet. See the README.

A systematic glyph script for the range of sounds the human voice can make, built from the RE_iO Script charts 16176 (chart i, all possible sounds; chart ii, sounds found in speech) and 16180 (the full chart with the attested sounds marked in blue). The charts credit **Luciano Canepari, *La Fonetica naturale*, con IPA** as the work they are based upon. This document explains what the grid means, how to type it, and what is and is not confirmed.

> ## Make sure the font is loaded
> **The glyphs in this document, and in the typing sheet, only display correctly when the `REiO-Script.ttf` font is installed or loaded.** The glyphs live in the Unicode Private Use Area (U+E000 to U+E8DB), which no other font draws. If the font is missing you will see empty boxes, question marks, or nothing at all where a glyph should be.
>
> - **Linux:** copy `REiO-Script.ttf` to `~/.local/share/fonts/`, run `fc-cache -f`, then restart the app.
> - **Windows:** right-click the TTF, then Install (or Install for all users).
> - **macOS:** double-click the TTF, then Install Font.
> - **In a web page:** load it with `@font-face { font-family: "REiO"; src: url("REiO-Script.ttf"); }` and set `font-family: "REiO"` on the text. `REiO-Script-typing-sheet.html` already has the font embedded, so it needs no install.
> - **In this Markdown file:** your viewer must be using a system with the font installed. If the glyph columns below look blank, install the font and reopen the file. GitHub and most online Markdown viewers cannot load the font, so view this file locally.
> - **Check it works:** the next line should show a ring glyph with arcs, not a box: &nbsp; 

> **Repository layout:** in this repo the files named below live in `font/`, `web/`, `data/`, `input/` and `docs/`. See the README for the map.

## 1. What is in the font

- **2,268 glyphs**, one for every cell of chart i: 63 columns by 36 rows. No blanks.
- Codepoints run **U+E000 to U+E8DB** in chart order, left to right then top to bottom. Glyph at row *r*, column *c* is U+E000 + (*r*-1) x 63 + (*c*-1).
- Each glyph sits in a square cell with a fixed advance (1000 units), so glyphs line up on an even grid when set side by side.
- It is a standalone script. It does not map to IPA letters, and it contains no Latin letters. The only non-script character is a space.
- The font was traced from the chart images (about 133 px per cell), so outlines are smooth but not hand-drawn. Very large sizes show the source resolution.

## 2. What the chart's grid means

The grid is a systematic table of articulations, decoded by comparing the chart with fig 10.1 (pp. 166-168) of Canepari's free book *Natural Phonetics & Tonetics* (see section 7). The counts match exactly.

### Columns: 63 places of articulation, in 13 families

Chart column groups run left to right, with the family number as Canepari numbers them (0 to 12). The sample glyph shown is the **voiced stop** (row 5) at that place, which shows how the place changes the glyph.

| Col group | Family | Sub-places | Column no. | Place code | Place name | Typing keys | Sample |
|---|---|---|---|---|---|---|---|
| 1 | Bilabial | 5 | 1 | 0.1 | Bilabial | `a1` |  |
|  |  |  | 2 | 0.2 | Bilabial rounded | `a2` |  |
|  |  |  | 3 | 0.3 | Palatalized bilabial | `a3` |  |
|  |  |  | 4 | 0.4 | Uvularized bilabial | `a4` |  |
|  |  |  | 5 | 0.5 | Labial-apical | `a5` |  |
| 2 | Labiodental | 5 | 6 | 1.1 | Labiodental | `b1` |  |
|  |  |  | 7 | 1.2 | Labiodental rounded | `b2` |  |
|  |  |  | 8 | 1.3 | Palatalized labiodental | `b3` |  |
|  |  |  | 9 | 1.4 | Uvularized labiodental | `b4` |  |
|  |  |  | 10 | 1.5 | Dental-bilabial | `b5` |  |
| 3 | Dental | 7 | 11 | 2.1 | Pre-dental | `c1` |  |
|  |  |  | 12 | 2.2 | Pro-dental | `c2` |  |
|  |  |  | 13 | 2.3 | Dental | `c3` |  |
|  |  |  | 14 | 2.4 | Dental rounded | `c4` |  |
|  |  |  | 15 | 2.5 | Labiodental dental | `c5` |  |
|  |  |  | 16 | 2.6 | Uvularized dental | `c6` |  |
|  |  |  | 17 | 2.7 | Denti-alveolar | `c7` |  |
| 4 | Alveolar | 6 | 18 | 3.1 | Alveolar | `d1` |  |
|  |  |  | 19 | 3.2 | Alveolar rounded | `d2` |  |
|  |  |  | 20 | 3.3 | Labiodental alveolar | `d3` |  |
|  |  |  | 21 | 3.4 | Alveo-prevelar | `d4` |  |
|  |  |  | 22 | 3.5 | Velarized alveolar | `d5` |  |
|  |  |  | 23 | 3.6 | Uvularized alveolar | `d6` |  |
| 5 | Postalveolar | 6 | 24 | 4.1 | [Apico-]postalveolar | `e1` |  |
|  |  |  | 25 | 4.2 | [Apico-]postalveolar rounded | `e2` |  |
|  |  |  | 26 | 4.3 | Velarized apico-postalveolar | `e3` |  |
|  |  |  | 27 | 4.4 | Velarized apico-postalveolar rounded | `e4` |  |
|  |  |  | 28 | 4.5 | Apico-palatal | `e5` |  |
|  |  |  | 29 | 4.6 | Apico-palatal rounded | `e6` |  |
| 6 | Postalveo-palatal | 5 | 30 | 5.1 | Postalveo-palatal | `f1` |  |
|  |  |  | 31 | 5.2 | Postalveo-palatal protruded | `f2` |  |
|  |  |  | 32 | 5.3 | Postalveo-palatal over-rounded | `f3` |  |
|  |  |  | 33 | 5.4 | Velarized postalveolar | `f4` |  |
|  |  |  | 34 | 5.5 | Velarized postalveolar protruded | `f5` |  |
| 7 | Prepalatal | 4 | 35 | 6.1 | Prepalatal | `g1` |  |
|  |  |  | 36 | 6.2 | Bilabialized prepalatal | `g2` |  |
|  |  |  | 37 | 6.3 | Prepalatal rounded | `g3` |  |
|  |  |  | 38 | 6.4 | Labiodentalized palatal | `g4` |  |
| 8 | Palatal | 5 | 39 | 7.1 | Palatal | `h1` |  |
|  |  |  | 40 | 7.2 | Palatal rounded | `h2` |  |
|  |  |  | 41 | 7.3 | Uvularized palatal | `h3` |  |
|  |  |  | 42 | 7.4 | Postpalatal | `h4` |  |
|  |  |  | 43 | 7.5 | Postpalatal rounded | `h5` |  |
| 9 | Prevelar | 5 | 44 | 8.1 | Prevelar | `i1` |  |
|  |  |  | 45 | 8.2 | Prevelar rounded | `i2` |  |
|  |  |  | 46 | 8.3 | Postalveolar prevelar rounded | `i3` |  |
|  |  |  | 47 | 8.4 | Provelar | `i4` |  |
|  |  |  | 48 | 8.5 | Provelar rounded | `i5` |  |
| 10 | Velar | 6 | 49 | 9.1 | Velar | `j1` |  |
|  |  |  | 50 | 9.2 | Velar rounded | `j2` |  |
|  |  |  | 51 | 9.3 | Velar-bilabial | `j3` |  |
|  |  |  | 52 | 9.4 | Labiodentalized velar | `j4` |  |
|  |  |  | 53 | 9.5 | Velar-dental/alveolar | `j5` |  |
|  |  |  | 54 | 9.6 | Uvulo-postalveolarized velar rounded | `j6` |  |
| 11 | Uvular | 4 | 55 | 10.1 | Uvular | `k1` |  |
|  |  |  | 56 | 10.2 | Uvular rounded | `k2` |  |
|  |  |  | 57 | 10.3 | Pharyngealized uvular | `k3` |  |
|  |  |  | 58 | 10.4 | Pharyngealized uvular rounded | `k4` |  |
| 12 | Pharyngeal | 3 | 59 | 11.1 | Prepharyngeal | `l1` |  |
|  |  |  | 60 | 11.2 | Pharyngeal | `l2` |  |
|  |  |  | 61 | 11.3 | Pharyngeal rounded | `l3` |  |
| 13 | Laryngeal | 2 | 62 | 12.1 | Laryngeal | `m1` |  |
|  |  |  | 63 | 12.2 | Laryngeal rounded | `m2` |  |

Place codes use Canepari's numbering: the whole number is the family (0 = bilabial ... 12 = laryngeal), the digit after the point is the position within it. Names such as "rounded", "uvularized" or "velarized" describe secondary articulation added to the main place.

### Rows: 18 manners, each as a voiced/voiceless pair, in 7 groups

Each manner takes two adjacent rows. The sample glyph is at the bilabial column (column 1) for the voiced row of each manner.

| Row group | Manner | Rows | Typing keys (rows) | Sample (voiced) |
|---|---|---|---|---|
| 1 | Semi-nasal | 1-2 | `11`, `12` |  |
|  | Nasal | 3-4 | `13`, `14` |  |
| 2 | Stop | 5-6 | `21`, `22` |  |
|  | Stop-strictive | 7-8 | `23`, `24` |  |
|  | Grooved stop-strictive | 9-10 | `25`, `26` |  |
| 3 | Constrictive | 11-12 | `31`, `32` |  |
| 4 | Grooved constrictive | 13-14 | `41`, `42` |  |
| 5 | Approximant | 15-16 | `51`, `52` |  |
|  | Lateralized approximant | 17-18 | `53`, `54` |  |
| 6 | Trill | 19-20 | `61`, `62` |  |
|  | Constrictive trill | 21-22 | `63`, `64` |  |
|  | Tap | 23-24 | `65`, `66` |  |
|  | Flap | 25-26 | `67`, `68` |  |
| 7 | Lateral approximant | 27-28 | `71`, `72` |  |
|  | Lateral constrictive | 29-30 | `73`, `74` |  |
|  | Unilateral | 31-32 | `75`, `76` |  |
|  | Semilateral | 33-34 | `77`, `78` |  |
|  | Lateral tap | 35-36 | `79`, `70` |  |

Row-group meanings in plain terms: group 1 is the nasals; group 2 the stops and stop-strictives (the "affricates" of ordinary IPA); groups 3 and 4 the constrictives ("fricatives"), plain and grooved; group 5 the approximants; group 6 the trills, taps and flaps; group 7 the lateral family.

**Voicing order is an assumption.** Within each pair, the first row is treated as **voiced** and the second as **voiceless**. This is inferred from which nasal rows are marked blue in chart 16180 (the voiced rows are marked, the voiceless rows are nearly empty). The charts do not say so explicitly, so confirm with whoever designed them.

### The other marks on the chart
- **Red marks along the top and left edges** are labels for each column and row, drawn in the script's own style. They are not glyphs and are not in the font.
- **Turquoise box and orange lines** show the grid outline and the group boundaries.
- **The small 5 by 6 grid at the top right** of each chart is a legend of the ring's building blocks. Its meaning has not been decoded here.
- **Blue glyphs in chart 16180** mark the sounds actually found in human speech: **566 of the 2,268**. Chart ii shows the same set on its own. The remaining 1,702 are the other possible combinations.

## 3. Typing

Every glyph has a four-key code that follows the chart's own groups:

1. **Column group letter**, a to m (the 13 families, left to right).
2. **Column in group**, 1 to 7.
3. **Row group**, 1 to 7 (top to bottom).
4. **Row in group**, 1 to 9, with **0** meaning the 10th row.

The first glyph (top left) is `a111`. The last (bottom right) is `m270`. The complete code list is in the `typing_code` column of `REiO-Script-glyphs.csv`.

| Platform | How | File |
|---|---|---|
| Any browser | Open the sheet. Click a glyph, or type the 4-key code in the box. Copy button included. | `REiO-Script-typing-sheet.html` |
| Linux | Append the file to `~/.XCompose` (keep an `include "%L"` line), log out and in, then press Compose and the 4 keys. | `REiO-Script.XCompose` |
| Windows | Install AutoHotkey v2 and run the script. Ctrl+Alt+R toggles RE_iO mode (Esc also leaves it). While on, plain a-m start a code, and Shift+letter still gives capitals. | `REiO-Script-Windows.ahk` |
| macOS | Copy to `~/Library/Keyboard Layouts/`, log out and in, add "RE_iO Script" under Input Sources. Lowercase a-m start a code. Use Shift for capitals or Option+letter for plain letters. | `REiO-Script-Mac.keylayout` |

## 4. Files

| File | Purpose |
|---|---|
| `REiO-Script.ttf` | The font |
| `REiO-Script-typing-sheet.html` | Click-to-type chart and typing box, font embedded, works offline |
| `REiO-Script-glyphs.csv` | One row per glyph: codepoint, row and column, groups, typing code, attested flag, place and manner labels |
| `REiO-Script.XCompose` | Linux input sequences |
| `REiO-Script-Windows.ahk` | Windows input script |
| `REiO-Script-Mac.keylayout` | macOS keyboard layout |
| `preview.png` | Sample render |
| `README.md` | Short install notes |
| `build/` | Scripts that rebuild everything from the chart PNGs |

Columns in the CSV: `codepoint, glyph, row, col, row_group, row_in_group, col_group, col_in_group, attested_in_speech, has_ink, typing_code, place_code, place_name, place_family, manner, manner_code, voicing`.

## 5. How it was built

1. Chart i (10000 x 5333 px) was read as a regular grid: 63 columns by 36 rows inside the turquoise box, about 133 px per cell. Checked against the orange group lines (13 column groups, 7 row groups) and confirmed that glyphs do not cross cell borders.
2. Each cell was upscaled, blurred slightly and thresholded, then traced to smooth outlines, with stray edge lines removed.
3. Outlines were assembled into a TrueType font at U+E000 upward, with metrics set so each glyph occupies one square cell.
4. Chart 16180's blue pixels were counted per cell. Counts were cleanly bimodal (zero or over 1,000 pixels), giving the 566 attested cells.
5. Labels, typing codes and the keyboard files were generated from the same grid, and checked by simulation: all 2,268 codes produce the right glyph in the Mac layout, and the Windows script uses the same arithmetic.

## 6. Limits and open questions

- **Voicing order** within each row pair is inferred, not stated (section 2).
- **Attested set** (blue cells) agrees with the book's table in every spot check made (11 of 11), but the book's table shows only about 70% of articulations, so the other cells could not be cross-checked.
- **Canepari's own symbols** are not attached to the cells. The book's canIPA symbols use custom fonts that do not extract as text. Matching each cell to its symbol would need the page images read by eye or by OCR.
- **The legend grid** at the top right of the charts is not decoded.
- **Windows and macOS input files** were not run on real machines. The Mac layout was validated by simulating all 2,268 codes. The Windows script's glyph arithmetic was checked, but the script itself was not run.
- **Resolution:** outlines come from roughly 133 px cells. A higher-resolution source would give cleaner large-size output.
- **Private Use Area:** the codepoints are not standard. Text typed with this font will show as boxes or other symbols on any system without the font.

## 7. Sources and credit

- The RE_iO Script charts 16176-1 (chart i), 16176-2 (chart ii) and 16180, which state: "based upon work by: Luciano Canepari, La Fonetica naturale, con IPA".
- Luciano Canepari, *Natural Phonetics & Tonetics: Articulatory, Auditory & Functional* (Lincom, 2007, updated 2008), fig 10.1, "canIPA contoids", pp. 166-168, and chapter 10's note that the contoids are grouped into seven sections. Free PDF: [Chs. 7-14](https://canipa.net/lib/exe/fetch.php?media=docs:npt-ch-07-14_2023-07-20_main.pdf). Further free material is listed at [canipa.net](https://canipa.net/doku.php?id=pdf).
- Background on the author and the system: [Luciano Canepari on Wikipedia](https://en.wikipedia.org/wiki/Luciano_Canepari).

The ring script itself, its design and the chart layout are the work of your uncle. Canepari's work is the phonetic classification the grid is based on. This documentation only records how the two line up.
