import sys
from collections import Counter

def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            num_words = len(words)
            print(f"Total number of words in file: {num_words}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def count_word_frequencies(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().lower()
            words = content.split()
            word_frequencies = Counter(words)
            frequencies = {word: frequency for word, frequency in word_frequencies.items()}
            return frequencies
    except FileNotFoundError:
        return f"File not found: {file_path}"
    except Exception as e:
        return f"An error occurred: {e}"

def process_file(mode, file_path):
    if mode == "count":
        result = count_words_in_file(file_path)
    elif mode == "freq":
        frequencies = count_word_frequencies(file_path)
        result = '\n'.join([f"'{word}': {frequency} times" for word, frequency in frequencies.items()])
    else:
        result = "Invalid mode. Use 'count' or 'freq'."
    return result

if __name__ == "__main__":
    # Example usage
    file_path = 'user_study.txt' 
    mode = 'freq'  # or 'count'
    print(process_file(mode, file_path))
