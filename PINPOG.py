import pygame
pygame.init()

# Устанавливаем размеры окна
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")

# Устанавливаем цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Рисуем ракетки и мяч
paddle_height = 75
paddle_width = 15
paddle_speed = 5
paddle1_pos = (50, 225)
paddle2_pos = (635, 225)
ball_pos = (350, 250)
ball_radius = 10
ball_speed = [5, 5]

# Основной игровой цикл
game_over = False
while not game_over:
# Обработка событий
    for event in pygame.event.get():
    if event.type == pygame.QUIT:
game_over = True
# Рисуем фон
screen.fill(WHITE)
# Рисуем ракетки и мяч
pygame.draw.rect(screen, BLACK, (paddle1_pos[0], paddle1_pos[1], paddle_width, paddle_height))
pygame.draw.rect(screen, BLACK, (paddle2_pos[0], paddle2_pos[1], paddle_width, paddle_height))
pygame.draw.circle(screen, RED, (ball_pos[0], ball_pos[1]), ball_radius)
# Движение мяча по полю
ball_pos[0] += ball_speed[0]
ball_pos[1] += ball_speed[1]
# Отскок от стен
if ball_pos[1] <= 0 or ball_pos[1] >= 490:
    ball_speed[1] = -ball_speed[1]
# Отскок от ракеток
    if ball_pos[0] <= paddle1_pos[0] + paddle_width and ball_pos[1] >= paddle1_pos[1] and ball_pos[1] <= paddle1_pos[1] + paddle_height:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[0] >= paddle2_pos[0] - ball_radius and ball_pos[1] >= paddle2_pos[1] and ball_pos[1] <= paddle2_pos[1] + paddle_height:
        ball_speed[0] = -ball_speed[0]
# Движение ракеток
keys = pygame.key.get_pressed()
if keys[pygame.K_w] and paddle1_pos[1] > 0:
    paddle1_pos = (paddle1_pos[0], paddle1_pos[1] - paddle_speed)
elif keys[pygame.K_s] and paddle1_pos[1] < 425:
    paddle1_pos = (paddle1_pos[0], paddle1_pos[1] + paddle_speed)
if keys[pygame.K_UP] and paddle2_pos[1] > 0:
    paddle2_pos = (paddle2_pos[0], paddle2_pos[1] - paddle_speed)
elif keys[pygame.K_DOWN] and paddle2_pos[1] < 425:
    paddle2_pos = (paddle2_pos[0], paddle2_pos[1] + paddle_speed)
# Обновляем экран
pygame.display.update()

pygame.quit()