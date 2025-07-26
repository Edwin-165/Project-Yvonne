# game_logic.py

import os
import time
from utils import clear_screen, delay_print
from story import STORY_CONTENT, STORY_FLOW

# --- Configuration ---
SAVE_FILE = "yvonne_story_save.txt"

# --- Save/Load Functions ---

def save_game(story_point):
    """Saves the current story point to a file."""
    try:
        with open(SAVE_FILE, "w") as f:
            f.write(story_point)
        print("Game saved successfully!")
    except IOError as e:
        print(f"Error saving game: {e}")
    time.sleep(1) # Give user time to read message

def load_game():
    """Loads the story point from a file if it exists."""
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r") as f:
                story_point = f.read().strip()
            print("Game loaded successfully!")
            time.sleep(1)
            return story_point
        except IOError as e:
            print(f"Error loading game: {e}")
            return None
    else:
        return None

def delete_save():
    """Deletes the save game file."""
    if os.path.exists(SAVE_FILE):
        print("Are you sure you want to delete your save game? This cannot be undone. (yes/no)")
        confirmation = input("> ").lower().strip()
        if confirmation == "yes":
            os.remove(SAVE_FILE)
            print("Save game deleted.")
        else:
            print("Save deletion cancelled.")
    else:
        print("No save game found to delete.")
    time.sleep(1)

# --- Game Play Function ---

def play_story(start_point="prologue_start"):
    """
    Manages the flow of the story.
    Starts from 'start_point' or the beginning if not specified.
    """
    current_story_point = start_point

    while current_story_point != "END":
        clear_screen()
        
        # Get the content for the current story point
        story_lines = STORY_CONTENT.get(current_story_point)

        if story_lines:
            for line in story_lines:
                delay_print(line)
            
            # Determine the next story point from the flow map
            next_story_point = STORY_FLOW.get(current_story_point)
            
            if next_story_point:
                save_game(next_story_point) # Save the *next* point, so we resume there
                current_story_point = next_story_point
            else:
                # If there's no next point defined in STORY_FLOW, it means we've reached an end.
                current_story_point = "END" # Signal to end the loop
        else:
            print(f"Error: Story segment '{current_story_point}' content not found or flow ended unexpectedly.")
            current_story_point = "END" # Force end on error

    if current_story_point == "END":
        clear_screen()
        delay_print("--- The End of the Prologue ---")
        delay_print("Thank you for experiencing the story of Yvonne's awakening.")
        delay_print("More chapters to come...")
        time.sleep(2) # Give time to read "The End"

