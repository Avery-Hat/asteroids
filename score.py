import pygame


class Score(object):
    def __init__(self):
        self.count = 0
        self.font = pygame.font.SysFont("comicsans",50,True,True)
        self.text = self.font.render("Score :" +str(self.count),1,"white")
    
    def show_score(self,screen):
        screen.blit(self.text,(100,100))
    
    def score_up(self):
        self.count += 100
        self.text = self.font.render("Score :" +str(self.count),1,"white")
        