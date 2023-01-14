# КРЕСТИКИ - НОЛИКИ
def intro(score_):
    print('xo' * 37, '\n',
          'xo' * 5, '  Добро пожаловать в игру  КРЕСТИКИ - НОЛИКИ !!!  ', 'xo' * 5, '\n',
          'xo' * 36)
    print(f'         Счет:     x - {score_["x"]} : o - {score_["o"]}')


area = [['-'] * 3 for _ in range(3)]
player = 'o'
win_combinations = [[[0, 0], [0, 1], [0, 2]],
                    [[1, 0], [1, 1], [1, 2]],
                    [[2, 0], [2, 1], [2, 2]],
                    [[0, 0], [1, 0], [2, 0]],
                    [[0, 1], [1, 1], [2, 1]],
                    [[0, 2], [1, 2], [2, 2]],
                    [[0, 0], [1, 1], [2, 2]],
                    [[0, 2], [1, 1], [2, 0]]]
score = {'x': 0, 'o': 0}


def show_area():
    print('  0 1 2')
    for i in range(3):
        print(f'{i} {" ".join(area[i])}')


def decor_player_turn(fn):
    def wrapper():
        print(f'Ход игрока {player}')
        return fn()
    return wrapper


@decor_player_turn
def player_turn():
    print('Введите координаты: ', end='')
    while True:
        coordinates = input().split()
        if len(coordinates) != 2:
            print('Введите две координаты через пробел: ', end='')
            continue
        elif coordinates[0] not in '012' or coordinates[1] not in '012':
            print('Введите координаты от 0 до 2 включительно: ', end='')
            continue
        elif area[int(coordinates[0])][int(coordinates[1])] != '-':
            print('Повторение хода. Введите другие координаты: ', end='')
            continue
        else:
            break
    return list(int(i) for i in coordinates)


def check_win():
    result = False
    for combination in win_combinations:
        for i in combination:
            if area[i[0]][i[1]] != player:
                break
        else:
            result = True
            break
    return result


def turns():
    for i in area:
        for j in i:
            if j == '-':
                return True
    return False


def next_player():
    global player
    player = 'x' if player == 'o' else 'o'


def play_game():
    global player, area
    player = 'o'
    intro(score)
    show_area()
    while not check_win():
        next_player()
        coordinates = player_turn()
        area[coordinates[0]][coordinates[1]] = player
        show_area()
        if not turns():
            print(f'***   Ничья   *** \n         Счет:     x - {score["x"]} : o - {score["o"]}')
            break
    else:
        score[player] += 1
        print(f'*** Выиграл игрок {player} *** \n         Счет:     x - {score["x"]} : o - {score["o"]}')
    area = [['-'] * 3 for _ in range(3)]


play_game()
while True:
    again = input('Сыграть еще? (y/n) ')
    if again == 'y':
        play_game()
    elif again == 'n':
        print('*** До встречи! ***')
        break
