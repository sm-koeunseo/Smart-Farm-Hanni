from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
#import RPi.GPIO as GPIO
import threading
import time
import atexit
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 최대 파일 크기 설정 (16MB)

'''def cleanup():
    GPIO.cleanup()

atexit.register(cleanup)'''

# 홈 페이지 라우트
@app.route('/')
def home():
    return redirect(url_for('monitoring'))

# 마이 페이지 라우트
@app.route('/mypage')
def mypage():
    return render_template('mypage.html')

# 설정 페이지 라우트
@app.route('/settings')
def settings():
    return render_template('settings.html')

# 모니터링 페이지 라우트
@app.route('/monitoring')
def monitoring():
    return render_template('monitoring.html')

# 일지 작성 페이지 라우트
@app.route('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        date = request.form['date']
        plant = request.form['plant']
        length = request.form['length']
        status = request.form['status']
        notes = request.form['notes']
        photo = request.files['photo']

        if photo:
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        log_entry = {
            "date": date,
            "plant": plant,
            "length": length,
            "status": status,
            "notes": notes,
            "photo": filename if photo else None
        }

        return render_template('log.html', log_entry=log_entry)

    return render_template('log.html')

'''@app.route('/setting')
def setting():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17,GPIO.OUT)
    return "complete!"

@app.route('/on')
def ligthOn():
    GPIO.output(17,True)
    return "Lingt On!"

@app.route('/off')
def ligthOff():
    GPIO.output(17,False)
    return "Lingt Off!"

flag = threading.Event()
def background_task():
    while flag.is_set():
        print("repeat!")
        time.sleep(2)


@app.route('/set')
def set_flag():
    if not flag.is_set():
        flag.set()
        thread = threading.Thread(target=background_task)
        print("Background task started!")
        thread.start()
    return render_template('home.html')

@app.route('/unset')
def unset():
    flag.clear()
    print("Background task stopped!")
    return render_template('home.html')'''

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port="3000") # port open