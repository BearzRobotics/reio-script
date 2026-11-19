import csv, sys
from xml.sax.saxutils import quoteattr
OUT=sys.argv[1]
COLG=[5,5,7,6,6,5,4,5,5,6,4,3,2]; ROWG=[4,6,2,2,4,8,10]
CS=[sum(COLG[:i]) for i in range(13)]; RS=[sum(ROWG[:i]) for i in range(7)]
def cp(cg,cc,rg,rr): return 0xE000+(RS[rg-1]+rr-1)*63+(CS[cg-1]+cc-1)
L='abcdefghijklm'
# ---------------- Windows: AutoHotkey v2 ----------------
ahk='''#Requires AutoHotkey v2.0
#SingleInstance Force
; RE_iO Script input for Windows.
;   Ctrl+Alt+R  toggles RE_iO mode (Esc also leaves it).
;   In RE_iO mode type 4 keys per glyph:
;     column-group letter a-m, column-in-group 1-7, row-group 1-7, row-in-group 1-9 (0 = 10)
;   e.g.  a111  = top-left glyph.   Shift+letter types a normal capital; digits type normally.
;   Plain lowercase a-m are captured while the mode is on; toggle it off to type them.
; Needs the REiO-Script.ttf font installed (right-click > Install for all users).

colG := [5,5,7,6,6,5,4,5,5,6,4,3,2]
rowG := [4,6,2,2,4,8,10]
active := false
buf := ""

Tip(msg, ms := 1500) {
    ToolTip(msg)
    SetTimer(() => ToolTip(), -ms)
}

Sum(arr, n) {
    s := 0
    Loop n
        s += arr[A_Index]
    return s
}

Valid(code) {
    n := StrLen(code), c := SubStr(code, n)
    if (n = 1)
        return InStr("abcdefghijklm", c) > 0
    cg := Ord(SubStr(code, 1, 1)) - 96
    if (n = 2)
        return IsInteger(c) && c >= 1 && c <= colG[cg]
    rg := SubStr(code, 3, 1)
    if (n = 3)
        return IsInteger(c) && c >= 1 && c <= 7
    rr := (c = 0) ? 10 : c
    return IsInteger(c) && rr <= rowG[Integer(rg)]
}

Emit(code) {
    cg := Ord(SubStr(code, 1, 1)) - 96
    cc := Integer(SubStr(code, 2, 1))
    rg := Integer(SubStr(code, 3, 1))
    rr := Integer(SubStr(code, 4, 1))
    if (rr = 0)
        rr := 10
    col := Sum(colG, cg - 1) + cc
    row := Sum(rowG, rg - 1) + rr
    SendText(Chr(0xE000 + (row - 1) * 63 + (col - 1)))
}

Press(k, *) {
    global buf
    if (buf = "" && IsInteger(k)) {
        SendText(k)
        return
    }
    try_ := buf . k
    if !Valid(try_) {
        buf := ""
        Tip("RE_iO: invalid code, cancelled")
        return
    }
    buf := try_
    if (StrLen(buf) = 4) {
        Emit(buf)
        buf := ""
        ToolTip()
    } else
        ToolTip("RE_iO: " . buf)
}

Leave(*) {
    global active, buf
    active := false, buf := ""
    Tip("RE_iO mode OFF")
}

^!r:: {
    global active, buf
    active := !active, buf := ""
    Tip(active ? "RE_iO mode ON  (Ctrl+Alt+R or Esc to leave)" : "RE_iO mode OFF")
}

HotIf (*) => active
for k in StrSplit("abcdefghijklm0123456789")
    Hotkey(k, Press.Bind(k))
Hotkey("Escape", Leave)
HotIf
'''
open(OUT+'/REiO-Script-Windows.ahk','w',encoding='utf-8-sig').write(ahk)
# ---------------- macOS: .keylayout ----------------
US_BASE={0:'a',1:'s',2:'d',3:'f',4:'h',5:'g',6:'z',7:'x',8:'c',9:'v',11:'b',12:'q',13:'w',14:'e',15:'r',16:'y',17:'t',
 18:'1',19:'2',20:'3',21:'4',22:'6',23:'5',24:'=',25:'9',26:'7',27:'-',28:'8',29:'0',30:']',31:'o',32:'u',33:'[',34:'i',35:'p',
 37:'l',38:'j',39:"'",40:'k',41:';',42:'\\',43:',',44:'/',45:'n',46:'m',47:'.',50:'`'}
