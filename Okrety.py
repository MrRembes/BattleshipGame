import os
game_field=[[' 0', ' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9'],
            ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19'],
            ['20', '21', '22', '23', '24', '25', '26', '27', '28', '29'],
            ['30', '31', '32', '33', '34', '35', '36', '37', '38', '39'],
            ['40', '41', '42', '43', '44', '45', '46', '47', '48', '49'],
            ['50', '51', '52', '53', '54', '55', '56', '57', '58', '59'],
            ['60', '61', '62', '63', '64', '65', '66', '67', '68', '69'],
            ['70', '71', '72', '73', '74', '75', '76', '77', '78', '79'],
            ['80', '81', '82', '83', '84', '85', '86', '87', '88', '89'],
            ['90', '91', '92', '93', '94', '95', '96', '97', '98', '99']]
class Okrety_gra:
    def Graj(self):
        os.system('cls')
        player1 = Okrety_int
        player1.ustawienie(player1)
        
        player2 = Okrety_int
        player2.ustawienie(player2)


class Okrety_int:
    def __init__(self):
        self.game_field = game_field
                
    def print_line(self):
        print('-------------------------------')

    # Wypisanie Planszy gry
    def print_game(self):
        for i in range(10):
            self.print_line(self)
            for j in range(10):
                print('|'+self.game_field[i][j], end='')
                if(j == 9):
                    print('|')


    # Ustawienie początkowe zawodnika
    def ustawienie(self):
        n_ones = 4
        n_twos = 3
        n_threes = 2
        n_fours = 1
        n_places_ships = 0
        while(True):

            # Wybór statku
            print()
            print("Wybierz statek do Ustawienia:")
            print("1. Wielkość 1. (", n_ones,")")
            print("2. Wielkość 2. (", n_twos,")")
            print("3. Wielkość 3. (", n_threes,")")
            print("4. Wielkość 4. (", n_fours,")")
            ship_size = int(input("Wybrana liczba: "))

            # Walidacja wielkości statków
            if(ship_size < 1 or ship_size > 4):
                print("Niepoprawna wartość podaj poprawną liczbę!")
                continue

            # Walidacja ilości statków
            err = False
            match ship_size:
                case 1:
                    if(n_ones > 0):
                        n_ones -= 1
                    else:
                        err = True
                        print("Masz już Wykorzystane wszystkie pojedyncze statki!")
                case 2:
                    if(n_twos > 0):
                        n_twos -= 1
                    else:
                        err = True
                        print("Masz już Wykorzystane wszystkie podwójne statki!")
                case 3:
                    if(n_threes > 0):
                        n_threes -= 1
                    else:
                        err = True
                        print("Masz już Wykorzystane wszystkie potrójne statki!")
                case 4:
                    if(n_fours > 0):
                        n_fours -= 1
                    else:
                        err = True
                        print("Masz już Wykorzystane wszystkie poczwórne statki!")
                
            if(err):
                continue

            # Ustawienie statku 
            b_vertical = False
            if(ship_size != 1):
                print()
                print("Jak chcesz ustawić statek?")
                b_vertical = int(input("Pionowo(1) / Poziomo(0): ")) != 0

            # Wyświetlenie pola gry
            self.print_game(self)

            # Wybranie Położenia statku
            while(True): 
                u_point = int(input("Wybierz punkt startowy: "))
                n_unity = u_point%10
                n_dozens = int(u_point/10)

                if(u_point < 0 or u_point > 99):
                    print("Niepoprawna wartość. Wartość musi być od 0 do 99")
                    continue

                if(not b_vertical and n_unity  + ship_size > 10):
                    print("Statek jest zbyt blisko krawędzi poziom")
                    continue

                if(b_vertical and n_dozens + ship_size > 10):
                    print("Statek jest zbyt blisko krawędzi pion")
                    continue

                # Blokada przed wstawieniem statku w zajęte miejsce
                if(self.game_field[n_dozens][n_unity] == ' x' or self.game_field[n_dozens][n_unity] == ' .'):
                    print("Podane Pole jest zajęte!")
                    continue
                # Sprawdzanie czy statki nie wejdą na inny statek lub nie będą siąsiednio do niego
                if(ship_size != 1):
                    if(b_vertical):
                        if(ship_size == 2):
                            if(self.game_field[n_dozens+1][n_unity] == ' x' or self.game_field[n_dozens+1][n_unity] == ' .'):
                                print("Statek nie zmieści się na tym polu!")
                                continue
                        if(ship_size == 3):
                            if(self.game_field[n_dozens+2][n_unity] == ' x' or self.game_field[n_dozens+2][n_unity] == ' .'):
                                print("Statek nie zmieści się na tym polu!")
                                continue
                        if(ship_size == 4):
                            if(self.game_field[n_dozens+3][n_unity] == ' x' or self.game_field[n_dozens+3][n_unity] == ' .'):
                                print("Statek nie zmieści się na tym polu!")
                                continue
                    else:
                        if(ship_size == 2):
                            if(self.game_field[n_dozens][n_unity+1] == ' x' or self.game_field[n_dozens][n_unity+1] == ' .'):
                                print("Statek nie zmieści się na tym polu!")
                                continue
                        if(ship_size == 3):
                            if(self.game_field[n_dozens][n_unity+2] == ' x' or self.game_field[n_dozens][n_unity+2] == ' .'):
                                print("Statek nie zmieści się na tym polu!")
                                continue
                        if(ship_size == 4):
                            if(self.game_field[n_dozens][n_unity+3] == ' x' or self.game_field[n_dozens][n_unity+3] == ' .'):
                                print("Statek nie zmieści się na tym polu!")
                                continue
                
                 # Ustawienie statku i blokowanie miejsc obok statków dla kolejnych statków
                match ship_size:
                    # Dla statku o wielkości 1
                    case 1:          
                        self.game_field[n_dozens][n_unity] = ' x'
                                #prawo
                        if(n_unity < 9):
                            self.game_field[n_dozens][n_unity+1] = ' .'
                                #lewo
                        if(n_unity > 0):
                            self.game_field[n_dozens][n_unity-1] = ' .'
                                #gora
                        if(n_dozens > 0):
                            self.game_field[n_dozens-1][n_unity] = ' .'
                                #lewo gora
                        if(n_unity > 0 and n_dozens > 0):
                            self.game_field[n_dozens-1][n_unity-1] = ' .'
                                #prawo gora
                        if(n_unity < 9 and n_dozens > 0):
                            self.game_field[n_dozens-1][n_unity+1] = ' .'
                                #dol
                        if(n_dozens < 9):
                            self.game_field[n_dozens+1][n_unity] = ' .'
                                #lewo dol
                        if(n_unity > 0 and n_dozens < 9):
                            self.game_field[n_dozens+1][n_unity-1] = ' .'
                                #prawo dol
                        if(n_unity < 9 and n_dozens < 9):
                            self.game_field[n_dozens+1][n_unity+1] = ' .'

                    #Dla Statku o wielkości 2
                    case 2:
                            # pionowo
                        if(b_vertical): 
                            self.game_field[n_dozens][n_unity] = ' x'
                            self.game_field[n_dozens+1][n_unity] = ' x'
                                    #prawo
                            if(n_unity < 9):
                                self.game_field[n_dozens][n_unity+1] = ' .'
                                self.game_field[n_dozens+1][n_unity+1] = ' .'
                                    #lewo
                            if(n_unity > 0):
                                self.game_field[n_dozens][n_unity-1] = ' .'
                                self.game_field[n_dozens+1][n_unity-1] = ' .'                            
                                    #gora
                            if(n_dozens > 0):
                                self.game_field[n_dozens-1][n_unity] = ' .'
                                    #lewo gora
                            if(n_unity > 0 and n_dozens > 0):
                                self.game_field[n_dozens-1][n_unity-1] = ' .'
                                    #prawo gora
                            if(n_unity < 9 and n_dozens > 0):
                                self.game_field[n_dozens-1][n_unity+1] = ' .'
                                    #dol
                            if(n_dozens + ship_size-1 < 9):
                                self.game_field[n_dozens + ship_size][n_unity] = ' .'
                                #lewo dol
                            if(n_unity > 0 and n_dozens + ship_size-1 < 9):
                                self.game_field[n_dozens + ship_size][n_unity-1] = ' .'
                                    #prawo dol
                            if(n_unity < 9 and n_dozens + ship_size-1 < 9):
                                self.game_field[n_dozens + ship_size][n_unity+1] = ' .'

                        else:   #poziomo
                            self.game_field[n_dozens][n_unity] = ' x'
                            self.game_field[n_dozens][n_unity+1] = ' x'
                                    #prawo
                            if(n_unity + ship_size-1 < 9):
                                self.game_field[n_dozens][n_unity + ship_size] = ' .'
                                    #lewo
                            if(n_unity > 0):
                                self.game_field[n_dozens][n_unity-1] = ' .'                         
                                    #gora
                            if(n_dozens > 0):
                                self.game_field[n_dozens-1][n_unity] = ' .'
                                self.game_field[n_dozens-1][n_unity+1] = ' .'
                                    #lewo gora
                            if(n_unity > 0 and n_dozens > 0):
                                self.game_field[n_dozens-1][n_unity-1] = ' .'
                                    #prawo gora
                            if(n_unity + ship_size-1 < 9 and n_dozens > 0):
                                self.game_field[n_dozens-1][n_unity + ship_size] = ' .'
                                    #dol
                            if(n_dozens < 9):
                                self.game_field[n_dozens+1][n_unity] = ' .'
                                self.game_field[n_dozens+1][n_unity+1] = ' .'
                                #lewo dol
                            if(n_unity > 0 and n_dozens + 1 < 9):
                                self.game_field[n_dozens+1][n_unity-1] = ' .'
                                    #prawo dol
                            if(n_unity + ship_size-1 < 9 and n_dozens + ship_size-1 < 9):
                                self.game_field[n_dozens + 1][n_unity + ship_size] = ' .'
                    #Dla Statku o wielkości 3
                    case 3:
                            # pionowo
                        if(b_vertical): 
                            self.game_field[n_dozens][n_unity] = ' x'
                            self.game_field[n_dozens + 1][n_unity] = ' x'
                            self.game_field[n_dozens + 2][n_unity] = ' x'
                                    #prawo
                            if(n_unity < 9):
                                self.game_field[n_dozens][n_unity+1] = ' .'
                                self.game_field[n_dozens+1][n_unity+1] = ' .'
                                self.game_field[n_dozens+2][n_unity+1] = ' .'
                                    #lewo
                            if(n_unity > 0):
                                self.game_field[n_dozens][n_unity-1] = ' .'
                                self.game_field[n_dozens+1][n_unity-1] = ' .'
                                self.game_field[n_dozens+2][n_unity-1] = ' .'
                                    #gora
                            if(n_dozens > 0):
                                self.game_field[n_dozens-1][n_unity] = ' .'
                                    #lewo gora
                            if(n_unity > 0 and n_dozens > 0):
                                self.game_field[n_dozens-1][n_unity-1] = ' .'
                                    #prawo gora
                            if(n_unity < 9 and n_dozens > 0):
                                self.game_field[n_dozens-1][n_unity+1] = ' .'
                                    #dol
                            if(n_dozens + ship_size-1 < 9):
                                self.game_field[n_dozens + ship_size][n_unity] = ' .'
                                #lewo dol
                            if(n_unity > 0 and n_dozens + ship_size-1 < 9):
                                self.game_field[n_dozens + ship_size][n_unity-1] = ' .'
                                    #prawo dol
                            if(n_unity < 9 and n_dozens + ship_size-1 < 9):
                                self.game_field[n_dozens + ship_size][n_unity+1] = ' .'

                        else:   #poziomo
                            self.game_field[n_dozens][n_unity] = ' x'
                            self.game_field[n_dozens][n_unity+1] = ' x'
                            self.game_field[n_dozens][n_unity+2] = ' x'
                                    #prawo
                            if(n_unity + ship_size-1 < 9):
                                self.game_field[n_dozens][n_unity + ship_size] = ' .'
                                    #lewo
                            if(n_unity > 0):
                                self.game_field[n_dozens][n_unity-1] = ' .'                         
                                    #gora
                            if(n_dozens > 0):
                                self.game_field[n_dozens-1][n_unity] = ' .'
                                self.game_field[n_dozens-1][n_unity+1] = ' .'
                                self.game_field[n_dozens-1][n_unity+2] = ' .'                                
                                    #lewo gora
                            if(n_unity > 0 and n_dozens > 0):
                                self.game_field[n_dozens-1][n_unity-1] = ' .'
                                    #prawo gora
                            if(n_unity + ship_size-1 < 9 and n_dozens > 0):
                                self.game_field[n_dozens-1][n_unity + ship_size] = ' .'
                                    #dol
                            if(n_dozens < 9):
                                self.game_field[n_dozens+1][n_unity] = ' .'
                                self.game_field[n_dozens+1][n_unity+1] = ' .'
                                self.game_field[n_dozens+1][n_unity+2] = ' .'
                                #lewo dol
                            if(n_unity > 0 and n_dozens < 9):
                                self.game_field[n_dozens+1][n_unity-1] = ' .'
                                    #prawo dol
                            if(n_unity + ship_size-1 < 9 and n_dozens + ship_size-1 < 9):
                                self.game_field[n_dozens + 1][n_unity + ship_size] = ' .'
                    #Dla Statku o wielkości 4
                    case 4:
                            # pionowo
                        if(b_vertical): 
                            self.game_field[n_dozens][n_unity] = ' x'
                            self.game_field[n_dozens + 1][n_unity] = ' x'
                            self.game_field[n_dozens + 2][n_unity] = ' x'
                            self.game_field[n_dozens + 3][n_unity] = ' x'
                                    #prawo
                            if(n_unity < 9):
                                self.game_field[n_dozens][n_unity+1] = ' .'
                                self.game_field[n_dozens+1][n_unity+1] = ' .'
                                self.game_field[n_dozens+2][n_unity+1] = ' .'
                                self.game_field[n_dozens+3][n_unity+1] = ' .'
                                    #lewo
                            if(n_unity > 0):
                                self.game_field[n_dozens][n_unity-1] = ' .'
                                self.game_field[n_dozens+1][n_unity-1] = ' .'
                                self.game_field[n_dozens+2][n_unity-1] = ' .'
                                self.game_field[n_dozens+3][n_unity-1] = ' .'
                                    #gora
                            if(n_dozens > 0):
                                self.game_field[n_dozens-1][n_unity] = ' .'
                                    #lewo gora
                            if(n_unity > 0 and n_dozens > 0):
                                self.game_field[n_dozens-1][n_unity-1] = ' .'
                                    #prawo gora
                            if(n_unity < 9 and n_dozens > 0):
                                self.game_field[n_dozens-1][n_unity+1] = ' .'
                                    #dol
                            if(n_dozens + ship_size-1 < 9):
                                self.game_field[n_dozens + ship_size][n_unity] = ' .'
                                #lewo dol
                            if(n_unity > 0 and n_dozens + ship_size-1 < 9):
                                self.game_field[n_dozens + ship_size][n_unity-1] = ' .'
                                    #prawo dol
                            if(n_unity < 9 and n_dozens + ship_size-1 < 9):
                                self.game_field[n_dozens + ship_size][n_unity+1] = ' .'

                        else:   #poziomo
                            self.game_field[n_dozens][n_unity] = ' x'
                            self.game_field[n_dozens][n_unity+1] = ' x'
                            self.game_field[n_dozens][n_unity+2] = ' x'
                            self.game_field[n_dozens][n_unity+3] = ' x'
                                    #prawo
                            if(n_unity + ship_size-1 < 9):
                                self.game_field[n_dozens][n_unity + ship_size] = ' .'
                                    #lewo
                            if(n_unity > 0):
                                self.game_field[n_dozens][n_unity-1] = ' .'                         
                                    #gora
                            if(n_dozens > 0):
                                self.game_field[n_dozens-1][n_unity] = ' .'
                                self.game_field[n_dozens-1][n_unity+1] = ' .'
                                self.game_field[n_dozens-1][n_unity+2] = ' .'    
                                self.game_field[n_dozens-1][n_unity+3] = ' .'                               
                                    #lewo gora
                            if(n_unity > 0 and n_dozens > 0):
                                self.game_field[n_dozens-1][n_unity-1] = ' .'
                                    #prawo gora
                            if(n_unity + ship_size-1 < 9 and n_dozens > 0):
                                self.game_field[n_dozens-1][n_unity + ship_size] = ' .'
                                    #dol
                            if(n_dozens < 9):
                                self.game_field[n_dozens+1][n_unity] = ' .'
                                self.game_field[n_dozens+1][n_unity+1] = ' .'
                                self.game_field[n_dozens+1][n_unity+2] = ' .'
                                self.game_field[n_dozens+1][n_unity+3] = ' .'
                                #lewo dol
                            if(n_unity > 0 and n_dozens < 9):
                                self.game_field[n_dozens+1][n_unity-1] = ' .'
                                    #prawo dol
                            if(n_unity + ship_size-1 < 9 and n_dozens + ship_size-1 < 9):
                                self.game_field[n_dozens + 1][n_unity + ship_size] = ' .'
                n_places_ships += 1
                print("Statek Ustawiony")
                break
            if(n_places_ships == 10):
                self.print_game(self)
                print("Wszystkie statki ustawione.")
                input("Wciśnij ENTER aby potwierdzić.")
                break
            
        
game = Okrety_gra

game.Graj(game)
