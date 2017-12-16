
import os
import shutil #Shell utilities
from os import path
from shutil import make_archive
from zipfile import ZipFile

def main():

    if path.exists("newfile.txt"):
        src = path.realpath("newfile.txt")

    head, tail = path.split(src)
    print("path:",head)
    print("file:",tail)

    dst = src + ".bak" # dst-Variable (Backup) bekommt eine .bak Endung
    shutil.copy(src,dst) # Der Inhalt der Src-File wird in die Dst-File übertragen

    #os.rename("textfile.txt", "newfile.txt")

    #root_dir, tail = path.split(src)
    #shutil.make_archive("archive", "zip", root_dir)

    with ZipFile("testzip.zip","w") as newzip: #Macht einen Local scope. Mit Newzip kann man auf die ZipFile welche man gemacht hat zugreifen
        newzip.write("newfile.txt")
        newzip.write("newfile.txt.bak")

if __name__ == "__main__":
    main()
