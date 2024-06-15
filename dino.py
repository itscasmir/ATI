import pygame
import os

pygame.init()

# Global constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

Running = [pygame.image.load(os.path.join("pic/dino", "DinoRun1.png")), pygame.image.load(os.path.join("pic/dino", "DinoRun2.png"))]
Jumping = pygame.image.load(os.path.join("pic/dino", "DinoJump.png"))
Ducking = [pygame.image.load(os.path.join("pic/dino/DinoDuck1 (1).png")), pygame.image.load(os.path.join("pic/dino/DinoDuck2 (1).png"))]
small_cactus = [pygame.image.load(os.path.join("pic/cactus/SmallCactus1.png")),
                pygame.image.load(os.path.join("pic/cactus/SmallCactus2.png")),
                pygame.image.load(os.path.join("pic/cactus/SmallCactus3.png"))]

large_cactus = [pygame.image.load(os.path.join("pic/cactus/LargeCactus1.png")), 
                pygame.image.load(os.path.join("pic/cactus/LargeCactus2.png")),
                pygame.image.load(os.path.join("pic/cactus/LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("pic/bird/Bird1.png")), 
        pygame.image.load(os.path.join("pic/bird/Bird2.png"))]

CLOUD = pygame.image.load(os.path.join("pic/other/Cloud.png"))

BG = pygame.image.load(os.path.join("pic/other/Track.png"))

class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    

    def __init__(self):
        self.duck_img = Ducking
        self.run_img = Running
        self.jump_img = Jumping

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0
        
        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        pass

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

def main():
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        clock.tick(30)
        pygame.display.update()

main()
