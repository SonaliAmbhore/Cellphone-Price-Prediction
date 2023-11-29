import numpy as np
import pickle
import json
import config

class CellphonePrice():
    def __init__(self,Product_id,Sale,weight,resolution,ppi,cpu_core, cpu_freq, internal_mem, ram, RearCam, Front_Cam,
       battery, thickness):
        self.Product_id= Product_id
        self.Sale = Sale
        self.weight = weight
        self.resolution = resolution
        self.ppi = ppi
        self.cpu_core = cpu_core
        self.cpu_freq = cpu_freq
        self.internal_mem = internal_mem
        self.ram = ram
        self.RearCam = RearCam
        self.Front_Cam = Front_Cam
        self.battery = battery
        self.thickness = thickness
        
        
    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)
            
        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)
            
    def predict_cellphone_price(self):
        self.load_model()
        
        test_array = np.zeros(len(self.json_data['columns']))
        test_array[0] = self.Product_id
        test_array[1] = self.Sale
        test_array[2] = self.weight
        test_array[3] = self.resolution
        test_array[4] = self.ppi
        test_array[5] = self.cpu_core
        test_array[6] = self.cpu_freq
        test_array[7] = self.internal_mem
        test_array[8] = self.ram
        test_array[9] = self.RearCam
        test_array[10] = self.Front_Cam
        test_array[11] = self.battery
        test_array[12] = self.thickness
        
        
        predict_price  = self.model.predict([test_array])

        return predict_price
            