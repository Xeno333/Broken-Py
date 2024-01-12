import pygame
#space invaders
	


def exit_proc():
	pygame.quit()
	quit()


class invader:
    pos = [0, 0]
	
    def __init__(self, value):
        self.value = value
        return
    
    def __str__(self):
         return f"pos: {self.pos} value: {self.value})"
    
    def move(self):
		#do move here
        return


class shooter:
    pos = [0, 0]

    def __init__(self, lives):
        self.lives = lives
        return
    
    def __str__(self):
         return f"pos: {self.pos} lives: {self.lives})"
    
    def move(self):
		#do move here
        return




exit_proc()