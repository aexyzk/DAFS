try:
    from googlesearch import search
except ImportError: 
    print("No module named 'google' found")

def find_link(query):
    for j in search(f"{query} Spotify Album", tld="co.in", num=1, stop=1, pause=2):
        return j