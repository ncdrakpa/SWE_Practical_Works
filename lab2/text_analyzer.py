# Open and Read a Text File
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

content = read_file('sample.txt')
print(content[:100])  

# Count the Number of Lines
def count_lines(content):
    return len(content.split('\n'))
num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")

# Count the Number of Words
def count_words(content):
    return len(content.split())
num_words = count_words(content)
print(f"Number of words: {num_words}")

 #Find the Most Common Word
from collections import Counter

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

common_word, count = most_common_word(content)
print(f"Most common word: '{common_word}' (appears {count} times)")

# Calculate Average Word Length
def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")

# Combine Everything into a Main Function
def analyze_text(filename):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")

analyze_text('sample.txt')

# Modify the program to count the number of unique words in the text.

def cunt_uninque_words(text):
    words = text.lower().split()
    unique_words = set(words)
    return len(set(words))
    text = "Unique words are counted only once"
    unique_word_count = cunt_uninque_words(text)
    print(f"Number of unique words: {unique_word_count}")

# Add a function to find the longest word in the text.
def find_longest_word(text):
    words = text.split()
    longest_word = max(words, key=len)
    return longest_word

def count_unique_words(text):
    words = text.lower().split()
    unique_words = set(words)
    return len(unique_words)

text = "Longest word is found by comparing word lengths"
longest_word = find_longest_word(text)
unique_word_count = count_unique_words(text)

print("Number of unique words:", unique_word_count)
print("Longest word: {longest_word}")

#Implement a feature to count the occurrences of a specific word (case-insensitive).
def count_unique_words(text):
    words = text.lower().split()
    unique_words = set(words)
    return len(unique_words)

def find_longest_word(text):
    words = text.split()
    longest_word = max(words, key=len)
    return longest_word

def count_specific_word(text, target_word):
    words = text.lower().split()
    target_word = target_word.lower()
    return words.count(target_word)

text = "This is a sample text with some sample words. Words can repeat, but unique words are counted once."
unique_word_count = count_unique_words(text)
longest_word = find_longest_word(text)
specific_word_count = count_specific_word(text, "sample")

print("Number of unique words:", unique_word_count)
print("Longest word:", longest_word)
print("Occurrences of the word 'sample':", specific_word_count)

# Create a function to calculate the percentage of words that are longer than the average word length.

def count_unique_words(text):
    words = text.lower().split()
    unique_words = set(words)
    return len(unique_words)

def find_longest_word(text):
    words = text.split()
    longest_word = max(words, key=len)    
    return longest_word

def count_specific_word(text, target_word):
    words = text.lower().split()
    target_word = target_word.lower()
    return words.count(target_word)

def percentage_longer_than_average(text):
    words = text.split()
    average_length = sum(len(word) for word in words) / len(words)
    longer_words_count = sum(1 for word in words if len(word) > average_length)
    percentage = (longer_words_count / len(words)) * 100
    return percentage

text = "This is a sample text with some longer and shorter words."
unique_word_count = count_unique_words(text)
longest_word = find_longest_word(text)
specific_word_count = count_specific_word(text, "sample")
percentage_longer_avg = percentage_longer_than_average(text)

print("Number of unique words:", unique_word_count)
print("Longest word:", longest_word)
print("Occurrences of the word 'sample':", specific_word_count)
print("Percentage of words longer than average length:", percentage_longer_avg)