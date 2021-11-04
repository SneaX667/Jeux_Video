import pygame

class Projectile_Goku1(pygame.sprite.Sprite):

    # definir le constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velociy = 1
        self.player = player
        self.image = pygame.image.load('assets/Boule_d_energie/Sprite/Goku_projectile.png')
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 75
        self.rect.y = player.rect.y + 5
        self.origin_image = self.image
        self.angle = 0

    ####################################################################################################################

    def remove(self):
        self.player.all_projectiles_player.remove(self)

    ####################################################################################################################

    def move(self, player):
        self.rect.x += self.velociy

        # verifier si notre projectile n'est plus present sur l'ecran
        if self.rect.x > player.rect.x + 100:
            # supprimer le projectile (en dehors de l'ecran)
            self.remove()
