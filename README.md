# RE_iO Script

A font, typing tools and documentation for **RE_iO Script**: a systematic glyph script for the range of sounds the human voice can make, designed as an alternative to the many different IPA symbols. The charts credit *Luciano Canepari, La Fonetica naturale, con IPA* as the work they are based upon.

**Version 0.0.2**

> ## ⚠️ Work in progress
> This project is an **unfinished, unreviewed draft (v0.0.2)**. It is a first attempt to turn the RE_iO Script charts into a usable font, and it has **not yet been reviewed by the script's designer**. The glyph labels, the voiced/voiceless row order, the typing codes and the file layout may all change or be wrong. The Windows and macOS input files have not been tested on real machines. Do not treat anything here as final or authoritative.
>
> **All rights reserved.** See `LICENSE`. The script design belongs to its designer and the phonetic classification it is based on is Luciano Canepari's. The files are published for review only; a licence may be chosen later with the designer.

> **The glyphs only display if the font is loaded.** They live in the Unicode Private Use Area (U+E000 to U+E8DB). Install `font/REiO-Script.ttf` (and optionally `font/REiO-Script-Attested.ttf`) first (Linux: copy to `~/.local/share/fonts/` and run `fc-cache -f`; Windows: right-click, Install; macOS: double-click, Install Font). Without it you will see empty boxes. `web/REiO-Script-typing-sheet.html` has the font embedded and works without installing.

## What is here
| Path | What |
|---|---|
| `font/REiO-Script.ttf` | **Complete font** ("RE_iO Script"): 2,268 glyphs, every possible sound, every cell of chart i |
| `font/REiO-Script-Attested.ttf` | **Attested font** ("RE_iO Script Attested"): only the 566 glyphs marked blue in chart 16180, the sounds actually found in human speech |
| `web/REiO-Script-typing-sheet.html` | Click-to-type chart and 4-key typing box (offline, font embedded) |
| `data/REiO-Script-glyphs.csv` | One row per glyph: codepoint, grid position, typing code, attested flag, place/manner/voicing labels |
| `input/` | Keyboard input: Linux `.XCompose`, Windows AutoHotkey v2 script, macOS `.keylayout` |
| `charts/` | The source charts (16176 chart i and ii, 16180), the designer's work |
| `docs/docs.md` | Full documentation: what the grid means, how to type, limits |
| `docs/question.md` | **Open questions for the designer** |
| `tools/` | Scripts that rebuild the font, data and input files from the charts |
| `upstream/` | Pointers to the free Canepari material the labels come from (not copied here) |

## Two fonts
- **RE_iO Script** is the complete set: every possible combination.
- **RE_iO Script Attested** has only the blue glyphs. It uses the **same codepoints** as the complete font, so text typed with one displays in the other. Codepoints for sounds not in the attested set have no glyph and show as blank or a fallback box. The typing codes are the same for both.

## The idea in brief
- 63 columns are the 63 canIPA places of articulation, in 13 families.
- 36 rows are 18 manners of articulation, each as a voiced/voiceless pair, in 7 groups.
- 566 of the 2,268 glyphs are marked in chart 16180 as sounds actually found in human speech. The rest are the remaining possible combinations.
- Type any glyph with four keys: column-group letter a to m, column in group 1 to 7, row group 1 to 7, row in group 1 to 9 (0 = 10). Example: `a111` is the top-left glyph.

## Status and known gaps
- The voiced-first order within each row pair is inferred, not confirmed. See `docs/question.md`.
- The legend grid at the top right of the charts is not decoded.
- The Windows and macOS input files were not run on real machines.
- All rights reserved for now (see `LICENSE`); a licence should be decided with the designer.

See `CHANGELOG.md` for versions.
