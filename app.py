from flask import Flask
from flask import request
from flask import send_file
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, cm
import requests,os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image,Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import io
import os
import random,string
app = Flask(__name__)

@app.route("/")
def index():
	return "what you lookin here, is not here"
	# return """
	# <form action='get_pdf' method='post'>
	# 	<input name="data">
	# 	<button>go</button>
	# </form>
	# """

@app.route('/get_pdf', methods=['GET', 'POST'])
def get_pdf():
    error = ''
    try:
        if request.method == "POST":
        	data = request.form['data']

        	letters = string.ascii_lowercase
        	result_str = ''.join(random.choice(letters) for i in range(36))
        	file_path = result_str+".pdf"

        	filename = '250px-CYBSECGROUP_LOGO.png'
        	styles = getSampleStyleSheet()
        	title_style = styles['Heading1']
        	title_style.alignment = 1
        	doc = SimpleDocTemplate(file_path, pagesize=letter)
        	parts = []
        	parts.append(Image(filename))
        	parts.append(Paragraph("Cyber Security Group",title_style))
        	parts.append(Paragraph(str(data),style=styles["Normal"]))
        	doc.build(parts)
        	return_data = io.BytesIO()
        	with open(file_path, 'rb') as fo:
        		return_data.write(fo.read())
        	return_data.seek(0)
        	os.remove(file_path)
        	return send_file(return_data, mimetype='application/pdf',
		                     attachment_filename='download_filename.pdf')
        return "something wrong"

    except Exception as e:
        #flash(e)
        return str(e)


if __name__ == '__main__':
    app.run()
