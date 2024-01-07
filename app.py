import time
import pyautogui
import random



# Function to type a string with a delay between each letter
def type_with_delay(text, delay=0.1):
    for char in text:
        pyautogui.write(char)
        time.sleep(delay)

# Function to perform a search with a given keyword
def perform_search(keyword, search_bar_location):
    # Click on the specified search bar location
    pyautogui.click(search_bar_location)

    # Type the keyword with a delay between each letter and press Enter
    type_with_delay(keyword)
    pyautogui.press('enter')
    
    # Wait for a random time between 1 and 5 seconds (adjust as needed)
    sleep_time = random.uniform(2, 5)
    time.sleep(sleep_time)
    pyautogui.hotkey('ctrl', 'n')
# Example XY coordinates for the search bar (replace with your actual coordinates)
search_bar_location = (1203, 173) #chaange coords to search bar

search_words= ['strings']
# Loop through the list and perform searches
for word in search_words:
    perform_search(word, search_bar_location)

print("Searches completed.")


