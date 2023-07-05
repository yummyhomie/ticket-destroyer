import pyautogui, time, msvcrt

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"Program will start in {i} seconds...")
        time.sleep(1)

def pg1():
    countdown_duration = 6
    countdown(countdown_duration) 
    pyautogui.write('Student called in and was needing help logging into their myUVU portal. FERPA verified them and updated their verification methods. They were then able to reset their password and log in!')

def pg2():
    countdown_duration = 6
    countdown(countdown_duration)
    pyautogui.write('Student was needing help logging into their myUVU portal. FERPA verified them and set up their authentication methods. I was then able to show them how to reset their password. They were then able to log in!')

def pg3():
    countdown_duration = 6
    countdown(countdown_duration)
    pyautogui.write('Student recently changed their phone number and was wanting to update her authentication methods. FERPA verified her and got that phone number updated to receive verification texts!')
    
def pg4():
    countdown_duration = 6
    countdown(countdown_duration)
    pyautogui.write('I do need you to verify the following.')
    pyautogui.keyDown('shift'), pyautogui.press('enter'), pyautogui.keyUp('shift')
    pyautogui.write('- Name')
    pyautogui.keyDown('shift'), pyautogui.press('enter'), pyautogui.keyUp('shift')
    pyautogui.write('- Date of Birth')
    pyautogui.keyDown('shift'), pyautogui.press('enter'), pyautogui.keyUp('shift')
    pyautogui.write('- Address')
    pyautogui.keyDown('shift'), pyautogui.press('enter'), pyautogui.keyUp('shift')
    pyautogui.write('- Email Address')
    pyautogui.keyDown('shift'), pyautogui.press('enter'), pyautogui.keyUp('shift')
    pyautogui.write('- Major Declared')
    pyautogui.keyDown('shift'), pyautogui.press('enter'), pyautogui.keyUp('shift')
    pyautogui.write('- Previous High School attended')
    pyautogui.keyDown('shift'), pyautogui.press('enter'), pyautogui.keyUp('shift')
    pyautogui.write('Then allow me a few moments to ')
def pg5():
    quit()

def dp_menu():
    print("Select one of the following:")
    print("[1] 'Login Help, They reset password'")
    print("[2] 'Login Help, showed where to reset passwrd'")
    print("[3] 'Updating Azure Authentication Methods'")
    print("[4] 'I need you to verify the following'")
    print("[z] to exit")

dp_menu()

choice = msvcrt.getch().decode("utf-8")

if choice == "1":
    pg1()
elif choice == "2":
    pg2()
elif choice == "3":
    pg3()
elif choice == "4":
    pg4()
elif choice == "z":
    pg5()
else: print('Bruh. Try again. ')




#       No Programming Experience?
#
#⠀⣞⢽⢪⢣⢣⢣⢫⡺⡵⣝⡮⣗⢷⢽⢽⢽⣮⡷⡽⣜⣜⢮⢺⣜⢷⢽⢝⡽⣝
#⠸⡸⠜⠕⠕⠁⢁⢇⢏⢽⢺⣪⡳⡝⣎⣏⢯⢞⡿⣟⣷⣳⢯⡷⣽⢽⢯⣳⣫⠇
#⠀⠀⢀⢀⢄⢬⢪⡪⡎⣆⡈⠚⠜⠕⠇⠗⠝⢕⢯⢫⣞⣯⣿⣻⡽⣏⢗⣗⠏⠀
#⠀⠪⡪⡪⣪⢪⢺⢸⢢⢓⢆⢤⢀⠀⠀⠀⠀⠈⢊⢞⡾⣿⡯⣏⢮⠷⠁⠀⠀
#⠀⠀⠀⠈⠊⠆⡃⠕⢕⢇⢇⢇⢇⢇⢏⢎⢎⢆⢄⠀⢑⣽⣿⢝⠲⠉⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⡿⠂⠠⠀⡇⢇⠕⢈⣀⠀⠁⠡⠣⡣⡫⣂⣿⠯⢪⠰⠂⠀⠀⠀⠀
#⠀⠀⠀⠀⡦⡙⡂⢀⢤⢣⠣⡈⣾⡃⠠⠄⠀⡄⢱⣌⣶⢏⢊⠂⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⢝⡲⣜⡮⡏⢎⢌⢂⠙⠢⠐⢀⢘⢵⣽⣿⡿⠁⠁⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠨⣺⡺⡕⡕⡱⡑⡆⡕⡅⡕⡜⡼⢽⡻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⣼⣳⣫⣾⣵⣗⡵⡱⡡⢣⢑⢕⢜⢕⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⣴⣿⣾⣿⣿⣿⡿⡽⡑⢌⠪⡢⡣⣣⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⡟⡾⣿⢿⢿⢵⣽⣾⣼⣘⢸⢸⣞⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠁⠇⠡⠩⡫⢿⣝⡻⡮⣒⢽⠋⠀                                        
