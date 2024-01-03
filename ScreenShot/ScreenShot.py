import pyautogui

# Get the size of the monitor.
screenWidth, screenHeight = pyautogui.size()

# Get the coordinates of the center of the screen.
center_x, center_y = screenWidth / 2, screenHeight / 2

# Move the mouse to the center of the screen and click.
pyautogui.moveTo(center_x, center_y)
pyautogui.click()

# Capture a screenshot.
screenshot = pyautogui.screenshot()

# Save the screenshot with a file name.
screenshot.save("screenshot.png")

# Prompt the user for their name.
answer = pyautogui.confirm('I took a screenshot of your window.\nDo you want to tell me your name?')
if answer == 'OK':
    name = pyautogui.prompt('What is your name?')
    print(name)
else:
    # Show a window with a message.
    pyautogui.alert('Okay, but I was upset with you.', title='Window Title', button='OK')