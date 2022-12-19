import random

def run():
    user_name = input('Cual es tu nombre: ')

    def check_ruler(user_option, computer_option, user_wins, computer_wins):
        if user_option == computer_option:
            print('Empate!')
        elif user_option == 'piedra':
            if computer_option == 'tijera':
                print('Ganaste!!!')
                user_wins +=1
            else:
                print('Perdiste :(')
                computer_wins += 1
        elif user_option == 'papel':
            if computer_option == 'piedra':
                print('Ganaste!!!')
                user_wins +=1
            else:
                print('perdiste :(')
                computer_wins += 1
        elif user_option == 'tijera':
            if computer_option == 'papel':
                print('Ganaste!!!')
                user_wins +=1
            else:
                print('perdiste :(')
                computer_wins += 1
        print(f'{user_name} wins: ', user_wins)
        print('Compueter wins: ', computer_wins)

        return user_wins, computer_wins

    def choose_options():
        opciones = ('piedra', 'papel', 'tijera')
        user_option = input(f'{user_name} elige una opcion piedra, papel, tijera: ')
        user_option = user_option.lower()
        computer_option = random.choice(opciones)

        if not user_option in opciones:
            print('Elige una opcion valida')
            exit()

        print(f'{user_name}: ', user_option)
        print('Computadora: ',computer_option)
        return user_option, computer_option

    def run_game():
        computer_wins = 0
        user_wins = 0
        rounds = 1
        while True:
            print('*'*50)
            print('Round ', rounds)
            print('*'*50)
            rounds += 1

            user_option, computer_option = choose_options()
            user_wins, computer_wins = check_ruler(user_option, computer_option, user_wins, computer_wins)
            end_game(user_wins, computer_wins)

    def end_game(user_wins, computer_wins):   
        if computer_wins == 3:
            print('La Computadora gana')
            exit()
        elif user_wins == 3:
            print(f'{user_name} gana')
            exit()
    
    run_game()


if __name__ == '__main__':
    run()