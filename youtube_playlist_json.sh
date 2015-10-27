#!/bin/bash

#URL=${1:-$WATCH_LATER_PLAYLIST}
URL=$1
JSON_FILENAME=${2:-wl.json}

youtube-dl --flat-playlist --ignore-config --ignore-errors --netrc -J "$URL" > "$JSON_FILENAME"
