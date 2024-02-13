from bs4 import BeautifulSoup

import requests
import os
import errno
import cloudscraper

def download_chapter(url,dir):
    pg_num = 1
    ses = requests.Session()
    ses.headers = {
    'referer': 'https://www.lightnovelworld.co/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'accept': 'application/json'
    }
    for i in range(1,252):
         
         scraper = cloudscraper.create_scraper(
             browser={ 'browser': 'chrome', 'platform': 'windows', 'desktop': True }
         )
         meG = scraper.get(url + str(pg_num))

         pg_num=pg_num+1
         soup = BeautifulSoup(meG.content,'html.parser')

         div = soup.find('div',attrs={'class':'chapter-content'})
         p = div.find_all('p')
         
         title = soup.find('span', attrs={'class':'chapter-title'})
         chapter_name = title.text.strip().partition(':')[0]         
         
         with open(dir+'/'+f'{chapter_name}.txt', 'w', encoding='utf-8') as f_out:
             f_out.write(title.text.strip()+'\n\n')
             for line in p:
                 f_out.write(line.text +'\n')
             f_out.write('\n\n')
             print(chapter_name +' done !')

def main():

    print('--------------------------------------------------')
    title='player who returned 10000 years later'
    cwd = os.getcwd()
    title_dir = os.path.join(cwd,title)

    try:
        os.mkdir(title_dir)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass

    base_url ='https://www.lightnovelworld.co/novel/player-who-returned-10000-years-later-1524/chapter-'
    download_chapter(base_url,title_dir)

if __name__ == '__main__' :
    main()
