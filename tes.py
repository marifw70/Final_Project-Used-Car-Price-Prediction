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

@app.route('/grafik')
def grafik():
    return render_template('grafik.html')

@app.route('/dataset')
def dataset():
    df = pd.read_csv(r'D:\belajar data scientist\Purwadhika\Mobil\data_for_dashboard.csv')
    return render_template('dataset.html',df_view = df.head(100))
@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST': 
        Year = request.form['year']
        Manufacturer = request.form['manufacturer']
        Condition = request.form['condition']
        Cylinders = request.form['cylinders']
        Fuel = request.form['fuel']
        Odometer = request.form['odometer']
        title_status = request.form['title_status']
        Transmission = request.form['transmission']
        Drive = request.form['drive']
        Size = request.form['size']
        Type = request.form['type']
        State = request.form['state']
        class_car = request.form['class_car']

        Year = int(Year)
        Odometer = int(Odometer)
        class_car = int(class_car)

        data = {  
            'year' : Year,                      
            'manufacturer' : Manufacturer,
            'condition' : Condition,
            'cylinders' : Cylinders,
            'fuel' : Fuel,
            'odometer' : Odometer,
            'title_status' : title_status,
            'transmission' : Transmission,
            'drive' : Drive,
            'size' : Size,
            'state' : State,
            'type': Type,
            'class_car' : class_car
        }
        #kota
        if State == 'tx':
            kota = 'Texas'
                
        if State == 'ny':
            kota = 'New York'
        
        if State == 'ca':
            kota = 'California'

        if State == 'fl':
            kota = 'Florida'

        if State == 'oh':
            kota = 'Ohio'
        
        if State == 'mi':
            kota = 'Michigan'

        if State == 'wa':
            kota = 'Washington'

        if State == 'wi':
            kota = 'Wisconsin'

        if State == 'nc':
            kota = 'North Carolina'
        
        if State == 'tn':
            kota = 'Tennese'

        if State == 'al':
            kota = 'Alabama'

        if State == 'nv':
            kota = 'Nevada'

        if State == 'pa':
            kota = 'Pennsylvania'

        if State == 'nj':
            kota = 'New Jersey'        

        if State == 'ks':
            kota = 'Kansas'
            
        if State == 'ma':
            kota = 'Massachusetts'        

        # class car
        if class_car == 0:
            car = 'Basic Car'
        if class_car ==1 : 
            car = 'Luxury Car'

    df_predict = pd.DataFrame(data = data, index = [1])
    model = joblib.load(r'D:\belajar data scientist\punya-arif\Model_RF_tuned_for_dashboard')
    prediction = model.predict(df_predict)
    predict_fix= round(prediction[0],2)
    print('harga mobil: ',predict_fix)
    return render_template('index.html',Year=Year,Manufacturer=Manufacturer,Condition=Condition,
                Cylinders=Cylinders,
                Fuel=Fuel,
                Odometer=Odometer,
                title_status=title_status,
                Transmission=Transmission,
                Drive=Drive,
                Size=Size,
                Type=Type,
                State=kota,
                class_car=car,
                predict_fix = predict_fix) 

    
if __name__ == "__main__":

    app.run(debug=True)

