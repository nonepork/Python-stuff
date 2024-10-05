from pynput import keyboard
from pynput.keyboard import Controller

english_to_arabic = {
    'a': 'ا', 'b': 'ب', 'c': 'ت', 'd': 'ث', 'e': 'ج', 'f': 'ح', 'g': 'خ',
    'h': 'د', 'i': 'ذ', 'j': 'ر', 'k': 'ز', 'l': 'س', 'm': 'ش', 'n': 'ص',
    'o': 'ض', 'p': 'ط', 'q': 'ظ', 'r': 'ع', 's': 'غ', 't': 'ف', 'u': 'ق',
    'v': 'ك', 'w': 'ل', 'x': 'م', 'y': 'ن', 'z': 'ه'
}

def keyboard_listener():
    global listener
    def on_press(key):
        try:
            if key.char.lower() in english_to_arabic:
                keyboard_controller = Controller()
                keyboard_controller.type(english_to_arabic[key.char.lower()])
        except AttributeError:
            pass

    def on_release(key):
        if key == keyboard.Key.esc:
            return False

    def win32_event_filter(msg, data):
        if (msg == 257 or msg == 256) and 65 <= data.vkCode and data.vkCode <= 90:
            listener._suppress = True
        else:
            listener._suppress = False
        return True

    return keyboard.Listener(
        on_press = on_press,
        on_release = on_release,
        win32_event_filter=win32_event_filter,
    )

listener = keyboard_listener()

if __name__ == '__main__':
    with listener as ml:
        ml.join()
