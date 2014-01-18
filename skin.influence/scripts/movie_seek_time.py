
import xbmc, xbmcgui

try:
    player = xbmc.Player()
    if not player.isPlaying():
        
        def get_browse_dialog( default="", heading="", dlg_type=3, shares="files", mask="", use_thumbs=False, treat_as_folder=False ):
            """ shows a browse dialog and returns a value
                - 0 : ShowAndGetDirectory
                - 1 : ShowAndGetFile
                - 2 : ShowAndGetImage
                - 3 : ShowAndGetWriteableDirectory
            """
            dialog = xbmcgui.Dialog()
            value = dialog.browse( dlg_type, heading, shares, mask, use_thumbs, treat_as_folder, default )
            return value

        movie = get_browse_dialog( heading="Browse video", dlg_type=1, shares="video" )

        player.play( movie )
    player.pause()

    time_to_start = xbmcgui.Dialog().numeric( 2, "Enter time in format: HH:MM", "00:01" )

    HH, MM = time_to_start.split( ":" )
    time_to_start = ( int( HH ) * 60 * 60 ) + ( int( MM ) * 60 )


    """
    seekTime(...)
        seekTime() -- Seeks the specified amount of time as fractional seconds.
                      The time specified is relative to the beginning of the
                      currently playing media file.
         
        Throws: Exception, if player is not playing a file.
    """

    player.seekTime( int( time_to_start ) )
except:
    import traceback
    traceback.print_exc()

