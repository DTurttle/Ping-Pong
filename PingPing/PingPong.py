from pygame import *
back = (200, 255, 255)
win_height = 500
win_width = 600
background = transform.scale(image.load("background.jpg"), (win_width, win_height))
window = display.set_mode((win_width, win_height))
window.fill(back)
display.set_caption('Пинг-Понг')
clock = time.Clock()
FPS = 60
speed = 2
game = True
finish = False
mixer.init()
mixer.music.load('Dream.ogg')
mixer.music.play()
font.init()
font = font.SysFont('Arial', 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))
speed_x = 3
speed_y = 3
score_1 = 0
score_2 = 0
class GameSprite(sprite.Sprite):
   #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
    def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 500:
            lost += 1
            self.rect.x = randint(80, 700-80)
            self.rect.y = 0
ball = GameSprite('steelball.png', 270, 230, 50, 50, 2)
racket1 = Player('plunk.png', 35, 180, 40, 150, 5)
racket2 = Player('plunk.png', 530, 180, 40, 150, 5)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
  
    if finish != True:
        window.fill(back)
        window.blit(background, (0, 0))
        racket1.update_l()
        racket2.update_r()
        text = font.render("Счет Игрока 1: " + str(score_1), 1, (0, 180, 255))
        window.blit(text, (10, 20))
        text1 = font.render("Счет Игрока 2: " + str(score_2), 1, (254, 180, 1))
        window.blit(text1, (360, 20))
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
      
       #если мяч достигает границ экрана, меняем направление его движения
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

       #если мяч улетел дальше ракетки, выводим условие проигрыша для первого игрока
        if ball.rect.x < 0:
            window.blit(lose1, (200, 200))
            finish = True
            game_over = True
       #если мяч улетел дальше ракетки, выводим условие проигрыша для второго игрока
        if ball.rect.x > win_width:
            window.blit(lose2, (200, 200))
            finish = True
            game_over = True
        keys = key.get_pressed()
        if keys[K_y]:
           speed_x += 1
        if keys[K_t]:
           speed_y += 1
        if keys[K_g]:
           speed_x -= 1
        if keys[K_h]:
           speed_y -= 1
        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
