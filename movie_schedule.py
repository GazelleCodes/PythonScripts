current_movies = {'The Grinch': '11:00 AM', 
                  'Frozen II': '1:30 PM', 
                  'Toy Story 4': '4:00 PM', 
                  'Avengers: Endgame': '7:00 PM'}

print("we are currently showing the following movies:")
for title in current_movies:
    print(title)

movie = input("What would you like the show time for?\n")

show_time = current_movies.get(movie)
if show_time == None:
    print("Requested movie is not playing today.")
else:
    print(movie + ' is playing at', show_time)