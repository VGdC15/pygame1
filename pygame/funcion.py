import json

#funcion para guardar ranking
def read_data(archivo: str) -> list:
    # bloque with, que garantiza que el archivo se cierre correctamente después de su uso.
    with open(archivo, "r", encoding='utf-8') as file: 
        data = json.load(file) #Esto convierte el JSON en un diccionario de Python

    list_score = data.get("ranking", [])

    return list_score

def save_data(ranking:list,name:str,score:int):
    ranking.append({"name": name, "score": score})
    with open("programacion\ejercicios\pygame\data.json", 'w', encoding='utf-8') as file:
        json.dump({"ranking": ranking}, file, indent=4)