from flask import Flask, render_template

app = Flask(__name__)

@app.route('/carousel/prev')
def carousel_prev():
  # Update current_slide_index (logic omitted for brevity)
  return render_template('carousels.html', image_urls=['https://picsum.photos/id/237/400/300', 'https://picsum.photos/id/883/400/300', 'https://picsum.photos/id/1025/400/300'], current_slide_index=current_slide_index)

@app.route('/carousel/next')
def carousel_next():
  # Update current_slide_index (logic omitted for brevity)
  return render_template('carousels.html', image_urls=['https://picsum.photos/id/237/400/300', 'https://picsum.photos/id/883/400/300', 'https://picsum.photos/id/1025/400/300'], current_slide_index=current_slide_index)