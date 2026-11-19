# Tools

Rebuild pipeline. Run from the **repo root** (the scripts read `charts/` by relative path). Needs Python 3 with Pillow, NumPy, fontTools, and `potracer` (`pip install potracer`).

1. `python tools/attested.py` : finds the chart-16180 grid and the blue cells (writes `att.npy`, a copy is kept in this folder; copy it to where `build_font.py` runs).
2. `python tools/build_font.py` : traces the 2,268 cells, writes `REiO-Script.ttf` and `REiO-Script-glyphs.csv` in the current folder. Slow (several minutes, pure Python).
3. `python tools/mkinput.py REiO-Script.ttf` : adds typing codes and labels to the CSV, writes `REiO-Script.XCompose` and the typing sheet (needs `labels.py` and `sheet.tpl.html`).
4. `python tools/mkkeyboards.py <outdir>` : writes the Windows and macOS input files.

`labels.py` holds the place and manner names taken from Canepari's fig 10.1 (see `upstream/SOURCES.md`).

Note: these scripts were developed in a scratch folder and copied here with the chart paths adjusted. The full pipeline has not been re-run end to end from this layout.
