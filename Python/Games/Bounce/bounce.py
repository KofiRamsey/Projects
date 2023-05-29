import pygame

pygame.init()

width = 1000
height = 600
screen_res = (width, height)

pygame.display.set_caption("Ramsey's Bounce")
screen = pygame.display.set_mode(screen_res)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# ball
ball_obj = pygame.draw.circle(surface=screen, color=red, center=[100, 100], radius=40)
# speed = [X direction speed, Y direction speed]
speed = [1, 1]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill(black)

    # move the ball
    # Let center of the ball is (100,100) and the speed is (1,1)
    ball_obj = ball_obj.move(speed)
    
    # if ball goes out of screen then change direction of movement
    if ball_obj.left <= 0 or ball_obj.right >= width:
        speed[0] = -speed[0]
    if ball_obj.top <= 0 or ball_obj.bottom >= height:
        speed[1] = -speed[1]

    # draw ball at new centers that are obtained after moving ball_obj
    pygame.draw.circle(surface=screen, color=red, center=ball_obj.center, radius=40)

    pygame.display.flip()
