from interesting_numbers.interests import is_word, WORDS
def find_words(n):
    results = []
    for b in range(2,10000):
        if is_word(n,b):
            results.append(is_word(n,b))
    return [res.printed_number for res in sorted(results, key = lambda x: WORDS.index(x.description))]