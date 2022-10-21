import re

def count_frequencies_of_symbols(text):
    probabilities = {}

    if isinstance(text, str):
        for ch in text:
            if ch in probabilities:
                probabilities[ch] += 1
            else:
                probabilities[ch] = 1
        for ch in probabilities:
            probabilities[ch] = probabilities.get(ch)/len(text)
        
        return probabilities

    else:
        return {}

