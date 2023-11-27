from pymongo import MongoClient
import banapresso 

name_list, address_list, img_path_list = banapresso.bana()

url = "mongodb+srv://wnsvy1237:Dldzmtor15@cluster0.qorzsry.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)

database = client["kdtWork"]
collection = database["banapressoMarkets"]

for i in range(len(name_list)):
    data_insert = {"name": name_list[i], "location": address_list[i], "img": img_path_list[i]}
    result = collection.insert_one(data_insert)