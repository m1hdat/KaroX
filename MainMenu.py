from Library import *
from ClassGameState import * 
from Sound import *
from VolumeChange import change_volume_with_mouse
import math

class MainMenu(GameState):
    # Chạy nhạc nền với âm lượng mặc định
    default_volume = 0.5

    def __init__(self, game):

        super().__init__(game)
        self.font = pg.font.SysFont(font_link, 20)
        self.chosen = 0
        self.menu_items = [(start_button, start_clicked), (settings_button, settings_clicked), (quit_button, quit_clicked)]
        self.logo = pg.transform.scale(pg.image.load(Logo_Link), (444, 167))
        self.volume = MainMenu.default_volume  # Lưu âm lượng hiện tại
        self.open_credits = False
        self.names = ["Project KaroX - Nhóm 2 :", "- Phạm Minh Đạt", "- Lê Hoài Tuấn Khang", "- Nguyễn Phước Khang", "- Lê Minh Trí", "- Võ Đình Trường"]
        play_background_music(self.volume)  # Phát nhạc nền với âm lượng mặc định

    def handle_input(self, event):

        if event.type == pg.KEYDOWN:
            self.game.game_data[table_size] = 30
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if button_start_clicked.on() and not self.open_credits :
                    play_sound_xo(self.volume)  # Sử dụng âm lượng hiện tại
                    pg.mixer.music.stop()
                    self.volume = change_volume_with_mouse("Resources/background_sound.mp3")
                    play_background_music(self.volume)  # Áp dụng âm lượng mới
                    self.game.change_state(GAME_PLAYING)
                
                if button_credits_clicked.on() and not self.open_credits :
                    play_sound_xo(self.volume)  # Sử dụng âm lượng hiện tại
                    self.open_credits = True
                    
                if button_quit_clicked.on() and not self.open_credits :
                    play_sound_xo(self.volume)  # Sử dụng âm lượng hiện tại
                    self.game.change_state(EXIT_SIGN)

                if button_menu_clicked_1.on() : 
                    play_sound_xo(self.volume)
                    self.open_credits = False

    def draw(self):

        pg.display.set_caption("KaroX : Menu")
        offset = int(5 * math.sin(pg.time.get_ticks() / 300))
        screen.blit(background, (0,0))
        screen.blit(self.logo, ((main_width / 2 - 222, 50 + offset)))
        screen.blit(start_button, (main_width / 2 - 250, main_height / 2 - 100))
        screen.blit(credits_button, (main_width / 2 - 250, main_height / 2 + 20))
        screen.blit(quit_button, (main_width / 2 - 250, main_height / 2 + 140))

        if button_start_clicked.on() and not self.open_credits :
            button_start_clicked.draw()
        if button_credits_clicked.on() and not self.open_credits :
            button_credits_clicked.draw()
        if button_quit_clicked.on() and not self.open_credits :
            button_quit_clicked.draw()

        if self.open_credits :
            screen.blit(game_over_tab, (0, 0))
            font = pg.font.Font(font_link, 45)

            # Hiển thị credits
            tab_text = "Credits"
            tab_surface = font.render(tab_text, True, (250,250,75))
            screen.blit(tab_surface, (405, 175))

            font = pg.font.Font(font_link, 25)

            # Hiển thị tên
            for i in range(0,6) :
                names_surface = font.render(self.names[i], True, black)
                screen.blit(names_surface, (300, 245 + 26 * i))

            # Tạo nút quay về menu
            screen.blit(menu_button, (main_width / 2 - 105, main_height / 2 - 40  + 132))
            if button_menu_clicked_1.on() :
                button_menu_clicked_1.draw()

        """ # Màu xanh là hàm muốn chọn, trắng là được chọn
        for i, item in enumerate(self.menu_items):
            if i == self.chosen :
                selection = 1
            else : selection = 0
            #text = font.render(item, True, color)
            #text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 60))
            screen.blit(item[selection], (main_width / 2 - 250, main_height / 2 + (i - 1) * 100)) """

