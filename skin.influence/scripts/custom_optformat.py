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
        self.RunOpt = params.get( "RunOpt", "" )
        self.RunOpt_var = params.get( "RunOpt_var", "" )

    def __init__( self ):
        # parse argv for any preferences
        self._parse_argv()
	print self.RunOpt_var + "-> PATH:" + self.RunOpt
        if re.match('plugin.video',self.RunOpt):
		xbmc.executebuiltin ("Skin.SetString(" + self.RunOpt_var + ", ActivateWindow(10024,plugin://"+ self.RunOpt +"/))")
        elif re.match('plugin.audio',self.RunOpt):
		xbmc.executebuiltin ("Skin.SetString(" + self.RunOpt_var + ", ActivateWindow(10501,plugin://"+ self.RunOpt +"/))")
        elif re.match('plugin.program',self.RunOpt):
		xbmc.executebuiltin ("Skin.SetString(" + self.RunOpt_var + ", ActivateWindow(10001,plugin://"+ self.RunOpt +"/))")
        elif re.match('plugin.games',self.RunOpt):
		xbmc.executebuiltin ("Skin.SetString(" + self.RunOpt_var + ", ActivateWindow(10001,plugin://"+ self.RunOpt +"/))")
        elif re.match('script',self.RunOpt):
                xbmc.executebuiltin ("Skin.SetString(" + self.RunOpt_var + ", runscript("+ self.RunOpt +" ))")
        print self.RunOpt
        

if ( __name__ == "__main__" ):
    Main()

