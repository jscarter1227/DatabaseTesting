import sqlite3
import os

os.remove("toy.db")

conn = sqlite3.connect("toy.db")

c = conn.cursor()

# table 6.2 cheatsheet for class

c.execute('''CREATE TABLE songs
             (name text NOT NULL, artist text,
              file text PRIMARY KEY NOT NULL, duration int NOT NULL DEFAULT 10,
              genre text, album text,
              CONSTRAINT SONGFK FOREIGN KEY (artist, album) REFERENCES
              album(artist, name))''')

c.execute('''CREATE TABLE albums
             (name text NOT NULL,
              artist text NOT NULL, 
              cover_image_file text,
              CONSTRAINT ALBUMPK PRIMARY KEY (name,artist))''')

c.execute('''INSERT INTO songs VALUES ('Doom (short concert version)',
                'Umaut Lords of Death Metal II', 'doomandruinshort.mp6',
                6, 'metal as heck', 'Unicorns and Pansies')''')

c.execute('''INSERT INTO songs VALUES ('Doom and Ruin',
                'Umaut Lords of Death Metal II',
                'doomandruin.mp6', 667, 'metal as heck',
                'Unicorns and Pansies')''')

c.execute('''INSERT INTO albums VALUES ('Unicorns and Pansies',
            'Umaut Lords of Death Metal II', 'foo.jpg')''')

c.execute('''INSERT INTO songs VALUES ('My Favorite Things',
                'Alex Groce', 'alexfavorite.mp3', 300,
                'contemporary adult', 'Alex Groce Sings the Blues')''')

c.execute('''INSERT INTO songs VALUES ('My Favorite Things',
                'John Coltrane', 'coltranefavorite.mp3', 250,
                'jazz', 'The Best of John Coltrane')''')

c.execute('''INSERT INTO songs VALUES ('Happy Bday',
                'Church People', 'morman.mp3', 120,
                'choir', 'The Best of Mormanism')''')

# c.execute("DELETE FROM songs WHERE name = 'Doom (short concert version)'")

query = '''SELECT * FROM songs, albums WHERE duration > 100
        AND albums.cover_image_file = 'foo.jpg'
        AND albums.name = songs.album'''

c.execute(query)

print("QUERY:", query)
print()
f = c.fetchone()
while f is not None:
    print("*"*40)
    print("RESULT:")
    print(f)
    print()
    f = c.fetchone()
print()
print("ALL DONE")
