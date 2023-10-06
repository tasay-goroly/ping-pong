from pygame import*
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, sise_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, sise_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        windows.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys_pressed[K_DOWN] and self.rect.y<620:
            self.rect.y+=self.speed
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys_pressed[K_s] and self.rect.y<620:
            self.rect.y+=self.speed

back =(200,225,225)
win_width=600
win_height=500
windows = display.set_mode((600,500))
windows.fill(back)
game=True
finish=False
clock=time.Clock()
FPS=60


racket1=Player('images.jpg',30,200,50,150,4)
racket2=Player('images.jpg',500,200,50,150,4)
ball= GameSprite('мяч.png',200,200,50,50,4)

font.init()
font = font.Font( None, 35)
lose1=font.render('player 1 lose', True, (180,0,0))
lose2=font.render('player 2 lose', True, (180,0,0))
speed_x=3
speed_y=3
while game:
    for e in event.get():
        if e.type == QUIT:
            game=False
    if finish != True:
        windows.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        

        if sprite.collide_rect(racket1, ball)or sprite.collide_rect(racket2, ball):
            speed_y*=-1
            speed_x*=-1


        if ball.rect.y>win_height-50 or ball.rect.y<0:
            speed_y*=-1

        if ball.rect.x<0:
            finish=True
            windows.blit(lose1,(200,200))
            game_over=True
        if ball.rect.x>win_width:
            finish=True
            windows.blit(lose2,(200,200))
            game_over=True
        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)