import pygame

class Projectile_Freezer1(pygame.sprite.Sprite):

    # definir le constructeur de cette classe
    def __init__(self, boss):
        super().__init__()
        self.velociy = 2
        self.boss = boss
        self.image = pygame.image.load('assets/Boule_d_energie/Sprite/Freezer_projectil_deco.png')
        self.image = pygame.transform.scale(self.image, (170, 170))
        self.rect = self.image.get_rect()
        self.rect.x = boss.rect.x - 120
        self.rect.y = boss.rect.y - 10
        self.origin_image = self.image
        self.angle = 0

    ####################################################################################################################

    def remove(self):
        self.boss.all_projectiles_boss.remove(self)

    ####################################################################################################################

    def move(self, boss):
        self.rect.x -= self.velociy

        # verifier si notre projectile n'est plus present sur l'ecran
        if self.rect.x < boss.rect.x - 170:
            # supprimer le projectile (en dehors de l'ecran)
            self.remove()
