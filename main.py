import sys
import time
import cv2
import keyboard
import numpy as np
import pytesseract
from PIL import ImageGrab
from pyautogui import keyDown, keyUp
from tkinter import *

# pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe'


def welcome():
    print('Welcome to D2 AutoFishing!')
    print('If your monitor is 2560 x 1440, please input 0.')
    print('If your monitor is 3840 x 2160, please input 1.')
    print('If your monitor is 1920 x 1080, please input 2. (not yet implemented)')
    print('If your monitor is 2560 x 1080, please input 3. (not yet implemented)')
    print('If your monitor is 1920 x 800,  please input 4. (not yet implemented)')
    print('If your monitor is 3440 x 1440, please input 5. (not yet implemented)')
    print('If your monitor is 7680 x 4320, please input 6. (not yet implemented)')
    resolution = int(input())
    print('Adjusting settings...')
    print('Press CTRL to stop at any time.')
    return resolution


# def compare(tuple, colour):
#     if colour == 'white':
#         if tuple[0] > 225 and tuple[1] > 224 and tuple[2] > 222:
#             return True
#         else:
#             return False
#     elif colour == 'black':
#         if 40 < tuple[0] < 60 and 40 < tuple[0] < 60 and 40 < tuple[0] < 60:
#             return True
#         else:
#             return False

def compare(tuple):
    if tuple[0] > 225 and tuple[1] > 224 and tuple[2] > 222:
        return True
    else:
        return False


def catch(resolution_select):
    myRes = resolution_select
    perf_count = 0
    perfs = []

    if myRes == 0:  # 2560 x 1440
        px = ImageGrab.grab(
            bbox=(1243, 980, 1425, 981)).load()  # bbox specifies specific region (bbox= x,y,width,height))

        perfs.append(px[0, 0])
        perfs.append(px[13, 0])
        perfs.append(px[20, 0])
        perfs.append(px[29, 0])
        perfs.append(px[37, 0])
        perfs.append(px[48, 0])
        perfs.append(px[57, 0])
        perfs.append(px[67, 0])
        perfs.append(px[75, 0])
        perfs.append(px[84, 0])
        perfs.append(px[91, 0])
        perfs.append(px[108, 0])
        perfs.append(px[130, 0])
        perfs.append(px[139, 0])
        perfs.append(px[147, 0])
        perfs.append(px[156, 0])
        perfs.append(px[166, 0])
        perfs.append(px[172, 0])

    elif myRes == 1:  # 3840 x 2160
        px = ImageGrab.grab(
            bbox=(1863, 1470, 2138, 1471)).load()  # bbox specifies specific region (bbox= x,y,width,height))

        perfs.append(px[0, 0])
        perfs.append(px[28, 0])
        perfs.append(px[42, 0])
        perfs.append(px[54, 0])
        perfs.append(px[72, 0])
        perfs.append(px[85, 0])
        perfs.append(px[99, 0])
        perfs.append(px[110, 0])
        perfs.append(px[125, 0])
        perfs.append(px[136, 0])
        perfs.append(px[161, 0])
        perfs.append(px[195, 0])
        perfs.append(px[209, 0])
        perfs.append(px[221, 0])
        perfs.append(px[235, 0])
        perfs.append(px[250, 0])
        perfs.append(px[260, 0])
        perfs.append(px[274, 0])

    elif myRes == 2:  # 1920 x 1080
        px = ImageGrab.grab(
            bbox=(1107, 985, 1448, 986)).load()  # bbox specifies specific region (bbox= x,y,width,height))

        # THESE ARE INACCURATE AND WILL NOT WORK
        perfs.append(px[0, 0])
        perfs.append(px[13, 0])
        perfs.append(px[20, 0])
        perfs.append(px[29, 0])
        perfs.append(px[37, 0])
        perfs.append(px[48, 0])
        perfs.append(px[57, 0])
        perfs.append(px[67, 0])
        perfs.append(px[75, 0])
        perfs.append(px[84, 0])
        perfs.append(px[91, 0])
        perfs.append(px[108, 0])
        perfs.append(px[130, 0])
        perfs.append(px[139, 0])
        perfs.append(px[147, 0])
        perfs.append(px[156, 0])
        perfs.append(px[166, 0])
        perfs.append(px[172, 0])

    elif myRes == 3:  # 2560 x 1080
        px = ImageGrab.grab(
            bbox=(1107, 985, 1448, 986)).load()  # bbox specifies specific region (bbox= x,y,width,height))

        # THESE ARE INACCURATE AND WILL NOT WORK
        perfs.append(px[0, 0])
        perfs.append(px[13, 0])
        perfs.append(px[20, 0])
        perfs.append(px[29, 0])
        perfs.append(px[37, 0])
        perfs.append(px[48, 0])
        perfs.append(px[57, 0])
        perfs.append(px[67, 0])
        perfs.append(px[75, 0])
        perfs.append(px[84, 0])
        perfs.append(px[91, 0])
        perfs.append(px[108, 0])
        perfs.append(px[130, 0])
        perfs.append(px[139, 0])
        perfs.append(px[147, 0])
        perfs.append(px[156, 0])
        perfs.append(px[166, 0])
        perfs.append(px[172, 0])

    elif myRes == 4:  # 1920 x 800
        px = ImageGrab.grab(
            bbox=(1107, 985, 1448, 986)).load()  # bbox specifies specific region (bbox= x,y,width,height))

        # THESE ARE INACCURATE AND WILL NOT WORK
        perfs.append(px[0, 0])
        perfs.append(px[13, 0])
        perfs.append(px[20, 0])
        perfs.append(px[29, 0])
        perfs.append(px[37, 0])
        perfs.append(px[48, 0])
        perfs.append(px[57, 0])
        perfs.append(px[67, 0])
        perfs.append(px[75, 0])
        perfs.append(px[84, 0])
        perfs.append(px[91, 0])
        perfs.append(px[108, 0])
        perfs.append(px[130, 0])
        perfs.append(px[139, 0])
        perfs.append(px[147, 0])
        perfs.append(px[156, 0])
        perfs.append(px[166, 0])
        perfs.append(px[172, 0])

    for i in range(len(perfs)):
        if compare(perfs[i]):
            perf_count += 1

    if perf_count > 12:
        keyDown('e')
        keyUp('e')
        keyDown('e')
        keyUp('e')
        keyDown('e')
        keyUp('e')
        print("Fish detected: Reeling In!")
        return True
    else:
        return False


