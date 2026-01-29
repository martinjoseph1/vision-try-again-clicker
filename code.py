import pyautogui
import time

# Sensitivity setting (0.0 to 1.0). 
# Increase if it's not finding it; decrease if it's clicking the wrong things.
CONFIDENCE_LEVEL = 0.8 

def automate_click():
    print("Searching for 'Try Again' button... (Press Ctrl+C to stop)")
    
    while True:
        try:
            # Locate the center of the button on screen
            button_location = pyautogui.locateCenterOnScreen(r"C:\Users\marti\try_again.png.png", confidence=CONFIDENCE_LEVEL)
            
            if button_location:
                print(f"Button found at {button_location}. Clicking...")
                pyautogui.click(button_location)
                
                # Wait a few seconds to avoid double-clicking or clicking too fast
                time.sleep(5) 
            
        except pyautogui.ImageNotFoundException:
            # Button isn't on screen yet, just keep looking
            pass
        
        time.sleep(1) # Check every 1 second to save CPU

if __name__ == "__main__":
    automate_click()
