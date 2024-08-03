import random

import pygame

pygame.init()

# Window init :
res = (1248, 672)
color_window = (0, 0, 0)
pygame.display.set_caption("LE PONDUE")
game_window = pygame.display.set_mode(res)
game_window.fill(color_window)
row_tiles = int(672/32)
col_tiles = int(1248/32)

# init image :
# background element :
background = pygame.image.load("images\\Background\\BG Image.png")
sky = pygame.image.load("images\\Background\\Additional Sky.png")
water = pygame.image.load("images\\Background\\Additional Water.png")

clouds = []
for i in range(3):
    clouds.append(pygame.image.load("images\\Background\\Small Cloud "+str(i+1)+".png"))

water_reflection = []
for i in range(4):
    water_reflection.append(pygame.image.load("images\\Background\\Water Reflect Small 0"+str(i+1)+".png"))

for i in range(4):
    water_reflection.append(pygame.image.load("images\\Background\\Water Reflect Medium 0"+str(i+1)+".png"))

for i in range(4):
    water_reflection.append(pygame.image.load("images\\Background\\Water Reflect Big 0"+str(i+1)+".png"))

# Banner element :
banner_tiles = []
for i in range(33):
    banner_tiles.append(pygame.image.load("images\\Big Banner\\"+str(i+1)+".png"))

banner_menu = pygame.image.load("banner map\\banner menu.png")
banner_stat = pygame.image.load("banner map\\stat banner.png")
banner_word = pygame.image.load("banner map\\banner word.png")

banner_nbr = 3
banner_index = 0
banner_line_index = [19, 11, 19]
banner_image = [banner_menu, banner_stat, banner_word]
banner_type = []
banner_tiles_nbr = []
for k in range(banner_nbr):
    banner_map = []
    temp_nbr = 0
    for i in range(row_tiles):
        for j in range(col_tiles):
            color = banner_image[k].get_at([j, i])
            if color.g != 255:
                temp_nbr += 1
                banner_index = int(color.g/7)
                banner_map.append(banner_index)
    banner_tiles_nbr.append(temp_nbr)
    banner_type.append(banner_map)


def draw_banner(banner_type_index, posX, posY):
    for i in range(banner_tiles_nbr[banner_type_index]):
        left = int(i % banner_line_index[banner_type_index])
        top = int(i / banner_line_index[banner_type_index])
        game_window.blit(banner_tiles[banner_type[banner_type_index][i]], [posX + left*32, posY + top*32])


# board element :
board_tiles = []
for i in range(16):
    board_tiles.append(pygame.image.load("images\\Yellow Board\\"+str(i+1)+".png"))

board_nbr = 3
board_index = 0
board_line_index = [9, 8, 17]
board_menu = pygame.image.load("board map\\board menu.png")
board_play = pygame.image.load("board map\\play board 1.png")
board_play_2 = pygame.image.load("board map\\play board 2.png")
board_image = [board_menu, board_play, board_play_2]
board_type = []
board_tiles_nbr = []
for k in range(board_nbr):
    board_map = []
    temp_nbr = 0
    for i in range(row_tiles):
        for j in range(col_tiles):
            color = board_image[k].get_at([j, i])
            if color.b != 255:
                temp_nbr += 1
                board_index = int(color.b/15)
                board_map.append(board_index)
    board_tiles_nbr.append(temp_nbr)
    board_type.append(board_map)


def draw_board(board_type_index, posX, posY):
    for i in range(board_tiles_nbr[board_type_index]):
        left = int(i % board_line_index[board_type_index])
        top = int(i / board_line_index[board_type_index])
        game_window.blit(board_tiles[board_type[board_type_index][i]], [posX + left*32, posY + top*32])


# init terrain element :
terrain = pygame.image.load("images\\Terrain\\Terrain (32x32).png")
terrain_tiles = []
for i in range(5):
    for j in range(17):
        terrain_tiles.append(terrain.subsurface([j*32, i*32, 32, 32]))

# init pirates :
captain = []
for i in range(32):
    captain.append(pygame.image.load("images\\pirate\\captain\\"+str(i+1)+".png"))

big_guy = []
for i in range(38):
    big_guy.append(pygame.image.load("images\\pirate\\big guy\\idle\\"+str(i+1)+".png"))

small_guy = []
for i in range(34):
    small_guy.append(pygame.image.load("images\\pirate\\small guy\\idle\\"+str(i+1)+".png"))

