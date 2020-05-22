# import kivy
# from kivy.app import App
# from kivy.uix.label import Label

# class MyApp(App):
#     def build(self):
#         label = Label(text='Hello from Kivy App')
#         return label
        
# if __name__ == '__main__':
#     MyApp().run()

# from kivy.app import App
# from kivy.uix.image import Image

# class MainApp(App):
#     def build(self):
#         return Image(source='C:/Users/rahul.shah/Desktop/1.PNG')

# if __name__ == '__main__':
#     app = MainApp()
#     app.run()

import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]

class HBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(padding=10)
        colors = [red, green, blue, purple]

        for i in range(10):
            btn = Button(text="Button #%s" % (i+1),
                         background_color=random.choice(colors)
                         )

            layout.add_widget(btn)
        return layout

if __name__ == "__main__":
    app = HBoxLayoutExample()
    app.run()