from Library import *
from ClassGameState import *
from GameOverScreen import print_game_over_screen
from Sound import *

class GamePlay(GameState):
    def __init__(self, game):

        super().__init__(game)
        self.size_1_o = 640 / self.game.game_data[table_size]  #kích thước của 1 ô vuông
        # X, O, N đại diện cho 'x', 'o', 'n' được khai báo trong Library (ai đọc nhớ thêm vô trên máy mình)
        self.luu_ban_co = {} # dùng để lưu trạng thái bàn cờ nếu đánh X là X, ô đó đánh O là O, chưa đánh gì thì tọa độ đó là N
        for i in range(0, self.game.game_data[table_size] ):# gán N (none) cho tất cả
            for j in range(0, self.game.game_data[table_size]):
                self.luu_ban_co[(i, j)] = N #none
        self.luu_o_phu = (-1, -1) # dùng để lưu ô chứa ảnh X hay O mờ
        self.flag = X #check trạng thái hiện tại
        self.new_pos = [0,0]
        self.recent_move = [-1,-1] # lưu lại nước đi mới nhất
        self.click = 0 # xử lý chuột: 1 là click, 0 là chỉ di chuột
        self.round = 1 # đếm số round
        self.rosemary_font = pg.font.Font(font_link, 55)
        self.border = 2 # viền ngoài của chữ
        self.win_state = 0
        self.x_img = pg.transform.scale(x_img, (0.9 * self.size_1_o, 0.9 * self.size_1_o))
        self.o_img = pg.transform.scale(o_img, (0.9 * self.size_1_o, 0.9 * self.size_1_o))
        self.x_img2 = pg.transform.scale(x_img2, (0.9 * self.size_1_o, 0.9 * self.size_1_o))
        self.o_img2 = pg.transform.scale(o_img2, (0.9 * self.size_1_o, 0.9 * self.size_1_o))
        self.glow = pg.transform.scale(glow, (self.size_1_o, self.size_1_o))

    def handle_input(self, event):

        if self.win_state == 0 :
            self.new_pos = lam_tron_vi_tri_chuot(pg.mouse.get_pos(), self.size_1_o) # lấy tọa độ chuột hiện tại
            
            # nếu có thắc mắc thì xem lại def lam_tron_vi_tri_chuot ở dưới
            # nếu click chuột thì self.click = 1 và không click là 0:
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                play_sound_xo()
                if button_menu_clicked_0.on() :
                    self.game.change_state(MAIN_MENU)
                self.click = 1
            else:
                self.click = 0

        if event.type == pg.KEYDOWN:     
            if event.key == pg.K_ESCAPE:
                self.game.change_state(MAIN_MENU)
        
    def update(self):

        self.text_surface_main = self.rosemary_font.render(str(self.round), True, (250,250,75))
        self.text_surface_sub = self.rosemary_font.render(str(self.round), True, (240,150,0))

        if self.new_pos[0] >= self.game.game_data[table_size] or self.win_state != 0 : #nếu nằm ngoài bàn cờ hoặc trò chơi đã kết thúc
            self.luu_o_phu = (-1, -1)
            return
        else : # nếu nằm trong
            if self.click == 1: #nếu là click
                if self.luu_ban_co[(self.new_pos[0], self.new_pos[1])] == N: #nếu ô đó là N (chưa được đánh)
                    self.luu_ban_co[self.new_pos] = self.flag # đánh dấu ô đó là flag (flag là trạng thái nước đi hiện tại)
                    self.recent_move = self.new_pos
                    self.win_state = (check_win(self.luu_ban_co, self.new_pos[0], self.new_pos[1]))
                    if self.win_state != 0 : play_win_sound()

                    if self.flag == O:
                        self.round += 1 #tăng ruond lên
                    self.flag = O if self.flag == X else X # đổi trạng thái
                    self.luu_o_phu = (-1, -1) # Không có ô nào đang mờ nên gán (-1, -1)
            else: # nếu chỉ là di chuột
                if self.luu_ban_co[(self.new_pos[0], self.new_pos[1])] == N:
                    self.luu_o_phu = self.new_pos
                else:
                    self.luu_o_phu = (-1, -1)

    def draw(self):

        pg.display.set_caption("KaroX : Gameplay")

        screen.blit(ban_co,(0,0)) #reset lại màn hình sau mỗi khung

        offset = 3 * self.size_1_o / 40

        if self.recent_move != (-1,-1) :
            screen.blit(self.glow,(self.recent_move[0] * self.size_1_o, self.recent_move[1] * self.size_1_o))
            
        for i in range(0, self.game.game_data[table_size] + 1) :
            screen.blit(ver_line, (i * (640 / self.game.game_data[table_size] ) - 10, 0))
            screen.blit(hor_line, (0, i * (640 / self.game.game_data[table_size] ) - 10))

        screen.blit(menu_button, (800 - 105, 545))
        if button_menu_clicked_0.on() :
            button_menu_clicked_0.draw()

        for (a, b) in self.luu_ban_co :
            if self.luu_ban_co[(a, b)] == X :
                screen.blit(self.x_img, (a * self.size_1_o + offset, b * self.size_1_o + offset))
            elif self.luu_ban_co[(a, b)] == O :
                screen.blit(self.o_img, (a * self.size_1_o + offset, b * self.size_1_o + offset))
        if self.luu_o_phu != (-1,-1) :
            if self.flag == X:
                screen.blit(self.x_img2,(self.luu_o_phu[0] * self.size_1_o + offset, self.luu_o_phu[1] * self.size_1_o + offset))
            else:
                screen.blit(self.o_img2, (self.luu_o_phu[0] * self.size_1_o + offset, self.luu_o_phu[1] * self.size_1_o + offset))
        
        if self.round < 10 :
            offset = 8
        elif self.round < 100 :
            offset = 0
        else : 
            offset = -12
        screen.blit(self.text_surface_sub, (850 - self.border + offset, 43 - self.border))
        screen.blit(self.text_surface_sub, (850 - self.border + offset, 43 + self.border))
        screen.blit(self.text_surface_sub, (850 + self.border + offset, 43 - self.border))
        screen.blit(self.text_surface_main, (850 + offset, 43))   

        if self.flag == X: #Bat mau chu player
            screen.blit(p1_selected, (640 - 15, 190 - 55))
            screen.blit(p2_nametag, (650, 290 - 50))
        else:
            screen.blit(p1_nametag, (650, 190 - 50))
            screen.blit(p2_selected, (640 - 15, 290 - 55))

        if print_game_over_screen(screen,self.win_state,self.round) == 1 :
            self.game.change_state(MAIN_MENU)

