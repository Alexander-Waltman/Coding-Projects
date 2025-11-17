spaces = {
    "a1":(), "a2":(), "a3":(), "a4":(), "a5":(), "a6":(), "a7":(), "a8":(),
    "b1":(), "b2":(), "b3":(), "b4":(), "b5":(), "b6":(), "b7":(), "b8":(),
    "c1":(), "c2":(), "c3":(), "c4":(), "c5":(), "c6":(), "c7":(), "c8":(),
    "d1":(), "d2":(), "d3":(), "d4":(), "d5":(), "d6":(), "d7":(), "d8":(),
    "e1":(), "e2":(), "e3":(), "e4":(), "e5":(), "e6":(), "e7":(), "e8":(),
    "f1":(), "f2":(), "f3":(), "f4":(), "f5":(), "f6":(), "f7":(), "f8":(),
    "g1":(), "g2":(), "g3":(), "g4":(), "g5":(), "g6":(), "g7":(), "g8":(),
    "h1":(), "h2":(), "h3":(), "h4":(), "h5":(), "h6":(), "h7":(), "h8":()
}

col_list = ["a", "b", "c", "d", "e", "f", "g", "h"]

def right_column(current_col):
    """
    Returns the column name that's to the right of the inputted one.
    Returns 0 if there is not one.

    Parameters:
    current_col (type: str) - name of the column the piece is currently in

    Returns:
    (type: str) - name of the column to the right
    (type: int) - 0 if no column is to the right
    """
    # TODO: implement function

def board_setup(board):
    # set up pawns
    for col in col_list:
        # white pawns
        code = f"board[\"{col}2\"] = (\"pawn\", \"w\")"
        exec(code)

        # black pawns
        code = f"board[\"{col}7\"] = (\"pawn\", \"b\")"
        exec(code)
    
    # rooks
    for col in ["a", "h"]:
        code = f"board"


board_setup(spaces)
print(spaces)