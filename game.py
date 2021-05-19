from computer import Computer
from player import Player
import random


person_player = Player()
print('Enter second player name')
person_player2 = Player()
computer_player = Computer()


def play_game_single():
    while computer_player.win_count < 2 or person_player.win_count < 2:
        single_player()
        if computer_player.win_count == 2:
            print(f"{computer_player.name} won the best out of 3")
            break
        if person_player.win_count == 2:
            print(f"{person_player.name} won the best out of 3")
            break


def play_multi():
    while person_player2.win_count < 2 or person_player.win_count < 2:
        multi_player()
        if person_player2.win_count == 2:
            print(f"{person_player2.name} won!")
            break
        if person_player.win_count == 2:
            print(f"{person_player.name} won!")
            break


def rules():
    print(' *RULES*'
          'Rock crush Scissors'
          'Rock crushes Lizard'
          'Paper covers Rock'
          'Lizard poisons Spock'
          'Spock smashes Scissors'
          'Scissors decapitates Lizard'
          'Lizard eats Paper'
          'Paper disproves Spock'
          'Spock vaporizes Rock')


def game_option():
    game_alert = input('Multiplayer or single player? Enter 2 for multiplayer and 1 for single player.')
    while game_alert != '1' or game_alert != '2':

        if game_alert == '1':
            play_game_single()
            break

        elif game_alert == '2':
            play_multi()
            break
        else:
            print('Invalid, try again')
            game_alert = input('Multiplayer or single player? Enter 2 for multiplayer and 1 for single player.')

def single_player():
    computer_player.move = Player.choice[random.randint(0, 4)]
    person_player.move = input(f"{person_player.name} what would you like your move to be?")

    # Rock move
    if computer_player.move == Player.choice[0] and person_player.move == Player.choice[
        2] or computer_player.move == Player.choice[0] and person_player.move == Player.choice[3]:
        computer_player.win_count += 1
        print(f'{computer_player.name} wins this round')
    elif computer_player.move == Player.choice[0] and person_player.move == Player.choice[
        1] or computer_player.move == Player.choice[0] and person_player.move == Player.choice[4]:
        person_player.win_count += 1
        print(f'{person_player.name} wins this round.')
    elif computer_player.move == Player.choice[0] and person_player.move == Player.choice[0]:
        print(f'its a tie')

    # Paper
    elif computer_player.move == Player.choice[1] and person_player.move == Player.choice[
        0] or computer_player.move == Player.choice[1] and person_player.move == Player.choice[4]:
        computer_player.win_count += 1
        print(f'{computer_player.name} wins this round')
    elif computer_player.move == Player.choice[1] and person_player.move == Player.choice[
        3] or computer_player.move == Player.choice[1] and person_player.move == Player.choice[2]:
        person_player.win_count += 1
        print(f'{person_player.name} wins this round.')
    elif computer_player.move == Player.choice[1] and person_player.move == Player.choice[1]:
        print(f'its a tie')

    # Scissors
    elif computer_player.move == Player.choice[2] and person_player.move == Player.choice[
        1] or computer_player.move == Player.choice[2] and person_player.move == Player.choice[3]:
        computer_player.win_count += 1
        print(f'{computer_player.name} wins this round')
    elif computer_player.move == Player.choice[2] and person_player.move == Player.choice[
        4] or computer_player.move == Player.choice[2] and person_player.move == Player.choice[0]:
        person_player.win_count += 1
        print(f'{person_player.name} wins this round')
    elif computer_player.move == Player.choice[2] and person_player.move == Player.choice[2]:
        print(f'its a tie')

    # Lizard
    elif computer_player.move == Player.choice[3] and person_player.move == Player.choice[
        1] or computer_player.move == Player.choice[3] and person_player.move == Player.choice[4]:
        computer_player.win_count += 1
        print(f'{computer_player.name} wins this round')
    elif computer_player.move == Player.choice[3] and person_player.move == Player.choice[
        0] or computer_player.move == Player.choice[3] and person_player.move == Player.choice[2]:
        person_player.win_count += 1
        print(f'{person_player.name} wins this round.')
    elif computer_player.move == Player.choice[3] and person_player.move == Player.choice[3]:
        print(f'its a tie')

    # Spock
    elif computer_player.move == Player.choice[4] and person_player.move == Player.choice[
        0] or computer_player.move == Player.choice[4] and person_player.move == Player.choice[2]:
        computer_player.win_count += 1
        print(f'{computer_player.name} wins this round')
    elif computer_player.move == Player.choice[4] and person_player.move == Player.choice[
        1] or computer_player.move == Player.choice[4] and person_player.move == Player.choice[3]:
        person_player.win_count += 1
        print(f'{person_player.name} wins this round.')
    elif computer_player.move == Player.choice[4] and person_player.move == Player.choice[4]:
        print(f'its a tie')
    else:
        print('please choose a correct play')


def multi_player():