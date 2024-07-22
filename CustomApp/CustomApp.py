#
#   A simple custom FlexTools application
#

from flextoolslib import main

from Version import Title
from CustomAppMenu import customMenu

from CustomAppStatusbar import statusbarCallback


#----------------------------------------------------------- 

main(Title, customMenu, statusbarCallback)
