user_name = input("Please enter your name: ")
favourite_movie = input("Please enter your favourite movie: ")
imdb_rating = int(input("Please enter the imdb rating (/10): "))
imdb_rating *= 10

print("Hello {}, Your percentage rating of {} is {}%.".format(user_name, favourite_movie, imdb_rating))

if imdb_rating >= 70:
    print("We have a Winner")
elif imdb_rating >= 50:
    print("Not bad")
elif imdb_rating >= 30:
    print("Not a hit")
else:
    print("Getting worse")
