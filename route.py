from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello():

    return render_template('home.html',  title = 'Home')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)

if __name__ == '__main__':
    app.run(debug=True)