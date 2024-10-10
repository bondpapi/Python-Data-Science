from chess import coord_num_ltr, ltr_to_num, can_take


import unittest


class TestChessCaptureLogic(unittest.TestCase):

    def test_coord_num_ltr(self):
        # Test valid coordinates
        self.assertTrue(coord_num_ltr("a1"))
        self.assertTrue(coord_num_ltr("h8"))
        self.assertTrue(coord_num_ltr("d4"))

        # Test invalid coordinates
        self.assertFalse(coord_num_ltr("i9"))  # Invalid column
        self.assertFalse(coord_num_ltr("a9"))  # Invalid row
        self.assertFalse(coord_num_ltr("4d"))  # Invalid format
        self.assertFalse(coord_num_ltr("a11"))  # Invalid length

    def test_ltr_to_num(self):
        # Test converting coordinates
        self.assertEqual(ltr_to_num("a1"), [0, 0])  # Bottom-left corner
        self.assertEqual(ltr_to_num("h8"), [7, 7])  # Top-right corner
        self.assertEqual(ltr_to_num("c4"), [2, 3])  # Middle board

    def test_knight_can_take(self):
        # White knight at c4 (converted to [2, 3] in 0-based indexing)
        white_piece = "knight"
        white_coords = [2, 3]

        # Set up black pieces in various places
        black_pieces = [
            ((3, 1), "pawn"),  # d2 (can be taken by the knight)
            ((1, 4), "rook"),  # b5 (cannot be taken)
            ((4, 2), "knight"),  # e3 (can be taken by the knight)
            ((0, 4), "bishop"),  # a5 (can be taken by the knight)
            ((3, 5), "queen"),  # d6 (can be taken by the knight)
        ]

        # Call can_take and check if the correct pieces are returned
        can_take_pieces = can_take(white_piece, white_coords, black_pieces)

        # Expected output: knight can take pieces at d2, e3, a5, and d6
        expected_output = [
            ((3, 1), "pawn"),
            ((4, 2), "knight"),
            ((0, 4), "bishop"),
            ((3, 5), "queen"),
        ]
        self.assertCountEqual(can_take_pieces, expected_output)


def test_pawn_can_take(self):
    # White pawn at e4 (converted to [4, 3] in 0-based indexing)
    white_piece = "pawn"
    white_coords = [4, 3]

    # Set up black pieces
    black_pieces = [
        ((5, 4), "bishop"),  # f5 (can be taken by pawn)
        ((5, 2), "rook"),  # d5 (can be taken by pawn)
        ((6, 5), "queen"),  # g6 (cannot be taken)
    ]

    # Call can_take and check if the correct pieces are returned
    can_take_pieces = can_take(white_piece, white_coords, black_pieces)

    # Expected output: pawn can take pieces at f5 and d5
    expected_output = [((5, 4), "bishop"), ((5, 2), "rook")]
    self.assertCountEqual(can_take_pieces, expected_output)


if __name__ == "__main__":
    unittest.main()
