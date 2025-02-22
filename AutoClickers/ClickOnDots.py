from time import sleep

import pyautogui as pt


class Clicker:
    def __init__(self, target, duration):
        self.duration = duration
        self.target = target
        pt.FAILSAFE = True  

    def navToImag(self):
        try:
            pos = pt.locateOnScreen(self.target, confidence=0.8)  # Try 0.8 or 0.9
            if pos is None:
                print("Failed to detect anything")
                return 0
            
            pt.moveTo(pos.left + 10, pos.top + 10, duration=self.duration)
            print("Found one")
            pt.click()
            return 1
        except Exception as e:
            print(f"Error: {e}")
            return 0

if __name__ == '__main__':
    sleep(2)
    button = Clicker("D:/Python/AutoClickers/target.png", duration=0.001)

    flag = 0
    while True:
        if not button.navToImag():
            flag += 1
        if flag > 200:
            break
