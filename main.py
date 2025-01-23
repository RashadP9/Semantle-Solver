from word2vec_utils import calculate_similarities
from load_model import load_model
from user_input import get_user_inputs

def main():
    
    model = load_model()

    first_word, first_similarity, second_word, second_similarity = get_user_inputs()

    common_elements = calculate_similarities(model, first_word, first_similarity, second_word, second_similarity)

    print(f"The most likely answers are: {common_elements}")

if __name__ == "__main__":
    main()