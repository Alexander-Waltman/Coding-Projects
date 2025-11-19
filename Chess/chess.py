def create_board():
    """
    Creates a board list

    Returns:
    (type: list) - the empty board
    """
    out_board = []

    # outer loop to keep track of how many columns to make
    for i in range(8):
        col = []
        # inner loop to create the columns
        for j in range(8):
            col.append("")
        
        # apped column created in inner loop
        out_board.append(col)

    return out_board

def board_setup(board):
    # pawns
    for x in range(8):
        # white pawns
        board[x][1] = "P"

        # black pawns
        board[x][6] = "p"
    
    # white pieces
    y = 0

    # rooks
    board[0][y] = "R"
    board[7][y] = "R"

    # knights
    board[1][y] = "N"
    board[6][y] = "N"

    # bishops
    board[2][y] = "B"
    board[5][y] = "B"

    # royal couple
    board[3][y] = "Q"
    board[4][y] = "K"


    # black pieces
    y = 7

    # rooks
    board[0][y] = "r"
    board[7][y] = "r"

    # knights
    board[1][y] = "n"
    board[6][y] = "n"

    # bishops
    board[2][y] = "b"
    board[5][y] = "b"

    # royal couple
    board[3][y] = "k"
    board[4][y] = "q"

def row(row_num, board):
    """
    Returns a row of the chess board

    Parameters:
    row_num (type: int) - number row to return (0-indexed)

    Returns:
    (type: list) - list of tuples of that row
    """
    row = []
    for col in board:
        row.append(col[row_num])
    
    return row

def is_occupied(position, board):
    """
    Tells you if a square is occupied by a piece

    Parameters:
    position (type: tuple) - tuple of x, y position on board to check

    Returns:
    (type: boolean) - True if space is occupied, False if not occupied
    """

    x, y = position

    if board[x][y] == "":
        return False
    else:
        return True

def color_on_square(position, board):
    """
    Tells you the color of the piece on a square.

    Parameters:
    position (type: tuple) - tuple of x, y position to check

    Returns:
    None if square is empty
    (type: string) - "w" or "b" depending on color of piece
    """

    # empty square
    if not is_occupied(position, board):
        return None
    # occupied square
    else:
        x, y = position
        piece: str = board[x][y]
        if piece.isupper():
            return "w"
        else:
            return "b"

def piece_on_square(position, board):
    """
    Tells you the name of the piece on a square.

    Parameters:
    position (type: tuple) - tuple of x, y position to check

    Returns:
    None if square is empty
    (type: string) - letter of piece, always lowercase
    """

    # empty square
    if not is_occupied(position, board):
        return None
    # occupied square
    else:
        x, y = position
        name = board[x][y].lower()
        return name

def on_board(position):
    """
    Checks if a position is a valid spot on a chess board

    Parameters:
    position (type: tuple) - x, y coordinate pair for the board

    Returns:
    (type: bool) - True if valid spot, False if not
    """
    x, y = position

    return (0 <= x <= 7) and (type(x) == int) and (0 <= y <= 7) and (type(y) == int)

def enemy_color(color):
    """
    
    """

    if color == "w":
        return "b"
    elif color == "b":
        return "w"
    else:
        raise ValueError("enemy_color function was passed an incorrect character")

def pawn_valid_moves(current_pos, board):
    """
    Checks which sqares a pawn can move to.

    Parameters:
    current_pos (type: tuple) - tuple of x, y position of pawn

    Returns:
    (type: list) - list of tuples of x, y positions the pawn can move
    """
    # check there actually is a pawn
    if piece_on_square(current_pos, board) != "p":
        raise ValueError("there is not a pawn on the position input to the pawn_valid_moves function")
    

    x, y = current_pos
    valid_moves = []

    # white pawns
    if color_on_square(current_pos, board) == "w":
        # square right in front of it
        if not is_occupied((x, y + 1), board):
                valid_moves.append((x, y+1))
            
        # if pawn hasn't moved yet
        if (current_pos[1] == 1) and (not is_occupied((x, y + 2), board)):
            valid_moves.append((x, y+2))
        
        # captures
        if (is_occupied((x + 1, y + 1), board)) and (color_on_square((x + 1, y + 1), board) == "b"):
            valid_moves.append((x+1, y+1))
        if (is_occupied((x - 1, y + 1), board)) and (color_on_square((x - 1, y + 1), board) == "b"):
            valid_moves.append((x-1, y+1))

    
    # black pawns
    if color_on_square(current_pos, board) == "b":
        # square right in front of it
        if not is_occupied((x, y - 1), board):
                valid_moves.append((x, y-1))
            
        # if pawn hasn't moved yet
        if (current_pos[1] == 6) and (not is_occupied((x, y - 2), board)):
            valid_moves.append((x, y-2))
        
        # captures
        if (is_occupied((x + 1, y - 1), board)) and (color_on_square((x + 1, y - 1), board) == "w"):
            valid_moves.append((x+1, y-1))
        if (is_occupied((x - 1, y - 1), board)) and (color_on_square((x - 1, y - 1), board) == "w"):
            valid_moves.append((x-1, y-1))
    
    # remove positions that aren't actually on the board
    for pair in valid_moves:
        if not on_board(pair):
            valid_moves.remove(pair)

    return valid_moves

def rook_valid_moves(current_pos, board):
    """
    
    """

    # check there actually is a rook
    if piece_on_square(current_pos, board) != "r":
        raise ValueError("there is not a rook on the position input to the rook_valid_moves function")
    

    x, y = current_pos
    valid_moves = []
    this_color = color_on_square(current_pos, board)
    enemy_color = enemy_color(this_color)
    
    # TODO: add taking for all other directions than up

    # up
    move_y = y + 1
    enemy_found = color_on_square((x, move_y), board) == enemy_color
    while (move_y <= 7) and ((not is_occupied(x, move_y), board) or (enemy_found)):
        valid_moves.append(move_x, y)

        move_y += 1
        enemy_found = color_on_square((x, move_y), board) == enemy_color
        if enemy_found:
            break

    # down
    move_y = y - 1
    while (move_y >= 0) and (not is_occupied(x, move_y), board):
        valid_moves.append(move_x, y)
        move_y -= 1
    
    # left
    move_x = x - 1
    while (move_x >= 0) and (not is_occupied(move_x, y), board):
        valid_moves.append(move_x, y)
        move_x -= 1
    
    # right
    move_x = x + 1
    while (move_x <= 7) and (not is_occupied(move_x, y), board):
        valid_moves.append(move_x, y)
        move_x += 1
    
    # remove positions that aren't actually on the board
    for pair in valid_moves:
        if not on_board(pair):
            valid_moves.remove(pair)

def knight_valid_moves(current_pos, board):
    """
    
    """
    x, y = current_pos
    valid_moves = []

    # check there actually is a knight
    if piece_on_square(current_pos, board) != "n":
        raise ValueError("there is not a knight on the position input to the knight_valid_moves function")
    
    # top right moves
    

    # TODO: implement this function
    


def main():
    board = create_board()
    board_setup(board)
    print(pawn_valid_moves((0, 1), board))


if __name__ == "__main__":
    main()