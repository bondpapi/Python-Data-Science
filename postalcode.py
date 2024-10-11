regex_integer_in_range = r"^[1-9][0-9]{5}$"
# Regex checks if postal code is a 6-digit number btn 100000 and 999999

regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"
# Regex detects alternating repetitive digit pairs

import re

P = input()

print(
    bool(re.match(regex_integer_in_range, P)) #Returns true if input P matches regex
    and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2 # finds all instances of alternating repetitive digit pairs in P
)
