import search_albums

def save_songs():
    query = input("Please enter Artist and Album/Song Title: ")
    try:
        link = search_albums.find_link(query)

        if link[:24] == "https://open.spotify.com":
            print(f"Found {link}")
            choice = 'a'
            while choice.lower()[0] != "y" and choice.lower()[0] != "n":
                choice = input("is that correct? (Y/n): ")
                if choice.lower()[0] == "n":
                    print("Aborted! Try again")
                    save_songs()
                elif choice.lower()[0] == "y":
                    with open("albums.txt", "a") as links:
                        links.write(f"{link}\n")
                        print("Saved!")
                    return
        else:
            print("Google didn't return a Spotify Link TwT")
    except Exception as e:
        print(f"There was an error XwX: {e}")