# main.py

import sys
import time
from utils import clear_screen, get_menu_choice
from game_logic import play_story, load_game, delete_save, SAVE_FILE
import os # Needed here to check SAVE_FILE existence

def display_main_menu():
    # Displays the main menu options.
    clear_screen()
    print("--- The Awakening of Yvonne (Prolog) ---")
    print("1. Start New Game")
    print("2. Load Game")
    print("3. Delete Save")
    print("4. Exit")
    print("---------------------------------------")

def main():

    while True:
        display_main_menu()
        choice = get_menu_choice(4)

        if choice == 1: # Start New Game
            print("Starting a new game...")
            # If a save exists, ask to overwrite
            if os.path.exists(SAVE_FILE):
                print("A save game already exists. Starting a new game will overwrite it. Continue? (yes/no)")
                overwrite = input("> ").lower().strip()
                if overwrite != "yes":
                    print("New game cancelled.")
                    time.sleep(1)
                    continue
            play_story("prologue_start") # Start from the very beginning
        elif choice == 2: # Load Game
            loaded_point = load_game()
            if loaded_point:
                print(f"Resuming from: {loaded_point.replace('_', ' ').title()}...")
                time.sleep(1)
                play_story(loaded_point)
            else:
                print("No save game found. Please start a new game.")
                time.sleep(2)
        elif choice == 3: # Delete Save
            delete_save()
            time.sleep(1)
        elif choice == 4: # Exit
            print("Exiting game. Goodbye!")
            sys.exit() # Exit the program

if __name__ == "__main__":
    main()