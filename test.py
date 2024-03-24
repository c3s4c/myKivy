import kivy
from kivy.app import App
from kivy.uix.label import Label

class Test(App):
    def build(self):
        return Label(text="kif bokhor",font_size="50")

if __name__ == "__main__":
    Test().run()