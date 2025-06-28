from .questions import Questions

class LevelController:
    def __init__(self):
        pass
        
    def lvl2(self, game):
        game.q.operation = [1, 2, 3, 4]    
        
    def lvl3(self, game):        
        game.q.operation = [1, 2, 3, 4, 5]
        
    def change_level(self, pontuation, game):
        if pontuation == 1000:
            self.lvl2(game)
            game.current_level = 2 
        if pontuation == 2000:
            self.lvl3(game)            
            game.current_level = 3  