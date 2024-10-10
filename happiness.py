def happiness_score(n, m, array, A, B):
    """Function calculates happiness"""
    # n - the number of elements in the array
    # m - the number of elements in sets A and B
    # array - list of integers repping the array
    # A - list of integers repping set A
    # B - list of integers repping set B
    # happiness intialized at 0

    happiness = 0

    A = set(A)  # Convert A to set for quick lookup
    B = set(B)  # Convert B to set for quick lookup

    for i in array:
        if i in A:
            happiness += 1
        elif i in B:
            happiness -= 1
    return happiness


"""Input Reading"""
n, m = map(
    int, input().split()
)  # This reads the first line of input, which contains two integers: n (the number of elements in the array) and m (the number of elements in sets A and B
array = list(map(int, input().split()))  # Second Line: array of n integers
A = list(map(int, input().split()))  # Third line: set A of m integers
B = list(map(int, input().split()))  # Fourth line: set B of m integers


"""Output the final happiness score"""
print(happiness_score(n, m, array, A, B))