def lam_tron_vi_tri_chuot(pos, t) : # t đại diện cho self.size_1_o có nghĩa là kích thước 1 ô
        x = int (pos[0] / t)
        y = int (pos[1] / t)
        return (x, y)

# Hàm check_win được gọi khi có 1 người chơi thực hiện 1 nước đi
# Truyền vào hàm bàn cờ đang đánh và tọa độ người chơi vừa đánh
# nếu X thắng thì trả về 1
# nếu O thắng thì trả về 2
# nếu chưa có ai thắng thì trả về 0
# không trả về kết quả hòa vì sẽ làm chậm tốc độ check

def check_win(ban_co : dict, x, y):
    x0, y0 = x, y
    for xm,ym in huong:
        count = 0
        x, y = x0, y0
        while(True):
            x += xm
            y += ym
            if(count == 4):
                return 1 if ban_co[(x0, y0)] == X else 2
            if (x, y) not in ban_co or ban_co[(x, y)] != ban_co[(x0, y0)]:
                break
            if ban_co[(x, y)] == N:
                break
            count += 1
        x, y = x0, y0
        while(True):
            x -= xm
            y -= ym
            if(count == 4):
                return 1 if ban_co[(x0, y0)] == X else 2
            if (x, y) not in ban_co or ban_co[(x, y)] != ban_co[(x0, y0)]:
                break
            if ban_co[(x, y)] == N:
                break
            count += 1
    return 0