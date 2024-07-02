import pygame as pg
import random
import time


pg.init()
SCREEN_SIZE = (800, 900)
screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("Shulte table")

screen.fill((255, 255, 255))
IMG_SIZE = 160

def get_img_pos(pos):
        return (pos % 5 * IMG_SIZE, pos // 5 * IMG_SIZE)

class Number:
    """Each table cell has a num_value, an image, and position.
    Positions are counted as following:
    [0 1 2
     3 4 5
     6 7 8]
     the default table is 5x5
    """

    def __init__(self, value:int, path_to_img:str, pos:int):
        self.value = value
        self.img = pg.image.load(path_to_img).convert()
        self.pos = pos
        self.img_pos = get_img_pos(pos)
    

numbers = []
positions = [i for i in range(25)]
random.shuffle(positions)
table = {} # {position: value} (to instantly find a number by position when table is clicked)
for i in range(1, 26):
    pos = positions.pop()
    numbers.append(Number(value=i, path_to_img=f"./img/{i}.jpg", pos=pos))
    table[pos] = i

for num in numbers:
    screen.blit(num.img, num.img_pos)

font_small = pg.font.SysFont('Arial', 36)
font_big = pg.font.SysFont('Arial', 48)
next_num = 1
text = font_small.render("Next number:", True, [5, 5, 5])
text_pos = (80, 830)
screen.blit(text, text_pos)
next_num_text= font_big.render(str(next_num), True, [5, 5, 5])
next_num_text_pos = (270, 820)
screen.blit(next_num_text, next_num_text_pos)

# Transparent surface for highlighting clicked cells
surface = pg.Surface((IMG_SIZE, IMG_SIZE), pg.SRCALPHA)
surface.set_alpha(60)

def highlight_cell(pos_clicked:tuple[int, int], color:str, clicked_num:int):
    if color == 'green':
        color = pg.Color(50, 255, 50)
    elif color == 'red':
        color = pg.Color(255, 50, 50)
    img_x, img_y = get_img_pos(pos_clicked)
    square = pg.Rect(0, 0, IMG_SIZE, IMG_SIZE)
    pg.draw.rect(surface, color, rect=square)
    screen.blit(numbers[clicked_num-1].img, numbers[clicked_num-1].img_pos)
    screen.blit(surface, (img_x, img_y))

mouse_down = False
cell_highlighted = False
correct_num = False

run = True
start_time = time.time()

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    if pg.mouse.get_pressed()[0] and not mouse_down:
        mx, my = pg.mouse.get_pos()
        if mx < 5 * IMG_SIZE and my < 5 * IMG_SIZE: # check if the click is within the table
            pos_clicked = (my // IMG_SIZE * 5 + mx // IMG_SIZE)
            clicked_num = table[pos_clicked]
            if next_num == clicked_num:
                correct_num = True
                if not cell_highlighted:
                    highlight_cell(pos_clicked, 'green', clicked_num)
                    cell_highlighted = True
            else:
                correct_num = False
                if not cell_highlighted:
                    highlight_cell(pos_clicked, 'red', clicked_num)
                    cell_highlighted = True
            pg.display.flip()
        mouse_down = True

    if mouse_down and not pg.mouse.get_pressed()[0]: # if mouse was clicked and now is released
        # removing cell highlighting
        if cell_highlighted:
            screen.blit(numbers[clicked_num-1].img, numbers[clicked_num-1].img_pos)
            cell_highlighted = False
        if correct_num:
            next_num += 1
            # painting over the previous number with white rectangle
            pg.draw.rect(screen, (255, 255, 255), (next_num_text_pos, (60, 60)))
            text = font_big.render(str(next_num), True, [5, 5, 5])
            screen.blit(text, next_num_text_pos)
            correct_num = False
        mouse_down = False
            
    #Displaying timer:
    elapsed_time = time.time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    milliseconds = int((elapsed_time * 1000) % 10)
    elapsed_time_str = f"{minutes:1}:{seconds:02}:{milliseconds:01}"

    timer_text = font_small.render(elapsed_time_str, True, [5, 5, 5])
    timer_pos = (680, 830)
    pg.draw.rect(screen, (255, 255, 255), ((600, 800), (200, 100)))
    screen.blit(timer_text, timer_pos)
    pg.display.flip()

    if next_num == 26:
        run = False
    pg.display.update()

print(f"Your time is {elapsed_time_str}")