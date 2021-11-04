import pygame
import math

# definir une classe qui va s'occuper des animations
class AnimateSprite(pygame.sprite.Sprite):

    # definir les choses a faire a la création de l'entité
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.current_image = 0  # commencer l'anim a l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    # definir une methode pour demarrer l animation
    def start_animation(self):
        self.animation = True

    def animate(self, loop=False):

        # verifier si l animation est active
        if self.animation:

            # passer a l'image suivante
            self.current_image += 0.03

            # verifier si on a atteint la fin de l'animation
            if self.current_image >= len(self.images):
                # remettre l'animation au depart
                self.current_image = 0

                # verifier si l'animation n'est pas en mode boucle
                if loop is False:
                    # desactivation de l'animation
                    self.animation = False

            # modifier l'image precedente par la suivante
            self.image = self.images[math.floor(self.current_image)]
            self.image = pygame.transform.scale(self.image, (150, 150))


def load_animation_freezer_projectile_images(sprite_name):
    images = []

    # definie le chemin empruntée
    path = f"assets/freezer/{sprite_name}"

    # boucler sur chaque image dans ce dossier
    for num in range(1, 7):
        image_path = path + str(num) + '.png'
        images.append((pygame.image.load(image_path)))

    # renvoyer le contenu de la liste d'images
    return images


class AnimateSprite1(pygame.sprite.Sprite):

    # definir les choses a faire a la création de l'entité
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.current_image = 0  # commencer l'anim a l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    # definir une methode pour demarrer l animation
    def start_animation(self):
        self.animation = True

    def animate(self, loop=False):

        # verifier si l animation est active
        if self.animation:

            # passer a l'image suivante
            self.current_image += 0.02

            # verifier si on a atteint la fin de l'animation
            if self.current_image >= len(self.images):
                # remettre l'animation au depart
                self.current_image = 0

                # verifier si l'animation n'est pas en mode boucle
                if loop is False:
                    # desactivation de l'animation
                    self.animation = False

            # modifier l'image precedente par la suivante
            self.image = self.images[math.floor(self.current_image)]
            self.image = pygame.transform.scale(self.image, (150, 150))


def load_animation_goku_projectile_images(sprite_name):
    images = []

    # definie le chemin empruntée
    path = f"assets/goku/{sprite_name}"

    # boucler sur chaque image dans ce dossier
    for num in range(1, 6):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    # renvoyer le contenu de la liste d'images
    return images


def load_animation_dash_arriere_images(sprite_name):
    images = []

    # definie le chemin empruntée
    path = f"assets/goku/dash/{sprite_name}"

    # boucler sur chaque image dans ce dossier
    for num in range(1, 3):
        image_path = path + str(num) + '.png'
        images.append((pygame.image.load(image_path)))

    # renvoyer le contenu de la liste d'images
    return images


# definir un dictionnaire qui va contenir les images chargées de chaque sprite
# mummy -> [...mummy1.png,...
animations = {
    'goku': load_animation_goku_projectile_images('goku'),
    'freezer': load_animation_freezer_projectile_images('freezer'),
    'dash': load_animation_dash_arriere_images('dash')
    }
