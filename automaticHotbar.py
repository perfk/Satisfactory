# Install the following
# pip install keyboard
# pip install pyautogui

import keyboard
import pyautogui
import time

word_lists = [
    #1
    ["Power Line", "Conveyor belt mk.5", "Conveyor lift mk.5", "conveyor lift floor hole", "Conveyor Merger", "Industrial Storage", "Foundation (2 m)", "Pipeline Support", "pipeline mk.2", "blueprint designer mk.2"],
    #2
    ["Power Line", "Constructor", "Smelter", "Miner mk.3", "water extractor", "", "", "", "", ""],
    #3
    ["Power Line", "hypertube support", "hypertube entrance", "hypertube", "railway", "block signal", "electric Locomotive", "", "", ""],
    #4
    [""],
    #5
    [""],
    #6
    [""],
    #7
    [""],
    #8
    [""],
    #9
    [""],
    #10
    ["Power Line", "Crafting Bench", "AWESOME Sink", "Blueprint designer mk.2", "MAM", "", "", "", "", ""],
    # ["Power Line", "", "", "", "", "", "", "", "", ""],
    # Add up to 10 lists in total, each list can only have 10 words
]

# Coordinates list for storing the saved screen positions
coordinates = []
x_coordinates = []


# Function to wait for F1 press to continue
def wait_for_f1():
    print("Waiting for F1 to be pressed...")
    keyboard.wait('f1')
    print("F1 pressed. Continuing script...")

# Function to exit the script when F2 is pressed
def stop_script():
    if keyboard.is_pressed('f2'):
        print("F2 pressed. Stopping script.")
        exit()

# I was not able to get any of the other pyautogui or keyboard functions to work
def press_key(keyToPress):
    pyautogui.keyDown(keyToPress)
    time.sleep(0.1)
    pyautogui.keyUp(keyToPress)
    time.sleep(0.1)

def scroll(direction, amount):
    pyautogui.keyDown('alt')
    for x in range(amount):
        if direction == "up":
            pyautogui.scroll(1)
        if direction == "down":
            pyautogui.scroll(-1)
    pyautogui.keyUp('alt')


# Function to save the cursor position (F3 key)
def save_coordinate():
    print("Press F3 to save a coordinate...")
    while True:
        if keyboard.is_pressed('f3'):
            x, y = pyautogui.position()
            coordinates.append((x, y))
            print(f"Coordinate saved: {x}, {y}")
            print("Now mouse over the x to the right of the search bar and press F4")
            time.sleep(0.5)  # Delay to avoid multiple saves from a single press
            break

def save_x_coordinate():
    print("Press F4 to save X location")
    press_key('space')
    time.sleep(0.1)
    keyboard.write('test')
    time.sleep(0.1)
    while True:
        if keyboard.is_pressed('f4'):
            x, y = pyautogui.position()
            x_coordinates.append((x, y))
            pyautogui.click()
            print(f"Coordinate saved: {x}, {y}")
            print("Click F1 to proceseed, ensure you are not in any menu and the game is active")
            press_key('q')
            time.sleep(0.5)  # Delay to avoid multiple saves from a single press
            break


# Function to automate the task
def perform_task():
    # Step 5: Press Q to open the build menu
    press_key('q')
    for list_index, word_list in enumerate(word_lists):
        for word_index, word in enumerate(word_list):
            if word != '':
                #type = word ## add support for blueprint and x
                #if "x_" in type:
                #    word = word[len(x_):]
                #    press_key('esc') 
                #    time.sleep(0.1)
                #    press_key('q')
                #    time.sleep(0.1)

                # Step 6: Press space to start searching
                press_key('space')
                time.sleep(0.1)

                # Step 7: Write the word from the current list
                keyboard.write(word)
                print(f"Writing the word: {word}")
                time.sleep(0.5)

                # Step 8: Move the cursor to the saved coordinate
                if coordinates:
                    time.sleep(0.5)
                    pyautogui.moveTo(coordinates[0])
                    time.sleep(0.1)

                # Step 9: Press the number corresponding to the word's position (1-based index)
                number_to_press = str(word_index + 1);
                print(f"Pressing number: {number_to_press}")
                if number_to_press != '10':
                    press_key(number_to_press)
                    press_key(number_to_press)
                else:
                    press_key('0')
                    press_key('0')
                time.sleep(0.1)

                # click x to get ready for the next value
                if x_coordinates:
                    time.sleep(0.5)
                    pyautogui.click(x_coordinates[0])
                    time.sleep(0.1)

                # Step 10: Repeat until all 10 lists are performed
                if keyboard.is_pressed('f2'):
                    print("F2 pressed. Stopping script.")
                    exit()
        scroll('up',1)
        print("Going to the next hotbar")

def main():
    
    # Saving the first coordinate (press F3)
    save_coordinate()

    save_x_coordinate()

    # Wait for the user to have first cliceked the 
    wait_for_f1()
    
    # Start performing tasks with the 10 lists
    perform_task()

if __name__ == "__main__":
    main()
