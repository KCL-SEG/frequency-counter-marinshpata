"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in items:
        if str(i) not in frequencies:
            frequencies[str(i)] = 1
        else:
            frequencies[str(i)] +=1
    return frequencies

print(frequencies([100, 'Hello', '100', '100', 100]))