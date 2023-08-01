import time
import pyautogui as py

py.press('win')
time.sleep(0.5)
py.write('chrome')
py.press('enter')
time.sleep(1)
py.write('youtube.com')
py.press('enter')

# def search(image_path_1):
#     try:
#         x, y = py.locateCenterOnScreen(image_path_1, confidence=0.9)
#         py.moveTo(x,y)
#     except:
#         print("masla aarha hai")
# image_path_1 = "/search.png"
# time.sleep(3)
# search(image_path_1)
# time.sleep(2)
# image_path_1 = "D://Projects//first sample//search.png"
# x, y = py.locateCenterOnScreen(image_path_1)
# py.moveTo(x, y)

# py.click


def move_cursor_to_image(image_path):
    try:
        location = py.locateOnScreen(image_path, confidence=0.5)
        if location is not None:
            x, y, width, height = py.center(location)
            py.moveTo(x, y)
            print("Image found and cursor moved to the center of the image.")
        else:
            print("Image not found on the screen.")
    except py.ImageNotFoundException:
        print("Image not found on the screen.")

# Provide the path to the image you want to search for
image_path = "D://Projects//first sample//search.png"
move_cursor_to_image(image_path)
py.click()