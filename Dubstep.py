def song_decoder(song):
    s = ''
    if len(song) <= 200:
        raw_songs = song.split('WUB')
        for raw_song in raw_songs:
            if raw_song != '':
                s = raw_song + s

        return s[-1:-8: -1].strip()
    else:
        return -1


song = "WUBLWUBWWUBHWUB"
raw_song = song_decoder(song)
print(raw_song)