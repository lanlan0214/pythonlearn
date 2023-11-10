# 初始化全局計數器，追踪遊戲回合次數
counter = 0

# 初始化遊戲棋盤的三行，每行有三個空格表示的位置
row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']  # 4, 5, 6 => row2 index 0, 1, 2
row3 = [' ', ' ', ' ']  # 7, 8, 9

# 函數：顯示當前遊戲棋盤狀態
def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

# 函數：獲取玩家輸入的位置（1-9）
def user_choice():
    choice = input("Please enter a number (1-9): ")
    while not choice.isdigit() or (int(choice) not in range(1, 10)):
        if not choice.isdigit():
            print("Sorry, your choice is not valid")
        else:
            print("Your choice is not within the range of 1 - 9.")
        choice = input("Please enter a number (1-9): ")
    return int(choice)

# 函數：獲取當前玩家的符號（'X' 或 'O'）
def getCurrentSymbol():
    global counter
    symbol_list = ['X', 'O']
    counter += 1
    return symbol_list[counter % 2]

# 函數：更新遊戲棋盤的指定位置
def update_table(index):
    global row1, row2, row3
    if index in range(1, 4):
        if row1[index - 1] == ' ':
            row1[index - 1] = getCurrentSymbol()
            return True
        else:
            return False
    elif index in range(4, 7):
        if row2[index % 3 - 1] == ' ':
            row2[index % 3 - 1] = getCurrentSymbol()
            return True
        else:
            return False
    else:
        if row3[index % 3 - 1] == ' ':
            row3[index % 3 - 1] = getCurrentSymbol()
            return True
        else:
            return False

# 函數：檢查是否有玩家獲勝，並返回結果
def check_winning():
    player_1_wins = False
    player_2_wins = False
    # 檢查每行是否有相同符號且不為空格，表示某位玩家獲勝
    if (row1[0] == row1[1] and row1[1] == row1[2] and (" " not in row1)):
        if (row1[0] == "X"):
            player_2_wins = True
        else:
            player_1_wins = True
    elif (row2[0] == row2[1] and row2[1] == row2[2] and (" " not in row2)):
        if (row2[0] == "X"):
            player_2_wins = True
        elif (row2[0] == "O"):
            player_1_wins = True
    elif (row3[0] == row3[1] and row3[1] == row3[2] and (" " not in row3)):
        if (row3[0] == "X"):
            player_2_wins = True
        elif (row3[0] == "O"):
            player_1_wins = True
    elif (row1[0] == row2[0] and row2[0] == row3[0] and (row1[0] != " " and row2[0] != " " and row3[0] != " ")):
        if (row1[0] == "X"):
            player_2_wins = True
        elif (row1[0] == "O"):
            player_1_wins = True
    elif (row1[1] == row2[1] and row2[1] == row3[1] and (row1[1] != " " and row2[1] != " " and row3[1] != " ")):
        if (row1[1] == "X"):
            player_2_wins = True
        elif (row1[1] == "O"):
            player_1_wins = True
    elif (row1[2] == row2[2] and row2[2] == row3[2] and (row1[2] != " " and row2[2] != " " and row3[2] != " ")):
        if (row1[2] == "X"):
            player_2_wins = True
        elif (row1[2] == "O"):
            player_1_wins = True
    elif (row1[0] == row2[1] and row2[1] == row3[2] and (row1[0] != " " and row2[1] != " " and row3[2] != " ")):
        if (row1[0] == "X"):
            player_2_wins = True
        elif (row1[0] == "O"):
            player_1_wins = True
    elif (row1[2] == row2[1] and row2[1] == row3[0] and (row1[2] != " " and row2[1] != " " and row3[0] != " ")):
        if (row1[2] == "X"):
            player_2_wins = True
        elif (row1[2] == "O"):
            player_1_wins = True

    if player_1_wins:
        return "player 1 wins"
    elif player_2_wins:
        return "player 2 wins"
    else:
        return "no one wins"

# 函數：遊戲主循環
def start_game():
    while True:
        display(row1, row2, row3)
        # 玩家選擇位置，並更新遊戲棋盤
        while True:
            choice = user_choice()
            if update_table(choice):
                break
            else:
                print("Wrong position to put your choice")
                
        # 檢查是否有玩家獲勝或平局
        result = check_winning()
        if result == "player 1 wins":
            display(row1, row2, row3)
            print("Player 1 wins!! Congrats")
            return
        elif result == "player 2 wins":
            display(row1, row2, row3)
            print("Player 2 wins!! Congrats")
            return
        elif result == "no one wins" and counter == 9:
            display(row1, row2, row3)
            print("Tie game!!")
            return

# 啟動遊戲
start_game()
