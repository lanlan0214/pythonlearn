# 初始化五子棋盤
board_size = 19
board = [[' ' for _ in range(board_size)] for _ in range(board_size)]

# 函數：顯示當前五子棋盤狀態
def display_board():
    for row in board:
        print(' '.join(row))
    print()

# 函數：檢查是否有玩家獲勝
def check_winner(row, col, player_symbol):
    # 檢查水平、垂直和兩個對角線方向
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    for dr, dc in directions:
        count = 0
        for i in range(-4, 5):
            r, c = row + i * dr, col + i * dc
            if 0 <= r < board_size and 0 <= c < board_size and board[r][c] == player_symbol:
                count += 1
                if count == 5:
                    return True
            else:
                count = 0
    return False

# 函數：判斷是否平局
def check_draw():
    return all(board[i][j] != ' ' for i in range(board_size) for j in range(board_size))

# 函數：主遊戲循環
def play_game():
    player_symbols = ['X', 'O']
    current_player = 0

    while True:
        display_board()
        print(f"Player {current_player + 1}'s turn")

        # 獲取玩家輸入的位置
        while True:
            try:
                row = int(input("Enter row (0-14): "))
                col = int(input("Enter column (0-14): "))
                if 0 <= row < board_size and 0 <= col < board_size and board[row][col] == ' ':
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # 下棋
        board[row][col] = player_symbols[current_player]

        # 檢查是否有玩家獲勝
        if check_winner(row, col, player_symbols[current_player]):
            display_board()
            print(f"Player {current_player + 1} wins!")
            break

        # 檢查是否平局
        if check_draw():
            display_board()
            print("It's a draw!")
            break

        # 切換到下一位玩家
        current_player = 1 - current_player

# 啟動五子棋遊戲
play_game()
