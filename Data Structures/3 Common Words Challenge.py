# Program to find the 3 most common words for a given text

from collections import Counter
import re

string1 = """
    Python is an easy programmers language.
    Python syntax is like the English language.
    Python language is easy to learn and adapt to compared to Java and C.
    In Python language, the same task can be performed using fewer lines of code.
    It's easy learning and easy to code.
    """

words = re.findall(r'\w+', string1)

results = Counter(words)
top3 = results.most_common(3)
print(top3)
