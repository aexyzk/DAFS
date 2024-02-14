import os
import eyed3
from shutil import move

# Function to extract metadata from a downloaded song
def get_metadata(song_path):
    audiofile = eyed3.load(song_path)
    if audiofile.tag is None:
        return {}
    return {
        "album": audiofile.tag.album,
        "artist": audiofile.tag.artist,
        "title": audiofile.tag.title
    }

# Path to the directory containing the downloaded songs
download_dir = "Music"
not_allowed_chars = '[<>:"/\\|?*]'

def sort():
    # Iterate over the downloaded songs
    for song_file in os.listdir(download_dir):
        if song_file.endswith(".mp3"):
            song_path = os.path.join(download_dir, song_file)
            metadata = get_metadata(song_path)
            album_name = metadata.get("album")
            artist_name = metadata.get("artist")

            if album_name is not None and artist_name is not None:
                album_name = album_name.translate({ord(i): None for i in not_allowed_chars})
                artist_name = artist_name.translate({ord(i): None for i in not_allowed_chars})

                # Create artist folder if it doesn't exist
                artist_dir = os.path.join(download_dir, artist_name)
                if not os.path.exists(artist_dir):
                    os.makedirs(artist_dir)

                # Create album folder if it doesn't exist within artist folder
                album_dir = os.path.join(artist_dir, album_name)
                if not os.path.exists(album_dir):
                    os.makedirs(album_dir)

                # Move the song file to the album folder
                new_song_path = os.path.join(album_dir, song_file)
                move(song_path, new_song_path)

sort()