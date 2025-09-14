import pygame as pg # type: ignore
import sys
import time

#Kích thước cửa sổ
main_width = 960
main_height = 640

#Luồng màn hình
screen = pg.display.set_mode((main_width,main_height))

#Các biến toàn cục toàn bộ chương trình
table_size = "table_size" # table_size = n tức là bàn cờ có kích thước nxn
main_volume = "main_volume"
is_single = "is_single"

#Links image
#Cú pháp tên Link = <Tên File sẽ link> + _link 
Logo_Link = "Resources/Logo KaroX.png"
background_link = "Resources/menu_background.png"
game_over_tab_link = "Resources/Game Over Tab.png"

start_button_link = "Resources/Start.png"
start_clicked_link = "Resources/Start (clicked).png"
settings_button_link = "Resources/Settings.png"
settings_clicked_link = "Resources/Settings (clicked).png"
quit_button_link = "Resources/Quit.png"
quit_clicked_link = "Resources/Quit (clicked).png"
menu_button_link = "Resources/Menu.png"
menu_clicked_link = "Resources/Menu clicked.png"
credits_button_link = "Resources/Credits.png"
credits_clicked_link = "Resources/Credits clicked.png"

ban_co_link = "Resources/Blank_Chessboard.png"
settings_menu_link = "Resources/Settings_Menu.png"
line_link = "Resources/Line.png"
tick_link = "Resources/tick.png"

x_img_link = "Resources/X.png"
x_img2_link = "Resources/X (clicked).png"
o_img_link = "Resources/O.png"
o_img2_link = "Resources/O (clicked).png"
glow_link = "Resources/Glow.png"

p1_nametag_link = "Resources/P1 nametag.png"
p2_nametag_link = "Resources/P2 nametag.png"
p1_selected_link = "Resources/P1 nametag selected.png"
p2_selected_link = "Resources/P2 nametag selected.png"

font_link = "Resources/Rosemary.ttf"

background_sound_link = "Resources/background_sound.mp3"
mouse_click_sound_link = "Resources/mouse_click_sound.mp3"
XO_tick_sound_link = "Resources/XO_tick_sound.mp3"
Winning_sound_link = "Resources/Winning_sound.mp3"
mouse_move_sound_link = "Resources/mouse_move_sound.mp3"

#Đồ họa
background = pg.image.load(background_link)
game_over_tab = pg.image.load(game_over_tab_link).convert_alpha()

start_button = pg.transform.scale(pg.image.load(start_button_link).convert_alpha(), (500,125))
start_clicked = pg.transform.scale(pg.image.load(start_clicked_link).convert_alpha(), (520,130))
settings_button = pg.transform.scale(pg.image.load(settings_button_link).convert_alpha(), (500,125))
settings_clicked = pg.transform.scale(pg.image.load(settings_clicked_link).convert_alpha(), (520,130))
quit_button = pg.transform.scale(pg.image.load(quit_button_link).convert_alpha(), (500,125))
quit_clicked = pg.transform.scale(pg.image.load(quit_clicked_link).convert_alpha(), (520,130))
menu_button = pg.transform.scale(pg.image.load(menu_button_link).convert_alpha(), (210,80))
menu_clicked = pg.transform.scale(pg.image.load(menu_clicked_link).convert_alpha(), (230,88))
credits_button = pg.transform.scale(pg.image.load(credits_button_link).convert_alpha(), (500,125))
credits_clicked = pg.transform.scale(pg.image.load(credits_clicked_link).convert_alpha(), (520,130))

ban_co = pg.image.load(ban_co_link)
settings_menu = pg.image.load(settings_menu_link)
hor_line = pg.transform.scale(pg.image.load(line_link).convert_alpha(), (640,20))
ver_line = pg.transform.rotate(hor_line, 90)
tick = pg.transform.scale(pg.image.load(tick_link).convert_alpha(), (50, 50))

x_img = pg.image.load(x_img_link).convert_alpha()
x_img2 = pg.image.load(x_img2_link).convert_alpha()
o_img = pg.image.load(o_img_link).convert_alpha()
o_img2 = pg.image.load(o_img2_link).convert_alpha()
glow = pg.image.load(glow_link).convert_alpha()

p1_nametag = pg.transform.scale(pg.image.load(p1_nametag_link).convert_alpha(), (300,100))
p2_nametag = pg.transform.scale(pg.image.load(p2_nametag_link).convert_alpha(), (300,100))
p1_selected = pg.transform.scale(pg.image.load(p1_selected_link).convert_alpha(), (330,110))
p2_selected = pg.transform.scale(pg.image.load(p2_selected_link).convert_alpha(), (330,110))

# Màu sắc
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# Trạng thái menu
SPLASH_SCREEN = 0
MAIN_MENU = 1
GAME_PLAYING = 2
GAME_OVER = 3
PAUSE = 4
SETTINGS = 5
INSTRUCTIONS = 6
EXIT_SIGN =-1

# Center pos 
Center_pos = (main_width / 2, main_height / 2)

# Thiết lập đồng hồ 
clock = pg.time.Clock()

# Thời gian chớp tắt (ms)
blink_time = 500

class button:
    def __init__(self,rect:pg.Rect,image:pg.Surface):
        self.rect = rect
        self.img = image
    def draw(self):
        screen.blit(self.img,(self.rect[0],self.rect[1]))
    def on(self,):
        return self.rect.collidepoint(pg.mouse.get_pos())

#Khai báo các class button cần dùng, cú pháp button_<tên nút>
button_start_clicked = button(pg.Rect(main_width / 2 - 260, main_height / 2 - 100, 520, 110), start_clicked)
button_credits_clicked = button(pg.Rect(main_width / 2 - 260, main_height / 2 + 20, 520, 110), credits_clicked)
button_quit_clicked = button(pg.Rect(main_width / 2 - 260, main_height / 2 + 140, 520, 110), quit_clicked)
button_menu_clicked_0 = button(pg.Rect(800 - 115, 540, 230, 88), menu_clicked)
button_menu_clicked_1 = button(pg.Rect(main_width / 2 - 115, main_height / 2 - 44 + 132, 230, 88), menu_clicked)

#Khai báo các biến liên quan đến bàn cờ
X = 'x'
O = 'o'
N = 'n'
doi_co = {N:N,X:O,O:X}
huong = [(1,1),(-1,1),(1,0),(0,-1)]

# Chỉ thêm vào những class hay source ứng dụng cho all project