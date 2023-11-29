from flask import Flask,render_template,request
import numpy as np
from function import CellphonePrice
import config

app = Flask(__name__)

@app.route('/')
def fun():
    return render_template("home1.html")


@app.route('/predict',methods=['POST'])
def cellphone_price_pred():
   
    data = request.form
    
    Product_id = eval(data['Product_id'])
    Sale = eval(data['Sale'])
    weight = eval(data['weight'])
    resolution = (data['resolution'])	
    ppi = eval(data['ppi'])
    cpu_core = eval(data['cpu_core'])
    cpu_freq = eval(data['cpu_freq'])
    internal_mem = eval(data['internal_mem'])
    ram = eval(data['ram'])
    RearCam = eval(data['RearCam'])
    Front_Cam = eval(data['Front_Cam'])
    battery = eval(data['battery'])
    thickness = eval(data['thickness'])

    
    phone_price = CellphonePrice(Product_id,Sale,weight,resolution,ppi,cpu_core,cpu_freq,internal_mem,ram,
                                 RearCam,Front_Cam,battery,thickness)
    
    price = phone_price.predict_cellphone_price()
    return f"Predicted Cellphone price is: {np.round(price[0], 2)}"

    
       
if __name__ == '__main__':
    app.run(port = config.PORT_NUMBER,debug=True)
    
    
