import pygame
import math
from game import Game

pygame.init()

# generer la fenetre de notre jeu
pygame.display.set_caption("DBZ")
screen = pygame.display.set_mode((1575, 600))

########################################################################################################################

# importer et charger l'arriere plan de notre jeu
background = pygame.image.load('assets/Terre_plaine2.png')
background = pygame.transform.scale(background, (1575, 600))


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# importer et charger la banniere de notre jeu
banner = pygame.image.load('assets/logo.png')
banner = pygame.transform.scale(banner, (624, 193))
banner_rect = banner.get_rect()
banner_rect.y = 150
banner_rect.x = 470

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# importer et charger le bouton de la banniere de notre jeu
play_button = pygame.image.load('assets/bouton1.png')
play_button = pygame.transform.scale(play_button, (250, 250))
play_button_rect = play_button.get_rect()
play_button_rect.y = 300
play_button_rect.x = 650

########################################################################################################################

# charger notre jeu
game = Game()

running = True

# boucle tant que cette condition est vrai
while running:

    # appliquer la fenetre du jeu
    screen.blit(background, (0, 0))

    ####################################################################################################################

    # verifier si notre jeu a commence ou non
    if game.is_playing:
        # declencher les instructions de la partie
        game.update1(screen)
        game.gravite_jeu1()
        game.gravite_jeu2()

        ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    # verifier si notre jeu n'a pas commence
    else:
        # ajouter mon ecran de bienvenue
        screen.blit(play_button, (play_button_rect))
        screen.blit(banner, (banner_rect))

    # mettre à jour l'ecran
    pygame.display.flip()

    ####################################################################################################################

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

            ############################################################################################################

        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True


            ############################################################################################################

            # detecter si la touche choisie est enclenchée pour lancer notre projectile
            # pour le joueur
            if event.key == pygame.K_s:
                game.player.lauch_projectile()

            ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

            # pour le boss
            if event.key == pygame.K_DOWN:
                game.boss.lauch_projectile()

            ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

            # detecter si la touche choisie est enclenchée pour sauter
            if event.key == pygame.K_z:
                game.player.jump()

            ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

            # detecter si la touche chosie est enclenchée pour sauter
            if event.key == pygame.K_UP:
                game.boss.jump()

            ############################################################################################################

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

            ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification pour savoir si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode "lancé"
                game.start()
