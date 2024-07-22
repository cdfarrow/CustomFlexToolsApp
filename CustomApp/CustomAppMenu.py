#
#   Custom menu functions
#

import os
import Version

from System.Windows.Forms import (
    Shortcut,
    MessageBox, 
    MessageBoxButtons, 
    MessageBoxIcon,
    )
    

#----------------------------------------------------------- 

def RunHelp(sender, event):
    HelpFile = os.path.join("Help", "CustomApp Help.txt")
    os.startfile(HelpFile)

def RunAbout(sender, event):
    MessageBox.Show(f"{Version.Name} version {Version.Version}",
                    "About CustomApp",
                    MessageBoxButtons.OK)
          
#----------------------------------------------------------- 
customMenu = ("CustomApp Menu",
              [(RunHelp, "Help", Shortcut.CtrlH, None),
               (RunAbout, "About", None, "About CustomApp")])

