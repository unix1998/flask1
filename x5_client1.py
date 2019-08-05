from flask import Flask
from flask import jsonify
app = Flask(__name__)
empDB=[
 {
 'id':'101',
 'name':'Saravanan S',
 'title':'Technical Leader'
 },
 {
 'id':'201',
 'name':'Rajkumar P',
 'title':'Sr Software Engineer'
 }
 ]

#@app.route("/")
#def hello():
#    return "Hello World!"
@app.route('/empdb/employee',methods=['GET'])
def getAllEmp():
    return jsonify({'emps':empDB})

if __name__ == "__main__":
    app.run()
