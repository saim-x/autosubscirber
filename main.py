import time
import pyautogui as py
user = input("Which channel you want to subscribe? \n enter the name : ")
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
        location = py.locateOnScreen(image_path, confidence=0.6)
        if location is not None:
            x, y = py.center(location)
            py.moveTo(x, y)
            print("Image found and cursor moved to the center of the image.")
        else:
            print("Image not found on the screen.")
            print(location)
    except py.ImageNotFoundException:
        print("Image not found on the screen.")
        print(location)

# Provide the path to the image you want to search for
image_path = "t2.png"
time.sleep(1.5)
move_cursor_to_image(image_path)
py.click()
time.sleep(0.9)
py.write(user)
py.press('enter')
def move_cursor_to_image1(image_path_1):
    try:
        location = py.locateOnScreen(image_path_1, confidence=0.6)
        if location is not None:
            x, y = py.center(location)
            py.moveTo(x, y)
            print("Image found and cursor moved to the center of the image.")
            py.click()
            time.sleep(1)
            py.click()
        else:
            print("Image not found on the screen.")
            print(location)
    except py.ImageNotFoundException:
        print("Image not found on the screen.")
        print(location)

# Provide the path to the image you want to search for
image_path_1 = "t3.png"
time.sleep(1.5)
move_cursor_to_image1(image_path_1)




def move_cursor_to_image2(image_path_2):
    try:
        location = py.locateOnScreen(image_path_2, confidence=0.9)
        if location is not None:
            x, y = py.center(location)
            py.moveTo(x, y)
            print("Image found and cursor moved to the center of the image.")
            py.click()
        else:
            print("Image not found on the screen.")
            print(location)
    except py.ImageNotFoundException:
        print("Image not found on the screen.")
        print(location)

# Provide the path to the image you want to search for
image_path_2 = "t5.png"
time.sleep(1.5)
move_cursor_to_image2(image_path_2)

