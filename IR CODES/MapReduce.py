from collections import defaultdict

# Input dataset
data = """
Hello World!
This is an Information Retrieval assignment.
MapReduce counts alphabetic characters.
Hello Python!
"""

# ---------------- MAP PHASE ----------------

mapped_data = []

for character in data:

    if character.isalpha():

        character = character.lower()

        mapped_data.append((character, 1))


# ---------------- SHUFFLE AND SORT ----------------

grouped_data = defaultdict(list)

for character, count in mapped_data:

    grouped_data[character].append(count)


# ---------------- REDUCE PHASE ----------------

result = {}

for character, counts in grouped_data.items():

    result[character] = sum(counts)


# ---------------- OUTPUT ----------------

print("Character Occurrence Count")
print("---------------------------")

for character in sorted(result):

    print(character, ":", result[character])