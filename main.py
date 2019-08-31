from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
import numpy as np

class Fly(Widget):


    def __init__(self, **kwargs):
        super(Fly, self).__init__(**kwargs)
        self.velocity_x = NumericProperty(0)
        self.velocity_y = NumericProperty(0)
        self.angle = NumericProperty(0)
        self.velocity = ReferenceListProperty(self.velocity_x, self.velocity_y)
        self.btn1 = Button(text='Hello World 1', font_size="15sp",
                      background_color=(1, 1, 1, 1),
                      color=(1, 1, 1, 1),
                        pos = (self.x, self.y))
        self.btn1.bind(on_press = self.callback)
        self.add_widget(self.btn1)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
        self.angle = Vector(*self.velocity).angle((0, 180))
        # print("POS: {}".format(self.pos))
        # print("VEL: {}".format(self.velocity))
        # print("ANGLE: {}".format(self.angle))
        self.btn1.text = "{:.0f}".format(self.angle)

    def callback(self, instance):
        self.velocity = Vector(4, 0).rotate(randint(0, 360))

class FlyGame(Widget):
    fly = ObjectProperty(None)

    def start_fly(self):
        self.fly.center = self.center
        self.fly.velocity = Vector(4, 0).rotate(randint(0, 360))

    def update(self, dt):
        self.fly.move()

        # bounce off top and bottom
        if (self.fly.y < 0) or (self.fly.top > self.height):
            self.fly.velocity.y *= -1

        # bounce off left and right
        if (self.fly.x < 0) or (self.fly.right > self.width):
            self.fly.velocity.x *= -1


class PongApp(App):
    def build(self):
        game = FlyGame()
        game.start_fly()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    PongApp().run()
