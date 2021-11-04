import pygame

# definir la classe qui va gérer le projectile de notre Boss
class Projectile_Freezer(pygame.sprite.Sprite):

    # definir le constructeur de cette classe
    def __init__(self, boss):
        super().__init__()
        self.velociy = 4
        self.boss = boss
        self.image = pygame.image.load('assets/Boule_d_energie/Sprite/Freezer_projectile.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = boss.rect.x - 195
        self.rect.y = boss.rect.y + 45
        self.origin_image = self.image
        self.angle = 0

    ####################################################################################################################

    def remove(self):
        self.boss.all_projectiles_boss.remove(self)

    ####################################################################################################################

    def move(self, boss):
        self.rect.x -= self.velociy

        # verifier si le projectile entre en collision avec le joueur
        for player in  self.boss.game.check_collision(self, self.boss.game.all_players):
            # supprimer le projectile
            self.remove()
            # infliger des degats
            player.damage(self.boss.attack)

        ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

        # verifier si notre projectile n'est plus present sur l'ecran
        if self.rect.x > 3000:
            # supprimer le projectile (en dehors de l'ecran)
            self.remove()
