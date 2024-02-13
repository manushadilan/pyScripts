import glob
import shutil
import os
from ftplib import FTP
import tkinter as tk
import tkinter.simpledialog

def ftpUploader():
    #upload created text file into as400 server using ftp

    print('File upload started !')

    #GUI dialog box for credential input
    tk.Tk().withdraw()
    # ip = tkinter.simpledialog.askstring("Sytem IP address", "Enter IP address:")
    # if ip None:
        # exit()
    uname = tkinter.simpledialog.askstring("User Name", "Enter User Name:")
    if uname is None:
        exit()
    pwd = tkinter.simpledialog.askstring("Password", "Enter password:", show='*')
    if pwd is None:
        exit()
    tk.Tk().destroy() # clean-up yourself!

    # FTP with your login details
    ftp = FTP('192.168.100.40',uname,pwd)
    print('Logged in to the system !')
    #ftp = FTP(ip,uname,pwd)
    ftp.cwd('ONLINEAL01')  
    file = open('NEW.txt','rb')    # file to send
    ftp.storlines('STOR NEW.txt', file)   # send the file
    #ftp.storlines('STOR TEST2.txt', file)   # send the file
    # close file and FTP
    file.close()   
    ftp.quit()
    print('File Transfer Success !')

def fileMerger():
    #get text file list in current folder
    print('Merging files !')
    files = glob.glob("*.txt")
    #write all text data into single file
    with open('Test.txt','wb') as wfd:
        for f in files:
            with open(f,'rb') as fd:
                shutil.copyfileobj(fd, wfd)
            wfd.write(b"\n")

    #remove  character from file

    print('Cleaning the file !')

    infile = "Test.txt"
    outfile = "NEW.txt"

    delete_list = [""]
    fin = open(infile)
    fout = open(outfile, "w+")
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
        fout.write(line)
    fin.close()
    fout.close()

def main():
    fileMerger()
    ftpUploader()

if __name__ == '__main__':
  main()