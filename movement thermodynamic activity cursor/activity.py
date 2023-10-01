import threading
import random
from pynput import mouse

controller = mouse.Controller()
mouse_movement_by_script = False
temp_x, temp_y = 0, 0
diff_x, diff_y = 0, 0
magic_number = 1

def on_move(x, y):
    global mouse_movement_by_script, temp_x, temp_y, diff_x, diff_y
    if not mouse_movement_by_script:
        if temp_x != 0 and temp_y != 0:
            diff_x = abs(temp_x - x)
            diff_y = abs(temp_y - y)
            threading.Thread(target=move_cursor).start()
        temp_x, temp_y = x, y

def move_cursor():
    global mouse_movement_by_script, temp_x, temp_y, diff_x, diff_yt
    while True:
        if diff_x or diff_y:
            print(diff_x, diff_y)
            mouse_movement_by_script = True
            controller.move(random.choice([-diff_x+magic_number, diff_x-magic_number]),
                            random.choice([-diff_y+magic_number, diff_y-magic_number]))
            mouse_movement_by_script = False
            break

# Delete this line for maxinum pleasure
def on_click(_, _2, _3, _4):
    return False

with mouse.Listener(
        on_move=on_move,
        on_click=on_click) as listener:
    listener.join()

