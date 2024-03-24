import kivy
from kivy.app import App
from kivy.uix.label import Label

class Test(App):
    def build(self):
        return Label(text="[b][i][color=1a89ba]kif[/color][/b] bokhor[/i]...\n [b]are dash[/b]",font_size="50sp",markup=True)#color=[0.5,0.5,1,1]

if __name__ == "__main__":
    Test().run()