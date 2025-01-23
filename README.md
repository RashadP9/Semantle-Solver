# Semantle Solver
A Python project that solves the word guessing game *Semantle* using the Word2Vec algorithm and cosine similarities.

## Play the Game
You can play the game *Semantle* here: [Play Semantle](https://semantle.com)

## Requirements

Before running this project, you will need to download the Google News Word2Vec model. This file is used for semantic similarity calculations.

1. [Download Google News Word2Vec Model](https://www.kaggle.com/datasets/adarshsng/googlenewsvectors)

2. Place the downloaded file into the project folder where the script is located.


## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/semantle-solver.git
    ```
2. Navigate to the project folder:
    ```bash
    cd semantle-solver
    ```
    
## Usage
To solve the *Semantle* puzzle:
1. Run the script:
    ```bash
    python semantle_solver.py
    ```
2. Enter the target word you’re trying to guess.
3. The solver will suggest words based on semantic similarity.

## Performance
Based on my own testing, the *Semantle Solver* is able to solve the game in **2 guesses** on average.
