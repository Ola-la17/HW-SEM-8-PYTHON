ratio: float

MWW = MAIN_WINDOW_WIDTH = 400
MWH = MAIN_WINDOW_HEIGHT = 820

AWW = ADD_WINDOW_WIDTH = 500
AWH = ADD_WINDOW_HEIGHT = 200

BS = BUTTON_SIZE = 80

def get_screen_ratio():
    return

def get_screen_size(window):
    global ratio
    ratio = window.winfo_screenheight() / (MWH + MWH * 0.2)
    return f'{int(MWW * ratio)}x{int(MWH * ratio)}' 

def get_dialog_window_size():
    return f'{int(AWW * ratio)}x{int(AWH * ratio)}'

def get_button_size():
    global ratio
    return (f'{int(BS * ratio)}')

def get_size(points: int):
    global ratio
    return f'{int(points * ratio)}'

def get_point(points: int):
    global ratio
    return int(points * ratio)

def get_int_size(size: int):
    global ratio
    return int(size * ratio)
