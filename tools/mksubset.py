"""Build the attested-only font (just the glyphs marked blue in chart 16180) from the complete font.
Same codepoints as the complete font, so text typed with one works with the other.
Usage (from repo root): python tools/mksubset.py font/REiO-Script.ttf data/REiO-Script-glyphs.csv font/REiO-Script-Attested.ttf"""
import csv, sys
from fontTools.ttLib import TTFont
from fontTools import subset
src, table, out = sys.argv[1:4]
cps = [int(r['codepoint'][2:], 16) for r in csv.DictReader(open(table)) if r['attested_in_speech'] == 'yes']
opts = subset.Options(); opts.notdef_outline = True; opts.name_IDs = ['*']; opts.layout_features = []
font = TTFont(src)
s = subset.Subsetter(opts); s.populate(unicodes=cps + [0x20]); s.subset(font)
for rec in font['name'].names:
    if rec.nameID == 1: rec.string = 'RE_iO Script Attested'
    elif rec.nameID == 4: rec.string = 'RE_iO Script Attested Regular'
    elif rec.nameID == 6: rec.string = 'REiO-Script-Attested-Regular'
font.save(out)
print(len(cps), 'glyphs ->', out)
