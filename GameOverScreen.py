from Library import *
from GamePlay import * 
from MainMenu import *

def print_game_over_screen (screen, check_win, self_round):

    # print(check_win)
    # Xuất ra kết quả dựa trên check_win 
    if check_win == 0:
        return # GamePlay()
    elif check_win == 1:
        result_text = "Player X Won!"
    elif check_win == 2:
        result_text = "Player O Won!"
    else:
        result_text = "It's a Draw!"

    screen.blit(game_over_tab, (0, 0))
    font = pg.font.Font(font_link, 36)

    # Hiển thị kết quả
    result_surface = font.render(result_text, True, (250,250,75))
    screen.blit(result_surface, (375, 175))

    # Hiển thị số vòng đã đấu
    round_surface = font.render(f"Rounds Played: {self_round}", True, black)
    screen.blit(round_surface, (350, 250))

    # Tạo nút quay về menu
    screen.blit(menu_button, (main_width / 2 - 105, main_height / 2 - 40  + 132))
    if (button_menu_clicked_1.on()) :
        button_menu_clicked_1.draw()

    # Quay về menu dựa nếu người chơi click chuột vào
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            # Gọi hàm Menu khi bấm nút
            if (button_menu_clicked_1.on()) :
                # print("to the menu!")
                return 1
            else :
                return 0
