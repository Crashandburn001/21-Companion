import colorama
from colorama import Fore, Back, Style
menuChoice = 0
playerList = []
startBalance = 1
costPerCard = 1
def menu():
    global menuChoice
    print(Fore.BLUE + Style.BRIGHT + "Welcome to 21-Companion!!!")
    while menuChoice == 0 or menuChoice == '!':
        try:
            print("\n" + Fore.CYAN + Style.BRIGHT + "Menu")
            print(Style.RESET_ALL + "\n\n" + Fore.GREEN + "[1] Play\n" + Fore.LIGHTMAGENTA_EX + "[2] Exit Game\n" + Fore.YELLOW + "[3] Credits")
            menuChoice = int(input(Fore.WHITE + Style.BRIGHT + "\nEnter your choice: "))
        except ValueError:
            print(Fore.RED + Style.NORMAL + "Uh Oh! Looks like you didn't enter a number. Please try again and set your choice to the number next to the menu option!")
            menuChoice = '!'
        if menuChoice == 1:
            playerconfig()
        elif menuChoice == 2:
            rusure = input(Fore.RED + Style.NORMAL + "Are you sure you wish to exit the game? (y/n) \t")
            if rusure == "y":
                exit()
            elif rusure == "n":
                menuChoice = 0
            else:
                print("Invalid Input. Returning to menu.")
        elif menuChoice == 3:
            print(Style.RESET_ALL + "This game was created by " + Style.BRIGHT + Fore.BLUE + "Crashandburn001." + Style.RESET_ALL + "\n It is designed to help players of the game " + Style.BRIGHT + Fore.BLUE + "21/Blackjack" + Style.RESET_ALL + " with game administration!")
            menuChoice = 0
        elif menuChoice != '!':
            print(Style.RESET_ALL + Fore.RED + "Invalid Input. Returning to menu.")
            menuChoice = 0
        else:
            menuChoice = 0


def playerconfig():
    global playerList
    print(Style.RESET_ALL + Fore.RED + "[Devlog] Play!")
    queryCorrect = 0
    while queryCorrect == 0:
        print(Style.RESET_ALL + Fore.BLUE + "Step 1: Player Configuration\n" + Style.RESET_ALL + "Please input each player's name separated by a comma, in the order that they will play.\nNo need to include the dealer.")
        user_input = input(Fore.LIGHTCYAN_EX + "\nPlayer Names:\t").strip()
        playerList = [name.strip() for name in user_input.split(',') if name.strip()]
        print(Fore. LIGHTGREEN_EX + "\nPlease double check these names are correct:")
        for name in playerList:
            print(f"- {name}")
        queryCorrect = input("Are these names correct? (y/n) \t")
        if queryCorrect == 'y':
            gameConfig()
        else:
            queryCorrect = 0

def gameConfig():
    global playerList
    global costPerCard
    global startBalance
    print(Style.RESET_ALL + Fore.RED + "[Devlog] Game Configuration!")
    startBalance = 0
    while startBalance == 0:
        try:
            startBalanceQuery = int(input(Style.RESET_ALL + Style.BRIGHT + "\nHow many coins does each player start with?\t\t"))
            if startBalanceQuery < 20:
                print(Style.NORMAL + Fore.RED + "Invalid Input. Starting Balance must be greater than 20.")
            else:
                startBalance = startBalanceQuery

        except:
            print(Style.NORMAL + Fore.RED + "Invalid Input! Please try again. Your input must be a number.")
    costPerCard = 0
    while costPerCard == 0:
        try:
            costPerCardQuery = int(input(Style.RESET_ALL + Style.BRIGHT + "\nWhat is the cost per card?\t\t"))
            if costPerCardQuery <= 0 or costPerCardQuery > startBalance / 15:
                print(
                    Style.NORMAL + Fore.RED + "Invalid input. Cost per card must be greater than 0 and low enough for each player to afford at least 15 cards.")


            else:
                costPerCard = costPerCardQuery

        except:
            print(Style.NORMAL + Fore.RED + "Invalid Input! Please try again. Your input must be a whole number.")



# Execute Functions!
menu()