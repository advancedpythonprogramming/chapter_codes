from collections import namedtuple

#namedtuple is a tuple subclass that has fields (with arbitrary names),
#which can be accessed as tuple.field
Movie = namedtuple("Movie", ["title", "director", "genre"])
movies = [Movie("Into the Woods", "Rob Marshall", "Adventure"),
          Movie("American Sniper", "Clint Eastwood", "Action"),
          Movie("Birdman", "Alejandro Gonzalez Inarritu", "Comedy"),
          Movie("Boyhood", "Richard Linklater", "Drama"),
          Movie("Taken 3", "Olivier Megaton", "Action"),
          Movie("The Imitation Game", "Morten Tyldum", "Biography"),
          Movie("Gone Girl", "David Fincher", "Drama")]

# set comprehension
action_directors = {b.director for b in movies if b.genre == 'Action'}
print(action_directors)
