import re


"""Input Handling"""
# Reading number of rows and columns
R, C = map(int, input().split())

# Reading mtrix rows
matrix = [input() for _ in range(R)]

"""Reading Columns and Concatenating"""
decoded_string = "".join([matrix[row][col] for col in range(C) for row in range(R)])

""" Replaceing Non-Aplhanumeric characters with a single Space"""
decoded_string = re.sub(r"(?<=\w)[^a-zA-Z0-9]+(?=\w)", " ", decoded_string)

print(decoded_string)
