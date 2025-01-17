from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.properties import ObjectProperty  # Import for swipe gestures

class ImageDot(Button):
    """A small button representing a dot for carousel navigation."""
    def __init__(self, **kwargs):
        super(ImageDot, self).__init__(**kwargs)
        self.background_color = (0.5, 0.5, 0.5, 1)  # Default inactive dot color

class ImageCarousel(BoxLayout):
    """A Kivy widget representing an image carousel with navigation."""

    current_image = ObjectProperty(None)  # Reference to the current image

    def __init__(self, **kwargs):
        super(ImageCarousel, self).__init__(**kwargs)
        self.image_urls = [
            "https://picsum.photos/id/237/400/300",
            "https://picsum.photos/id/883/400/300",
            "https://picsum.photos/id/1025/400/300",
            "https://picsum.photos/id/1074/400/300",
        ]
        self.current_index = 0

        # Create image container with swipe gestures (optional)
        self.image_container = FloatLayout()
        self.current_image = AsyncImage(source=self.image_urls[self.current_index])
        self.image_container.add_widget(self.current_image)

        # Add navigation buttons with proper positioning
        self.previous_button = Button(text="<<", on_press=self.prev_image)
        self.next_button = Button(text=">>", on_press=self.next_image)  # Corrected line

        self.previous_button.anchor_x = 'left'
        self.previous_button.center_y = 0.5
        self.next_button.anchor_x = 'right'
        self.next_button.center_y = 0.5

        # Create dots for navigation
        self.dots = []
        for i in range(len(self.image_urls)):
            dot = ImageDot()
            dot.index = i 
            dot.bind(on_press=self.on_dot_press) 
            self.dots.append(dot)

        def on_dot_press(self, instance):
            index = instance.index 
            # Use the 'index' here

        # Add widgets to the layout
        self.add_widget(self.image_container)
        self.add_widget(self.previous_button)
        self.add_widget(self.next_button)

        # Schedule automatic image switching (optional)
        Clock.schedule_interval(self.auto_switch_image, 5)  # Change image every 5 seconds

        # Set the first dot as active
        self.dots[self.current_index].background_color = (0, 1, 0, 1)  # Active dot color

    def auto_switch_image(self, dt):
        """Automatically switches the image after a specific interval."""
        self.next_image(None)

    def on_dot_press(self, instance, index):
        """Handles dot press for manual image selection."""
        self.current_index = index
        self.current_image.source = self.image_urls[self.current_index]
        for dot in self.dots:
            dot.background_color = (0.5, 0.5, 0.5, 1)
        self.dots[index].background_color = (0, 1, 0, 1)  # Set selected dot as active

    def prev_image(self, instance):
        """Displays the previous image in the carousel."""
        self.current_index = (self.current_index - 1) % len(self.image_urls)
        self.current_image.source = self.image_urls[self.current_index]
        for dot in self.dots:
            dot.background_color = (0.5, 0.5, 0.5, 1)
        self.dots[self.current_index].background_color = (0, 1, 0, 1) 
    def next_image(self, instance):
        """Displays the next image in the carousel."""
        self.current_index = (self.current_index + 1) % len(self.images)
        self.current_image.source = self.images[self.current_index]
        for dot in self.dots:
            dot.background_color = (0.5, 0.5, 0.5, 1)  # Set all dots to inactive color
        self.dots[self.current_index].background_color = (0, 1, 0, 1)  # Set the current dot to active color
# ... (rest of the code for MyApp and running the app)