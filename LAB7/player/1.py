import pygame
pygame.init()
pygame.mixer.init()
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")
playlist = ['1.mp3', '2.mp3', '3.mp3']
current_track = 0
pygame.mixer.music.load(playlist[current_track])
pygame.mixer.music.play()
running = True
while running:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_track])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_track = (current_track - 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_track])
                pygame.mixer.music.play()
    pygame.display.flip()
    
pygame.quit()