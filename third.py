#!/usr/bin/env python
import multiprocessing
import os
from threading import Thread

import requests

from timeit import timeit

CPU_CORES_COUNT = 4
DEST_DIR = 'sample_videos/'
BASE_URL = 'http://www.sample-videos.com/video'
VIDEOS_LIST = [
    'mp4/720/big_buck_bunny_720p_2mb.mp4',
    'mp4/480/big_buck_bunny_480p_2mb.mp4',
    'mp4/360/big_buck_bunny_360p_2mb.mp4',
    'mp4/240/big_buck_bunny_240p_2mb.mp4',
    'flv/720/big_buck_bunny_720p_2mb.flv',
    'flv/480/big_buck_bunny_480p_2mb.flv',
    'flv/360/big_buck_bunny_360p_2mb.flv',
    'flv/240/big_buck_bunny_240p_2mb.flv',
    'mkv/720/big_buck_bunny_720p_2mb.mkv',
    'mkv/480/big_buck_bunny_480p_2mb.mkv',
    'mkv/360/big_buck_bunny_360p_2mb.mkv',
    'mkv/240/big_buck_bunny_240p_2mb.mkv'
]


def download_video(video):
    url = '{}/{}'.format(BASE_URL, video)
    print("Downloading {}...".format(url))
    resp = requests.get(url)
    filename = video.split('/')[-1]
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(resp.content)
        print('{} downloaded'.format(filename))


@timeit
def do_consequently():
    for video in VIDEOS_LIST:
        download_video(video)


@timeit
def do_with_threads():
    threads = []
    for video in VIDEOS_LIST:
        thread = Thread(target=download_video, args=(video,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()


@timeit
def do_with_processes():
    pool = multiprocessing.Pool(10)
    pool.map(download_video, VIDEOS_LIST)


if __name__ == '__main__':
    do_consequently()
    do_with_threads()
    do_with_processes()
