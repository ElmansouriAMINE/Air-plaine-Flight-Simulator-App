import pygame

pygame.init()

# création de la fenêtre
screen = pygame.display.set_mode((640, 480))

# définir la couleur de fond
bg_color = (255, 255, 255)

# créer un objet police
font = pygame.font.Font(None, 36)

# créer un objet texte
text = font.render("Texte brillant", True, (255, 0, 0))

# définir le rect du texte
text_rect = text.get_rect()
text_rect.center = screen.get_rect().center

# définition des variables de clignotement
blink_interval = 500  # temps de clignotement en millisecondes
next_blink = pygame.time.get_ticks() + blink_interval
blink = True

# boucle de jeu
while True:
    # gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # dessiner le fond
    screen.fill(bg_color)

    # vérifier si le texte doit clignoter
    if pygame.time.get_ticks() >= next_blink:
        next_blink += blink_interval
        blink = not blink

    # dessiner le texte si nécessaire
    if blink:
        screen.blit(text, text_rect)

    # mise à jour de l'affichage
    pygame.display.update()
