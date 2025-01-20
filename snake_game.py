
import pygame
import random

pygame.init()

# Налаштування екрану
back = (50, 50, 50)
mw = pygame.display.set_mode((500, 500))
mw.fill(back)
clock = pygame.time.Clock()

# Розміри блоків
block_size = 20

# Початкові налаштування змійки та яблука
snake_pos = [(100, 100), (80, 100), (60, 100)]
apple_pos = (random.randint(0, 24) * block_size, random.randint(0, 24) * block_size)
direction = 'RIGHT'
new_direction = direction
game_over = False

# Кольори
snake_color = (0, 255, 0)
apple_color = (255, 0, 0)
text_color = (255, 255, 255)

# Функція для відображення тексту
def draw_text(text, size, x, y, color):
    font = pygame.font.SysFont('verdana', size)
    label = font.render(text, True, color)
    mw.blit(label, (x, y))

while not game_over:
    mw.fill(back)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                new_direction = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                new_direction = 'DOWN'
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                new_direction = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                new_direction = 'RIGHT'

    # Оновлення напрямку
    direction = new_direction

    # Рух змійки
    head_x, head_y = snake_pos[0]
    if direction == 'UP':
        head_y -= block_size
    if direction == 'DOWN':
        head_y += block_size
    if direction == 'LEFT':
        head_x -= block_size
    if direction == 'RIGHT':
        head_x += block_size

    new_head = (head_x, head_y)
    snake_pos.insert(0, new_head)

    # Перевірка на з'їдання яблука
    if new_head == apple_pos:
        apple_pos = (random.randint(0, 24) * block_size, random.randint(0, 24) * block_size)
    else:
        snake_pos.pop()

    # Перевірка на вихід за межі екрану або зіткнення зі змійкою
    if (head_x < 0 or head_x >= 500 or head_y < 0 or head_y >= 500 or new_head in snake_pos[1:]):
        game_over = True
        break

    # Малювання яблука
    pygame.draw.rect(mw, apple_color, (apple_pos[0], apple_pos[1], block_size, block_size))

    # Малювання змійки
    for segment in snake_pos:
        pygame.draw.rect(mw, snake_color, (segment[0], segment[1], block_size, block_size))

    # Оновлення екрану
    pygame.display.update()
    clock.tick(10)

# Кінець гри
mw.fill(back)
draw_text("GAME OVER", 50, 150, 200, text_color)
pygame.display.update()
pygame.time.wait(3000)
pygame.quit()
