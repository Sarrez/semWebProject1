import requests
from owlready import *

onto_path.append("/Users/George/Desktop/SemanticWeb/SWProj4/pokemon.owl")
onto = get_ontology(onto_path)
onto.load()