# init player:
player_idle = []
for i in range(36):
    player_idle.append(pygame.image.load("images\\player\\cuncomber\\idle\\"+str(i+1)+".png"))

player_dead = []
for i in range(6):
    player_dead.append(pygame.image.load("images\\player\\cuncomber\\Dead Hit\\"+str(i+1)+".png"))

# init bomb
bomb_off = pygame.image.load("images\\bomb\\1-Bomb Off\\1.png")

bomb_on = []
for i in range(10):
    bomb_on.append(pygame.image.load("images\\bomb\\2-Bomb On\\"+str(i+1)+".png"))

explotion = []
for i in range(9):
    explotion.append(pygame.image.load("images\\bomb\\3-Explotion\\"+str(i+1)+".png"))

# init button :
# menu :
menu_b = pygame.image.load("images\\button\\button_atlas.png")

play_b = []
play_b_used = False
play_b_hitbox = pygame.Rect(24*32, 9*32, 160, 64)
for i in range(3):
    play_b.append(menu_b.subsurface([i*160, 0, 160, 64]))

option_b = []
option_b_used = False
option_b_hitbox = pygame.Rect(24*32, 12*32, 160, 64)
for i in range(3):
    option_b.append(menu_b.subsurface([i*160, 64, 160, 64]))

quit_b =[]
quit_b_used = False
quit_b_hitbox = pygame.Rect(24*32, 15*32, 160, 64)
for i in range(3):
    quit_b.append(menu_b.subsurface([i*160, 128, 160, 64]))

# sound control:
sound_b = pygame.image.load("images\\button\\sound_button.png")
volume_control = pygame.image.load("images\\button\\volume_buttons.png")
volume_bar = volume_control.subsurface([84, 0, 215, 44])

music_b_hitbox = pygame.Rect(13*32, 9*32 + 5, 42, 42)
sfx_b_hitbox = pygame.Rect(13*32, 11*32 - 15, 42, 42)

volume_bar_slide_posX = 9*32 - 10 + volume_bar.get_width()/2 - 28/2
volume_bar_min = 9*32 - 10
volume_bar_max = 9*32 - 10 + volume_bar.get_width() - 28
volume_bar_slide_hitbox = pygame.Rect(volume_bar_slide_posX, 14*32 - 20, 28, 44)

music_is_on = True
sfx_is_on = True
music_b_used = False
sfx_b_used = False
volume_bar_is_sliding = False

sound_on = []
for i in range(3):
    sound_on.append(sound_b.subsurface([i*42, 0, 42, 42]))

sound_off = []
for i in range(3):
    sound_off.append(sound_b.subsurface([i*42, 42, 42, 42]))

volume_bar_slide = []
for i in range(3):
    volume_bar_slide.append(volume_control.subsurface([i*28, 0, 28, 44]))

# pause menu :
pause_menu = pygame.image.load("images\\pause_menu.png")
urm_b = pygame.image.load("images\\button\\urm_buttons.png")

stop_pause_b_hitbox = pygame.Rect(9*32 + 20, 15*32, 56, 56)
return_menu_hitbox = pygame.Rect(12*32 + 20, 15*32, 56, 56)

stop_pause_b = []
for i in range(3):
    stop_pause_b.append(urm_b.subsurface([i*56, 0, 56, 56]))

return_menu = []
for i in range(3):
    return_menu.append(urm_b.subsurface([i*56, 112, 56, 56]))

stop_pause_b_used = False
return_menu_used = False

# accessory :
barel = pygame.image.load("images\\accessory\\barel.png")
cannon = pygame.image.load("images\\accessory\\cannon.png")
chest = pygame.image.load("images\\accessory\\chest.png")

# level map :
level = pygame.image.load("level.png")
leve_height = level.get_height()
leve_width = level.get_width()
level_map = []
for i in range(leve_height):
    for j in range(leve_width):
        color = level.get_at([j, i])
        terrain_index = color.r/3
        level_map.append(terrain_index)


# init level display :
def draw_backgroud():
    # init background :

    for i in range(10):
        for j in range(col_tiles):
            game_window.blit(sky, [j*32, i*32])

    for i in range(row_tiles-14):
        for j in range(col_tiles):
            game_window.blit(water, [j*32, (i*32)+(14*32)])

    for i in range(4):
        game_window.blit(background, [i*384, 320])


draw_backgroud()


