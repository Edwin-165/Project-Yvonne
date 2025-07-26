import os
import time
import sys

# --- Terminal Utility Functions ---

def clear_screen():
    # Clears the terminal screen.
    os.system('cls' if os.name == 'nt' else 'clear')

def delay_print(text, delay=0.02):
    # Prints text character by character for a typewriter effect, then waits for Enter.
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
    input() # Wait for user to press Enter

def get_menu_choice(max_choice):
    # Gets a valid numerical choice from the user for the menu.
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= max_choice:
                return choice
            else:
                print(f"Invalid choice. Please enter a number between 1 and {max_choice}.")
        except ValueError:
            print("Invalid input. Please enter a number.")