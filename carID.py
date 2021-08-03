import qrcode as qr
import json
# pip install pillow
# pip install qrcode
# pillow is a request of qrcode module

tags=["Patente","Estado","Dueno","Rut","Ano","Permiso de Circulacion","Modelo","Color"]
example=["ABCD12","ROBADO","Linus Torvalds","12345678-9","1800","Vigente","Kia Morning PLUS","Azul"]

def listToDict(data):
    dict={}
    assert len(tags)==len(data)
    for i in range(len(tags)):
        dict[tags[i]]=data[i]
    return dict

def jsonToList(fileName):
    with open(fileName) as json_file:
        data = json.load(json_file)
    list=[]
    for i in data:
        list.append(i)
    return list

class Vehiculo():
    def __init__(self,data=example):
        self.data=listToDict(data)
        self.qrcode()
    def update(self,data):
        self.data=listToDict(data)
        self.qrcode()
    def qrcode(self):      
        # Serializing json   
        json_object = json.dumps(self.data, indent = 4)
        f=open("auto.json","w")
        f.write(json_object)
        f.close()
        # JSON file
        with open('auto.json') as json_file:
            auto = json.load(json_file)    
        message=""
        for i in range(len(tags)):
            message+=tags[i]+": "+auto[tags[i]]+"\n"
        # Create QR
        img = qr.make(message)
        img_file = open('qr.png', 'wb')
        img.save(img_file)
        img_file.close()
        self.qr='qr.png'