# init terrain :
def draw_level_map():
    for i in range(row_tiles):
        for j in range(col_tiles):
            tile_index = level_map[j + i*col_tiles]
            left = int(tile_index % 17)
            top = int(tile_index / 17)
            game_window.blit(terrain.subsurface(left*32, top*32, 32, 32), [j*32, i*32])

    # init decoration :

    game_window.blit(barel, [8*32 + 5, 14*32 + 5])
    game_window.blit(barel, [8*32 + 3 + barel.get_width(), 14*32 + 5])
    game_window.blit(cannon, [13*32 - 5, 14*32+7])
    game_window.blit(chest, [1*32, 10*32+1])
    game_window.blit(chest, [5*32 + 20, 17*32+1])
    game_window.blit(chest, [8*32 - 10, 17*32+1])
    game_window.blit(barel, [9*32 - 10, 17*32+5])


draw_level_map()

# int entity :
captain_index = 0
small_guy_index = 0
big_guy_index = 0
player_idle_index = 0

game_window.blit(captain[captain_index], [1*32 - 10, 6*32 - 7])
game_window.blit(big_guy[big_guy_index], [10*32 + 10, 13*32 - 9])
game_window.blit(small_guy[small_guy_index], [3*32 + 8, 13*32 - 3])
game_window.blit(player_idle[player_idle_index], [8*32, 6*32 - 3])

# init bomb :
game_window.blit(bomb_off, [6*32, 6*32 - 23])

pygame.display.flip()

#init player state :
p_alive = True
p_dead = False
player_dead_index = 0

#init entity state :
idle = False
captain_idle = False
big_guy_idle = False
small_guy_idle = False
player_idle_waiting = False

#init bomb state :
bomb_is_on = False
bomb_is_off = True
bomb_explotion = False

# init game state :
lunched = True
menu = True
playing = False
option = False
lost = False


#init button state comp:
button_up = False


def button_state(button_hitbox, mouse_pos):
    if button_hitbox.collidepoint(mouse_pos[0], mouse_pos[1]):
        if button_up:
            return 2
        else:
            return 1
    else:
        return 0


# key input :
game_pause = False

# init fonts :
text_black = (40, 40, 40)
text_white = (235, 235, 235)

font_title = pygame.font.Font("font\\JackPirate_PERSONAL_USE_ONLY.ttf", 90)
font_stat = pygame.font.Font("font\\JackPirate_PERSONAL_USE_ONLY.ttf", 24)
font_stat_title = pygame.font.Font("font\\JackPirate_PERSONAL_USE_ONLY.ttf", 38)
font_word = pygame.font.Font("font\\JackPirate_PERSONAL_USE_ONLY.ttf", 60)
nbr_font = pygame.font.Font("font\\Pirate Scroll.otf", 24)

name_game = font_word.render("W o r d s > o < R u s h", True, text_black)
option_title = font_title.render("O p t i o n", True, text_black)
stat_title = font_stat_title.render("S t a t :", True, text_black)
option_stat = font_stat.render("", True, text_white)
time = font_stat.render("Time passed :", True, text_white)
time_nbr = nbr_font.render("00:00:00", True, text_white)
try_left = font_stat.render("Try left :", True, text_white)
nbr_try_render = nbr_font.render("5", True, text_white)
best_score = font_stat.render("Best score :", True, text_white)
current_score = font_stat.render("Current score :", True, text_white)
current_score_nbr = nbr_font.render("0", True, text_white)
letters_used = font_stat.render("Letters used :", True, text_white)
word_render = font_word.render("", True, text_black)

# time calcul :
#def played_time(current_time_f):

# init files :
# init words list :


def init_words_list():
    words_list = []
    words_files = open("words.txt", "r")
    for i in range(1000):
        temp = words_files.readline()
        temp = temp.replace("â€™", "'")
        temp = temp[:-1]
        words_list.append(temp.strip().lower())
    words_files.close()
    return words_list

# init stats :

# init previous stats :


stat_files = open("stat.txt", "r")
time_played_previously = int(stat_files.readline())
best_score_nbr = int(stat_files.readline())
played_rounds = int(stat_files.readline())
rounds_won = int(stat_files.readline())
rounds_lost = int(stat_files.readline())
stat_files.close()


# init current stats :
def stat_write(time_played_total, best_score_played):
    stat_files = open("stat.txt", "w")
    stat_files.write(str(time_played_total) + "\n")
    stat_files.write(str(best_score_played) + "\n")
    stat_files.write(str(played_rounds) + "\n")
    stat_files.write(str(rounds_won) + "\n")
    stat_files.write(str(rounds_lost) + "\n")
    stat_files.close()


