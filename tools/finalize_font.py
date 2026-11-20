"""Make a font file valid and installable on Windows: complete name table, OS/2 style bits.
Usage: python tools/finalize_font.py <font.ttf> "<Family Name>" "<PostScriptFamily>" [version]"""
import sys
from fontTools.ttLib import TTFont
path, family, ps = sys.argv[1:4]
version = sys.argv[4] if len(sys.argv) > 4 else '0.0.2'
f = TTFont(path)
name = f['name']
name.names = []
recs = {
    0: 'All rights reserved.',
    1: family,
    2: 'Regular',
    3: f'{ps}-Regular;{version}',
    4: f'{family} Regular',
    5: f'Version {version}',
    6: f'{ps}-Regular',
}
for nid, s in recs.items():
    name.setName(s, nid, 3, 1, 0x409)   # Windows, Unicode BMP, en-US
    name.setName(s, nid, 1, 0, 0)       # Macintosh, Roman, English
os2 = f['OS/2']
os2.fsSelection = 0x40          # REGULAR
os2.fsType = 0                  # installable embedding
os2.usWeightClass = 400; os2.usWidthClass = 5
os2.ulCodePageRange1 = 1        # Latin 1 bit so the font is not rejected as "no codepage"
os2.ulCodePageRange2 = 0
f['head'].macStyle = 0
f.save(path)
print('finalized', path)
