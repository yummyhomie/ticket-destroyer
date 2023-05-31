import msvcrt, time

def script_1():
    # Code for script 1
    def countdown(seconds):
        for i in range(seconds, 0, -1):
            print(f"Program will start in {i} seconds...")
        time.sleep(1)

    countdown_duration = 6 # Set the countdown duration in seconds
    countdown(countdown_duration) # Display the message and countdown
    print("Running script 1")

def script_2():
    # Code for script 2
    print("Running script 2")

def script_3():
    # Code for script 3
    print("Running script 3")

def display_menu():
    print("Menu:")
    print("1. Run script 1")
    print("2. Run script 2")
    print("3. Run script 3")

# Main program
display_menu()

choice = msvcrt.getch().decode("utf-8")

if choice == "1":
    script_1()
elif choice == "2":
    script_2()
elif choice == "3":
    script_3()
else:
    print("Invalid choice. Please enter a number from 1 to 3.")
