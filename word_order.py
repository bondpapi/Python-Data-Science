# OrderedDict from Collection modules remembers order in which keys(words) are added.
from collections import OrderedDict


def word_occurences():
    # input contains integer n, tells how many words will follow
    n = int(input())

    # Initialize OrderedDict called word_count to store each word and number of occurences
    word_count = OrderedDict()

    """Loop read each word to count number of occurences"""
    for _ in range(n):
        # for each word, we use 'input().strip() to clean up any spaces.
        word = input().strip()

        # Checking if the word is already in word_count
        if word in word_count:
            word_count[word] += 1  # if it is we increase it's count by 1.
        else:
            word_count[word] = 1  # if it isn't we add the word and set count to 1.
    """Output the number of distinct words"""
    print(len(word_count))  # number of distinct words

    """Output the occurences of each word in order of appearance"""
    print(
        " ".join(map(str, word_count.values()))
    )  # occurences of words in the order they first appeared.


word_occurences()
