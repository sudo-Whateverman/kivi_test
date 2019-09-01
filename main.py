from kivy.animation import Animation
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class Fly_b(Widget):
    def __init__(self, **kwargs):
        self.velocity_x = NumericProperty(0)
        self.velocity_y = NumericProperty(0)
        self.angle_prop = randint(0, 360)
        self.velocity = ReferenceListProperty(self.velocity_x, self.velocity_y)
        self.angle = self.angle_prop
        super(Fly_b, self).__init__(**kwargs)

        
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
        self.angle = Vector(*self.velocity).angle((1, 0))
        # print("POS: {}".format(self.pos))
        # print("VEL: {}".format(self.velocity))
        # print("ANGLE: {}".format(self.angle))
        # self.btn1.text = "{:.0f}".format(self.angle)

    def callback(self, instance):
        # print("click")
        self.velocity = Vector(4, 0).rotate(randint(0, 360))

class FlyGame(Widget):
    fly_b = ObjectProperty(None)

    def start_fly(self):
        self.fly_b.center = self.center
        self.fly_b.velocity = Vector(4, 0).rotate(randint(0, 360))

    def update(self, dt):
        self.fly_b.move()

        # bounce off top and bottom
        if (self.fly_b.btn.y < 0) or (self.fly_b.btn.top > self.height):
            self.fly_b.velocity.y *= -1
        # bounce off left and right
        if (self.fly_b.btn.x < 0) or (self.fly_b.btn.right > self.width):
            self.fly_b.velocity.x *= -1

        self.fly_b.btn.text = "{:.0f}".format(self.fly_b.angle)

class PongApp(App):
    def build(self):
        game = FlyGame()
        game.start_fly()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    PongApp().run()
