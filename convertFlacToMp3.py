#!/usr/bin/python
import os
import sys

ffmpeg = "ffmpeg -i "
options = " -ab 320k -ac 2 -ar 48000 "
source = "audio"
DS = "/"
quote = "\"" #the "\"" are to allow ffmpeg to handle flac & path names which contain spaces!

def convertFlacToMp3(parent):
    for artist in os.listdir(parent):
        artist_path = concat([parent, DS, artist])

        if isntDsStore(artist_path) and os.path.isdir(artist_path):
            for album in os.listdir(artist_path):
                album_path = concat([artist_path, DS, album])

                if isntDsStore(album_path):
                    for song in os.listdir(album_path):

                        if ".flac" in song:
                            flac = song.decode("UTF-8")
                            mp3 = flac.replace(".flac", ".mp3")

                            execute = concat([
                                ffmpeg,
                                quote, album_path, DS, flac, quote,
                                options,
                                quote, album_path, DS, mp3, quote])

                            print os.system(execute)


def isntDsStore(item):
    if ".DS_Store" in item:
        return False
    else:
        return True


def concat(words):
    return "".join(words)


if __name__ == "__main__":
    convertFlacToMp3(os.getcwd() + DS + source)
