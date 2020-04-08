import pyautogui
import cv2
import secrets
import time
import os

def main():
    #Avoid to make same name picture
    filename="screen_shot_"+secrets.token_hex()+".jpg"
    screen_shot_picture=pyautogui.screenshot(filename)
    img=cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    img=cv2.flip(img,1)
    cv2.imshow("image",img)
    cv2.moveWindow("image", 0,0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()