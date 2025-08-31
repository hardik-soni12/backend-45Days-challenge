# Count Word Frequency in a Text

'''Question:

Write a function that takes a piece of text and counts how many times each word appears, ignoring case.
Example Input: "The cat and the hat"
Expected Output:
{"the": 2, "cat": 1, "and": 1, "hat": 1}
'''

import re
from collections import Counter

def method1(text):
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)

    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count


def method2(text):

    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

example = 'The Cat and the hat'
print(method1(example))
print(method2(example))