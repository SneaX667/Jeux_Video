import pygame

# definir la classe qui va gérer le projectile de notre joueur
class Projectile_Goku(pygame.sprite.Sprite):

    # definir le constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velociy = 5
        self.player = player
        self.image = pygame.image.load('assets/Boule_d_energie/Sprite/Goku_projectile.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 65
        self.rect.y = player.rect.y + 15
        self.origin_image = self.image
        self.angle = 0

    ####################################################################################################################

    def remove(self):
        self.player.all_projectiles_player.remove(self)

    ####################################################################################################################

    def move(self, player):
        self.rect.x += self.velociy

        # verifier si le projectile entre en collision avec le BOSS
        for boss in self.player.game.check_collision(self, self.player.game.all_boss):
            # supprimer le projectile
            self.remove()
            # infliger des degats
            boss.damage(self.player.attack)

        ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

        # verifier si notre projectile n'est plus present sur l'ecran
        if self.rect.x > 1575:
            # supprimer le projectile (en dehors de l'ecran)
            self.remove()
