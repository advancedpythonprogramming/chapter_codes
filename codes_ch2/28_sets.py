songs_list = [("Uptown Funk", "Mark Ronson"),
              ("Thinking Out Loud", "Ed Sheeran"),
              ("Sugar", "Maroon 5"),
              ("Patterns In The Ivy", "Opeth"),
              ("Take Me To Church", "Hozier"),
              ("Style", "Taylor Swift"),
              ("Love Me Like You Do", "Ellie Goulding")]

artists = set()

for song, artist in songs_list:
    # The add() method append a new item to the set. We do not require to
    # check whether the item exist or not previously in the set.
    artists.add(artist)

print(artists)

# We can create a set using brackets including items separated by coma.
songs = {'Style', 'Uptown Funk', 'Take Me To Church', 'Sugar',
         'Thinking Out Loud', 'Patterns In The Ivy', 'Love Me Like You Do'}

print(songs)
print('Sugar' in songs)

for artist in artists:
    print("{} plays excellent music".format(artist))

# Build a list from a set
artists_list = list(artists)
artists_list.sort()
print(artists_list)

# Mathematical Operations
my_artists = {
    'Hozier', 'Opeth', 'Ellie Goulding', 'Mark Ronson', 'Taylor Swift'
}

artists_album = {'Maroon 5', 'Taylor Swift', 'Amy Wadge'}

print("All: {}".format(my_artists.union(artists_album)))
print("both: {}".format(artists_album.intersection(my_artists)))

# The A.difference(B) returns a set of items that exist only in A but
# not in B.
print("Only in A: {}".format(my_artists.difference(artists_album)))

# The symmetric difference returns a set of items that exist only in
# one of the sets, but not both.
print("Any but not both: {}".format(my_artists.symmetric_difference(
    artists_album)))

# Operation Order
bands = {"Opeth", "Guns N' Roses"}

print("my_artist is to bands:")
print("issuperset: {}".format(my_artists.issuperset(bands)))
print("issubset: {}".format(my_artists.issubset(bands)))
print("difference: {}".format(my_artists.difference(bands)))

print("-" * 20)

print("bands is to my_artists:")
print("issuperset: {}".format(bands.issuperset(my_artists)))
print("issubset: {}".format(bands.issubset(my_artists)))
print("difference: {}".format(bands.difference(my_artists)))
