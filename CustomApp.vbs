' Run CustomApp (a FlexTools application)
'
' The '0' parameter to Run hides the console window.

Set WshShell = CreateObject("WScript.Shell")

PYTHON = "py"

WshShell.Run PYTHON & " CustomApp\CustomApp.py", 0, False

WshShell = Null
