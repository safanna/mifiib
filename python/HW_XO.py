def draw_board(board):
    """
    Отрисовка текущего игрового поля
    :param board: словарь c текущими значениями для клеток поля (dict)
    """
    print(" " * 4, " ".join([f" {i} " for i in range(3)]), " ")
    print(" " * 3, "-" * 13)
    for i in range(3):
        print(f" {i} ", "|", board[(i, 0)], "|", board[(i, 1)], "|", board[(i, 2)], "|")
        print(" " * 3, "-" * 13)


def win_combination():
    """
    Список выигрышных комбинаций
    """
    # диагонали
    win_coordinates = [((0, 0), (1, 1), (2, 2)),
                       ((0, 2), (1, 1), (2, 0))]
    # строки и столбцы
    for i in range(3):
        win_coordinates.extend([((i, 0), (i, 1), (i, 2)),
                                ((0, i), (1, i), (2, i))])
    return win_coordinates


def check_win_combination(win_coords, board):
    """
    Проверка выигрышных комбинаций
    :param win_coords: список выигрышных комбинаций  (list)
    :param board: текущее состояние игрового поля  (dict)
    :return: индикация есть ли выигрышная комбинация на текущем поле
    """
    for coord in win_coords:
        if len({board[coord[0]], board[coord[1]], board[coord[2]]}) == 1 \
                and board[coord[0]] in 'XO':
            return board[coord[0]]
    return False


def take_input(player_token, board):
    """
    Ход игрока
    :param player_token: токен игрока (X или O) (char)
    :param board: текущее состояние игрового поля (dict)
    :return board: новое состояние игрового поля (dict)
    """
    valid = False
    while not valid:
        player_answer = input(f"Ход игрока {player_token}. Введите строку и столбец через пробел:")
        try:
            row, col = player_answer.strip().split()
            row = int(row)
            col = int(col)
        except:
            print("Некорректный ввод. Вы уверены, что ввели строку и столбец корректно?")
            continue
        if 0 <= row <= 2 and 0 <= col <= 2:
            if str(board[(row, col)]) not in "XO":
                board[(row, col)] = player_token
                valid = True
            else:
                print("Эта клетка уже занята")
        else:
            print("Некорректный ввод. Строка и столбец между 0 и 2.")
    return board


if __name__ == "__main__":
    player = dict(enumerate('XO'))
    current_board = {(i // 3, i % 3): "-" for i in range(9)}
    counter, win = 0, 0
    win_coords = win_combination()
    while not win:
        draw_board(current_board)
        current_board = take_input(player[counter % 2], current_board)
        counter += 1
        if counter > 4:
            win = check_win_combination(win_coords, current_board)
            if win:
                print(f"Игрок {win} выиграл!")
                break
        if counter > 8:
            print("Ничья!")
            break
    draw_board(current_board)
