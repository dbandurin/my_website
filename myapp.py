from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    print('Index called')
    return render_template('home_product.html')

@app.route("/pred_repair", methods=['GET', 'POST'])
def pred_repair():
    print('Solutions called, request.method = ',request.method)
    return render_template('predictive_repair.html')

@app.route("/supply_chain", methods=['GET', 'POST'])
def supply_chain():
    print('Solutions called, request.method = ',request.method)
    return render_template('supply_chain.html')

@app.route("/logistics", methods=['GET', 'POST'])
def logistics():
    print('Solutions called, request.method = ',request.method)
    return render_template('logistics.html')

@app.route("/iiot", methods=['GET', 'POST'])
def iiot():
    print('Solutions called, request.method = ',request.method)
    return render_template('iiot.html')

# @app.route("/document", methods=['GET', 'POST'])
# def document():
#     print('Documents called, request.method = ',request.method)
#     return render_template('document.html')

# @app.route("/ecom", methods=['GET', 'POST'])
# def ecom():
#     print('ECom called, request.method = ',request.method)
#     return render_template('ecom.html')

@app.route("/dashboards", methods=['GET', 'POST'])
def dashboards():
    print('Solutions called, request.method = ',request.method)
    # if request.method == 'POST':
    #     return redirect(url_for('index'))
    
    # #else:
    # #Dashboard
    return render_template('dashboards.html')

@app.route("/blogs", methods=['GET', 'POST'])
def blogs():
    return render_template('blogs.html')

@app.route("/about_us", methods=['GET', 'POST'])
def about_us():
    return render_template('about_us.html')

@app.route("/contact_us", methods=['GET', 'POST'])
def contact_us():
    return render_template('contact_us.html')

if __name__ == '__main__':
    app.run(port=5001, debug=True)
