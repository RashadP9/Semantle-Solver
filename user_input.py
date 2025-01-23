def get_user_inputs():
    
    """Prompts the user for input and returns the values."""
    
    first_word = input("Enter your first guess: ")
    first_similarity = float(input(f"Enter the similarity for {first_word} seen on Semantle: "))

    second_word = input("Enter your second guess: ")
    second_similarity = float(input(f"Enter the similarity for {second_word} seen on Semantle: "))

    return first_word, first_similarity, second_word, second_similarity