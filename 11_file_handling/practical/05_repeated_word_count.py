# Task:
# Write a function to find how many times a word appears in a file.
# File name: count.txt


def get_my_word(file_name, word):
  with open(file_name, 'r') as file:
    # data = file.read().split()
    data = file.read().lower().split()
    # count_my_word = data.count(word)
    count_my_word = data.count(word.lower())
    return count_my_word

print(get_my_word("count.txt", "think"))
print(get_my_word("count.txt", "different."))
print(get_my_word("count.txt", "Think"))













# split() -> breaks the string into individual words
# and returns them as a list.
#
# Example:
# "Think different. Think big."
#       ↓ split()
# ["Think", "different.", "Think", "big."]



# count(word) -> counts how many times the given
# word occurs in the list.
#
# Example:
# ["Think", "different.", "Think"].count("Think")
#                         ↓
#                         2
