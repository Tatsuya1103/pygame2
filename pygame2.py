import pygame
import random

# 初期化
pygame.init()

# 画面サイズ
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# 画面生成
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Game")

# 色
WHITE = (255, 255, 255)

# メインループ
running = True
while running:
    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # クリックした位置にランダムな大きさの円を描画する
            pos = pygame.mouse.get_pos()
            radius = random.randint(10, 50)
            pygame.draw.circle(screen, WHITE, pos, radius)

    # 画面更新
    pygame.display.flip()

# 終了処理
pygame.quit()



