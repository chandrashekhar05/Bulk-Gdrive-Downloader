from datetime import datetime
import gdown

source = "links.txt"
filename = "converted_links.txt"
gdlink = "https://drive.google.com/uc?id="


def linkgen():
    global source 
    global filename
    global gdlink

    downloadthis = "No"

    temp = input(f"Enter Source filename [{source}] : ")

    source = valid_choice(source,temp)

    links = open(source,"r")
    temp  = input(f"Enter Output filename [{filename}] : ")

    filename = valid_choice(filename,temp)

    gdownl = open(f"{filename}","w")
    currDT = datetime.now()
    dt_string = currDT.strftime("%d-%B-%y %H:%M:%S")
    stamp = "-"*5+" "+dt_string+" "+"-"*5+"\n"
    gdownl.writelines(stamp)

    #reading lines from file
    lines1 = links.readlines()
    lines = str(lines1).split(sep=',')

    for line in lines:
        getStart = line.find("/d/")
        getStart+=3
        getEnd = line.find("/view")
        fileId = line[getStart:getEnd]
        fullLink = gdlink+fileId+"\n"
        gdownl.writelines(fullLink)

    gdownl.writelines("")
    gdownl.close()
    links.close()
    print(f"TASK COMPLETE\nNew Links in '{filename}' file")

    downloadthis = input("Do you want to download this? Yes/No [No] : ")
    downloadthis = downloadthis.upper()
    if downloadthis == "YES" or downloadthis == "Y":
        drive_downloader()
    else:
        print("Closing Program")

def download_menu():
    global filename
    filename = input("1.Enter filename with full path : ")
    drive_downloader()

def drive_downloader():
    dlinks = open(filename,"r")
    url_list = dlinks.readlines()

    for url in url_list[1:]:
        url = url.strip()
        try:
            gdown.download(url)
        except Exception:
            print(Exception)
    
    print("!!!!! Download Complete !!!!!")
    dlinks.close()

def valid_choice(old,new):
    if new:
        return new
    return old

if __name__=="__main__":
    print("Google Drive File Downloader\nThis script help you to download google drive file that are publicly accessible")
    print("Values in [] are default")
    print("1. Link Generate\n2. Download Files\n")
    choice = int(input("Select your choice : "))
    if choice == 1:
        linkgen()
    elif choice == 2:
        download_menu()
    else:
        print("INVALID INPUT rerun the script")