import xbmc, xbmcgui, os, sys
from xbmcgui import Window
from xml.dom.minidom import parseString

class Main:
    # grab the home window
    WINDOW = Window ( 10000 )

    def __init__( self ):
        self._clear_properties()
        self._read_file()
        self._parse_String()
        self._fetch_favourites()
        self.doc.unlink()

    def _clear_properties ( self ):
	for count in range ( 10 ):
            # clear property
	    xbmc.executebuiltin("Skin.Reset(Menu_Favorites_sub%d_run)" % ( count + 1  ,  ))
	    xbmc.executebuiltin("Skin.Reset(Menu_Favorites_sub%d_act)" % ( count + 1  ,  ))
	    xbmc.executebuiltin("Skin.Reset(Menu_Favorites_sub%d_lab)" % ( count + 1  ,  ))
            xbmc.executebuiltin("Skin.Reset(Menu_Favorites_sub%d_Ico)" % ( count + 1  ,  ))

    def _read_file( self ):
        # Set path
        self.fav_dir = 'special://masterprofile//favourites.xml'
        # Check to see if file exists
        if (os.path.isfile( self.fav_dir ) == False):
            self.favourites_xml = '<favourites><favourite name="Can Not Find favourites.xml">-</favourite></favourites>'
        else:
            # read file
            self.fav = open( self.fav_dir , 'r')
            self.favourites_xml = self.fav.read()
            self.fav.close()

    def _parse_String( self ):
        self.doc = parseString( self.favourites_xml )
        self.favourites = self.doc.documentElement.getElementsByTagName ( 'favourite' )

    def _fetch_favourites( self ):
        # Go through each favourites
        count = 0
        for self.doc in self.favourites:
            self.fav_path = self.doc.childNodes [ 0 ].nodeValue
	    print "Add " + self.fav_path + " __ " + self.doc.attributes ['name'].nodeValue
	    xbmc.executebuiltin("Skin.SetBool(Menu_Favorites_sub_act)")
	    xbmc.executebuiltin("Skin.ToggleSetting(Menu_Favorites_sub%d_act)" % ( count + 1  ,  ))
	    xbmc.executebuiltin("Skin.SetString(Menu_Favorites_sub%d_run,%s)" % ( count + 1  , self.fav_path ))
	    xbmc.executebuiltin("Skin.SetString(Menu_Favorites_sub%d_lab,%s)" % ( count + 1  , self.doc.attributes [ 'name' ].nodeValue ))
            try: xbmc.executebuiltin ("Skin.SetString(Menu_Favorites_sub%d_back,%s)" % ( count + 1  , self.doc.attributes [ 'thumb' ].nodeValue ))
            except: pass
	    try: xbmc.executebuiltin ("Skin.SetString(Menu_Favorites_sub%d_Ico,%s)" % ( count + 1  , self.doc.attributes [ 'thumb' ].nodeValue ))
	    except: pass
            count = count+1

if ( __name__ == "__main__" ):
    Main()
