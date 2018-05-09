from datetime import datetime
from bs4 import BeautifulSoup

import argparse
import urllib2
import os





headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def log(*args):
    print datetime.now().strftime('%m-%d %H:%M:%S'), 'crawling', args




if __name__ =='__main__': 
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", dest='chapter', required=False,
                        help="[int] if not specified, all will be downloaded", type = int)
    args = parser.parse_args()

    crawl_chapters = (0, 105) if args.chapter == None else (args.chapter, args.chapter + 1)
    log('This task is going to crawl', crawl_chapters)
    for i in range(crawl_chapters[0], crawl_chapters[1]):
        folder = 'AoT/%03d' % i
        if not os.path.exists(folder):
            os.makedirs(folder)
        sites = []
        try:
            for j in range(1, 105):
                site = 'http://web2.cartoonmad.com/c86es736z62/1221/%03d/%03d.jpg' % (i, j)
                req = urllib2.Request(site,headers=headers)
                log(site)
                with open((folder+'/%03d.jpg' % j),'wb') as f:
                    f.write(urllib2.urlopen(req).read())
        except Exception as e:
            log(i,j,str(e))
            continue













