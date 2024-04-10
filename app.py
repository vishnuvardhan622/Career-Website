from flask import Flask,render_template,jsonify

app=Flask(__name__)

JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru, India',
    'salary':'Rs. 10,00,000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Bengaluru, India',
    'salary':'Rs. 1,00,000'
  },
  {
    'id':1,
    'title':'Frontend Developer',
    'location':'Bengaluru, India',
    'salary':'Rs. 8,00,000'
  },
  {
    'id':1,
    'title':'Backend Developer',
    'location':'Bengaluru, India',
    'salary':'Rs. 8,00,000'
  }
]

@app.route("/")
def hello():
  return render_template("home.html",jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)



if __name__=="__main__":
  app.run('0.0.0.0',debug=True)