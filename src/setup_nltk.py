import nltk

def setup_nltk_resources():
    print("Downloading NLTK stopwords and punkt tokenizer...")
    nltk.download('stopwords')
    nltk.download('punkt')

if __name__ == "__main__":
    setup_nltk_resources()
    print("NLTK resources downloaded successfully!")
