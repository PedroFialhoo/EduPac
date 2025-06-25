import pygame
import pygame_gui
import pygame_gui.ui_manager
from settings import Colors
from .phantom import Phantom
from .maze import Maze
from .questions import Questions
import random
from .player import Player

class Game:
    def __init__(self):
          
        pygame.init()
          
        self.running = True
        self.START = 1
        self.PLAYING = 2
        self.END = 3
        
        self.status = self.START
          
        self.SCREEN_WIDTH = 1000
        self.SCREEN_HEIGHT = 800

        self.BUTTON_WIDTH = 150
        self.BUTTON_HEIGHT = 50
        
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption('EduPac')
        
        self.image = pygame.image.load("images/background.png")
        
        self.manager = pygame_gui.UIManager((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), "settings/themes.json")
        
        self.start_button = pygame_gui.elements.UIButton(
            relative_rect = pygame.Rect((self.SCREEN_WIDTH/2 - self.BUTTON_WIDTH/2, self.SCREEN_HEIGHT/2- self.BUTTON_HEIGHT/2) , (self.BUTTON_WIDTH, self.BUTTON_HEIGHT)),
            text = 'Start game',
            manager = self.manager,
            object_id = "#start_button"
        )

        self.end_button = pygame_gui.elements.UIButton(
            relative_rect = pygame.Rect((self.SCREEN_WIDTH/2 - self.BUTTON_WIDTH/2, self.SCREEN_HEIGHT/1.5- self.BUTTON_HEIGHT/2) , (self.BUTTON_WIDTH, self.BUTTON_HEIGHT)),
            text = 'X',
            manager = self.manager,
            object_id = "#end_button"
        )
        
        self.font = pygame.font.SysFont(None, 100)
        self.font2 = pygame.font.SysFont(None, 50)
        self.m = Maze(self.screen)
        self.phantoms = [
            Phantom(self.screen, self.m, 40, 120),     # canto superior esquerdo
            Phantom(self.screen, self.m, 920, 120),    # canto superior direito
            Phantom(self.screen, self.m, 40, 740),     # canto inferior esquerdo
            Phantom(self.screen, self.m, 920, 740),    # canto inferior direito
            ]

                
        self.q = Questions()
        self.q.run()

        self.player = Player(self.screen, self.m)

        
    def event_controller(self):
        for event in pygame.event.get():
            self.manager.process_events(event)
            
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                self.running = False
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.start_button:
                    self.status = self.PLAYING
                if event.ui_element == self.end_button:
                    self.status = self.END
            if event.type == pygame.KEYDOWN and self.status == self.PLAYING:
                self.player.walk_player(event.key)

                    
    
    def status_controller(self):
        if self.status == self.START:
            self.screen.fill(Colors.NAVY)
            self.screen.blit(self.image, (0, 0))
            text = self.font.render('Bem vindo ao EduPac', True, Colors.YELLOW)
            self.screen.blit(text, (150, 150))
            self.start_button.show()
            self.end_button.show()
            
            
        if self.status == self.PLAYING:   
            self.screen.fill(Colors.BLACK)
            self.start_button.hide()
            self.end_button.hide()
            for phantom in self.phantoms:
                phantom.update()
                phantom.show_phantom()

            self.m.draw_maze()       
            text = self.font.render(f"{self.q.n2} {self.q.symbol} {self.q.n1} = ?", True, Colors.YELLOW)
            self.screen.blit(text, (20, 0))
            
            self.draw_answer_options()
            self.player.showplayer()


            
            
        if self.status == self.END:
            pygame.quit()
            exit()
            self.running = False               
    
    def update_screen(self):
        self.manager.update(1/60)
        self.manager.draw_ui(self.screen) 
        pygame.display.flip()

    def draw_answer_options(self):
        pygame.draw.rect(self.screen,Colors.BLACK,((12, 85), (55,30)))
        pygame.draw.rect(self.screen,Colors.BLACK,((935, 85),(55,30)))
        pygame.draw.rect(self.screen,Colors.BLACK,((12, 740), (55,30)))
        pygame.draw.rect(self.screen,Colors.BLACK,((935, 740),(55,30)))
        options = self.q.wrong_answer.copy()
        options.append(self.q.answer)
        positions = [
        (12, 85),
        (935, 85),
        (12, 740),
        (935, 740)
        ]
        for i in range(4):            
            text = self.font2.render(f"{options[i]}", True, Colors.YELLOW)
            self.screen.blit(text, positions[i])        

    
    def run(self):       
        while self.running:
            self.event_controller()
            keys = pygame.key.get_pressed()
            if self.status == self.PLAYING:
                self.player.walk_player(keys)
            self.status_controller()
            self.update_screen()
    