# init time calculation :
timer_start = 0
seconds = 00
minutes = 00
hours = 00


def timer(current_time, timer_start):
    seconds_nbr = ""
    minutes_nbr = ""
    hours_nbr = ""
    time_passed = int((current_time - timer_start) / 1000)
    seconds = time_passed % 60
    minutes = int((time_passed % 3600) / 60)
    hours = int(time_passed / 3600)
    if hours < 10:
        hours_nbr = "0" + str(hours)
    else:
        hours = str(hours)
    if minutes < 10:
        minutes_nbr = "0" + str(minutes)
    else:
        minutes_nbr = str(minutes)
    if seconds < 10:
        seconds_nbr = "0" + str(seconds)
    else:
        seconds_nbr = str(seconds)
    timer = hours_nbr + ":" + minutes_nbr + ":" + seconds_nbr
    return timer


# init primary values :
color = (135, 206, 235)
rand_cloud_list = []
clouds_posX = []
clouds_posY = []
clouds_nbr = 0
clouds_del_nbr = 0
water_is_reflect = True
rand_reflect = []
rand_reflect_posX = []
rand_reflect_posY = []
previous_time = 0
cloud_delay = 0
idle_index = 0
delay_idle = 0
play_b_index = 0
quit_b_index = 0
option_b_index = 0
return_menu_index = 0
stop_pause_b_index = 0
bomb_on_index = 0
bomb_explotion_index = 0
mouse_pos = (0, 0)
update_images = pygame.time.Clock()
init_round = True
init_word = True
nbr_word = 1000
word_found = []
word_found_nbr = 0
nbr_try = 5
word_to_find_list = []
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",]
word_posX = 0
letter_input = False
letter_used = False
letter_use_allowed = True
word_to_find = ""
word_try = []
letter = ""
word_index = 0
word_temp = []
win_delay = 0
letters_used_render = ""
dead_delay = 0
stat = ""

