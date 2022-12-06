from time import sleep

import dbus
# import wakepy

bus = dbus.SessionBus()
spotify_obj = bus.get_object('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2')
spotify_pm = dbus.Interface(spotify_obj, 'org.freedesktop.DBus.Properties')

while True:
    playback_status = spotify_pm.Get('org.mpris.MediaPlayer2.Player', 'PlaybackStatus')
    match playback_status:
        case 'Playing':
            wakepy.set_keepawake()
        case 'Paused' | 'Stopped':
            wakepy.unset_keepawake()
    print(playback_status)
    sleep(5)
