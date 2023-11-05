from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/contact')
def contacts():
    return render_template('contact.html')

@app.route('/works')
def my_works():
    return render_template('works.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/areaofcircle', methods=['GET', 'POST'])
def compute():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('theRadius', '')
        try:
            radius_stringed = float(input_string)
        except(ValueError):
            result = "valueError"
            return render_template('areaofcircle.html', result=result)
        radius_stringed = float(input_string)
        powered = radius_stringed ** 2
        result = powered * 3.14
        
    return render_template('areaofcircle.html', result=result)

@app.route('/trianglearea', methods=['GET', 'POST'])
def calculate():
    result = None
    if request.method == 'POST':
        my_base = request.form.get('theBase', '')
        my_height = request.form.get('theHeight', '')
        try:
            base_stringed = float(my_base)
            height_stringed = float(my_height)
        except(ValueError):
            result = "valueError"
            return render_template('trianglearea.html', result=result)
        base_stringed = float(my_base)
        height_stringed = float(my_height)
        powered = base_stringed * height_stringed
        result = powered / 2
        
    return render_template('trianglearea.html', result=result)

@app.route('/contact')
def contact():
    return "Contact Page. please create me an html page with dummy contact info"

if __name__ == "__main__":
    app.run(debug=True)
