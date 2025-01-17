import time
s
class Carousel:
  def __init__(self, images, delay=2):
    self.images = images
    self.delay = delay
    self.current_index = 0

  def show(self):
    while True:
      self.print_image(self.current_index)
      self.current_index = (self.current_index + 1) % len(self.images)
      time.sleep(self.delay)

  def print_image(self, index):
    print(self.images[index])

# Example usage
images = ["https://picsum.photos/id/237/400/300", "https://picsum.photos/id/883/400/300", "https://picsum.photos/id/1025/400/300"]
carousel = Carousel(images)
carousel.show()