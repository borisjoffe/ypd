#!/usr/bin/python

import sys
from subprocess import run

if len(sys.argv) < 1:
    print('Must supply an argument: json convert download')

subcmd = sys.argv[1]
args = sys.argv[2:]

if subcmd.startswith('json'):
    run(['./youtube_playlist_json.sh'] + args)
elif subcmd.startswith('conv'):
    run(['./youtube_pl_json_to_txt.py'] + args)
elif subcmd.startswith('d'):
    run(['./youtube_dl_playlist_videos.py'] + args)
else:
    print('No such command: ' + subcmd)
