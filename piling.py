def can_stack_cubes(blocks):
    left = 0
    right = len(blocks) - 1
    top = float('inf')  # Initialize the top block size as infinity

    while left <= right:
        if blocks[left] > blocks[right]:
            current = blocks[left]
            left += 1
        else:
            current = blocks[right]
            right -= 1

        # If the current block is bigger than the top block, stacking is not possible
        if current > top:
            return "No"

        top = current  # Place the current block as the new top

    return "Yes"


# Main function to handle multiple test cases
def main():
    T = int(input())  # Number of test cases
    for _ in range(T):
        n = int(input())  # Number of cubes
        blocks = list(map(int, input().split()))  # Cube side lengths
        print(can_stack_cubes(blocks))


if __name__ == "__main__":
    main()
