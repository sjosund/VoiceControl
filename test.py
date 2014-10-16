from __future__ import print_function

from subprocess import Popen, call
import json
import wit

playlists = {
    'full-day_list': 'spotify:user:1146628823:playlist:6TSA3CY3vwcWrZSvG8Zgwi',
    'jazz': 'spotify:user:1146628823:playlist:1YEoE6AslVyAA6CTXv20zn'
}

def start_spotify():
    playlist = playlists['full-day_list']
    p = Popen(['spotify'])
    if p.poll() is None:
        p.wait()
    call(
        [
            'spotify-remote', 'play',
            playlist
        ]
    )


def start_vlc():
    print('Sorry VLC is not installed')


def query():
    access_token = 'XWST5FGSVQLMKGX6BHN7MBRXY3KCLGIH'
    wit.init()
    response = json.loads(
        wit.voice_query_auto(access_token)
    )
    print('Response: {}'.format(response))
    wit.close()

    return response

intents = {
    'start_spotify': start_spotify,
    'start_vlc': start_vlc
}

def handle_response(response):
    print('RESPONSE:', response)
    #intents[response['outcomes'][0]['intent']]()

def main():
    while True:
        response = query()
        handle_response(response)

if __name__ == '__main__':
    main()
