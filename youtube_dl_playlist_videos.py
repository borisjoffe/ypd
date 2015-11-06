#!/usr/bin/python

import sys, subprocess, config
from os import path
from datetime import datetime

YT_PREFIX = 'https://www.youtube.com/watch?v='
NOTIFY_CMD = config.notify_cmd or 'echo'

run = subprocess.run

def get_full_filename():
    config.directory = config.directory or ''
    config.directory = path.expanduser(config.directory)

    config.filename_template = config.filename_template or '%(id)s_%(title)s.%(ext)s'

    return path.join(config.directory, config.filename_template)

def notify(txt):
    run([NOTIFY_CMD, txt])

def download_urls(urls_filename, reverse=True, log_filename='youtube-playlist-download.log'):
    """Download playlist in reverse order"""
    urls_file = open(urls_filename)
    url_lines = urls_file.read().splitlines();
    urls_file.close()
    if reverse:
        url_lines = reversed(url_lines)

    logfile = open(log_filename, 'w')
    logfile.write('\n' + str(datetime.now()) + '\n')
    logfile.flush()

    # use -f best to avoid merging and just get the best overall format (saves time)
    youtube_cmd_with_args = ['youtube-dl', '--ignore-errors', '--ignore-config', '--write-info-json', '--no-mtime', '-f best', '-o ' + get_full_filename()]

    try:
        for line in url_lines:
            url_id, title = line.split('\t')[:2]
            print('Downloading video: "' + title + '" with id "' + url_id + '"')
            run(youtube_cmd_with_args + [YT_PREFIX + url_id])
            print('Done downloading url:', url_id)
            notify('Done downloading url:' + url_id)
            logfile.write('Downloaded\t' + url_id + '\t' + title + '\n')
            logfile.flush()
    except KeyboardInterrupt as e:
        print("Exiting")
        logfile.close()

    logfile.close()

if __name__=='__main__':
    if len(sys.argv) > 1:
        urls_filename = sys.argv[1]
    else:
        urls_filename = 'wl.txt'

    download_urls(urls_filename)
