def print_upper_words(words, must_start_with):
    """Print each word on sep line, uppercased, if starts with one of the letters defined in must_start_with """
    for word in words:
        for start in must_start_with:
            if word.startswith(start):
                print (word.upper())
                break


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
