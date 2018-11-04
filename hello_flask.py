from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_FlaskWorld():
    return 'Hello World!\n\n 你好，世界'


log_lat = [116.323394571, 40.0550706141]

points = [[116.323394571, 40.0550706141],
          [116.333394571, 40.0560706141],
          [116.343394571, 40.0570706141],
          [116.353394571, 40.0580706141]]
center = log_lat


@app.route('/map')
def map():
    return render_template('map_test.html', center=center, points=points)
