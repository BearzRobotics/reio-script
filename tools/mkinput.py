import csv, json, base64, sys, os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from labels import col_label, row_label
BASE=['codepoint','glyph','row','col','row_group','row_in_group','col_group','col_in_group','attested_in_speech','has_ink']
font=sys.argv[1]
rows=[{k:r[k] for k in BASE} for r in csv.DictReader(open('REiO-Script-glyphs.csv'))]
def code(r):
    return 'abcdefghijklm'[int(r['col_group'])-1]+str(int(r['col_in_group']))+str(int(r['row_group']))+str(int(r['row_in_group'])%10)
data=[]
for r in rows:
    pc,pn,fam=col_label(int(r['col_group']),int(r['col_in_group'])); mn,mc,vo=row_label(int(r['row_group']),int(r['row_in_group']))
    r['_l']=[pc,pn,fam,mn,mc,vo]
    data.append([int(r['row']),int(r['col']),code(r),int(r['codepoint'][2:],16),1 if r['attested_in_speech']=='yes' else 0,int(r['row_group']),int(r['col_group']),f'{pc} {pn}',f'{mn}, {vo}'])
codes=[d[2] for d in data]; assert len(set(codes))==2268
# CSV gets the typing code
with open('REiO-Script-glyphs.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(BASE+['typing_code','place_code','place_name','place_family','manner','manner_code','voicing'])
    for r in rows: w.writerow([r[k] for k in BASE]+[code(r)]+r['_l'])
# XCompose
with open('REiO-Script.XCompose','w') as f:
    f.write('# RE_iO Script compose sequences. Install: append to ~/.XCompose (keep an include line for the system file).\n# Type: Compose, then 4 keys = column-group letter a-m, column-in-group 1-7, row-group 1-7, row-in-group 1-9 (0 = 10).\n# Example: Compose a 1 1 1 -> first glyph\n')
    for d in data:
        keys=' '.join(f'<{c}>' for c in d[2])
        f.write(f'<Multi_key> {keys} : "\\U{d[3]:08X}" # r{d[0]:02d}c{d[1]:02d}{" attested" if d[4] else ""}\n')
b64=base64.b64encode(open(font,'rb').read()).decode()
html=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'sheet.tpl.html')).read().replace('__DATA__',json.dumps(data,separators=(',',':'))).replace('__FONT__',b64)
open('REiO-Script-typing-sheet.html','w').write(html)
print('ok',len(html))
