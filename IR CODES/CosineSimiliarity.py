import re
import math
from collections import Counter

# Function to preprocess document
def preprocess(text):

    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)

    return text.split()


# Function to calculate cosine similarity
def cosine_similarity(doc1, doc2):

    words1 = preprocess(doc1)
    words2 = preprocess(doc2)

    # Count word frequencies
    freq1 = Counter(words1)
    freq2 = Counter(words2)

    # Create vocabulary
    vocabulary = set(freq1.keys()).union(freq2.keys())

    # Calculate dot product
    dot_product = 0

    for word in vocabulary:
        dot_product += freq1[word] * freq2[word]

    # Calculate magnitudes
    magnitude1 = math.sqrt(
        sum(freq1[word] ** 2 for word in vocabulary)
    )

    magnitude2 = math.sqrt(
        sum(freq2[word] ** 2 for word in vocabulary)
    )

    # Avoid division by zero
    if magnitude1 == 0 or magnitude2 == 0:
        return 0

    similarity = dot_product / (magnitude1 * magnitude2)

    return similarity


# Main program
doc1 = input("Enter first document: ")
doc2 = input("Enter second document: ")

similarity = cosine_similarity(doc1, doc2)

print("\nCosine Similarity =", round(similarity, 4))
print("Similarity Percentage =", round(similarity * 100, 2), "%")