import sys
import time

import cv2
import keyboard
import numpy as np
import pytesseract
from PIL import ImageGrab
from pyautogui import keyDown, keyUp

pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


def welcome():
    print('Welcome to D2 AutoFishing!')
    print('Press CTRL to stop at any time.')


def compare(tuple, colour):
    if colour == 'white':
        if tuple[0] > 240 and tuple[1] > 240 and tuple[2] > 240:
            return True
        else:
            return False
    elif colour == 'black':
        if 40 < tuple[0] < 60 and 40 < tuple[0] < 60 and 40 < tuple[0] < 60:
            return True
        else:
            return False


def catch():
    perf_count = 0

    px = ImageGrab.grab(
        bbox=(1107, 985, 1448, 986)).load()  # bbox specifies specific region (bbox= x,y,width,height))

    perf1 = px[1182 - 1107, 0]  # perfect catch E black
    perf2 = px[1187 - 1107, 0]  # perfect catch E white
    perf3 = px[1243 - 1107, 0]  # perfect catch P white
    perf4 = px[1351 - 1107, 0]  # perfect catch C white

    if compare(perf1, 'black'):
        perf_count += 1

    if compare(perf2, 'white'):
        perf_count += 1

    if compare(perf3, 'white'):
        perf_count += 1

    if compare(perf4, 'white'):
        perf_count += 1

    if perf_count > 2:
        keyDown('e')
        keyUp('e')
        keyDown('e')
        keyUp('e')
        keyDown('e')
        keyUp('e')
        print("Fish detected: Reeling In!")


def roi(img, vertices):
    # blank mask:
    mask = np.zeros_like(img)
    catch()
    # fill the mask
    cv2.fillPoly(mask, vertices, 255)
    catch()
    # now only show the area that is the mask
    masked = cv2.bitwise_and(img, mask)
    catch()
    return masked


def identify(text):
    if ("Go Fishing" in text) or ("Fishing (Bait" in text) or ("Bait Held" in text):
        return True
    else:
        return False


def main():
    # configurations
    config = '-l eng --oem 1 --psm 3'
    welcome()
    while not keyboard.is_pressed('ctrl'):  # press ctrl to stop
        catch()
        img = ImageGrab.grab(bbox=(1100, 950, 1560, 1015))  # bbox specifies specific region (bbox= x,y,width,height))
        catch()
        img_np = np.array(img)
        catch()
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        catch()
        processed_img = cv2.Canny(frame, threshold1=100, threshold2=350)
        catch()
        vertices = np.array([[0, 65], [0, 0], [460, 0], [460, 65],
                             ], np.int32)
        catch()
        processed_img = roi(processed_img, [vertices])
        catch()
        cv2.imshow("Capture", processed_img)
        catch()
        # PyTesseract
        myText = pytesseract.image_to_string(processed_img, config=config)
        catch()
        if identify(myText):
            print("Prompt detected: Casting line...")
            keyDown('e')
            time.sleep(3)
            keyUp('e')
            print("And now we wait...")
        catch()

    print('Thank you for using D2 AutoFishing.')
    sys.exit()


if __name__ == "__main__":
    main()

# ======================== LEGACY CODE USING PIXELS TO CAST ========================
# go_count = 0
#
# go1 = px[1108 - 1107, 0]  # go fishing E black
# go2 = px[1125 - 1107, 0]  # go fishing E white
# go3 = px[1169 - 1107, 0]  # go fishing G white
# go4 = px[1217 - 1107, 0]  # go fishing F white
# go5 = px[1332 - 1107, 0]  # go fishing B white
# go6 = px[1391 - 1107, 0]  # go fishing H white
#
# if compare(go1, 'black'):
#     go_count += 1
#
# if compare(go2, 'white'):
#     go_count += 1
#
# if compare(go3, 'white'):
#     go_count += 1
#
# if compare(go4, 'white'):
#     go_count += 1
#
# if compare(go5, 'white'):
#     go_count += 1
#
# if compare(go6, 'white'):
#     go_count += 1
#
# # if go_count > 1:
#     print("Prompt detected: Casting line...")
#     keyDown('e')
#     time.sleep(3)
#     keyUp('e')
#     print("And now we wait...")
