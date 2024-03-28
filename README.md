
# Datascience X Logistic Regression: Harry Potter and a Data Scientist

## Overview
In this project, we embark on a magical journey to save Hogwarts from a bewitched Sorting Hat by employing the power of Data Science and Logistic Regression. Our goal is to develop a classifier that accurately sorts students into Hogwarts houses based on their characteristics and course preferences.

## Project Structure
```
project-root/
│
├── data/                   # Directory containing datasets
│   ├── dataset_train.csv   # Training dataset
│   └── dataset_test.csv    # Test dataset
│
├── src/                    # Source code for the project
│   ├── describe.py         # Script for data description
│   ├── histogram.py        # Script for generating histograms
│   ├── scatter_plot.py     # Script for creating scatter plots
│   ├── pair_plot.py        # Script for generating pair plots
│   ├── logreg_train.py     # Script for training the logistic regression model
│   └── logreg_predict.py   # Script for making predictions with the model
│
├── models/                 # Trained model weights and parameters
│   └── logistic_model.pkl  # Saved logistic regression model
│
├── results/                # Results and output from scripts
│   ├── histograms/         # Histograms output
│   ├── scatter_plots/      # Scatter plots output
│   ├── pair_plots/         # Pair plots output
│   └── houses.csv          # Output predictions
│
├── requirements.txt        # List of dependencies to install
└── README.md               # This file
```

## Installation

Before running the project, ensure you have Python 3.8+ installed. Then, install the required Python packages using:

```bash
pip install -r requirements.txt
```

## Usage

Each script in the `src/` directory serves a specific purpose in the project pipeline:

1. **Data Description**:
    ```bash
    python src/describe.py data/dataset_train.csv
    ```
    Generates descriptive statistics for the training dataset.

2. **Data Visualization**:
    - **Histogram**:
        ```bash
        python src/histogram.py data/dataset_train.csv
        ```
    - **Scatter Plot**:
        ```bash
        python src/scatter_plot.py data/dataset_train.csv
        ```
    - **Pair Plot**:
        ```bash
        python src/pair_plot.py data/dataset_train.csv
        ```

3. **Logistic Regression Model**:
    - **Training**:
        ```bash
        python src/logreg_train.py data/dataset_train.csv
        ```
    - **Prediction**:
        ```bash
        python src/logreg_predict.py data/dataset_test.csv models/logistic_model.pkl
        ```

## Dataset

The dataset comprises characteristics and course preferences of Hogwarts students. Details include:

- **Numerical Features**: e.g., Magic Ability Score, Potion Making Score.
- **Categorical Features**: e.g., Favorite Hogwarts Course, House.

## Objective

The primary objective is to implement a logistic regression model that accurately predicts the Hogwarts house for each student, achieving a minimum precision of 98%.

## Contributing

Contributions to the project are welcome! Please fork the repository and submit a pull request with your enhancements. For major changes, please open an issue first to discuss what you would like to change.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgements

- Special thanks to Professor McGonagall and the Hogwarts School of Witchcraft and Wizardry for inspiring this project.
- Yann LeCun and the pioneers of artificial intelligence for making this project theoretically possible.
