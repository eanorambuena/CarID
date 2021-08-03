import qrcode as qr
import json
# pip install pillow
# pip install qrcode
# pillow is a request of qrcode module

initialTags=[""]
example=["ABCD12","ROBADO","Linus Torvalds","12345678-9","1800","Vigente","Kia Morning PLUS","Azul"]

def listToDict(data,tags=initialTags):
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

class Object():
    def __init__(self,data=example,tags=initialTags):
        self.update(data,tags)
    def update(self,data,tags=initialTags):
        self.name=data[0]
        self.data=listToDict(data,tags)
        self.tags=tags
        self.qrcode()
    def describeMe(self):
        print("I am an Object of type", type(self).__name__)
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
        for i in range(len(self.tags)):
            message+=self.tags[i]+": "+auto[self.tags[i]]+"\n"
        # Create QR
        self.qr=self.name+'.qr.png'
        img = qr.make(message)
        img_file = open(self.qr, 'wb')
        img.save(img_file)
        img_file.close()
        
class Vehiculo(Object):
    def __init__(self,data=example):
        tags=["Patente","Estado","Dueno","Rut","Ano","Permiso de Circulacion","Modelo","Color"]
        super().__init__(data,tags)

class Mascota(Object):
    def __init__(self,data=example):
        tags=["Nombre","Dueno","Telefono","Por favor"]
        super().__init__(data,tags)

class Person(Object):
    def __init__(self,data=example):
        tags=["Nombre","Rut","Telefono"],"Direccion"
        super().__init__(data,tags)