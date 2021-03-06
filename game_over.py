import time
import sys
def game_over():
    text = "Game Over\n"
    for char in text:
        sys.stdout.write(char)
        time.sleep(0.5)


    time.sleep(10)
    sys.exit()