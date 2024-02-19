import os
import subprocess
import sort_music as sort
import get_links
import get_linux_or_windows

global line_number
line_number = 0

def main():
    print("**********************************************************************")
    print("*                      Spotify Album Downloader                      *")
    print("**********************************************************************\n")
    if get_linux_or_windows.isLinux() == True:
        print("You are on Linux/Unix!")
    elif get_linux_or_windows.isLinux() == False:
        print("You are on Windows!\n")

    choice = 0

    while choice != 3:
        print("(1) Download Saved Songs!\n(2) Search Songs to Save!\n(3) Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            with open("albums.txt", "r") as albums:
                for i in albums:
                    global line_number
                    line_number += 1
                    print(f"Downloading {line_number}: {i}")
                    if get_linux_or_windows.isLinux() == False:
                        subprocess.run(f"spotdl.exe --output Music {i}")
                    elif get_linux_or_windows.isLinux() == True:
                        subprocess.run(["./spotdl-4.2.4-linux", "--output", "Music", i])
                    sort.sort()
            choice = 0
        elif choice == 2:
            get_links.save_songs()
            choice = 0

if __name__ == "__main__":
    main()