import pygame

pygame.init()

# set up the display window
screen = pygame.display.set_mode((800, 600))

# load the image to be animated
image = pygame.image.load('img/TT.png')
image_rect = image.get_rect()

# set the initial position of the image
x = 0
y = 0

# set the speed of the animation
speed = 0.02

# start the game loop
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # move the image
    x -= speed
    
    # check if the image has gone off the screen and reset its position
    if x > screen.get_width():
        x = 0
    
    # draw the image to the screen
    screen.blit(image, (x, y))
    
    # update the display
    pygame.display.update()
