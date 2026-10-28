# Stop Word Removal

# Sample stop word list
stop_words = {
    "a", "an", "the", "is", "are", "was", "were",
    "in", "on", "at", "to", "of", "and", "or",
    "for", "with", "as", "by", "this", "that",
    "it", "from", "be", "has", "have", "had"
}

# Input text
text = input("Enter the text document: ")

# Convert text to lowercase
text = text.lower()

# Tokenize the text
words = text.split()

# Remove stop words
filtered_words = []

for word in words:
    if word not in stop_words:
        filtered_words.append(word)

# Display output
print("\nOriginal Text:")
print(text)

print("\nText after Stop Word Removal:")
print(" ".join(filtered_words))