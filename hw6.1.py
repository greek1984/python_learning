def fill_gamefield(gamefield):

    for i in range(3):
        print(gamefield[0 + i * 3], gamefield[1 + i * 3], gamefield[2 + i * 3])

def take_input(player_key):
    valid = False
    while not valid:
        player_answer = input("Сделайте ход " + player_key + ": ")
        try:
            player_answer = int(player_answer)
        except:
            print("Неверный ход. Вы вводите число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(pole[player_answer - 1]) not in "XO"):
                pole[player_answer - 1] = player_key
                valid = True
            else:
                print("Сюда уже ходили! Сделайте другой ход")
        else:
            print("Неверный ход. Выберите число от 1 до 9")

def check_win(gamefield):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if gamefield[each[0]] == gamefield[each[1]] == gamefield[each[2]]:
            return gamefield[each[0]]
    return False

def main(gamefield):
    counter = 0
    win = False
    while not win:
        fill_gamefield(gamefield)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(gamefield)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    fill_gamefield(gamefield)

pole = list(range(1, 10))
main(pole)