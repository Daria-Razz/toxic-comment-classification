# Toxic Comment Classification

## Project Overview

This project aims to classify toxic comments using machine learning models. The dataset contains user comments labeled as either toxic or non-toxic. The goal is to build a model that can accurately predict whether a given comment is toxic or not.

## Project Structure

toxic-comment-classification/
│
├── data/
│   └── toxic_comments.csv  # The dataset used in the project.
│
├── notebooks/
│   └── toxic-comment-classification.ipynb  # Jupyter notebook for project workflow.
│
├── src/
│   └── setup_nltk.py  # Script to download NLTK stopwords and punkt tokenizer data.
│
├── requirements.txt  # Project dependencies.
│
└── README.md  # Project documentation.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.11+

### Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/Daria-Razz/toxic-comment-classification.git
    ```

2. Navigate to the project folder and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Download the necessary NLTK data:

    ```bash
    python src/setup_nltk.py
    ```

5. The dataset is already provided in the repository, located in the data/ folder.

### Usage

1. **Jupyter Notebook**: Open the notebook to run the project interactively.

    ```bash
    jupyter notebook notebooks/toxic-comment-classification.ipynb
    ```

2. **Python Scripts**: All preprocessing and model training are handled within the Jupyter notebook. If you prefer running everything via a Python script, you can extract the code from the notebook and save it into a script, but currently, no separate preprocessing or model scripts are provided.

### Project Components

- **notebooks/toxic-comment-classification.ipynb**: The notebook contains the end-to-end project workflow including data preprocessing, model training, evaluation, and visualization.
- **src/setup_nltk.py**: Script to download the necessary NLTK corpora such as stopwords and punkt.

### Models Used

Multiple models such as Logistic Regression, CatBoost, and XGBoost were trained to classify toxic comments. Random oversampling was applied to handle class imbalance.
  
### Evaluation Metrics

- F1 Score

### Results

- **Logistic Regression**: F1 Score = 0.78
- **CatBoost**: F1 Score = 0.64
- **Multinomial Naive Bayes**: F1 Score = 0.73
- **Stochastic Gradient Descent (SGD)**: F1 Score = 0.78

On the test set, the Stochastic Gradient Descent (SGD) model achieved the best result with an F1 Score of 0.77.

## Contributing

Feel free to fork the repository, make changes, and create a pull request if you want to contribute to the project. Any improvements or bug fixes are welcome!
