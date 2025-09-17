; ===============================
; CS2 Safe Trash Talk Script
; ===============================

pythonFile := "C:\Users\lewis\Documents\Projects\Insult Generator\cs2_insult_gen.py"
tempOutput := A_Temp "\python_output.txt"

; Ctrl+Shift+L: Generate a new AI line and copy to clipboard
^+l::
{
    RunWait %ComSpec% /c python "%pythonFile%" > "%tempOutput%" 2>&1,, Hide

    FileRead, clipboard, %tempOutput%

    SoundPlay, *64

    Send, {Enter}

    Sleep, 50

    Send, ^v

    Sleep, 50
    
    Send, {Enter}
return
}
