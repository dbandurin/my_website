from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    print('Index called')
    return render_template('home_product.html')

@app.route("/blog.html", methods=['GET', 'POST'])
def blog():
    print('Solutions called, request.method = ',request.method)
    # if request.method == 'POST':
    #     return redirect(url_for('index'))
    return render_template('blog.html')

@app.route("/test.html", methods=['GET', 'POST'])
def test_dashboard():
    print('Solutions called, request.method = ',request.method)
    # if request.method == 'POST':
    #     return redirect(url_for('index'))
    
    # #else:
    # #Dashboard
    return render_template('test.html')

if __name__ == '__main__':
    app.run(port=5001, debug=True)
