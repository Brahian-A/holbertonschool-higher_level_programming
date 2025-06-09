import json

def serialize_and_save_to_file(data, filename):
    """Serializa los datos en formato json y los guarda en un archivo."""
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """Carga datos desde un archivo y los deserializa"""
    with open(filename, 'r') as f:
        return json.load(f)