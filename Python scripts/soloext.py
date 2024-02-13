from bs4 import BeautifulSoup
from PIL import Image

import requests
import os
import shutil
import stat
import errno
import glob

def find_chapters(link):

    r = requests.get(link)
    soup = BeautifulSoup(r.content,'html5lib')

    chapter_list = []
    grid = soup.find('div',attrs={'class':'grid space-y-2'})

    for h3 in grid.find_all('h3', attrs={'class':'text-lg font-bold md:text-xl'}):
        chapter_info = {}
        chapter_info['chapter'] = h3.a.text
        chapter_info['link'] = h3.a['href']

        chapter_list.append(chapter_info)

    for i in range(len(chapter_list)):
        print('Chapter {}'.format(chapter_list[i]['chapter']))
    
    print('--------------------------------------------------')

    return chapter_list

def remove_readonly(func,path, _):
    os.chmod(path,stat.S_IWRITE)
    func(path)


def download_chapter(chapters,dir,title,base):

    for i in range(len(chapters)):
        print('Begining to download chapter {}'.format(chapters[i]['chapter']))
        r = requests.get(base + chapters[i]['link'])
        soup = BeautifulSoup(r.content,'html5lib')

        div = soup.find('div',attrs={'class':'flex flex-col items-center justify-center'})
        images=[]

        for img in div.find_all('img',attrs={'class':'w-[650px]'}):
            images.append(img['src'])
        
        image_folder_path = os.path.join(dir,str(chapters[i]['chapter']))
        os.mkdir(image_folder_path)
       
        pg_num = 1
        f_ext='.jpg'
        
        for j in range(len(images)):
            res = requests.get(images[j])
            f_name = os.path.join(image_folder_path, str(pg_num)+ f_ext)
            pg_num=pg_num+1
            file = open(f_name,'wb')
            file.write(res.content)
            file.close()

        im_paths=[]

        for files in sorted(glob.glob(image_folder_path + '/*' + f_ext), key=os.path.getmtime):
            print(files)
            im = Image.open(files)
            im.convert('RGB')
            im_paths.append(im)

        try:
            im1 = im_paths[0]
            im_paths.pop(0)

            chapter_num = chapters[i]['chapter']
            pdf = os.path.join(dir,'{}.pdf'.format(chapter_num))
            im1.save(pdf, save_all=True, append_images=im_paths, subsampling=0, quality=95)

            shutil.rmtree(image_folder_path, onerror=remove_readonly)

        except:
            continue


def main():

    print('--------------------------------------------------')
    title='Solo Leveling'
    cwd = os.getcwd()
    title_dir = os.path.join(cwd,title)

    try:
        os.mkdir(title_dir)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass


    base_url ='https://www.solo-leveling-manhwa.com'

    chapter = find_chapters(base_url)
    download_chapter(chapter, title_dir,title,base_url)

    

if __name__ == '__main__' :
    main()

