from timer import timer25, s_break, l_break, test_timer
from menu import pause, options, clear

#User decides timer to start
print("Welcome to Pomodoro Timer! \n")
options()
choice = int(input("Selection: "))

#Loop for controlling choices
while choice != 0:
    if choice == 1:
        timer25()
        pause()
    elif choice == 2:
        s_break()
        pause()
    elif choice == 3:
        l_break()
        pause()
    elif choice == 4:
        test_timer()
        pause()
    else:
        print("Please try again.")
        pause()
    
    clear()
    options()
    #variable is defined again, since "int" isn't callable
    choice = int(input("Selection: "))
