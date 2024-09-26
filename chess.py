pieces = ["king", "queen", "rook", "pawn", "bishop", "knight"]


def coord_num_ltr(coords):
    """Check if coordinates are valid in chess notation."""
    if len(coords) != 2:
        return False
    coord_ltrs = [chr(i) for i in range(ord("a"), ord("h") + 1)]
    coord_num = range(1, 9)
    ltr = coords[0]
    try:
        n = int(coords[1])
    except ValueError:
        return False
    return ltr in coord_ltrs and n in coord_num


def ltr_to_num(coords):
    """Convert letter-based coordinates to numerical format."""
    coord_ltrs = [chr(i) for i in range(ord("a"), ord("h") + 1)]
    return [coord_ltrs.index(coords[0]), int(coords[1]) - 1]  # Adjust for 0-based index


def get_white_piece_and_coords():
    while True:
        try:
            piece_and_coords = input(
                "Enter White Piece (pawn or knight) and Coordinates: "
            ).lower()
            white_piece, white_coords = piece_and_coords.split(" ")
            if white_piece not in ["pawn", "knight"] or not coord_num_ltr(white_coords):
                print(
                    "Invalid input. Please enter a piece (pawn or knight) and coordinates (e.g., pawn b3)."
                )
                continue
            white_coords = ltr_to_num(white_coords)
            return white_piece, white_coords
        except ValueError:
            print(
                "Invalid input. Please enter a piece (pawn or knight) and coordinates (e.g., pawn b3)."
            )


def get_black_pieces_and_coords():
    black_pieces = []
    while True:
        piece_and_coords = input(
            "Now Enter Black Piece and Coordinates (or 'done' to finish): "
        ).lower()
        if piece_and_coords == "done":
            break
        try:
            black_piece, black_coords = piece_and_coords.split()
            if black_piece not in pieces:
                raise ValueError(
                    "Invalid piece. Please enter one of 'pawn', 'rook', 'knight', 'bishop', 'queen', or 'king'."
                )
            if not coord_num_ltr(black_coords):
                print(
                    "Invalid coordinates. Please enter coordinates in the format 'a1', 'd4', 'b2', etc."
                )
                continue
            black_coords_num = ltr_to_num(black_coords)
            if tuple(black_coords_num) in [tuple(coord) for coord, _ in black_pieces]:
                raise ValueError(
                    "A piece already occupies that coordinate, try a different coordinate."
                )

            black_pieces.append((tuple(black_coords_num), black_piece))
            print("Black Piece added successfully.")
        except ValueError as ve:
            print(ve)
    return black_pieces


def can_take(white_piece, white_coords, black_pieces):
    potential_takes = []

    if white_piece == "pawn":
        potential_takes = [
            (white_coords[0] + 1, white_coords[1] + 1),  # captures right diagonal
            (white_coords[0] - 1, white_coords[1] + 1),  # captures left diagonal
        ]
    elif white_piece == "knight":
        potential_takes = [
            (white_coords[0] + 2, white_coords[1] + 1),
            (white_coords[0] + 2, white_coords[1] - 1),
            (white_coords[0] - 2, white_coords[1] + 1),
            (white_coords[0] - 2, white_coords[1] - 1),
            (white_coords[0] + 1, white_coords[1] + 2),
            (white_coords[0] + 1, white_coords[1] - 2),
            (white_coords[0] - 1, white_coords[1] + 2),
            (white_coords[0] - 1, white_coords[1] - 2),
        ]

    # Convert potential_takes and black piece coordinates to tuples for consistent comparison
    potential_takes = [tuple(move) for move in potential_takes]

    # Find black pieces that can be taken
    can_take_pieces = [(tuple(bc), bp) for (bc, bp) in black_pieces if tuple(bc) in potential_takes]

    return can_take_pieces



def main():
    white_piece, white_coords = get_white_piece_and_coords()

    black_pieces = get_black_pieces_and_coords()

    can_take_pieces = can_take(white_piece, white_coords, black_pieces)

    if can_take_pieces:
        print("The white piece can take the following black pieces:")
        for black_coords, black_piece in can_take_pieces:
            chess_notation = f"{chr(black_coords[0] + ord('a'))}{black_coords[1] + 1}"
            print(f"{black_piece} at {chess_notation}")
    else:
        print("The white piece cannot take any black pieces.")


if __name__ == "__main__":
    main()
