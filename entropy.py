from math import log2
from pathlib import Path
from sys import argv
import matplotlib.pyplot as plt
from symbolfrequences import count_frequencies_of_symbols

def entropy(probability):
    if probability <= 0 or probability > 1:
        return 0
    H = probability * log2(probability)
    return H

def count_entropy_of_text(text):
    probabilities = count_frequencies_of_symbols(text)
    E = 0.0
    for value in probabilities.values():
        E += entropy(value)
    return -E

#text = Path(argv[1]).read_text()
#
#entropy_counted = count_frequencies_of_symbols(text)
#
#names = list(entropy_counted.keys())
#values = list(entropy_counted.values())
#
#print("Entropy of this text: " + str(count_entropy_of_text(text)))
#
#plt.bar(range(len(entropy_counted)), values, tick_label=names)
#plt.title("Frequencies of alphabet symbols in the text")
#plt.show()

