#Main archive
import contants as cons
import time
def main():
    #Here i can define objects.
    while True:
        time.sleep(0.5)
        print(cons.FULL_MENU)
        menu_choice = str(input("Your choice: "))
        if menu_choice == "1":

            time.sleep(0.5)
            print(cons.RETURNING_MENU)

        elif menu_choice == "2":

            time.sleep(0.5)
            print(cons.RETURNING_MENU)

        elif menu_choice == "3":

            time.sleep(0.5)
            print(cons.RETURNING_MENU)

        elif menu_choice == "4":

            time.sleep(0.5)
            print(cons.RETURNING_MENU)

        elif menu_choice == "5":

            time.sleep(0.5)
            print(cons.RETURNING_MENU)

        elif menu_choice == "6":

            time.sleep(0.5)
            print(cons.RETURNING_MENU)
        else:
            
            time.sleep(0.5)
            print(cons.INVALID_VALUE)
            time.sleep(0.5)
            print(cons.RETURNING_MENU)

