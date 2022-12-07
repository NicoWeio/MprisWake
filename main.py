from time import sleep

import dbus

# import wakepy
import mywake

bus = dbus.SessionBus()
spotify_obj = bus.get_object('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2')
spotify_pm = dbus.Interface(spotify_obj, 'org.freedesktop.DBus.Properties')


def is_playing():
    return spotify_pm.Get('org.mpris.MediaPlayer2.Player', 'PlaybackStatus') == 'Playing'


while True:
    if is_playing():
        with mywake.inhibit('Spotify', 'Playing music'):
            print("Inhibited")
            while is_playing():
                sleep(5)
            print("Uninhibited")
    sleep(5)
