import sys

if len(sys.argv) > 3:
    print("I need you to enter a Movie and  a rating")
    sys.exit(1)
else:
    movie_name, movie_rating = sys.argv[1], sys.argv[2]
    if movie_rating.isdigit():
        movie_rating = int(movie_rating)
        movie_percent = movie_rating * 10
        print("Movie: {}, Rating: {}".format(movie_name, movie_percent))
    else:
        print("I need a rating and a movie name")
