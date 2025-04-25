import pygame

pygame.init() # 초기화 반드시 필요

# 화면
screen_width = 1480
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# 이미지
background = pygame.image.load("E:/SourceTree/Python/study2/pygame_basic/background.png")

# 타이틀
pygame.display.set_caption("Hello, Pygame")

# 이벤트 루프
running = True #게임 진행중인가
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #screen.fill((0,0,0,1))
    screen.blit(background, (0,0)) # 배경 그리기

    pygame.display.update() # 매 프레임 화면 업데이트

# 종료
pygame.quit()


