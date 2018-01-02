#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import logging
import components.porn91 as porn91

logging.basicConfig(level=10,
                        format='%(asctime)s [%(module)s] %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    porn = porn91.Porn91()

    # fetch all video links
    video_links = []
    # video_links = porn.fetch_home_page()
    video_links += porn.fetch("http://www.91porn.com/v.php?category=hot&viewtype=basic")
    video_links = list(set(video_links))

    logging.debug("Found %u Video Links!" % len(video_links))

    # fetch first video actual downloadable url
    for link in video_links:
        porn.download(link)
