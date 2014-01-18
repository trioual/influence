import xbmc
from xbmcgui import Window
from urllib import quote_plus, unquote_plus
import re
import sys
import os

class Main:
    def __init__( self ):
        fileGenre=open('special://skin/720p/ListGenre.xml','w')

        # sql statement
        sql_genres = "select genre.* from genre "
        # query the database
        genres_xml = xbmc.executehttpapi( "QueryVideoDatabase(%s)" % quote_plus( sql_genres ), )
        # separate the records
        genres = re.findall( "<record>(.+?)</record>", genres_xml, re.DOTALL )
        # enumerate thru our records and set our properties
        fileGenre.write('<includes>\n')
        fileGenre.write('\t<include name="ListGenre">\n')
        fileGenre.write('\t\t<content>\n')

        for count, genre in enumerate( genres ):
            # separate individual fields
            fields = re.findall( "<field>(.*?)</field>", genre, re.DOTALL )
            # fields[1]=idgenre, fields[2]=genre
            fileGenre.write('\t\t\t<item id="'+fields[0]+'">\n')
            fileGenre.write('\t\t\t\t<label>"'+fields[0]+'"</label>\n')
            fileGenre.write('\t\t\t\t<label2>'+fields[1]+'</label2>\n')
            fileGenre.write('\t\t\t\t<onclick>-</onclick>\n')
            fileGenre.write('\t\t\t</item>\n')
        fileGenre.write('\t\t</content>\n')
        fileGenre.write('\t</include>\n')
        fileGenre.write('</includes>')
        fileGenre.close()

if ( __name__ == "__main__" ):
    Main()

