import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class Test(App):
    def build(self):
        lbl = Label(text="TEXT : ...")
        txt = TextInput(multiline=False)
        box = BoxLayout(orientation="vertical")
        box.add_widget(lbl)
        box.add_widget(txt)
        return box
        
    


if __name__ == "__main__":
    Test().run()