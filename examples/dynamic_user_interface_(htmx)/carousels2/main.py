from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from image_carousel import ImageCarousel  # Assuming your carousels2.py is in the same directory

class MyApp(App):
    def build(self):
        return ImageCarousel()

if __name__ == "__main__":
    MyApp().run()