#!/bin/bash

if [[ $# < 2 ]]; then
	echo "Must supply <playlist URL> and the <JSON filename> to write to."
	exit
fi

#URL=${1:-$WATCH_LATER_PLAYLIST}
URL=$1
JSON_FILENAME=${2:-wl.json}

youtube-dl --flat-playlist --ignore-config --ignore-errors --netrc -J "$URL" > "$JSON_FILENAME"
