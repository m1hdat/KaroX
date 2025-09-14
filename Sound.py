import pygame as pg # type: ignore

# Khởi tạo Pygame
pg.init()

# Khởi tạo mixer để xử lý âm thanh
pg.mixer.init()

# Tải âm thanh
pg.mixer.music.load("Resources/background_sound.mp3")           # Nhạc nền
sound_xo = pg.mixer.Sound("Resources/XO_tick_sound.mp3")        # Âm thanh đánh XO
sound_win = pg.mixer.Sound("Resources/Winning_sound.mp3")       # Nhạc chiến thắng
sound_click = pg.mixer.Sound("Resources/mouse_click_sound.mp3") # Âm thanh click chuột

# Giá trị mặc định cho âm lượng
default_music_volume = 0.5
default_effect_volume = 0.5

# Cài đặt âm lượng mặc định cho các hiệu ứng âm thanh
sound_xo.set_volume(0.3 * default_effect_volume)
sound_win.set_volume(default_effect_volume)
sound_click.set_volume(default_effect_volume)

# Hàm phát nhạc nền với âm lượng tùy chỉnh
def play_background_music(volume = default_music_volume):
    pg.mixer.music.set_volume(volume)  # Đặt âm lượng nhạc nền
    pg.mixer.music.play(-1)            # Phát nhạc nền lặp vô hạn

# Hàm dừng nhạc nền
def stop_background_music():
    pg.mixer.music.stop()

# Hàm phát âm thanh khi đánh XO với âm lượng tùy chỉnh
def play_sound_xo(volume = default_effect_volume):
    sound_xo.set_volume(volume)
    sound_xo.play()

# Hàm phát nhạc chiến thắng với âm lượng tùy chỉnh
def play_win_sound(volume = default_effect_volume):
    sound_win.set_volume(volume)
    sound_win.play()

# Hàm phát âm thanh click chuột với âm lượng tùy chỉnh
def play_click_sound(volume = default_effect_volume):
    sound_click.set_volume(volume)
    sound_click.play()