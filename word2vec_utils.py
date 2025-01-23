def is_within_range(value, theta, tolerance=0.005):
    
    """
        Checks if a value is within a range of theta ± tolerance.

        Semantle rounds the similarity values to the nearest hundredth, so we must
        check +- 0.005 of the similarity showed in order to correctly determine 
        if our word's similarity is within range of the similarity shown on Semantle
    
    """
    
    return abs(value - theta) <= tolerance

def calculate_similarities(model, first_word, first_similarity, second_word, second_similarity):
    
    """
        Calculates the common words based on similarities.
    
        We calculate (twice) which words can be candidate answers based on their similarities,
        and then use set intersection to determine the words that are candidates in both calculations
    
    """

    print("Calculating...")

    first_options, second_options = set(), set()

    for word in model.key_to_index:

        #We want to ignore all proper nouns and also all entries containing more than one word
        if word[0].isupper() or '_' in word:
            continue

        #Semantle rounds by taking the similarity and multiplying by 100, so we check similarities in the same way
        if is_within_range(model.similarity(word, first_word) * 100, first_similarity):
            first_options.add(word)

        if is_within_range(model.similarity(word, second_word) * 100, second_similarity):
            second_options.add(word)

    #The intersection between the sets will give us our candidate answer(s)
    return first_options & second_options