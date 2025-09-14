import pygame as pg
from MainMenu import *
from Sound import *

def change_volume_with_mouse(file_path):
    try:
        pg.init()
        screen = pg.display.set_mode((960, 640))
        pg.display.set_caption("KaroX : Settings")

        running = True
        volume = 0.5 # = self.game.game_data[main_volume] Giá trị âm lượng mặc định
        font = pg.font.Font(None, 36)
        flag = False
        (x, y) = (0, 0)



        while running:
            for event in pg.event.get():
                
                if flag :
                    (x, y) = event.pos

                if event.type == pg.QUIT:
                    running = False

                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    flag = True

                elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
                    flag = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:  # Nhấn Enter để quay lại Menu
                        print(f"Returning to Menu with volume: {volume:.2f}")
                        return volume

            if flag and x > 450 and y > 162 and y < 242 :
                volume = (x - 480) / 301  # Tỉ lệ hóa giá trị x để điều chỉnh âm lượng
                volume = max(0.0, min(1.0, volume))  # Đảm bảo âm lượng nằm trong khoảng 0.0 - 1.0
                pg.mixer.music.set_volume(volume)
                #self.game.game_data[main_volume] = volume

            # Vẽ giao diện
            screen.blit(settings_menu, (0,0))
            screen.blit(settings_button, (480 - 250, 10))

            # Thanh âm lượng
            volume_bar = pg.Rect(480, 195, int(volume * 301), 14)
            pg.draw.rect(screen, (235,150,45), volume_bar)

            """# Thêm chữ "Volume" cạnh thanh âm lượng
            volume_label = font.render("Volume", True, (255, 255, 255))
            screen.blit(volume_label, (50, 70))"""

            # Hiển thị thông báo
            text = font.render("Press Enter to Start the Game!", True, (255, 255, 255))
            screen.blit(text, (20, 600))

            # Hien thi dau tick cua table size
            #if self.game.game_data[table_size] == 16 :
            screen.blit(tick, (505 + 190 + 195, 285))

            pg.display.flip()

        return volume

    except Exception as e:
        print(f"Error: {e}")
        return 0.5  # Trả về giá trị mặc định nếu lỗi