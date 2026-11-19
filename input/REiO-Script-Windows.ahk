#Requires AutoHotkey v2.0
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
