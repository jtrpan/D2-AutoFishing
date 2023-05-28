import sys
import time
import cv2
import keyboard
import numpy as np
import pytesseract
from PIL import ImageGrab
from pyautogui import keyDown, keyUp

# pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def welcome():
    print('Welcome to D2 AutoFishing!')
    print('If your monitor is 2560 x 1440, please input 0.')
    print('If your monitor is 3840 x 2160, please input 1. (not yet implemented)')
    print('If your monitor is 1920 x 1080, please input 2. (not yet implemented)')
    print('If your monitor is 2560 x 1080, please input 3. (not yet implemented)')
    print('If your monitor is 1920 x 800,  please input 4. (not yet implemented)')
    print('If your monitor is 3440 x 1440, please input 5. (not yet implemented)')
    print('If your monitor is 7680 x 4320, please input 6. (not yet implemented)')
    resolution = input()
    print('Adjusting settings...')
    print('Press CTRL to stop at any time.')
    return resolution


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


def catch(dimensions):
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


def roi(img, vertices, dimensions):
    # blank mask:
    mask = np.zeros_like(img)
    catch(dimensions)
    # fill the mask
    cv2.fillPoly(mask, vertices, 255)
    catch(dimensions)
    # now only show the area that is the mask
    masked = cv2.bitwise_and(img, mask)
    catch(dimensions)
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
    resolution_select = welcome()

    if resolution_select == 0:
        dimensions = (1100, 950, 1560, 1015)
    elif resolution_select == 1:
        dimensions = (1100, 950, 1560, 1015)
    elif resolution_select == 2:
        dimensions = (1100, 950, 1560, 1015)
    elif resolution_select == 3:
        dimensions = (1100, 950, 1560, 1015)
    elif resolution_select == 4:
        dimensions = (1100, 950, 1560, 1015)

    while not keyboard.is_pressed('ctrl'):  # press ctrl to stop
        catch(dimensions)
        img = ImageGrab.grab(bbox=dimensions)  # bbox specifies specific region (bbox= x,y,width,height))
        catch(dimensions)
        img_np = np.array(img)
        catch(dimensions)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        catch(dimensions)
        processed_img = cv2.Canny(frame, threshold1=100, threshold2=350)
        catch(dimensions)
        vertices = np.array([[0, 65], [0, 0], [460, 0], [460, 65],
                             ], np.int32)
        catch(dimensions)
        processed_img = roi(processed_img, [vertices], dimensions)
        catch(dimensions)
        cv2.imshow("Capture", processed_img)
        catch(dimensions)
        # PyTesseract
        myText = pytesseract.image_to_string(processed_img, config=config)
        catch(dimensions)
        if identify(myText):
            print("Prompt detected: Casting line...")
            keyDown('e')
            time.sleep(3)
            keyUp('e')
            print("And now we wait...")
        catch(dimensions)

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
