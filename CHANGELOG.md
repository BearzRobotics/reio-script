# Changelog

## 0.0.3
- **Fix: both fonts failed to install on Windows ("not a valid font").** The name table was missing the full name, unique ID, version and PostScript name (name IDs 3 to 6), and the OS/2 table lacked the Regular style bit. Added `tools/finalize_font.py`, which writes a complete name table and sets the OS/2 bits. The glyphs are unchanged.
- Typing sheet regenerated with the corrected font embedded.

## 0.0.2
- Added the second font, **RE_iO Script Attested** (`font/REiO-Script-Attested.ttf`): only the 566 glyphs marked blue in chart 16180, with the same codepoints as the complete font. The complete font is unchanged.
- Added an explicit all-rights-reserved `LICENSE`.
- Added `tools/mksubset.py`.

## 0.0.1
First draft for review by the script's designer.
- Font with all 2,268 glyphs from chart i, traced from the chart images (Private Use Area, U+E000-U+E8DB).
- Glyph table with typing codes, attested flags (from chart 16180's blue cells), and Canepari place and manner labels.
- Typing sheet (HTML), Linux compose file, Windows AutoHotkey v2 script, macOS keyboard layout.
- Documentation and a list of open questions for the designer.