def roi(img, vertices, resolution_select):
    # blank mask:
    mask = np.zeros_like(img)
    catch(resolution_select)
    # fill the mask
    cv2.fillPoly(mask, vertices, 255)
    catch(resolution_select)
    # now only show the area that is the mask
    masked = cv2.bitwise_and(img, mask)
    catch(resolution_select)
    return masked


def identify(text):
    if ("Fishing" in text) or ("Bait" in text):
        return True
    else:
        return False


def main():
    # configurations
    config = '-l eng --oem 1 --psm 3'
    dimensions = (1100, 950, 1560, 1015)
    resolution_select = int(welcome())

    if resolution_select == 0:
        dimensions = (1125, 945, 1342, 1018)
    elif resolution_select == 1:
        dimensions = (1690, 1430, 1997, 1497)
    elif resolution_select == 2:
        dimensions = (1100, 950, 1560, 1015)
    elif resolution_select == 3:
        dimensions = (1100, 950, 1560, 1015)
    elif resolution_select == 4:
        dimensions = (1100, 950, 1560, 1015)

    while not keyboard.is_pressed('ctrl'):  # press ctrl to stop
        catch(resolution_select)
        img = ImageGrab.grab(bbox=dimensions)  # bbox specifies specific region (bbox= x,y,width,height))
        catch(resolution_select)
        img_np = np.array(img)
        catch(resolution_select)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        catch(resolution_select)
        processed_img = cv2.Canny(frame, threshold1=100, threshold2=350)
        catch(resolution_select)
        vertices = np.array([[0, 65], [0, 0], [460, 0], [460, 65],
                             ], np.int32)
        catch(resolution_select)
        processed_img = roi(processed_img, [vertices], resolution_select)
        catch(resolution_select)
        cv2.imshow("Capture", processed_img)
        catch(resolution_select)
        # PyTesseract
        myText = pytesseract.image_to_string(processed_img, config=config)
        catch(resolution_select)
        if identify(myText):
            print("Prompt detected: Casting line...")
            keyDown('e')
            time.sleep(3)
            keyUp('e')
            print("And now we wait...")
            timeout = time.time() + 25  # 30 sec from now
            while True:
                if catch(resolution_select) or time.time() > timeout:
                    break

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
