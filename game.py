import pygame
from player import Goku
from boss import Freezer
from sol import Sol1

# creer une seconde classe qui va representer notre jeu
class Game:

    def __init__(self):
        # definir si notre jeu a commence ou non
        self.is_playing = False
        self.gravite1 = (0, 1)
        self.gravite2 = (0, 1)
        self.resistance1 = (0, 0)
        self.resistance2 = (0, 0)
        self.sol = Sol1()

        ################################################################################################################

        # generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Goku(self)
        self.all_players.add(self.player)
        self.pressed = {}

        ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

        # generer notre Boss
        self.all_boss = pygame.sprite.Group()
        self.boss = Freezer(self)
        self.all_boss.add(self.boss)
        self.pressed = {}

    ####################################################################################################################

    def start(self):
        self.is_playing = True


    ####################################################################################################################

    def game_over(self):
        # remettre le jeu a neuf, retirer le boss, les projectiles, remettre le joueur a 100 de vie et le jeux en attente
        self.player.all_projectiles_player = pygame.sprite.Group()
        self.boss.all_projectiles_boss = pygame.sprite.Group()
        self.boss.health = self.boss.health_max
        self.player.health = self.player.health_max
        self.is_playing = False

    ####################################################################################################################

    def update1(self, screen):
        # appliquer l'image de mon monstre
        screen.blit(self.boss.image, self.boss.rect)

        # actualiser la barre de vie du Boss
        self.boss.update_health_bar(screen)
        self.boss.update_animation()

        # recuperer les projectiles du Boss
        for projectile in self.boss.all_projectiles_boss:
            projectile.move(self.boss)

        # appliquer l'ensemble des images de mon groupe de projectiles Boss
        self.boss.all_projectiles_boss.draw(screen)

        ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

        # appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)
        self.player.update_animation()

        # recuperer les projectiles du joueur
        for projectile in self.player.all_projectiles_player:
            projectile.move(self.player)

         # appliquer l'ensemble des images de mon groupe de projectiles player
        self.player.all_projectiles_player.draw(screen)

        ################################################################################################################

        # verifier si le joueur souhaite aller a gauche ou a droite
        if self.pressed.get(pygame.K_d) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_q) and self.player.rect.x > 0:
            self.player.move_left()

        ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

        if self.pressed.get(pygame.K_RIGHT) and self.boss.rect.x + self.boss.rect.width < 1350:
            self.boss.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.boss.rect.x > 0:
            self.boss.move_left()

        ################################################################################################################

        # verifier si le joueur souhaite sauter
        if self.sol.rect.colliderect(self.player.rect):
            self.resistance1 = (0, -1)
        else:
            self.resistance1 = (0, 0)

        ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

        if self.sol.rect.colliderect(self.boss.rect):
            self.resistance2 = (0, -1)
        else:
            self.resistance2 = (0, 0)

        ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



    ####################################################################################################################

    def gravite_jeu1(self):
        self.player.rect.y += self.gravite1[1] + self.resistance1[1]

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def gravite_jeu2(self):
        self.boss.rect.y += self.gravite2[1] + self.resistance2[1]

    ####################################################################################################################

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    ####################################################################################################################


