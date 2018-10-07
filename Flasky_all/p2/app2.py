from flask import Flask
app= Flask(__name__)
@app.route('/')
def index():
    return '''<h1> Wasim is owmer of Manipulator </h1> <br>
    <h3>Pakistan zina bad </h3>'''
@app.route('/about')
def about():
    return """ ther are other share holders as well \n
     our talent and skills are multi dimensinal <br> 
     our teams are our  our biggest asset \
      they make difference and impact which others can't"""


app.run(debug=True)