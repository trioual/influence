@echo off
ECHO ----------------------------------------
echo Creating Influence Build Folder
IF Exist ..\..\project\Win32BuildSetup\BUILD_WIN32\Xbmc\addons\skin.influence rmdir ..\..\project\Win32BuildSetup\BUILD_WIN32\Xbmc\addons\skin.influence /S /Q
md ..\..\project\Win32BuildSetup\BUILD_WIN32\Xbmc\addons\skin.influence\media\

Echo .svn>exclude.txt
Echo Thumbs.db>>exclude.txt
Echo Desktop.ini>>exclude.txt
Echo dsstdfx.bin>>exclude.txt
Echo build.bat>>exclude.txt
Echo \skin.influence\media\>>exclude.txt
Echo exclude.txt>>exclude.txt

ECHO ----------------------------------------
ECHO Creating XBT File...
START /B /WAIT ..\..\Tools\TexturePacker\TexturePacker -dupecheck -input media -output ..\..\project\Win32BuildSetup\BUILD_WIN32\Xbmc\addons\skin.influence\media\Textures.xbt

ECHO ----------------------------------------
ECHO XBT Texture Files Created...
ECHO Building Skin Directory...
xcopy "..\skin.influence" "..\..\project\Win32BuildSetup\BUILD_WIN32\Xbmc\addons\skin.influence" /E /Q /I /Y /EXCLUDE:exclude.txt

del exclude.txt
