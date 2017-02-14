#!/usr/bin/python
import os
import sys

ffmpeg = "ffmpeg -i"
options = "-ab 320k -ac 2 -ar 48000"
export = "export"
space = " "
DS = "\\"
escape = "\"" #the "\"" are to allow ffmpeg to handle flac & path names which contain spaces!

def convertFlacToMp3(parent):
    for child in parent:
        path = os.getcwd() + child
        mp3s = os.listdir(path)
        output = os.mkdir(path.join([DS, export]))

        print "Converting files in: " + path

        for flac in flacs:

            if ".flac" in flac:
                flac = flac.decode("UTF-8")
                mp3 = flac.replace(".flac", ".mp3")

                print "--" + flac + " >>> " + mp3

                execute = ffmpeg.join([
                    space, escape, path, DS, flac, escape, space,
                    options, space,
                    escape, path, DS, out, DS, mp3, escape])

                print os.system(execute)


if __name__ == "__main__":
    convertFlacToMp3(os.listdir(os.getcwd()))
