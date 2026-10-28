"""Little Signals: an interactive starting point for your own Python app."""
import argparse
import os

WIDTH, HEIGHT = 800, 500


def add_signal(count):
    return count + 1


def capped_position(x, y, width, height):
    return max(0, min(x, width - 1)), max(0, min(y, height - 1))


def run(smoke_test=False):
    if smoke_test:
        os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
        os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
    import pygame

    pygame.init()
    try:
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Little Signals")
        font = pygame.font.Font(None, 36)
        small = pygame.font.Font(None, 25)
        clock = pygame.time.Clock()
        position = (WIDTH // 2, HEIGHT // 2)
        count = 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    position = capped_position(*event.pos, WIDTH, HEIGHT)
                    count = add_signal(count)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
            screen.fill((19, 41, 51))
            pygame.draw.circle(screen, (251, 190, 110), position, 30)
            screen.blit(font.render(f"Little Signals / {count}", True, (248, 244, 228)), (30, 30))
            screen.blit(small.render("Click to place a signal. Esc to quit.", True, (171, 208, 195)), (30, HEIGHT - 45))
            pygame.display.flip()
            clock.tick(60)
            if smoke_test:
                print("Smoke test: one frame drawn")
                break
    finally:
        pygame.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--smoke-test", action="store_true", help="draw one frame without a visible window")
    run(parser.parse_args().smoke_test)
