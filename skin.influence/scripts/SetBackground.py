import xbmc
from xbmcgui import Window
from urllib import quote_plus, unquote_plus
import re
import sys
import os


class Main:
    def _parse_argv( self ):
        try:
            # parse sys.argv for params
            params = dict( arg.split( "=" ) for arg in sys.argv[ 1 ].split( "&" ) )
        except:
            # no params passed
            params = {}
        # set our preferences
        self.bg = params.get( "bg", "" )
        self.bgmen = params.get( "bgmen", "" )
        self.run = params.get( "run", "" )

    def __init__( self ):
        # parse argv for any preferences
        self._parse_argv()
	print "YO" 
	print "bg:" + self.bg
	print "bgmen:" + self.bgmen
	print "run:" + self.run
        if self.bg:
		xbmc.executebuiltin ("Skin.SetString(CurrentBackground," + self.bg + ")")
		print "BG"
	else:
		xbmc.executebuiltin ("Skin.SetString(CurrentBackground," + self.bgmen + ")")
		print "BGMEN"
        
	xbmc.executebuiltin (self.run)
if ( __name__ == "__main__" ):
    Main()
