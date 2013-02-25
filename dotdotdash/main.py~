from Sprite import *
from Player import *
import sys
pygame.init()

FPS = 30
G = 1
fpsClock = pygame.time.Clock()

DISPLAY = pygame.display.set_mode((800,400), 0, 32)
pygame.display.set_caption('DotDotDASH!')
BLACK = (0,0,0)
WHITE = (255,255,255)
rabbit = Player('resources/dot.png')
block = Sprite('resources/dot.png')
block2 = Sprite('resources/dot.png')
block3 = Sprite('resources/dot.png')
super(Sprite,block).move((400,175))
super(Sprite,block2).move((410,175))
super(Sprite,block3).move((420,175))
drawables = (rabbit,block,block2,block3)

while True:
    DISPLAY.fill(WHITE)
    for n in drawables:
        n.draw(DISPLAY)
    pygame.draw.line(DISPLAY, BLACK, (0,200),(800,200),2)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN or event.type == KEYUP:
            rabbit.update(event)
    rabbit.checkCollision(drawables)
    rabbit.move()
    rabbit.updateVel(0,G)
    pygame.display.update()
    fpsClock.tick(FPS)
    
