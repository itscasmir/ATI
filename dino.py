'''
this game is going to be a representation of the intial dino game with changes done to improve user inteface.
this game will satisfy error handling, a search algorith as well as sort algorithm
there would be an instance to switch users implemented into this code 
the aim of this game is to facilitate and furtherly improve the initial game. providing a different feeling the past users of the chrome dino game


'''



#importing the required modules and libraries to run this game
import pygame
import os
import random
import json

pygame.init()

# Global constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Load images
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

# Font initialization
font = pygame.font.Font('freesansbold.ttf', 20)

# Variables to store player data
player_name = ""
high_scores = {}

# Dinosaur class definition
class Dinosaur:
    #dino x and y location in game
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = Ducking #for ducking birds
        self.run_img = Running #for running
        self.jump_img = Jumping # for jumping over cactus and obstacles

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    # Update the state of the dinosaur
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

    # Handle ducking animation
    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    # Handle running animation
    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    # Handle jumping animation
    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    # Draw the dinosaur on the screen
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


# Cloud class definition
class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    # Update cloud position
    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    # Draw cloud on the screen
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

# Obstacle class definition
class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    # Update obstacle position
    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    # Draw obstacle on the screen
    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


# Small Cactus class definition
class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325

# Large Cactus class definition
class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300

# Bird class definition
class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    # Draw bird with flapping wings
    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index // 5], self.rect)
        self.index += 1

# Function to Read high scores from file
def read_high_scores():
    global high_scores
    if not os.path.isfile('highscores.json'):
        return {}
    with open('highscores.json', 'r') as file:
        try:
            high_scores = json.load(file)
        except ValueError:
            return {}
    return high_scores

# Function to Write high scores to file
def write_high_scores():
    global high_scores
    with open('highscores.json', 'w') as file:
        json.dump(high_scores, file)

