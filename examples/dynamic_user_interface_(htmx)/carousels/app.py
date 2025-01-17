from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button


class ImageCarousel(BoxLayout):
    """A Kivy widget representing an image carousel with clickable arrows."""

    def __init__(self, **kwargs):
        super(ImageCarousel, self).__init__(**kwargs)
        self.image_urls = [
            "https://picsum.photos/id/237/400/300",
            "https://picsum.photos/id/883/400/300",
            "https://picsum.photos/id/1025/400/300",
            "https://picsum.photos/id/1074/400/300",
        ]
        self.current_index = 0

        # Create initial image and add it to the layout
        self.current_image = AsyncImage(source=self.image_urls[self.current_index])
        self.add_widget(self.current_image)

        # Add navigation buttons with proper positioning
        self.previous_button = Button(text="<<", on_press=self.prev_image)
        self.next_button = Button(text=">>", on_press=self.next_image)

        # Use anchor_x and anchor_y for button positioning
        self.previous_button.anchor_x = 'left'  # Anchor left side
        self.previous_button.center_y = 0.5  # Center vertically
        self.next_button.anchor_x = 'right'  # Anchor right side
        self.next_button.center_y = 0.5  # Center vertically

        self.add_widget(self.previous_button)
        self.add_widget(self.next_button)

    def next_image(self, instance):
        """Displays the next image in the carousel."""
        self.current_index = (self.current_index + 1) % len(self.image_urls)
        self.current_image.source = self.image_urls[self.current_index]

    def prev_image(self, instance):
        """Displays the previous image in the carousel."""
        self.current_index = (self.current_index - 1) % len(self.image_urls)
        self.current_image.source = self.image_urls[self.current_index]


class CarouselApp(App):
    """A Kivy app that displays an image carousel."""

    def build(self):
        # Create the carousel widget
        carousel = ImageCarousel()

        return carousel


if __name__ == "__main__":
    CarouselApp().run()


    # kalo ada error Import "kivy.app" could not be resolved > solve w/: ctrl + Shift + p, terus intpreternya ganti python global