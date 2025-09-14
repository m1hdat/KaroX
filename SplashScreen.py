from Library import *
from ClassGameState import GameState

class SplashScreen(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.Logo_Image = pg.image.load(Logo_Link)
        self.Logo_Image = pg.transform.scale(self.Logo_Image, (444,167))
        self.Logo_Image_rect = self.Logo_Image.get_rect()
        self.Logo_Image_rect.center = Center_pos
        self.font = pg.font.SysFont(font_link, 25)
        self.PressKey = self.font.render("Press any key to continue.....!", True, white)
        self.PressKey_rect = self.PressKey.get_rect()
        self.PressKey_rect.center = (main_width / 2, main_height / 2 + 60)
        self.Logo_Visible = True

        self.LastedTime = pg.time.get_ticks()
        self.blink_time = 500

    def handle_input(self, event):
        if event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN:
            self.game.change_state(MAIN_MENU)

    def update(self):
        currentTime = pg.time.get_ticks()
        if (currentTime - self.LastedTime >= self.blink_time): 
            self.Logo_Visible = not self.Logo_Visible
            self.LastedTime = currentTime

    def draw(self):
        screen.fill(black)
        screen.blit(self.Logo_Image, (main_width / 2 - 222, main_height / 2 - 120))

        if self.Logo_Visible == True:
            screen.blit(self.PressKey, self.PressKey_rect)        

# Đã hoàn thành 
# Nếu có đóng góp ý kiến thì nhắn lên nhóm