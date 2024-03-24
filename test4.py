import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class Test(App):
    def build(self):
        lbl = Label(text="TEXT : ...")
        self.lbl = lbl
        txt = TextInput(multiline=False)
        self.txt = txt
        btn = Button(font_size="50sp",size_hint=(0.5,0.2 ),pos_hint={'x':0.25 , 'y':0 },background_normal="btn.png",background_down="btn_p.png")
        self.btn = btn
        btn.bind(on_press=self.btnPress)
        box = BoxLayout(orientation="vertical")
        box.add_widget(lbl)
        box.add_widget(txt)
        box.add_widget(btn)
        return box
    def btnPress(self,event):
        self.txt.text = ""
        self.lbl.text = "OK"
        self.btn.disabled = True
        self.btn.text = "-----------"
        print("key pressed")
        
    


if __name__ == "__main__":
    Test().run()