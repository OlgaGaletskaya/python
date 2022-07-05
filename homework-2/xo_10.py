import pygame
import random


def check_line(start_row, finish_row, start_col, finish_col, mas, sign, diagonal, dr):
    sum = 0
    for row in range(start_col, finish_col):
        for col in range(start_row, finish_row):
            if (not diagonal) or row+col == dr or row-col == dr:
                if mas[row][col] == sign:
                    sum += 1
                    if sum >= 5:
                        return sign
                else:
                    sum = 0
    return False

def get_coords(position):
    start = position - 4
    if start < 0:
        start = 0
    finish = position + 5
    if finish > 10:
        finish = 10
    return (start, finish)

def check_win(col, row, mas, sign):
    screen.fill(BLACK)
    print ("PLAYER", sign, "COORDS", col, row)
    start_row, finish_row = get_coords(col)
    start_col, finish_col = get_coords(row)    
    if check_line(start_row, finish_row, row, row+1, mas, sign, False, False):
        return sign
    if check_line(col, col+1, start_col, finish_col, mas, sign, False, False):
        return sign
    if check_line(start_row, finish_row, start_col, finish_col, mas, sign, True, row+col):
        return sign
    if check_line(start_row, finish_row, start_col, finish_col, mas, sign, True, row-col):
        return sign
    return False

def copy_mas(mas):
    new_mas=[]
    for row in range(10):
        new_row=[]
        for col in range(10):
            new_row.append(mas[row][col])
        new_mas.append(new_row)
    return(new_mas)

def comp_turn(mas, help_mas):

    for row in range(10):
        for col in range(10):
            new_mas = copy_mas(mas)
            if help_mas[row][col] == 1:
                if mas[row][col] != 0:
                    help_mas[row][col] = 0
                else:
                    new_mas[row][col]='o'
                    if check_win(col, row, new_mas, 'o'):
                        help_mas[row][col] = 0
                    else:
                        return (help_mas, col, row)
    return(help_mas, random.randint(0, 9), random.randint(0, 9))

def check_blanks(help_mas):
    blanks = 0
    for i in help_mas:
        blanks += i.count(1)
    return blanks

pygame.init()
size_block = 50
margin = 5
num = 10
width = height = size_block*num + margin*(num+1)
size_window = (width, height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Обратные крестики-нолики 10х10")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

mas = [[0]*num for i in range(num)]
help_mas = [[1]*num for i in range(num)]
query = 0
col = 0
row = 0


game_over = False
while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and query % 2 == 0 and not game_over:
                x_mouse, y_mouse = pygame.mouse.get_pos()
                col = x_mouse // (size_block+margin)
                row = y_mouse // (size_block+margin)
                if mas[row][col] == 0 and query % 2 == 0:
                    mas[row][col] = 'x'
                    query += 1
                    game_over = check_win(col, row, mas, 'x')
                    
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_over = False
                mas = [[0]*num for i in range(num)]
                help_mas = [[1]*num for i in range(num)]
                query = 0
                screen.fill(BLACK)


    if query % 2 != 0 and not game_over :
        
        if check_blanks(help_mas)!=1:
            help_mas, col, row = comp_turn(mas, help_mas)
        else:
            for row1 in range(10):
                if mas[row1].count(0) >= 1:
                    row = row1
            for col1 in range(10):
                if mas[row][col1] == 0:
                    col = col1
        if mas[row][col] == 0:
            mas[row][col] = 'o'
            query += 1
            game_over = check_win(col, row, mas, 'o')


    for row in range(num):
        for col in range(num):
            x = col*size_block + (col+1)*margin
            y = row*size_block + (row+1)*margin
            pygame.draw.rect( screen, WHITE, (x, y, size_block, size_block))
            if mas[row][col] == 'x':
                pygame.draw.line(screen, GREEN, (x+5, y+5), (x+size_block-5, y+size_block-5), 5)
                pygame.draw.line(screen, GREEN, (x+5, y+size_block-5), (x+size_block-5, y+5), 5)
            elif mas[row][col] == 'o':
                pygame.draw.circle(screen, RED, (x+size_block//2, y+size_block//2), size_block//2-5, 5)
    
    if query == 100 and not game_over:
        game_over = 'piece'
    if game_over:
        font = pygame.font.SysFont('stxingkai', 80)
        if game_over == 'x':
            txt1 = font.render ("You Lose", True, BLUE)
        elif game_over == 'o':
            txt1 = font.render ("You Win", True, BLUE)
        else:
            txt1 = font.render ("Piece", True, BLUE)
        text_rect = txt1.get_rect()
        txt_x = width/2 - text_rect.width/2
        txt_y = height/2 - text_rect.height/2
        screen.blit(txt1, [txt_x, txt_y])
    

    pygame.display.update()