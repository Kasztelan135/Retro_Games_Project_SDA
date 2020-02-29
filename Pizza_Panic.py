from superwires import games, color
import random

games.init(screen_width=640, screen_height=480, fps=50)


class Pan(games.Sprite):
    image = games.load_image("patelnia.bmp")

    def __init__(self):
        super(Pan, self).__init__(image=Pan.image,
                                  x=games.mouse.x,
                                  bottom=games.screen.height)

        self.score = games.Text(value=0, size=40, color=color.black, top=5, right=games.screen.width-10)
        games.screen.add(self.score)

    def update(self):
        self.x = games.mouse.x

        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
        self.check_catch()

    def check_catch(self):
        for pizza in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10
            pizza.handle_caught()


class Pizza(games.Sprite):
    image = games.load_image("pizza.bmp")
    speed = 8

    def __init__(self, x, y=90):
        super(Pizza, self).__init__(image=Pizza.image,
                                    x=x, y=y,
                                    dy=Pizza.speed)

    def update(self):
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()

    def handle_caught(self):
        self.destroy()

    def end_game(self):
        end_message = games.Message(value="Pizza upadła! Koniec gry!",
                                    size=60,
                                    color=color.yellow,
                                    x=games.screen.width / 2,
                                    y=games.screen.height / 2,
                                    lifetime=5 * games.screen.fps,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)


class Chef(games.Sprite):
    image = games.load_image("kucharz.bmp")

    def __init__(self, y=55, speed=5, odds_change=500):
        super(Chef, self).__init__(image=Chef.image,
                                   x=games.screen.width/2,
                                   y=y,
                                   dx=speed)

        self.odds_change = odds_change
        self.time_til_drop = 0

    def update(self):
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx

        self.check_drop()

    def check_drop(self):
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_pizza = Pizza(x=self.x)
            games.screen.add(new_pizza)
            self.time_til_drop = int(new_pizza.height * 1.3 / Pizza.speed) + 1


def main():
    games.music.load('Lou Monte.mp3')
    games.music.play(-1)

    wall_image = games.load_image("sciana.jpg", transparent=False)
    games.screen.background = wall_image

    chef = Chef()
    games.screen.add(chef)

    pan = Pan()
    games.screen.add(pan)

    games.mouse.is_visible = False

    games.screen.mainloop()


if __name__ == "__main__":
    main()
