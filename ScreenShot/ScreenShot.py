import pyautogui
import time

# Get the size of the monitor.
screenWidth, screenHeight = pyautogui.size()

# Get the coordinates of the center of the screen.
x, y = screenWidth / 2, screenHeight / 2

# Move the mouse to the center of the screen.
pyautogui.moveTo(x, y)

# Click the left mouse button.
pyautogui.click()

# Capture a screenshot.
sg = screenshot = pyautogui.screenshot()

# Save the screenshot with a file name.
sg.save("screenshot.png")



# Delay before starting typing
time.sleep(5)

# Type a messageHello, World!Hello, World!
message = "Hello, World! I am reza latifi"
pyautogui.typewrite(message)