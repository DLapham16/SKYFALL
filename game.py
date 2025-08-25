import random
import sys
import pygame

from assets import create_player_frames, create_bird_image

WIDTH, HEIGHT = 800, 400
GRAVITY = 0.6


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.frames = create_player_frames()
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.vel_y = 0
        self.on_ground = True

    def jump(self):
        if self.on_ground:
            self.vel_y = -12
            self.on_ground = False

    def update(self):
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y
        if self.rect.bottom >= HEIGHT - 20:
            self.rect.bottom = HEIGHT - 20
            self.vel_y = 0
            self.on_ground = True
        self.animate()

    def animate(self):
        # Simple two frame animation
        self.frame_index += 0.1
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = create_bird_image()
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.speed = random.randint(5, 9)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()


def spawn_bird(group):
    y = random.randint(100, HEIGHT - 50)
    bird = Bird(WIDTH + 50, y)
    group.add(bird)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Skyfall")

    player = Player(100, HEIGHT - 20)
    all_sprites = pygame.sprite.Group(player)
    birds = pygame.sprite.Group()

    BIRD_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(BIRD_EVENT, 1500)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player.jump()
            elif event.type == BIRD_EVENT:
                spawn_bird(birds)
                all_sprites.add(birds)

        all_sprites.update()

        if pygame.sprite.spritecollide(player, birds, False):
            running = False

        screen.fill((135, 206, 235))  # sky blue
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
