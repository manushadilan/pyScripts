import glob
import shutil
import re


numbers = re.compile(r'(\d+)')

def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


def fileMerger():
    #get text file list in current folder
    print('Merging files !')
    files = sorted(glob.glob("*.txt"), key=numericalSort)
    #write all text data into single file
    with open('player who returned 10000 years later.txt','wb') as wfd:
        for f in files:
            print(f)
            with open(f,'rb') as fd:
                shutil.copyfileobj(fd, wfd)
            wfd.write(b"\n")

    print('Merge is Done')



def main():
    fileMerger()

if __name__ == '__main__':
  main()