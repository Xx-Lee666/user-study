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

def generate_summary(file_path, top_n=5):
    """Generate a summary by extracting top N frequent words and their frequencies."""
    try:
        frequencies = count_word_frequencies(file_path)
        if frequencies:
            print(f"Top {top_n} words in file:")
            for word, freq in frequencies.most_common(top_n):
                print(f"'{word}': {freq} times")
    except Exception as e:
        print(f"An error occurred while generating summary: {e}")

def process_file(mode, file_path):
    if mode == "count":
        count_words_in_file(file_path)
    elif mode == "freq":
        frequencies = count_word_frequencies(file_path)
        if frequencies:
            result = '\n'.join([f"'{word}': {frequency} times" for word, frequency in frequencies.items()])
            print(result)
    elif mode == "summary":
        generate_summary(file_path)
    else:
        print("Invalid mode. Use 'count', 'freq', or 'summary'.")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        file_path = sys.argv[1]
        mode = sys.argv[2]
        process_file(mode, file_path)
    else:
        print("Usage: python script.py <file_path> <mode>")
        print("Modes: 'count', 'freq', 'summary'")
