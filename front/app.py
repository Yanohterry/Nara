from flask import Flask , render_template
import requests 


app  = Flask (__name__) 

@app.route('/')
def home(): 
    # get date to api 
    response = requests.get("http://127.0.0.1:8000/")  
    # data = response.json()
    data = response

    print(response.status_code)
    print(response)

    return render_template('home.html', data=data)

@app.route('/start')
def start(): 
    response = requests.get("http://127.0.0.1:8000/start")  
    data = response
    print(response.status_code)
    print(data)
    return render_template('start.html', data=data)

@app.route('/anomalie')
def anomalie(): 
    response = requests.get("http://127.0.0.1:8000/anomalies/")  
    data = response.json()
    print(response.status_code)
    print(response)
    return render_template('anomalie.html' , data=data)


if __name__ == '__main__':
    app.run(debug=True)