import pygame

pygame.init() # 초기화 반드시 필요

# 화면
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀
pygame.display.set_caption("Hello, Pygame")

# 이벤트 루프
running = True #게임 진행중인가
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# 종료
pygame.quit()


