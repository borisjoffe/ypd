#!/usr/bin/python

import sys, json

def get_urls_from_playlist_json(playlist_json_filename):
    playlist_json = json.load(open(playlist_json_filename))

    """
    Example entry:

    {'_type': 'url',
      'id': '<ID>', // matches url (always?)
      'ie_key': 'Youtube',
      'title': '<TITLE>',
      'url': '<URL>'},
    """

    urls = []

    for video in playlist_json['entries']:
        urls.append(video['url'] + '\t' + video['title'])

    return urls

def write_playlist_urls_to_file(urls=[], playlist_txt_filename='wl.txt'):
    output_file = open(playlist_txt_filename, 'w')
    output_file.write('\n'.join(urls))
    output_file.close()
    print('Output url list to', playlist_txt_filename)

if __name__=='__main__':
    if len(sys.argv) > 1:
        playlist_json_filename = sys.argv[1]
    else:
        playlist_json_filename = 'wl.json'

    print('filename is', playlist_json_filename)

    urls = get_urls_from_playlist_json(playlist_json_filename)
    write_playlist_urls_to_file(urls)
