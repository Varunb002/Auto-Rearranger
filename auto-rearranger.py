#code written by Varun Salian
import os, shutil #imports operating system and file move modules
y = input("ENTER THE DIRECTORY PATH\t : ") #Directory where the files should be rearranged
os.chdir(y) #Change Current directory to the above specified path

z = y+"\Apps and Games" #Folder names for Apps and Games(Special Case)
k = y+"\TV SERIES" #Folder name for TV Series (Special Case)

f = ['Season','S1','S7'] #A small list to detect TV Series

#function to move files
def rearranger(fi,ty):
     shutil.move(fi,ty)

#if a single .exe file exists in the current folder move it to the folder named others
for fil in os.listdir(y):
    if fil.endswith((".exe",".EXE")):
        others = y+"\Others"
        if not os.path.isdir(others):
            os.makedirs(others)
        rearranger(fil,others)
#Search for TV series by looking for season/s1 or other similar keyword in the name and move the entire directory to TV Series folder
for dirpath,dirname,filename in os.walk(y):
    for ff in dirname:
        if any(x in ff for x in f):
            shutil.copytree(dirpath,os.path.join(k,os.path.basename(dirpath)))
            shutil.rmtree(dirpath)
#Search for exe except for the folder in TV series and move the entire directory tree to Apps and Games folder
for dirpath,dirname,filename in os.walk(y):
    dirname[:] = [d for d in dirname if d not in ['TV SERIES', 'Others']]
    if any((fn.lower().endswith(".exe") for fn in filename)):
        shutil.copytree(dirpath,os.path.join(z,os.path.basename(dirpath)))
        shutil.rmtree(dirpath)

#Move different files with different extension to their corresponding folder
for (paths,dires,fname) in os.walk(y):
    dires[:] = [d for d in dires if d not in ['Apps and Games','Others','TV SERIES']]
    for files in fname:
            if files.lower().endswith ((".pdf", ".lrf",".irx",".cbr",".cbz",".cb7",".chm",".doc",".docs",".epub",".pdb",".fbz",".xeb",".ceb",".htm",".html",".css",".ibooks",".inf",".azw3",".azw",".3gpp",".kf8",".lic",".prc",".mobi",".pka",".inf",".opg")):
                m = paths
                ebooks = y+"\Ebooks"
                if not os.path.isdir(ebooks):
                    os.makedirs(ebooks)
                os.chdir(ebooks)
                if not os.path.isfile(files):
                    os.chdir(m)
                    rearranger(files,ebooks)
            elif files.lower().endswith ((".tif",".jpg",".bmp",".jpg",".jpeg",".img",".gif",".png",".eps",".cr2",".raw",".nef",".orf",".sr2",".3gpp")) :
                m = paths
                images = y+"\Images"
                if not os.path.isdir(images):
                    os.makedirs(images)
                os.chdir(images)
                if not os.path.isfile(files):
                    os.chdir(m)
                    rearranger(files,images)
            elif files.lower().endswith ((".mkv",".mp4",".flv",".vob",".mpg",".mpg4",".3gp",".3gpp")):
                m = paths
                movies = y+"\Movies"
                if not os.path.isdir(movies):
                    os.makedirs(movies)
                os.chdir(movies)
                if not os.path.isfile(files):
                    os.chdir(m)
                    rearranger(files,movies)
            elif files.lower().endswith ((".zip",".rar",".7z",".tar",".gz",".iso")):
                m = paths
                archives = y+"\Archives"
                if not os.path.isdir(archives):
                    os.makedirs(archives)
                os.chdir(archives)
                if not os.path.isfile(files):
                    os.chdir(m)
                    rearranger(files,archives)
            elif files.endswith ((".apk",".APK")):
                m = paths
                androidapps = y+"\Android Apps"
                if not os.path.isdir(androidapps):
                    os.makedirs(androidapps)
                os.chdir(androidapps)
                if not os.path.isfile(files):
                    os.chdir(m)
                    rearranger(files,androidapps)
            elif not files.endswith (("Movies","Archives","Ebooks","Images")):
                m = paths
                others = y+"\Others"
                if not os.path.isdir(others):
                    os.makedirs(others)
                os.chdir(y + "\Others")
                if not os.path.isfile(files):
                    os.chdir(m)
                    rearranger(files,others)

print ("YOUR FILES HAVE BEEN REARRANGED SUCCESSFULLY GO CHECK THE FOLDER")
