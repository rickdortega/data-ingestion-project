import requests
from sqlmodel import SQLModel, Session
from .db import get_engine, create_db_and_tables
from .models import ParkScores, FilmLocations, PrivateOpenSpaces, Properties

DATA_URLS = {
    'film_locations' : 'https://data.sfgov.org/resource/yitu-d5am.json', 
    'park_scores' : 'https://data.sfgov.org/resource/fjq8-r8ws.json', 
    'private_open_spaces' : 'https://data.sfgov.org/resource/65ik-7wqd.json', 
    'properties' : 'https://data.sfgov.org/resource/gtr9-ntp6.json'  
}

film_locations_url = DATA_URLS['film_locations']
park_scores_url = DATA_URLS['park_scores']
private_open_spaces_url = DATA_URLS['private_open_spaces']
properties_url = DATA_URLS['properties']


def process_private_spaces(input: list[dict]) -> list[dict]:
    for record in input:
        lat, lon = record['the_geom']['coordinates']
        record['latitude'] = lat
        record['longitude'] = lon
        record['sf_find_neighborhoods'] = record[':@computed_region_6qbp_sg9q']
        record['current_police_districts'] = record[':@computed_region_qgnn_b9vv']
        record['current_supervisor_districts'] = record[':@computed_region_26cr_cadq']
        record['analysis_neighborhoods'] = record[':@computed_region_ajp5_b2md']
    return input

def process_film_locations(input: list[dict]) -> list[dict]:
    for record in input:
        if 'locations' in record:
            if "(" in record['locations']:
                record['address'] = record['locations'].split('(')[1].strip(')')
            else:
                record['address'] = record['locations']
    return input

film_locations_raw = requests.get(film_locations_url).json()
film_locations = process_film_locations(film_locations_raw)

park_scores = requests.get(park_scores_url).json()

private_open_spaces_raw = requests.get(private_open_spaces_url).json()
private_open_spaces = process_private_spaces(private_open_spaces_raw)

properties = requests.get(properties_url).json()


data_dict = {
    film_locations : FilmLocations,
    park_scores : ParkScores,
    private_open_spaces : PrivateOpenSpaces,
    properties : Properties
}


def insert_into_db(input: list[dict], model: SQLModel):
    engine = get_engine()
    with Session(engine) as sess:
        for record in input:
            print(record)
            r = model(**record)
            sess.add(r)
            sess.commit()

def insert_all_data():
    for data, model in data_dict.items():
        insert_into_db(data, model)



if __name__ == '__main__':
    insert_into_db(properties, model=Properties)
    insert_into_db(private_open_spaces, model=PrivateOpenSpaces)
    insert_into_db(film_locations, FilmLocations)
    insert_into_db(park_scores, model=ParkScores)
    
