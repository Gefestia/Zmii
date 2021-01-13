import pygame
from random import randrange

RES = 600
SIZE = 20

x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
grusha = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
trava = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
length = 1
snake = [(x, y)]
score = 0
speed_count=1
snake_speed = 10
dx, dy = 0, 0
fps = 60
dirs = {
    "W": True,
    "S": True,
    "A": True,
    "D": True,
}
pygame.init()
surface = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
png = pygame.image.load("Belii.png").convert()
font_score = pygame.font.SysFont('Monotype Corsiva', 26, bold=True)


def close_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


while True:
    surface.blit(png, (0, 0))
    [
        pygame.draw.rect(surface, pygame.Color("black"), (i, j, SIZE - 1, SIZE - 1))
        for i, j in snake
    ]
    pygame.draw.rect(surface, pygame.Color("red"), (*apple, SIZE, SIZE))
    pygame.draw.rect(surface, pygame.Color("green"), (*trava, SIZE, SIZE))
    pygame.draw.rect(surface, pygame.Color("yellow"), (*grusha, SIZE, SIZE))
    render_score = font_score.render(f'Очки: {score}', 1, pygame.Color('purple'))
    surface.blit(render_score, (5, 5))

    speed_count += 1
    if not speed_count % snake_speed:
        x += dx * SIZE
        y += dy * SIZE
        snake.append((x, y))
        snake = snake[-length:]

    if snake[-1] == apple:
        apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
        length += 1
        snake_speed -= 1
        score += 10
        snake_speed = max(snake_speed, 4)

    if snake[-1] == trava:
        trava = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
        if length>1:
            length-=1
            score -= 5
        else:
            length+=4
            score +=20

    if snake[-1] ==grusha:
        grusha = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
        length += 2
        score += 50
        snake_speed -= 3
        snake_speed = max(snake_speed, 4)

    if (
        x < 0
        or x > RES - SIZE
        or y < 0
        or y > RES - SIZE
        or len(snake) != len(set(snake))
    ):
        exit()

    pygame.display.flip()
    clock.tick(fps)
    close_game()

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        if dirs["W"]:
            dx, dy = 0, -1
            dirs = {
                "W": True,
                "S": False,
                "A": True,
                "D": True,
            }
    elif key[pygame.K_s]:
        if dirs["S"]:
            dx, dy = 0, 1
            dirs = {
                "W": False,
                "S": True,
                "A": True,
                "D": True,
            }
    elif key[pygame.K_a]:
        if dirs["A"]:
            dx, dy = -1, 0
            dirs = {
                "W": True,
                "S": True,
                "A": True,
                "D": False,
            }
    elif key[pygame.K_d]:
        if dirs["D"]:
            dx, dy = 1, 0
            dirs = {
                "W": True,
                "S": True,
                "A": False,
                "D": True,
            }
