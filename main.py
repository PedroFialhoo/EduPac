import pygame
import pygame_gui
import pygame_gui.ui_manager
from colors import Colors

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50

START = 1
PLAYING = 2
END = 3

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('EduPac')
screen.fill(Colors.NAVY)

image = pygame.image.load("background.png")
screen.blit(image, (0, 0))


font = pygame.font.SysFont(None, 100)
text = font.render('Bem vindo ao EduPac', True, Colors.YELLOW)
screen.blit(text, (150, 150))

manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT), "themes.json")


start_button = pygame_gui.elements.UIButton(
    relative_rect = pygame.Rect((SCREEN_WIDTH/2 - BUTTON_WIDTH/2, SCREEN_HEIGHT/2-BUTTON_HEIGHT/2) , (BUTTON_WIDTH,BUTTON_HEIGHT)),
    text = 'Start game',
    manager = manager,
    object_id = "#start_button"
)

end_button = pygame_gui.elements.UIButton(
    relative_rect = pygame.Rect((SCREEN_WIDTH/2 - BUTTON_WIDTH/2, SCREEN_HEIGHT/1.5-BUTTON_HEIGHT/2) , (BUTTON_WIDTH,BUTTON_HEIGHT)),
    text = 'X',
    manager = manager,
    object_id = "#end_button"
)


running = True
status = START

while running:
    for event in pygame.event.get():
        manager.process_events(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == start_button:
                status = PLAYING                
                print('jogando')
                screen.blit(image, (0, 0))
                text = font.render('Jogando', True, Colors.YELLOW)
                screen.blit(text, (350, 150))
                start_button.hide()
            if event.ui_element == end_button:
                status = END
                running = False

    manager.update(1/60)
    manager.draw_ui(screen)
    

    pygame.display.flip()