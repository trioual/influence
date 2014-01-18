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
        self.Menu = params.get( "Menu", "" )
        self.Nb = params.get( "Nb", "" )

    def __init__( self ):
        # parse argv for any preferences
        self._parse_argv()
	xbmc.executebuiltin( "Skin.Reset(Menu_%s_sub_act)" % ( self.Menu ) )
	for i in range( 1, int( self.Nb )+1 ):
    		print "Skin.HasSetting(Menu_%s_sub%i_act)" % ( self.Menu, i ) 
    		if xbmc.getCondVisibility( "Skin.HasSetting(Menu_%s_sub%i_act)" % ( self.Menu, i ) ):
         		print "Skin.SetBool(Menu_%s_sub_act)" % ( self.Menu ) 
         		xbmc.executebuiltin( "Skin.SetBool(Menu_%s_sub_act)" % ( self.Menu ) )

if ( __name__ == "__main__" ):
    Main()
