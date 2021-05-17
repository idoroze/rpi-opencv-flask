from flask import Flask, render_template, Response,jsonify,request,redirect,url_for
import cv2

app = Flask(__name__)

camera = cv2.VideoCapture(0)  # use 0 for web camera


def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/set_stat', methods=['GET','POST'])
def setVal():
    if request.method=='POST':
        i = request.form['num']
        i =int(i)
        if i>=1 and i<=3:
            with open('test.txt','w+') as db:
                db.write(f"{i}")
                db.close()
            return jsonify({"data":i})
        else:
            return redirect(url_for('/get_stat'))
    
         

# @app.route('/set_stat/<int:i>',)
# def setVal(i):
#   with open('test.txt','w+') as db:
#       db.write(f"{i}")
#       db.close()
#   return jsonify({"data":i})
     
@app.route('/get_stat',methods=['GET'])
def getVal():
    with open('test.txt', 'r') as db:
        x=db.read()
        print(x)
        db.close()
        return jsonify({"data":x})

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

if __name__ == '__main__':
    # app.run(debug=True,host='0.0.0.0')
    app.run(host='0.0.0.0')