US_SHIFT={**{k:v.upper() for k,v in US_BASE.items() if v.isalpha()},18:'!',19:'@',20:'#',21:'$',22:'^',23:'%',24:'+',25:'(',26:'&',27:'_',28:'*',29:')',30:'}',33:'{',39:'"',41:':',42:'|',43:'<',44:'?',47:'>',50:'~'}
SPECIAL={36:'&#x000D;',48:'&#x0009;',49:' ',51:'&#x0008;',53:'&#x001B;'}
def esc(s):
    return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}.get(s,s)
def out(s):
    if s.startswith('&#'): return s
    return esc(s)
keyletter={c:ch for c,ch in US_BASE.items() if ch in L}
keydigit={c:ch for c,ch in US_BASE.items() if ch.isdigit()}
def kmap(idx,fn):
    s=f'<keyMap index="{idx}">'
    for c in sorted(set(US_BASE)|set(SPECIAL)):
        s+=fn(c)
    return s+'</keyMap>'
def plain(table):
    def f(c):
        if c in SPECIAL: return f'<key code="{c}" output="{SPECIAL[c]}"/>'
        return f'<key code="{c}" output="{out(table[c])}"/>'
    return f
def base(c):
    if c in SPECIAL: return f'<key code="{c}" output="{SPECIAL[c]}"/>'
    if c in keyletter: return f'<key code="{c}" action="L_{keyletter[c]}"/>'
    if c in keydigit: return f'<key code="{c}" action="D_{keydigit[c]}"/>'
    return f'<key code="{c}" output="{out(US_BASE[c])}"/>'
caps_tbl={c:(v.upper() if v.isalpha() else v) for c,v in US_BASE.items()}
states=[]  # (name)
actions={}
for ch in L: actions[f'L_{ch}']=[('none',None,'S_'+ch)]
for d in '0123456789': actions[f'D_{d}']=[('none',d,None)]
for gi,ch in enumerate(L):
    n=COLG[gi]; st=f'S_{ch}'; states.append(st)
    for cc in range(1,min(n,7)+1):
        actions[f'D_{cc}'].append((st,None,f'{st}{cc}')); st2=f'{st}{cc}'; states.append(st2)
        for rg in range(1,8):
            actions[f'D_{rg}'].append((st2,None,f'{st2}{rg}')); st3=f'{st2}{rg}'; states.append(st3)
            for rr in range(1,ROWG[rg-1]+1):
                d=str(rr%10)
                actions[f'D_{d}'].append((st3,'&#x%04X;'%cp(gi+1,cc,rg,rr),None))
x='<?xml version="1.1" encoding="UTF-8"?>\n<!DOCTYPE keyboard SYSTEM "file://localhost/System/Library/DTDs/KeyboardLayout.dtd">\n'
x+='<keyboard group="126" id="-19190" name="RE_iO Script" maxout="1">\n<layouts><layout first="0" last="17" modifiers="mods" mapSet="ANSI"/><layout first="18" last="18" modifiers="mods" mapSet="ANSI"/></layouts>\n'
x+='<modifierMap id="mods" defaultIndex="0">\n'
x+='<keyMapSelect mapIndex="0"><modifier keys=""/></keyMapSelect>\n<keyMapSelect mapIndex="1"><modifier keys="anyShift"/></keyMapSelect>\n<keyMapSelect mapIndex="2"><modifier keys="caps"/></keyMapSelect>\n<keyMapSelect mapIndex="3"><modifier keys="anyOption"/></keyMapSelect>\n<keyMapSelect mapIndex="4"><modifier keys="command"/><modifier keys="anyControl"/></keyMapSelect>\n</modifierMap>\n'
x+='<keyMapSet id="ANSI">\n'+kmap(0,base)+'\n'+kmap(1,plain({**US_BASE,**US_SHIFT}))+'\n'+kmap(2,plain(caps_tbl))+'\n'+kmap(3,plain(US_BASE))+'\n'+kmap(4,plain(US_BASE))+'\n</keyMapSet>\n'
x+='<actions>\n'
for aid,ws in actions.items():
    x+=f'<action id="{aid}">'
    for st,o,nx in ws:
        x+=f'<when state="{st}" '+(f'output="{o if o.startswith("&#") else esc(o)}"' if o is not None else f'next="{nx}"')+'/>'
    x+='</action>\n'
x+='</actions>\n<terminators>'+''.join(f'<when state="{s}" output=""/>' for s in states)+'</terminators>\n</keyboard>\n'
open(OUT+'/REiO-Script-Mac.keylayout','w',encoding='utf-8').write(x)
print('states',len(states),'bytes',len(x))
