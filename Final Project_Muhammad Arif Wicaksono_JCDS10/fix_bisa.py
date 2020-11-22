from flask import Flask, render_template, jsonify, request,url_for
import joblib
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import json
from flask_material import Material

app = Flask(__name__)
Material(app)
# home route
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/dataset')
def dataset():
    df = pd.read_csv(r'D:\belajar data scientist\Purwadhika\Mobil\data_for_dashboard.csv')
    return render_template('dataset.html',df_view = df.head(100))

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        Manufacturer = request.form['manufacturer'] 
        Year = request.form['year']
        Type = request.form['type']
        Condition = request.form['condition']
        Odometer = request.form['odometer']
        Cylinders = request.form['cylinders']
        Fuel = request.form['fuel']
        title_status = request.form['title_status']
        Transmission = request.form['transmission']
        Drive = request.form['drive']
        Size = request.form['size']
        State = request.form['state']
        class_car = request.form['class_car']

        Year = int(Year)
        Odometer = int(Odometer)


        data = {            
            'manufacturer' : Manufacturer,
            'year' : Year,
            'type' : Type,
            'condition' : Condition,
            'odometer' : Odometer,
            'cylinders' : Cylinders,
            'fuel' : Fuel,
            'title_status' : title_status,
            'transmission' : Transmission,
            'drive' : Drive,
            'size' : Size,
            'state' : State,
            'class_car' : class_car
        }

    # model = joblib.load(r'D:\belajar data scientist\Purwadhika\Flask Final Project\Model_DT_tuned_vers2')

    # df = pd.read_csv(r'D:\belajar data scientist\Purwadhika\Final Project\data_for_eda.csv')
    df_predict = pd.DataFrame(data = data, index = [1])
    model = joblib.load(r'D:\belajar data scientist\Purwadhika\Flask Final Project\Model_DT_tuned_vers2')
    prediction = model.predict(df_predict)

    return render_template('index.html',Manufacturer=Manufacturer,Year=Year,Type=Type,Condition=Condition,
                Odometer=Odometer,
                Cylinders=Cylinders,
                Fuel=Fuel,
                title_status=title_status,
                Transmission=Transmission,
                Drive=Drive,
                Size=Size,
                State=State,
                class_car=class_car) 

    
if __name__ == "__main__":

    app.run(debug=True)

