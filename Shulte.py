import pygame, random

pygame.init()

screen = pygame.display.set_mode((800, 900))

pygame.display.set_caption("Shulte table")

clock = pygame.time.Clock()

screen.fill((255, 255, 255))

number1 = pygame.image.load('1.jpg').convert()
number10 = pygame.image.load('10.jpg').convert()
number2 = pygame.image.load('2.jpg').convert()
number11 = pygame.image.load('11.jpg').convert()
number3 = pygame.image.load('3.jpg').convert()
number12 = pygame.image.load('12.jpg').convert()
number4 = pygame.image.load('4.jpg').convert()
number13 = pygame.image.load('13.jpg').convert()
number5 = pygame.image.load('5.jpg').convert()
number14 = pygame.image.load('14.jpg').convert()
number6 = pygame.image.load('6.jpg').convert()
number15 = pygame.image.load('15.jpg').convert()
number7 = pygame.image.load('7.jpg').convert()
number16 = pygame.image.load('16.jpg').convert()
number8 = pygame.image.load('8.jpg').convert()
number17 = pygame.image.load('17.jpg').convert()
number9 = pygame.image.load('9.jpg').convert()
number18 = pygame.image.load('18.jpg').convert()
number19 = pygame.image.load('19.jpg').convert()
number20 = pygame.image.load('20.jpg').convert()
number21 = pygame.image.load('21.jpg').convert()
number22 = pygame.image.load('22.jpg').convert()
number23 = pygame.image.load('23.jpg').convert()
number24 = pygame.image.load('24.jpg').convert()
number25 = pygame.image.load('25.jpg').convert()

font = pygame.font.Font(None, 38)
text1 = font.render("Next number:", False, [5, 5, 5])

next_number = 1

numbers = [number1, number2, number3, number4, number5, number6, number7, number8, number9,
           number10, number11, number12, number13, number14, number15, number16, number17, number18,
           number19, number20, number21, number22, number23, number24, number25]

positions = [(0, 0), (160, 0), (320, 0), (480, 0), (640, 0), (0, 160), (160, 160), (320, 160), (480, 160), (640, 160),
             (0, 320),
             (160, 320), (320, 320), (480, 320), (640, 320), (0, 480), (160, 480), (320, 480), (480, 480), (640, 480),
             (0, 640),
             (160, 640), (320, 640), (480, 640), (640, 640)]

pos1 = positions.pop(random.randrange(0, 24 + 1))
pos2 = positions.pop(random.randrange(0, 23 + 1))
pos3 = positions.pop(random.randrange(0, 22 + 1))
pos4 = positions.pop(random.randrange(0, 21 + 1))
pos5 = positions.pop(random.randrange(0, 20 + 1))
pos6 = positions.pop(random.randrange(0, 19 + 1))
pos7 = positions.pop(random.randrange(0, 18 + 1))
pos8 = positions.pop(random.randrange(0, 17 + 1))
pos9 = positions.pop(random.randrange(0, 16 + 1))
pos10 = positions.pop(random.randrange(0, 15 + 1))
pos11 = positions.pop(random.randrange(0, 14 + 1))
pos12 = positions.pop(random.randrange(0, 13 + 1))
pos13 = positions.pop(random.randrange(0, 12 + 1))
pos14 = positions.pop(random.randrange(0, 11 + 1))
pos15 = positions.pop(random.randrange(0, 10 + 1))
pos16 = positions.pop(random.randrange(0, 9 + 1))
pos17 = positions.pop(random.randrange(0, 8 + 1))
pos18 = positions.pop(random.randrange(0, 7 + 1))
pos19 = positions.pop(random.randrange(0, 6 + 1))
pos20 = positions.pop(random.randrange(0, 5 + 1))
pos21 = positions.pop(random.randrange(0, 4 + 1))
pos22 = positions.pop(random.randrange(0, 3 + 1))
pos23 = positions.pop(random.randrange(0, 2 + 1))
pos24 = positions.pop(random.randrange(0, 1 + 1))
pos25 = (random.choice(positions))

pozs = [pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9,
        pos10, pos11, pos12, pos13, pos14, pos15, pos16, pos17,
        pos18, pos19, pos20, pos21, pos22, pos23, pos24, pos25]

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(number1, pos1)
    screen.blit(number2, pos2)
    screen.blit(number3, pos3)
    screen.blit(number4, pos4)
    screen.blit(number5, pos5)
    screen.blit(number6, pos6)
    screen.blit(number7, pos7)
    screen.blit(number8, pos8)
    screen.blit(number9, pos9)
    screen.blit(number10, pos10)
    screen.blit(number11, pos11)
    screen.blit(number12, pos12)
    screen.blit(number13, pos13)
    screen.blit(number14, pos14)
    screen.blit(number15, pos15)
    screen.blit(number16, pos16)
    screen.blit(number17, pos17)
    screen.blit(number18, pos18)
    screen.blit(number19, pos19)
    screen.blit(number20, pos20)
    screen.blit(number21, pos21)
    screen.blit(number22, pos22)
    screen.blit(number23, pos23)
    screen.blit(number24, pos24)
    screen.blit(number25, pos25)

    screen.blit(text1, (270, 840))
    text2 = font.render(str(next_number), False, [5, 5, 5])
    screen.blit(text2, (445, 840))

    if event.type == pygame.MOUSEBUTTONDOWN:
        mx, my = pygame.mouse.get_pos()
        if mx > pozs[next_number - 1][0] \
        and mx < pozs[next_number - 1][0] + 161 \
        and my > pozs[next_number - 1][1] \
        and my < pozs[next_number - 1][1] + 161:
            next_number += 1
            print(next_number)
            pygame.draw.rect(screen, (255, 255, 255), (440, 840, 50, 25))
            text2 = font.render(str(next_number), False, [5, 5, 5])
            screen.blit(text2, (445, 840))

    if next_number == 26:
        run = False

    # pygame.display.flip()
    pygame.display.update()