starting_game_time = pygame.time.get_ticks()
while lunched:

    # event window :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lunched = False
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            button_up = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            button_up = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_pause = True
            if playing:
                if letter_use_allowed:
                    if event.key == pygame.K_a:
                        letter = "a"
                        letter_used = True
                    elif event.key == pygame.K_b:
                        letter = "b"
                        letter_used = True
                    elif event.key == pygame.K_c:
                        letter = "c"
                        letter_used = True
                    elif event.key == pygame.K_d:
                        letter = "d"
                        letter_used = True
                    elif event.key == pygame.K_e:
                        letter = "e"
                        letter_used = True
                    elif event.key == pygame.K_f:
                        letter = "f"
                        letter_used = True
                    elif event.key == pygame.K_g:
                        letter = "g"
                        letter_used = True
                    elif event.key == pygame.K_h:
                        letter = "h"
                        letter_used = True
                    elif event.key == pygame.K_i:
                        letter = "i"
                        letter_used = True
                    elif event.key == pygame.K_j:
                        letter = "j"
                        letter_used = True
                    elif event.key == pygame.K_k:
                        letter = "k"
                        letter_used = True
                    elif event.key == pygame.K_l:
                        letter = "l"
                        letter_used = True
                    elif event.key == pygame.K_m:
                        letter = "m"
                        letter_used = True
                    elif event.key == pygame.K_n:
                        letter = "n"
                        letter_used = True
                    elif event.key == pygame.K_o:
                        letter = "o"
                        letter_used = True
                    elif event.key == pygame.K_p:
                        letter = "p"
                        letter_used = True
                    elif event.key == pygame.K_q:
                        letter = "q"
                        letter_used = True
                    elif event.key == pygame.K_r:
                        letter = "r"
                        letter_used = True
                    elif event.key == pygame.K_s:
                        letter = "s"
                        letter_used = True
                    elif event.key == pygame.K_t:
                        letter = "t"
                        letter_used = True
                    elif event.key == pygame.K_u:
                        letter = "u"
                        letter_used = True
                    elif event.key == pygame.K_v:
                        letter = "v"
                        letter_used = True
                    elif event.key == pygame.K_w:
                        letter = "w"
                        letter_used = True
                    elif event.key == pygame.K_x:
                        letter = "x"
                        letter_used = True
                    elif event.key == pygame.K_y:
                        letter = "y"
                        letter_used = True
                    elif event.key == pygame.K_z:
                        letter = "z"
                        letter_used = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                game_pause = False

    update_images.tick(100)

    # background animation:
    draw_backgroud()

    # init water reflect :
    # if water_is_reflect:
    for i in range(5):
        for j in range(2):
            rand_reflect.append(random.randrange(9))
            rand_reflect_posX.append(448 + i * 160 + random.randrange(160))
            rand_reflect_posY.append(416 + j * 128 + random.randrange(128))
    water_is_reflect = False

    for i in range(9):
        game_window.blit(water_reflection[rand_reflect[i]], [rand_reflect_posX[i], rand_reflect_posY[i]])

    # clouds :
    cloud_delay += 1
    if cloud_delay == 200:
        clouds_nbr += 1
        rand_cloud_index = random.randrange(3)
        rand_cloud = clouds[rand_cloud_index]
        rand_cloud_list.append(rand_cloud)
        rand_cloud_width = rand_cloud.get_width()
        clouds_posY.append(random.randrange(11) * 32)
        clouds_posX.append(0 - rand_cloud.get_width())
        cloud_delay = 0
    for i in range(clouds_nbr):
        if clouds_nbr != len(rand_cloud_list):
            i -= 1
        game_window.blit(rand_cloud_list[i], [clouds_posX[i], clouds_posY[i]])
        clouds_posX[i] += 1
        if clouds_posX[i] == game_window.get_width():
            rand_cloud_list.remove(rand_cloud_list[i])
            clouds_posY.remove(clouds_posY[i])
            clouds_posX.remove(clouds_posX[i])
    if clouds_nbr != len(rand_cloud_list):
        clouds_nbr -= 1

    # draw terrain :
    draw_level_map()

    # draw entity :
    delay_idle += 1
    if delay_idle > 50:
        if idle is False:
            idle_index = random.randrange(4)
            if idle_index == 0:
                captain_idle = True
            elif idle_index == 1:
                small_guy_idle = True
            elif idle_index == 2:
                big_guy_idle = True
            elif idle_index == 3:
                player_idle_waiting = True

            idle = True

        if captain_idle:
            captain_index += 1
            game_window.blit(captain[captain_index], [1 * 32 - 10, 6 * 32 - 7])
            if captain_index == 31:
                captain_index = 0
                captain_idle = False
                idle = False
                delay_idle = 0
            if p_alive:
                game_window.blit(player_idle[0], [8 * 32, 6 * 32 - 3])
            game_window.blit(big_guy[0], [10 * 32 + 10, 13 * 32 - 9])
            game_window.blit(small_guy[0], [3 * 32 + 8, 13 * 32 - 3])

        if small_guy_idle:
            small_guy_index += 1
            game_window.blit(small_guy[small_guy_index], [3 * 32 + 8, 13 * 32 - 3])
            if small_guy_index == 33:
                small_guy_index = 0
                small_guy_idle = False
                idle = False
                delay_idle = 0
            game_window.blit(captain[0], [1 * 32 - 10, 6 * 32 - 7])
            if p_alive:
                game_window.blit(player_idle[0], [8 * 32, 6 * 32 - 3])
            game_window.blit(big_guy[0], [10 * 32 + 10, 13 * 32 - 9])

        if big_guy_idle:
            big_guy_index += 1
            game_window.blit(big_guy[big_guy_index], [10 * 32 + 10, 13 * 32 - 9])
            if big_guy_index == 37:
                big_guy_index = 0
                big_guy_idle = False
                idle = False
                delay_idle = 0
            game_window.blit(captain[0], [1 * 32 - 10, 6 * 32 - 7])
            if p_alive:
                game_window.blit(player_idle[0], [8 * 32, 6 * 32 - 3])
            game_window.blit(small_guy[0], [3 * 32 + 8, 13 * 32 - 3])

        if p_alive:
            if player_idle_waiting:
                player_idle_index += 1
                game_window.blit(player_idle[player_idle_index], [8 * 32, 6 * 32 - 3])
                if player_idle_index == 35:
                    player_idle_index = 0
                    player_idle_waiting = False
                    idle = False
                    delay_idle = 0
                game_window.blit(captain[0], [1 * 32 - 10, 6 * 32 - 7])
                game_window.blit(big_guy[0], [10 * 32 + 10, 13 * 32 - 9])
                game_window.blit(small_guy[0], [3 * 32 + 8, 13 * 32 - 3])
    else:
        game_window.blit(captain[captain_index], [1 * 32 - 10, 6 * 32 - 7])
        game_window.blit(small_guy[small_guy_index], [3 * 32 + 8, 13 * 32 - 3])
        game_window.blit(big_guy[big_guy_index], [10 * 32 + 10, 13 * 32 - 9])
        if p_alive:
            game_window.blit(player_idle[player_idle_index], [8 * 32, 6 * 32 - 3])

    if bomb_is_off:
        game_window.blit(bomb_off, [6 * 32, 6 * 32 - 23])

    if bomb_is_on:
        game_window.blit(bomb_on[bomb_on_index], [6 * 32, 6 * 32 - 23])
        bomb_on_index += 1
        if bomb_on_index == 10:
            bomb_is_on = False
            bomb_explotion = True
            p_dead = True
            p_alive = False
            bomb_on_index = 0

    if bomb_explotion:
        game_window.blit(explotion[int(bomb_explotion_index)], [6 * 32, 6 * 32 - 10])
        bomb_explotion_index += 0.5
        if bomb_explotion_index == 9:
            bomb_explotion = False
            bomb_explotion_index = 0

    if p_dead:
        game_window.blit(player_dead[int(player_dead_index)], [8 * 32, 6 * 32 + 8])
        player_dead_index += 0.5
        if player_dead_index == 6:
            player_dead_index = 5
            if dead_delay == 10:
                menu = True
                playing = False
                player_dead_index = 0
                dead_delay = 0
            else:
                dead_delay += 1
    # menu :
    if menu:
        init_round = True
        bomb_is_off = True
        p_dead = False
        p_alive = True

        draw_banner(0, 17 * 32, 1 * 32)
        game_window.blit(name_game, [18 * 32 + 10, 2 * 32 + 10])
        draw_board(0, 22 * 32, 7 * 32)

        play_b_index = button_state(play_b_hitbox, mouse_pos)
        game_window.blit(play_b[play_b_index], [24 * 32, 9 * 32])
        if play_b_index == 2:
            play_b_used = True
        if play_b_used:
            if play_b_index == 1:
                menu = False
                playing = True
                play_b_used = False
            elif play_b_index == 0:
                play_b_used = False

        # option button usage :
        option_b_index = button_state(option_b_hitbox, mouse_pos)
        game_window.blit(option_b[option_b_index], [24 * 32, 12 * 32])
        if option_b_index == 2:
            option_b_used = True
        if option_b_used:
            if option_b_index == 1:
                menu = False
                option = True
                option_b_used = False
            elif option_b_index == 0:
                option_b_used = False

        # quit button usage :
        quit_b_index = button_state(quit_b_hitbox, mouse_pos)
        game_window.blit(quit_b[quit_b_index], [24 * 32, 15 * 32])
        if quit_b_index == 2:
            quit_b_used = True
        if quit_b_used:
            if quit_b_index == 1:
                lunched = False
            elif quit_b_index == 0:
                quit_b_used = False

    # option :
    if option:

        # draw option title :
        draw_banner(0, 10 * 32, 1 * 32)
        game_window.blit(option_title, [14 * 32 + 10, 2 * 32 - 10])

        # draw stat banner :
        draw_banner(1, 21 * 32, 7 * 32)
        game_window.blit(stat_title, [25 * 32 - 15, 7 * 32 + 20])

        # draw time played :
        total_time = time_played_previously + pygame.time.get_ticks() - starting_game_time
        time_played = timer(total_time, 0)
        time_played_render = font_stat.render("Time played : ", True, text_white)
        game_window.blit(time_played_render, [22 * 32, 9 * 32 + 25])
        time_played_nbr = nbr_font.render(time_played, True, text_white)
        game_window.blit(time_played_nbr, [28 * 32 - 10, 9 * 32 + 30])

        # draw best score :
        game_window.blit(best_score, [22 * 32, 11 * 32 + 10])
        best_score_nbr_render = nbr_font.render(str(best_score_nbr), True, text_white)
        game_window.blit(best_score_nbr_render, [28 * 32 - 10, 11 * 32 + 15])

        # draw rounds played :
        played_rounds_render = font_stat.render("Rounds played : ", True, text_white)
        game_window.blit(played_rounds_render, [22 * 32, 12 * 32 + 22])
        played_rounds_nbr_render = nbr_font.render(str(played_rounds), True, text_white)
        game_window.blit(played_rounds_nbr_render, [28 * 32 - 10, 12 * 32 + 27])

        # draw rounds won :
        rounds_won_render = font_stat.render("Rounds won : ", True, text_white)
        game_window.blit(rounds_won_render, [22 * 32, 14 * 32 + 2])
        rounds_won_nbr_render = nbr_font.render(str(rounds_won), True, text_white)
        game_window.blit(rounds_won_nbr_render, [28 * 32 - 10, 14 * 32 + 7])

        # draw rounds lost :
        rounds_lost_render = font_stat.render("Rounds lost : ", True, text_white)
        game_window.blit(rounds_lost_render, [22 * 32, 15 * 32 + 14])
        rounds_lost_nbr_render = nbr_font.render(str(rounds_lost), True, text_white)
        game_window.blit(rounds_lost_nbr_render, [28 * 32 - 10, 15 * 32 + 19])

        stat_write(total_time, best_score_nbr)
        game_window.blit(pause_menu.subsurface([0, 80, 258, 309]), [8 * 32, 8 * 32])

        # music on/off :
        music_b_index = button_state(music_b_hitbox, mouse_pos)
        if music_is_on:
            game_window.blit(sound_on[music_b_index], [13 * 32, 9 * 32 + 5])
        else:
            game_window.blit(sound_off[music_b_index], [13 * 32, 9 * 32 + 5])
        if music_b_index == 2:
            music_b_used = True
        if music_b_used:
            if music_b_index == 1:
                music_is_on = not music_is_on
                music_b_used = False
            elif music_b_index == 0:
                music_b_used = False

        # sfx on/off :
        sfx_b_index = button_state(sfx_b_hitbox, mouse_pos)
        if sfx_is_on:
            game_window.blit(sound_on[sfx_b_index], [13 * 32, 11 * 32 - 15])
        else:
            game_window.blit(sound_off[sfx_b_index], [13 * 32, 11 * 32 - 15])
        if sfx_b_index == 2:
            sfx_b_used = True
        if sfx_b_used:
            if sfx_b_index == 1:
                sfx_is_on = not sfx_is_on
                sfx_b_used = False
                sfx_b_index = False
            elif sfx_b_index == 0:
                sfx_b_used = False

        # volume bar use :
        game_window.blit(volume_bar, [9 * 32 - 10, 14 * 32 - 20])
        volume_bar_slide_index = button_state(volume_bar_slide_hitbox, mouse_pos)
        game_window.blit(volume_bar_slide[volume_bar_slide_index], [volume_bar_slide_posX, 14 * 32 - 20])
        if volume_bar_slide_index == 2:
            if mouse_pos[0] > volume_bar_max:
                volume_bar_slide_posX = volume_bar_max
            elif mouse_pos[0] < volume_bar_min + 28 / 2:
                volume_bar_slide_posX = volume_bar_min
            else:
                volume_bar_slide_posX = mouse_pos[0] - 28 / 2
            volume_bar_slide_hitbox.x = volume_bar_slide_posX

        # urm button :
        # stop pause :
        stop_pause_b_index = button_state(stop_pause_b_hitbox, mouse_pos)
        game_window.blit(stop_pause_b[stop_pause_b_index], [9 * 32 + 20, 15 * 32])
        if stop_pause_b_index == 2:
            stop_pause_b_used = True
        if stop_pause_b_used:
            if stop_pause_b_index == 1:
                option = False
                playing = True
                stop_pause_b_used = False
            elif stop_pause_b_index == 0:
                stop_pause_b_used = False

        # return menu :
        return_menu_index = button_state(return_menu_hitbox, mouse_pos)
        game_window.blit(return_menu[return_menu_index], [12 * 32 + 20, 15 * 32])
        if return_menu_index == 2:
            return_menu_used = True
        if return_menu_used:
            if return_menu_index == 1:
                option = False
                menu = True
                return_menu_used = False
            elif return_menu_index == 0:
                return_menu_used = False

    # init playing :
    if playing:

        # init round :
        if init_round:
            timer_start = pygame.time.get_ticks()
            time_nbr = nbr_font.render("00:00:00", True, text_white)
            word_to_find_list = init_words_list()
            letter_used = []
            word_found_nbr = 0
            current_score_nbr = nbr_font.render("0", True, text_white)
            init_word = True
            init_round = False

        # time passed :
        current_time = pygame.time.get_ticks()
        round_timer = timer(current_time, timer_start)
        time_nbr = nbr_font.render(round_timer, True, text_white)

        # init word :
        if init_word:
            letter_use_allowed = True
            played_rounds += 1
            word_index = random.randrange(nbr_word)
            word_to_find = word_to_find_list[word_index]
            word_try = []
            word_temp = []
            letters_used_render = ""
            letters_used = font_stat.render("letters used : " + letters_used_render, True, text_white)
            for i in range(len(word_to_find)):
                if word_to_find[i] in alphabet:
                    word_try.append("* ")
                    word_temp.append("*")
                else:
                    word_try.append(word_to_find[i]+" ")
                    word_temp.append(word_to_find[i])
            word_render = font_word.render("".join(word_try), True, text_black)
            nbr_try = 5
            nbr_try_render = nbr_font.render(str(nbr_try), True, text_white)
            init_word = False
            if len(word_to_find) >= 10:
                word_posX = 21 * 32
            elif len(word_to_find) >= 8:
                word_posX = 22 * 32
            elif len(word_to_find) >= 6:
                word_posX = 23 * 32
            elif len(word_to_find) >= 4:
                word_posX = 24 * 32
            elif len(word_to_find) >= 2:
                word_posX = 25 * 32
            else:
                word_posX = 26 * 32

        # playing (have fun) :
        if letter_used:
            if letter in word_to_find:
                for i in range(len(word_to_find)):
                    if word_to_find[i] == letter:
                        word_try[i] = letter + " "
                        word_temp[i] = letter
            else:
                nbr_try -= 1
            word_render = font_word.render("".join(word_try), True, text_black)
            letters_used_render = letters_used_render + letter + " "
            letters_used = font_stat.render("letters used : " + letters_used_render, True, text_white)
            nbr_try_render = nbr_font.render(str(nbr_try), True, text_white)
            letter_used = False

        # win/lose :
        if "".join(word_temp) == word_to_find:
            if win_delay == 10:
                if nbr_word == 1:
                    lunched = False
                else:
                    nbr_word -= 1
                    word_found_nbr += 1
                    rounds_won += 1
                    current_score_nbr = nbr_font.render(str(word_found_nbr), True, text_white)
                    word_to_find_list.remove(word_to_find)
                    init_word = True
                    if word_found_nbr > best_score_nbr:
                        best_score_nbr = word_found_nbr
                win_delay = 0
            else:
                win_delay += 1
        else:
            if nbr_try == 0:
                bomb_is_off = False
                bomb_is_on = True
                letter_use_allowed = False
                nbr_try = 5
                rounds_lost += 1


        # draw element :

        # word banner :
        draw_banner(2, 17 * 32, 2 * 32)
        game_window.blit(word_render, [word_posX, 4 * 32 - 10])

        # try left :
        draw_board(1, 18 * 32, 8 * 32 + 15)
        game_window.blit(try_left, [18 * 32 + 15, 9 * 32 - 5])
        game_window.blit(nbr_try_render, [23 * 32 + 15, 9 * 32])

        # timer :
        draw_board(1, 27 * 32, 8 * 32 + 15)
        game_window.blit(time, [27 * 32 + 15, 8 * 32 + 27])
        game_window.blit(time_nbr, [31 * 32 + 15, 9 * 32 ])

        # letter tried :
        draw_board(2, 18 * 32, 11 * 32 + 15)
        game_window.blit(letters_used, [18 * 32 + 15, 11 * 32 + 27])

        # scores :
        draw_board(1, 18 * 32, 14 * 32 + 15)
        game_window.blit(current_score, [18 * 32 + 15, 14 * 32 + 27])
        game_window.blit(current_score_nbr, [23 * 32 + 15, 15 * 32 ])
        draw_board(1, 27 * 32, 14 * 32 + 15)
        game_window.blit(best_score, [27 * 32 + 15, 14 * 32 + 27])
        best_score_nbr_render = nbr_font.render(str(best_score_nbr), True, text_white)
        game_window.blit(best_score_nbr_render, [32 * 32, 15 * 32])

        # init pause :
        if game_pause:
            playing = False
            option = True


    '''for i in range(row_tiles):
        rect = pygame.Rect(0, i*32, game_window.get_width(), 32)
        pygame.draw.rect(game_window, (0, 0, 0), rect,2)

    for j in range(col_tiles):
        rect = pygame.Rect(j*32, 0, 32, game_window.get_height())
        pygame.draw.rect(game_window, (0,0,0), rect,2)'''

    pygame.display.flip()
