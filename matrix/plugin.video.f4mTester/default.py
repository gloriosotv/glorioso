import xbmc, xbmcvfs, xbmcgui, xbmcaddon, xbmcplugin, re
import os
import urllib.parse as urlparse

__addon__       = xbmcaddon.Addon()
__addonname__   = __addon__.getAddonInfo('name')
__icon__        = __addon__.getAddonInfo('icon')
addon_id = 'plugin.video.f4mTester'
selfAddon = xbmcaddon.Addon(id=addon_id)

mode=None
paramstring=sys.argv[2]
name=''
if paramstring:
    paramstring="".join(paramstring[1:])
    params=urlparse.parse_qs(paramstring)
    url = params['url'][0]
    try:
        name = params['name'][0]
    except:pass

    iconImage=""
    try:
        iconImage = params['iconImage'][0]
    except:pass
    
    try:
        description = params['description'][0]
    except:
        description = ''
	
    mode='play'

    try:    
        mode =  params['mode'][0]
    except: pass
    
if mode ==None:
    xbmcgui.Dialog().textviewer('F4mTester Help', 'F4mTester with inputstream.ffmpegdirect\nKeeps live broadcast stable\nUse: plugin://plugin.video.f4mTester/?url=URL')
   
   
    
elif mode == "play":
    plugin = xbmcvfs.translatePath('special://home/addons/inputstream.ffmpegdirect')
    if os.path.exists(plugin)==False:
        try:
            xbmc.executebuiltin('InstallAddon(inputstream.ffmpegdirect)', wait=True)
        except:
            pass
    if name == "":
        name = "F4mTester"
    li=xbmcgui.ListItem(name, path=url)
    if iconImage:
        li.setArt({"icon": "DefaultVideo.png", "thumb": iconImage})
    li.setInfo(type="Video", infoLabels={"Title": name, "Plot": description})
    if not '.mp4' in url and not '.mp3' in url and not '.mkv' in url and not '.avi' in url and not '.rmvb' in url:
        if os.path.exists(plugin)==True:
            if '.m3u8' in url and '/live/' in url and int(url.count("/")) > 5:
                url = url.replace('/live', '').replace('.m3u8', '')               
            li.setProperty('inputstream', 'inputstream.ffmpegdirect')
            li.setProperty('inputstream.ffmpegdirect.is_realtime_stream', 'true')
            li.setProperty('inputstream.ffmpegdirect.is_catchup_stream', 'catchup')
            li.setProperty('inputstream.ffmpegdirect.catchup_granularity', '60')
            li.setProperty('inputstream.ffmpegdirect.catchup_terminates', 'true')
            li.setProperty('inputstream.ffmpegdirect.stream_mode', 'catchup')
            li.setProperty('inputstream.ffmpegdirect.open_mode', 'curl')            
            if '.mpd' in url:
                li.setProperty('inputstream.ffmpegdirect.manifest_type','mpd')
            else:                
                li.setProperty('inputstream.ffmpegdirect.manifest_type','hls') 
            li.setProperty('inputstream.ffmpegdirect.default_url',url)
            li.setProperty('inputstream.ffmpegdirect.catchup_url_format_string',url)
            li.setProperty('inputstream.ffmpegdirect.catchup_buffer_start_time','1')
            li.setProperty('inputstream.ffmpegdirect.catchup_buffer_offset','1') 
            li.setProperty('inputstream.ffmpegdirect.default_programme_duration','3600')
    xbmc.Player().play(item=url, listitem=li)