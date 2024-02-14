import os
import subprocess
import sort_music as sort
import get_links

def main():
    choice = 0

    while choice != 3:
        print("(1) Download Saved Songs!\n(2) Search Songs to Save!\n(3) Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            with open("albums.txt", "r") as albums:
                for i in albums:
                    print(f"Downloading {i}")
                    subprocess.run(f"spotdl.exe --output Music {i}")
                    sort.sort()
            choice = 0
        elif choice == 2:
            get_links.save_songs()
            choice = 0

if __name__ == "__main__":
    main()
