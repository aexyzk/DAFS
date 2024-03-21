import os
import subprocess
import sort_music as sort
import get_links
import get_linux_or_windows

def main():
    print("**********************************************************************")
    print("*                      Spotify Album Downloader                      *")
    print("**********************************************************************\n")
    if get_linux_or_windows.isLinux() == True:
        print("You are on Linux/Unix!")
    elif get_linux_or_windows.isLinux() == False:
        print("You are on Windows!\n")

    choice = 0

    while choice != 4:
        print("(1) Download Saved Songs!\n(2) Search Songs to Save!\n(3) Download Saved Videos!\n(4) Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            with open("albums.txt", "r") as albums:
                for i in albums:
                    print(f"Downloading: {i}")
                    if get_linux_or_windows.isLinux() == False:
                        subprocess.run(f"spotdl.exe --output Music {i}")
                    elif get_linux_or_windows.isLinux() == True:
                        subprocess.run(["./spotdl-4.2.4-linux", "--output", "Music", i])
                    sort.sort()
                line_number = 0
            choice = 0
        elif choice == 2:
            get_links.save_songs()
            choice = 0
        elif choice == 3:
            with open("videos.txt", "r") as videos:
                for i in videos:
                    print(f"Downloading: {i}")
                    if get_linux_or_windows.isLinux() == False:
                        subprocess.run(f"echo {i}")
                    elif get_linux_or_windows.isLinux() == True:
                        subprocess.run(["./yt-dlp_linux", i])
                    sort.sort()
                video_line_number = 0

if __name__ == "__main__":
    main()