import pygame
import random

class Enemy:
    def __init__(self, image_path, screen_width, screen_height):
        self.image = pygame.image.load(image_path)
        self.size = self.image.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        self.x = random.uniform(0, screen_width - self.width)
        self.y = 0 - self.height

    def moveDown(self, speed, dt):
        self.y += speed * dt  # 아래로 이동

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        rect = self.image.get_rect()
        rect.left = self.x
        rect.top = self.y
        return rect

    def isOutOfScreen(self):
        if self.y > 720:
            return True
        else:
            return False

