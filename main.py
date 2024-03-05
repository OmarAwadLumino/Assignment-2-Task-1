class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_name(self):
        return self.name


    def get_symbol(self):
        return self.symbol

def game(Mylist):
    print(" ", list_of_Game[0], end=" | ")
    print(list_of_Game[1], end=" | ")
    print(list_of_Game[2])
    print("=============")
    print(" ", list_of_Game[3], end=" | ")
    print(list_of_Game[4], end=" | ")
    print(list_of_Game[5])
    print("=============")
    print(" ", list_of_Game[6], end=" | ")
    print(list_of_Game[7], end=" | ")
    print(list_of_Game[8])
    print("=============")

def chk_choice(choice1):
    while True:
        if (choice1 not in range(1, 10)) or (list_of_Game[choice1 - 1] != choice1):
            print("\n******Invalid Choice******\n")
        else:
            break
        choice1 = int(input("\nEnter your choice from 1 to 9 : \n"))
    return choice1

def winner(mylist):
    if mylist[0] == mylist[1] == mylist[2]:
        if mylist[0] == "X":
            print(f"{player1_name} has won!")
        else:
            print(f"{player2_name} has won!")
        return True
    if mylist[3] == mylist[4] == mylist[5]:
        if mylist[3] == "X":
            print(f"{player1_name} has won!")
        else:
            print(f"{player2_name} has won!")
        return True
    if mylist[6] == mylist[7] == mylist[8]:
        if mylist[6] == "X":
            print(f"{player1_name} has won!")
        else:
            print(f"{player2_name} has won!")
        return True
    if mylist[0] == mylist[3] == mylist[6]:
        if mylist[0] == "X":
            print(f"{player1_name} has won!")
        else:
            print(f"{player2_name} has won!")
        return True
    if mylist[1] == mylist[4] == mylist[7]:
        if mylist[1] == "X":
            print(f"{player1_name} has won!")
        else:
            print(f"{player2_name} has won!")
        return True
    if mylist[2] == mylist[5] == mylist[8]:
        if mylist[2] == "X":
            print(f"{player1_name} has won!")
        else:
            print(f"{player2_name} has won!")
        return True
    if mylist[0] == mylist[4] == mylist[8]:
        if mylist[0] == "X":
            print(f"{player1_name} has won!")
        else:
            print(f"{player2_name} has won!")
        return True
    if mylist[2] == mylist[4] == mylist[6]:
        if mylist[2] == "X":
            print(f"{player1_name} has won!")
        else:
            print(f"{player2_name} has won!")
        return True
    return False







while True:
    player1_name = input("Player1, Enter your name : ")
    player_one = Player(player1_name, 'X')
    player2_name = input("Player2, Enter your name : ")
    player_two = Player(player2_name, 'O')
    list_of_Game = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    game(list_of_Game)
    flag = True
    for i in range(len(list_of_Game)):
        if i % 2 == 0:
            print(f"{player1_name}'s Turn\n")
            choice = int(input("Enter your choice from 1 to 9 : "))
            choice = chk_choice(choice)
            list_of_Game[choice - 1] = player_one.get_symbol()
            game(list_of_Game)
            if winner(list_of_Game):
                flag = False
                break
        else:
            print(f"{player2_name}'s Turn\n")
            choice = int(input("Enter your choice from 1 to 9 : "))
            choice = chk_choice(choice)
            list_of_Game[choice - 1] = player_two.get_symbol()
            game(list_of_Game)
            if winner(list_of_Game):
                flag = False
                break
    if flag:
        print("DRAW")
    print("\n\n1 - Continue \n 2 - Exit")
    choice = int(input("Enter your choice ==>"))
    if choice == 2:
        break
