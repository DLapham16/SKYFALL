import pygame


def create_player_frames():
    """Return list of surfaces representing player animation frames."""
    frames = []
    # Two frames: standing and crouched (jumping).
    # We draw a simple stick figure for demonstration.
    for pose in range(2):
        surf = pygame.Surface((40, 60), pygame.SRCALPHA)
        color = (200, 200, 200)
        # body
        pygame.draw.rect(surf, color, pygame.Rect(18, 20, 4, 25))
        # head
        pygame.draw.circle(surf, color, (20, 12), 8)
        if pose == 0:
            # legs standing
            pygame.draw.line(surf, color, (20, 45), (10, 60), 4)
            pygame.draw.line(surf, color, (20, 45), (30, 60), 4)
            # arms
            pygame.draw.line(surf, color, (20, 25), (5, 35), 4)
            pygame.draw.line(surf, color, (20, 25), (35, 35), 4)
        else:
            # legs jumping
            pygame.draw.line(surf, color, (20, 45), (5, 50), 4)
            pygame.draw.line(surf, color, (20, 45), (35, 50), 4)
            # arms up
            pygame.draw.line(surf, color, (20, 25), (10, 10), 4)
            pygame.draw.line(surf, color, (20, 25), (30, 10), 4)
        frames.append(surf)
    return frames


def create_bird_image():
    """Create a simple bird silhouette surface."""
    surf = pygame.Surface((40, 30), pygame.SRCALPHA)
    color = (50, 50, 50)
    # body
    pygame.draw.ellipse(surf, color, pygame.Rect(5, 10, 30, 15))
    # wings
    pygame.draw.polygon(surf, color, [(5, 15), (0, 5), (10, 12)])
    pygame.draw.polygon(surf, color, [(35, 15), (40, 5), (30, 12)])
    # head
    pygame.draw.circle(surf, color, (35, 15), 5)
    return surf
