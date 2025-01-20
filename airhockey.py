import pygame

pygame.init()

# Налаштування екрану
width, height = 600, 400
mw = pygame.display.set_mode((width, height))
pygame.display.set_caption("Аерохокей")

# Кольори
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Початкові змінні
clock = pygame.time.Clock()
fps = 60

# Параметри об'єктів
paddle_width, paddle_height = 20, 80
puck_radius = 15

player1_pos = [30, height // 2 - paddle_height // 2]
player2_pos = [width - 50, height // 2 - paddle_height // 2]
puck_pos = [width // 2, height // 2]
puck_speed = [4, 4]

player1_score = 0
player2_score = 0

# Функція для відображення тексту
def draw_text(text, size, x, y, color):
    font = pygame.font.SysFont('verdana', size)
    label = font.render(text, True, color)
    mw.blit(label, (x, y))

# Гра
running = True
while running:
    mw.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отримання натискань клавіш
    keys = pygame.key.get_pressed()
    # Рух грав
    # Рух гравців
    if keys[pygame.K_w] and player1_pos[1] > 0:
        player1_pos[1] -= 5
    if keys[pygame.K_s] and player1_pos[1] < height - paddle_height:
        player1_pos[1] += 5
    if keys[pygame.K_UP] and player2_pos[1] > 0:
        player2_pos[1] -= 5
    if keys[pygame.K_DOWN] and player2_pos[1] < height - paddle_height:
        player2_pos[1] += 5

    # Рух шайби
    puck_pos[0] += puck_speed[0]
    puck_pos[1] += puck_speed[1]

    # Відбивання шайби від верхньої та нижньої стінки
    if puck_pos[1] - puck_radius <= 0 or puck_pos[1] + puck_radius >= height:
        puck_speed[1] = -puck_speed[1]

    # Відбивання шайби від ракеток
    if (player1_pos[0] < puck_pos[0] - puck_radius < player1_pos[0] + paddle_width and
        player1_pos[1] < puck_pos[1] < player1_pos[1] + paddle_height):
        puck_speed[0] = -puck_speed[0]

    if (player2_pos[0] < puck_pos[0] + puck_radius < player2_pos[0] + paddle_width and
        player2_pos[1] < puck_pos[1] < player2_pos[1] + paddle_height):
        puck_speed[0] = -puck_speed[0]

    # Перевірка на гол
    if puck_pos[0] - puck_radius <= 0:
        player2_score += 1
        puck_pos = [width // 2, height // 2]
        puck_speed = [4, 4]

    if puck_pos[0] + puck_radius >= width:
        player1_score += 1
        puck_pos = [width // 2, height // 2]
        puck_speed = [-4, 4]

    # Малювання ракеток
    pygame.draw.rect(mw, blue, (*player1_pos, paddle_width, paddle_height))
    pygame.draw.rect(mw, red, (*player2_pos, paddle_width, paddle_height))

    # Малювання шайби
    pygame.draw.circle(mw, green, puck_pos, puck_radius)

    # Відображення рахунку
    draw_text(f"{player1_score}", 30, width // 4, 20, white)
    draw_text(f"{player2_score}", 30, 3 * width // 4, 20, white)

    # Оновлення екрану
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()



