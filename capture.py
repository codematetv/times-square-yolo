import numpy as np
import win32gui, win32ui, win32con, win32api
from PIL import Image
import pyautogui,time
import cv2 as cv

#https://timgolden.me.uk/pywin32-docs/contents.html

class WindowCapture:
    #w = 311
    #h = 134
    #l = 18
    t = 163

    w = 957
    h = 950
    l = 0
    t = 85
    
    hwnd = None

    def __init__(self, window_name):

        self.hwnd = win32gui.GetDesktopWindow()

    def get_screenshot(self):

        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)

        cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (self.l, self.t), win32con.SRCCOPY)

        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.frombuffer(signedIntsArray, dtype='uint8')

        # opencv now understands
        img.shape = (self.h, self.w, 4)

        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        #REMOVING ALPHA CHANEEL 
        img = img[...,:3]
        img = np.ascontiguousarray(img) 
        return img

    def test(self):
        while 1:
            img = self.get_screenshot()
            cv.imshow("Desktop", img)

            if cv.waitKey(1) & 0xFF == ord("q"):
                break

    @staticmethod
    def get_coordinates(path):
        time.sleep(8)
        print(pyautogui.locateOnScreen(path, confidence = 0.9))

#WindowCapture.get_coordinates("Capture.png")

#wincap = WindowCapture('Desktop')
#wincap.test()

