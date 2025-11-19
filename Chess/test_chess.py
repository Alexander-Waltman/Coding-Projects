import chess

def test_pawn_valid_moves():
    board = chess.create_board()
    chess.board_setup(board)
    
    assert set(chess.pawn_valid_moves((0, 1), board)) == {(0, 2), (0,3)}, "Starting white pawn cannot move properly"
    assert set(chess.pawn_valid_moves((0, 6), board)) == {(0, 5), (0,4)}, "Starting black pawn cannot move properly"

    board[1][2] = "n"
    assert set(chess.pawn_valid_moves((0, 1), board)) == {(0, 2), (0,3), (1, 2)}, "Starting white pawn cannot take"

    board[1][5] = "N"
    assert set(chess.pawn_valid_moves((0, 6), board)) == {(0, 5), (0,4), (1, 5)}, "Starting black pawn cannot take"

def main():
    test_pawn_valid_moves()


if __name__ == "__main__":
    main()