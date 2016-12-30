from flask import Flask, render_template, request, send_from_directory, redirect, g, make_response, Markup, flash
import readcsv
import readdrop
import chartout
import webbrowser
import charttab
import mvpout

app = Flask(__name__)
app.debug = True
app.secret_key = '2dyUy8v7d62jDFCEqnUr1X3XLIT31IxL'

gcustomer = None

@app.route('/', methods=['GET', 'POST', 'OPTIONS'])
def home():
    return render_template('index.html')


@app.route('/sasView.html', methods=['GET', 'POST', 'OPTIONS'])
def sasView():
    global gcustomer
    g.cust_id = gcustomer
    return render_template('sasView.html')


@app.route('/config.html', methods=['GET', 'POST', 'OPTIONS'])
def conf():
    global gcustomer
    g.cust_id = gcustomer
    return render_template('config.html')


@app.route('/opt.html', methods=['GET', 'POST', 'OPTIONS'])
def opt():
    global gcustomer
    g.cust_id = gcustomer
    return render_template('opt.html')


@app.route('/mvpres.html', methods=['GET', 'POST', 'OPTIONS'])
def mvpres():
    global gcustomer
    g.cust_id = gcustomer
    return render_template('mvpres.html')
	
	
@app.route('/chart.html', methods=['GET', 'POST', 'OPTIONS'])
def chart():
    global gcustomer
    g.cust_id = gcustomer
    g.segmentid = request.args.get('segmentid')
    g.level = request.args.get('level')
    return render_template('chart.html')


@app.route('/customers/', methods=['POST'])
def parse_customers():
    # global gcustomer
    # gcustomer = request.form['customer']
    # return redirect('/sasView.html')
    custid = request.form['customer']
    webbrowser.open_new_tab('http://orcoevasrv01.na.sas.com/SASVisualAnalyticsViewer/VisualAnalyticsViewer_guest.jsp?reportName=Kaman+Customer+Score+Card&reportPath=/Shared+Data/Kaman/')
    return redirect('/')

@app.route('/ids/', methods=['POST'])
def parse_ids():
    global gcustomer
    gcustomer = request.form['customer_hidden']
    return redirect('/sasView.html')


@app.route('/js/<path:filename>', methods=['GET', 'POST', 'OPTIONS'])
def send_js(filename):
    return send_from_directory('js', filename)


@app.route('/css/<path:filename>', methods=['GET', 'POST', 'OPTIONS'])
def send_css(filename):
    return send_from_directory('css', filename)


@app.route('/fonts/<path:filename>', methods=['GET', 'POST', 'OPTIONS'])
def send_fonts(filename):
    return send_from_directory('fonts', filename)


@app.route('/font-awesome-4.7.0/<path:filename>', methods=['GET', 'POST', 'OPTIONS'])
def send_fa(filename):
    return send_from_directory('font-awesome-4.7.0', filename)


@app.route('/csv/', methods=['GET', 'POST', 'OPTIONS'])
def get_json():
    cust_id = request.args.get('id')
    print cust_id
    body = readcsv.return_rest(cust_id)
    return body


@app.route('/drop/', methods=['GET', 'POST', 'OPTIONS'])
def get_control():
    body = readdrop.return_drop()
    return body


@app.route('/chartout/', methods=['GET', 'POST', 'OPTIONS'])
def get_chart_data():
    segmentid = request.args.get('segmentid')
    level = request.args.get('level')
    body = chartout.return_chart(segmentid, level)
    return body

	
@app.route('/charttab/', methods=['GET', 'POST', 'OPTIONS'])
def get_chart_table():
    body = charttab.return_table()
    return body
	
	
@app.route('/mvpopt', methods=['POST'])
def post_mvp():
	g.objective = request.form['objective']	
	g.tier = request.form['tier']	
	g.type = request.form['type']	
	g.target = request.form['target']
	print "Objective: " + g.objective
	return redirect('mvpres.html')

	
@app.route('/mvpresult/', methods=['GET', 'POST', 'OPTIONS'])
def get_mvp():
	objective = request.args.get('objective')	
	#tier = request.args.get['tier']	
	#type = request.args.get['type']	
	#target = request.args.get['target']	
	print "Objective in form args: " + objective
	body = mvpout.return_mvp(objective)
	return body
	
	
if __name__ == '__main__':
    app.run()