# Get player name
def get_player_name():
    global player_name
    run = True
    user_text = ''
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)
        text = font.render("Enter your name: " + user_text, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, text_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    player_name = user_text
                    run = False
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

# Search high score by username
def search_high_score(username):
    global high_scores
    return high_scores.get(username, "User not found")

# Sort high scores in descending order
def sort_high_scores():
    global high_scores
    return sorted(high_scores.items(), key=lambda item: item[1], reverse=True)

# Display all high scores
def display_high_scores():
    sorted_scores = sort_high_scores()
    y_offset = 50
    SCREEN.fill((255, 255, 255))
    font = pygame.font.Font('freesansbold.ttf', 30)
    title = font.render("High Scores", True, (0, 0, 0))
    title_rect = title.get_rect()
    title_rect.center = (SCREEN_WIDTH // 2, 20)
    SCREEN.blit(title, title_rect)

    for username, score in sorted_scores:
        score_text = font.render(f"{username}: {score}", True, (0, 0, 0))
        score_rect = score_text.get_rect()
        score_rect.topleft = (50, y_offset)
        SCREEN.blit(score_text, score_rect)
        y_offset += 30

    pygame.display.update()
    pygame.time.wait(3000)

# Function to display user's high score
def display_user_high_score(username, score):
    global player_name, high_scores
    SCREEN.fill((255, 255, 255))
    font = pygame.font.Font('freesansbold.ttf', 30)
    
    if username in high_scores:
        score_text = font.render(f"High Score for {username}: {high_scores[username]}", True, (0, 0, 0))
    else:
        score_text = font.render(f"No high score found for {username}", True, (0, 0, 0))
    
    score_rect = score_text.get_rect()
    score_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    SCREEN.blit(score_text, score_rect)
    
    pygame.display.update()
    pygame.time.wait(3000)


# Main function to run the game
def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles, player_name, high_scores
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    cloud = Cloud()
    game_speed = 14
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    obstacles = []
    death_count = 0

     # Function to display current score
    def score():
        global points, game_speed, high_scores
        points += 1
        if points % 100 == 0:
            game_speed += 1

        if points > high_scores.get(player_name, 0):
            high_scores[player_name] = points
            write_high_scores()

        text = font.render(f"Points: {points}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 40)
        SCREEN.blit(text, text_rect)


     # Function to display background
    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(small_cactus))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(large_cactus))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                death_count += 1
                menu(death_count)

        background()

        cloud.draw(SCREEN)
        cloud.update()

        score()

        pygame.display.update()
        clock.tick(30)

# Function to display menu
def menu(death_count):
    global points, player_name, high_scores
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)
        
        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
            SCREEN.blit(text, text_rect)
            # Draw a line below the text
            pygame.draw.line(SCREEN, (0, 0, 0), (text_rect.left, text_rect.bottom + 5), (text_rect.right, text_rect.bottom + 5), 2)
        elif death_count > 0:
            # Increase the size of the box
            box_width = 700
            box_height = 500
            box_x = (SCREEN_WIDTH - box_width) // 2
            box_y = (SCREEN_HEIGHT - box_height) // 2

            # Draw the background box
            pygame.draw.rect(SCREEN, (200, 200, 200), (box_x, box_y, box_width, box_height))
            pygame.draw.rect(SCREEN, (0, 0, 0), (box_x, box_y, box_width, box_height), 2)

            # Game Over Text
            game_over_text = font.render("Game Over", True, (0, 0, 0))
            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, box_y + 50))
            SCREEN.blit(game_over_text, game_over_rect)

            # Display Score
            score_text = font.render(f"Your Score: {points}", True, (0, 0, 0))
            score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, box_y + 100))
            SCREEN.blit(score_text, score_rect)

            # Display High Score
            high_score_text = font.render(f"High Score ({player_name}): {high_scores.get(player_name, 0)}", True, (0, 0, 0))
            high_score_rect = high_score_text.get_rect(center=(SCREEN_WIDTH // 2, box_y + 150))
            SCREEN.blit(high_score_text, high_score_rect)

            # Display Options
            options = [
                "Press any Key to Restart",
                "Press S to Switch User",
                "Press F to Search by Username",
                "Press P to Show Sorted High Scores"
            ]
            option_positions = [
                (SCREEN_WIDTH // 2, box_y + 200),
                (SCREEN_WIDTH // 2, box_y + 250),
                (SCREEN_WIDTH // 2, box_y + 300),
                (SCREEN_WIDTH // 2, box_y + 350)
            ]

            for i, option in enumerate(options):
                option_text = font.render(option, True, (0, 0, 0))
                option_rect = option_text.get_rect(center=option_positions[i])
                SCREEN.blit(option_text, option_rect)

        SCREEN.blit(Running[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 250))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    get_player_name()
                elif event.key == pygame.K_f:
                    pygame.event.clear()  # Clear previous events to avoid unexpected inputs
                    username_entered = False
                    username = ""
                    while not username_entered:
                        SCREEN.fill((255, 255, 255))
                        input_text = font.render(f"Enter username to search: {username}", True, (0, 0, 0))
                        input_text_rect = input_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                        SCREEN.blit(input_text, input_text_rect)
                        pygame.draw.line(SCREEN, (0, 0, 0), (input_text_rect.left, input_text_rect.bottom + 5), (input_text_rect.right, input_text_rect.bottom + 5), 2)
                        pygame.display.update()

                        for event_search in pygame.event.get():
                            if event_search.type == pygame.QUIT:
                                pygame.quit()
                                run = False
                                username_entered = True
                            elif event_search.type == pygame.KEYDOWN:
                                if event_search.key == pygame.K_RETURN:
                                    username_entered = True
                                elif event_search.key == pygame.K_BACKSPACE:
                                    username = username[:-1]
                                elif event_search.unicode.isalnum():
                                    username += event_search.unicode

                    if username.strip():  # If username is not empty after input
                        display_user_high_score(username, high_scores.get(username, 0))
                    pygame.time.delay(1000)  # Delay to avoid immediate exit
                elif event.key == pygame.K_p:
                    display_high_scores()
                else:
                    main()


# Main entry point of the game
if __name__ == "__main__":
    read_high_scores()
    get_player_name()
    menu(death_count=0)
