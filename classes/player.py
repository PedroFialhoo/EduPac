from settings import *
import pygame
from .maze import Maze

class Player:
    def __init__(self, screen, maze):
        self.WIDTH_PLAYER = 40
        self.HEIGHT_PLAYER = 30
        self.x_player = 480
        self.y_player = 337
        self.color = Colors.WHITE
        self.screen = screen
        self.walking = True
        self.last_direction = None        
        self.img_up = pygame.image.load("images/student-front.png")
        self.img_right = pygame.image.load("images/student-right.png")
        self.img_down = pygame.image.load("images/student-back.png")
        self.img_left = pygame.image.load("images/student-left.png")
        self.maze = maze.maze  
        self.current_img = self.img_up
        self.step_delay = 400 
        self.last_step_time = 0
        self.life = 3        
        self.player_rect = pygame.Rect(self.x_player, self.y_player, self.WIDTH_PLAYER, self.HEIGHT_PLAYER)
    
    def showplayer(self):
        self.screen.blit(self.current_img, (self.x_player, self.y_player))

    def walk_player(self, key):
        now = pygame.time.get_ticks()
        if now - self.last_step_time < self.step_delay:
             return 
        new_x = self.x_player
        new_y = self.y_player
        move = 40

        if key == pygame.K_UP or key == pygame.K_w:
            new_y -= move
            self.current_img = self.img_down
        elif key == pygame.K_DOWN or key == pygame.K_s:
            new_y += move
            self.current_img = self.img_up
        elif key == pygame.K_LEFT or key == pygame.K_a:
            new_x -= move
            self.current_img = self.img_left
        elif key == pygame.K_RIGHT or key == pygame.K_d: 
            new_x += move
            self.current_img = self.img_right

        new_rect = pygame.Rect(new_x, new_y, self.WIDTH_PLAYER, self.HEIGHT_PLAYER)

        collision = False
        for wall in self.maze:
            if new_rect.colliderect(wall):
                collision = True
                break

        if not collision:
            self.x_player = new_x
            self.y_player = new_y      
            self.player_rect.topleft = (self.x_player, self.y_player)      
            self.last_step_time = now

    def collision_answer(self, questions, rects, game):
        now = pygame.time.get_ticks()
        if now - game.last_answer_time < game.answer_cooldown:
            return  # espera cooldown terminar

        for rect in rects:
            if self.player_rect.colliderect(rect["rect"]):
                resposta = rect["text"]
                if resposta == questions.answer:
                    print("Resposta correta!")
                    game.pontuation += 100
                else:
                    print("Resposta errada!")
                    self.damage()

                self.x_player = 480
                self.y_player = 337
                self.player_rect.topleft = (self.x_player, self.y_player)

                game.last_answer_time = now  # define novo tempo base
                game.reset()
                return


    def damage(self):
        self.life -= 1