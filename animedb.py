import sqlite3
import os

os.remove("toy.db")

conn = sqlite3.connect("toy.db")

c = conn.cursor()

c.execute('''CREATE TABLE animes
             (name text, creator text,
              source_material text, num_episodes int,
              num_seasons int, classic boolean,
              genre text, cover_image text,
              weeb_level int, MAL_rating float)''')

c.execute('''CREATE TABLE creators
             (name text, years_in_industry int,
              wikipedia_link text, veteran boolean,
              art_school text)''')

# c.execute('''INSERT INTO songs VALUES ('Doom (short concert version)', 'Umaut Lords of Death Metal II', 'doomandruinshort.mp6', 6, 'metal as heck', 'Unicorns and Pansies')''')

# c.execute('''INSERT INTO songs VALUES ('Doom and Ruin', 'Umaut Lords of Death Metal II', 'doomandruin.mp6', 667, 'metal as heck', 'Unicorns and Pansies')''')

# c.execute('''INSERT INTO albums VALUES ('Unicorns and Pansies',          'Umaut Lords of Death Metal II', 'foo.jpg')''')

# c.execute('''INSERT INTO songs VALUES ('My Favorite Things', 'Alex Groce', 'alexfavorite.mp3', 300, 'contemporary adult', 'Alex Groce Sings the Blues')''')

# c.execute('''INSERT INTO songs VALUES ('My Favorite Things', 'John Coltrane', 'coltranefavorite.mp3', 250, 'jazz', 'The Best of John Coltrane')''')

# # c.execute("DELETE FROM songs WHERE name = 'Doom (short concert version)'")

# query = '''SELECT * FROM songs, albums WHERE duration > 100               AND albums.cover_image_file = 'foo.jpg'
#           AND albums.name = songs.album'''

# c.execute(query)

# print("QUERY:", query)
# print()
# f = c.fetchone()

# while f is not None:
#     print("*"*40)
#     print("RESULT:")
#     print(f)
#     print()
#     f = c.fetchone()
# print()
# print("ALL DONE")

