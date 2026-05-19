import pyautogui
import time
import threading
import sys

running = False


def mover(interval=30):
    while running:
        x, y = pyautogui.position()
        pyautogui.moveTo(x + 1, y)
        time.sleep(0.2)
        pyautogui.moveTo(x, y)
        time.sleep(interval)


def start(interval=30):
    global running
    if running:
        return
    running = True
    t = threading.Thread(target=mover, args=(interval,), daemon=True)
    t.start()
    print(f"StayAwake started (jiggle every {interval}s). Move mouse to top-left corner to failsafe.")


def stop():
    global running
    running = False
    print("Stopped.")


if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.1

    interval = 30
    if len(sys.argv) > 1:
        try:
            interval = int(sys.argv[1])
        except ValueError:
            print(f"Invalid interval '{sys.argv[1]}', using 30s.")

    start(interval)
    print("Ctrl+C to stop.")

    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, pyautogui.FailSafeException):
        stop()
        sys.exit()
