from Library import *
from MainMenu import *
from SplashScreen import *
from GamePlay import * 

#Khởi tạo game 
pg.init()

# Có thể sửa (Nhưng báo trước nội dung sửa để đồng bộ lại)
class Game:
    def __init__(self):
        self.state = SplashScreen(self)  # Màn hình chớp giật
        self.current_state = SPLASH_SCREEN
        self.game_data = {}
        self.game_data[table_size] = 16
        self.game_data[main_volume] = 0.5
        self.game_data[is_single] = True

    def change_state(self, new_state):

        if new_state == SPLASH_SCREEN:
            self.state = SplashScreen(self)
        elif new_state == MAIN_MENU:
            self.state = MainMenu(self)
        elif new_state == EXIT_SIGN:
            pg.quit()
            sys.exit()
        elif new_state == SETTINGS:
            #self.state = Settings(self)
            pass
        elif new_state == GAME_PLAYING:
            self.state = GamePlay(self)
        self.current_state = new_state

    def handle_input(self, event):
        self.state.handle_input(event)  # Gọi handle_input của trạng thái hiện tại

    def update(self):
        self.state.update()  # Cập nhật trạng thái game

    def draw(self):
        self.state.draw()  # Vẽ giao diện của trạng thái hiện tại
        
    def set_data(self, key, value):
        """Cập nhật dữ liệu trò chơi."""
        self.game_data[key] = value

    def get_data(self, key):
        """Lấy dữ liệu trò chơi."""
        return self.game_data.get(key)


#Không đc sửa bất kì cái gì trong def main()
def main():
    game = Game()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            game.handle_input(event)
        
        game.update()
        game.draw()

        pg.display.update()

if __name__ == "__main__":
    main()