import pygame
import animation
from projectile_Freezer1 import Projectile_Freezer
from projectile_Freezer_deco import Projectile_Freezer1



# creer une classe qui va gerer la notion du Boss sur notre jeu
class Freezer(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('freezer')
        self.game = game
        self.health = 100
        self.health_max = 100
        self.attack = 2
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = 1300
        self.rect.y = 350
        self.velocity = 1
        self.all_projectiles_boss = pygame.sprite.Group()

    def update_animation(self):
        self.animate()

    ####################################################################################################################

    def damage(self, amount):
        self.health -= amount

        # verifier sis on nouveau nombre de point de vie est inferieur ou egal a 0
        if self.health <= 0:
            self.game.game_over()

    ####################################################################################################################

    def update_health_bar(self, screen):
        # dessine la barre de vie du Boss
        pygame.draw.rect(screen, (249, 52, 10), [self.rect.x + 15, self.rect.y - 12, self.health_max, 5])
        pygame.draw.rect(screen, (111, 210, 46), [self.rect.x + 15, self.rect.y - 12, self.health, 5])

    ####################################################################################################################

    def lauch_projectile(self):
        self.start_animation()
        # creer une nouvelle instance de la classe Projectile
        self.all_projectiles_boss.add(Projectile_Freezer(self))
        self.all_projectiles_boss.add(Projectile_Freezer1(self))


    ####################################################################################################################

    def move_right(self):
        self.rect.x += self.velocity

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def move_left(self):
        # si le Boss n'est pas en collision avec le joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity

    ####################################################################################################################

    def jump(self):
        self.rect.y += -25
        self.rect.x += -7
        self.rect.y += -25
        self.rect.x += -7
        self.rect.y += -25
        self.rect.x += -7
        self.rect.y += -25
        self.rect.x += -7
        self.rect.y += -25
        self.rect.x += -7
        self.rect.y += -25
        self.rect.x += -7
