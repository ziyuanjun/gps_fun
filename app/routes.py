from app import app
from flask import render_template


log_lat = [116.323394571, 40.0550706141]

points = [[116.323394571, 40.0550706141],
          [116.333394571, 40.0560706141],
          [116.343394571, 40.0570706141],
          [116.353394571, 40.0580706141]]
center = log_lat


@app.route('/startPath', methods=['GET', 'POST'])
def startPath():
    date_time = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
    filename1 = 'static/data_csv_' + date_time + '.csv'
    filename2 = 'gps_Data/data_raw_' + date_time + '.txt'
    file_data = open(filename1, 'w')
    file_data.write('loc\n')
    file_raw = open(filename2, 'w')
    # t = threading.Thread(target=startGPS, args=(filename1, filename2))
    # t.start()
    try:
        startGPS(file_data, file_raw)
    except Exception as e:
        print(str(e))

    return filename1


@app.route('/test_back')
def test():
    # print('haha', file=sys.stdout)
    logging.info("haha")
    return "OK"


@app.route('/')
def hello_FlaskWorld():
    return 'Hello World!\n\n'


@app.route('/ajax')
def ajax():
    return render_template('ajax_test.html')


@app.route('/map')
def map():
    return render_template('map_test.html', center=center, points=points)


# if __name__ == '__main__':
#     app.run(debug=True)
