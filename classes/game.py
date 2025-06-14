import pygame
import pygame_gui
import pygame_gui.ui_manager
from settings import Colors
from .phantom import Phantom
from .maze import Maze

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
        self.p = Phantom(self.screen)
        self.m = Maze(self.screen)

        
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
            self.p.update()
            self.p.show_phantom()
            self.m.draw_maze()
            
            
        if self.status == self.END:
            pygame.quit()
            exit()
            self.running = False               
    
    def update_screen(self):
        self.manager.update(1/60)
        self.manager.draw_ui(self.screen) 
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.event_controller()
            self.status_controller()
            self.update_screen()
    