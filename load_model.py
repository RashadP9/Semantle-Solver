import os
from gensim.models import KeyedVectors

def load_model():
    
    """ 
        Loads the pre-trained Google News word2vec model.

        Attempts to load a cached version of the model, stored in
        KeyedVectors (.kv) format. If not found, it loads the binary file 
        and creates the .kv and .kv.npy files, and loads those for future use 

    """    
    
    #Get directory from which this script is running
    executing_directory = os.path.dirname(os.path.abspath(__file__))

    #Path to .kv and .bin files
    path_to_google_news_kv = executing_directory + "\GoogleNews-vectors-negative300.kv"
    path_to_google_news_bin = executing_directory + "\GoogleNews-vectors-negative300.bin"

    try:

        if os.path.isfile(path_to_google_news_kv):

            #If .kv file exists, load and then return it
            return KeyedVectors.load(path_to_google_news_kv)

        elif os.path.isfile(path_to_google_news_bin):

            #Load the .bin file, save it, return the model
            google_news_vectors = KeyedVectors.load_word2vec_format(path_to_google_news_bin, binary=True)
        
            google_news_vectors.save(path_to_google_news_kv)

            return google_news_vectors
        
        else:
            raise FileNotFoundError("Neither .kv nor .bin file found in executing directory.")
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise
