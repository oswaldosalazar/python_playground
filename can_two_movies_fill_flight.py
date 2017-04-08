final_set = set()

def can_two_movies_fill_flight(movie_lengths, flight_length):

    # movie lengths we've seen so far
    movie_lengths_seen = set()

    for first_movie_length in movie_lengths:

        matching_second_movie_length = flight_length - first_movie_length
        if matching_second_movie_length in movie_lengths_seen:
            print(final_set)
            return True

        movie_lengths_seen.add(first_movie_length)
        
        final_set.add(first_movie_length)
        final_set.add(matching_second_movie_length)

    # we never found a match, so return False
    return False


can_two_movies_fill_flight({122, 90, 93, 100}, 190)
