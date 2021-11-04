import pygame
import arcade
import math
import animation
from gokuanimation import GokuAnimation
from projectile_Goku import Projectile_Goku
from projectile_Goku_deco import Projectile_Goku1

# creer une premiere classe qui va representer notre joueur
class Goku(animation.AnimateSprite1):

    def __init__(self, game):
        super().__init__('goku')
        self.game = game
        self.health = 100
        self.health_max = 100
        self.attack = 2
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 350
        self.velocity = 1
        self.all_projectiles_player = pygame.sprite.Group()



    def change_animation(self, name): self.image = self.images[name]

    def update_animation(self):
        self.animate()

    ####################################################################################################################

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.game_over()


    ####################################################################################################################

    def update_health_bar(self, surface):
        # dessiner notre barre de vie
        pygame.draw.rect(surface, (249, 52, 10), [self.rect.x + 25, self.rect.y - 10, self.health_max, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 25, self.rect.y - 10, self.health, 5])

    ####################################################################################################################

    def lauch_projectile(self):
        self.start_animation()
        # creer une nouvelle instance de la classe Projectile
        self.all_projectiles_player.add(Projectile_Goku(self))
        self.all_projectiles_player.add(Projectile_Goku1(self))

    ####################################################################################################################

    def move_right(self):
        # si le joueur n'est pas en collision avec le Boss
        if not self.game.check_collision(self, self.game.all_boss):
            self.rect.x += self.velocity

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def move_left(self):

        self.rect.x -= self.velocity


    def jump(self):
        self.rect.y += -80
        self.rect.x += 7
        self.rect.y += -25
        self.rect.x += 7
        self.rect.y += -25
        self.rect.x += 7
        self.rect.y += -25
        self.rect.x += 15
        self.rect.y += -20


