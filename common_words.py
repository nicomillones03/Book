with open("book.txt") as file:
    text = file.read()
file.close()


# Create a dictionary of word frequencies
word_freq = {}
punctuation = ".,!?;:\n-()"
# remove punctuation
for p in punctuation:
    text = text.replace(p, "")

file = open("book.txt")
for line in file:
    for p in punctuation:
        line = line.replace(p, "")
    words = line.split(" ")
    for word in words:
        word = word.lower()
        if len(word) < 4:
            continue
        # check and add into dictionary
        if word in word_freq:
            # word in the dictionary, increase the frequency by 1
            word_freq[word] += 1
        else:
            # not there, so we add it with initial value o 1
            word_freq[word] = 1


print(word_freq)
frequencies = list(word_freq.values())
print(frequencies)
frequencies.sort(reverse=True)
top_frequencies = frequencies[1:10]
print(top_frequencies)

# match the words
for top_word in top_frequencies:
    for key in word_freq:

        if word_freq[key] == top_word:
            print(f"Word {key} appears {top_word} times")
            break


file.close()
