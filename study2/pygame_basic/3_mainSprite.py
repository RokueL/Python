import pygame

# <editor-fold desc="🌟 기본 설정 🌟">
pygame.init()  # 초기화 반드시 필요

# 화면
screen_width = 1480
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# 이미지
background = pygame.image.load("E:/SourceTree/Python/study2/pygame_basic/background.png")

# 타이틀
pygame.display.set_caption("Hello, Pygame")

# 이동 좌표
to_x = 0
to_y = 0

# </editor-fold>

# <editor-fold desc="🌟 이미지 설정 🌟">
# 스프라이트 불러오기
table = pygame.image.load("E:/SourceTree/Python/study2/pygame_basic/table.png")
table_size = table.get_rect().size
table_width = table_size[0]
table_height = table_size[1]
table_x_postion = 0  # 화면 왼쪽 위 상단이 0임
table_y_postion = 0

character = pygame.image.load("E:/SourceTree/Python/study2/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_postion = (screen_width / 2) - (character_width / 2)  # 화면 왼쪽 위 상단이 0임
character_y_postion = screen_height - character_height

# </editor-fold>

# 이벤트 루프
running = True  # 게임 진행중인가
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # <editor-fold desc="키 입력">
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 5
                pass
            elif event.key == pygame.K_RIGHT:
                to_x += 5
                pass
            elif event.key == pygame.K_UP:
                to_y -= 5
                pass
            elif event.key == pygame.K_DOWN:
                to_y += 5
                pass
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

        # </editor-fold>

    character_x_postion += to_x
    character_y_postion += to_y

    if character_x_postion < 0:
        character_x_postion = 0
    elif character_x_postion > screen_width - character_width:
        character_x_postion = screen_width - character_width

    if character_y_postion < 0:
        character_y_postion = 0
    elif character_y_postion > screen_height - character_height:
        character_y_postion = screen_height - character_height

    screen.blit(background, (0, 0))  # 배경 그리기

    screen.blit(table, (table_x_postion, table_y_postion))

    screen.blit(character, (character_x_postion, character_y_postion))

    pygame.display.update()  # 매 프레임 화면 업데이트

# 종료
pygame.quit()
