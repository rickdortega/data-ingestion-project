from datetime import datetime
from typing import Optional, Dict
from decimal import Decimal
from sqlmodel import Field, SQLModel, create_engine
from pydantic import validator

def clean_brackets(input_str: str) -> str:
    brackets = ['{', '}']
    for bracket in brackets:
        input_str = input_str.replace(bracket, '')
    return input_str

class FilmLocation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str  
    release_year: int 
    locations: str
    production_company: str  
    director: str
    writer: str #TODO handle list of writers (comma sep?)
    actor_1: str
    actor_2: str
    actor_3: str

class ParkScores(SQLModel, table=True):
    park_id: Optional[int] = Field(default=None, primary_key=True)
    psa: str  
    park: str 
    fq: str  
    score: int #TODO stored as a string, does it coerce correctly?

class PrivateOpenSpaces(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    popos_address: str
    hours: str
    type: str #TODO maybe enum?
    landscaping: str #TODO maybe list of attributes
    seating_no: str
    food_service: str #TODO maybe enum?
    art: str #TODO maybe bool?
    restrooms: str #TODO maybe bool?
    accessibility: str #TODO maybe enum?
    location: str
    year: int #TODO stored as a string, does it coerce correctly?
    description: str
    hours_type: str #TODO maybe enum?
    subject_to_downtown_pln: str #TODO maybe bool?
    signage: None
    block_num: int #TODO stored as a string, does it coerce correctly?
    lot_num: int #TODO stored as a string, does it coerce correctly?
    parcel_num: int #TODO stored as a string, does it coerce correctly?
    the_geom: Dict[str, str] #TODO check nested data

class Properties(SQLModel, table=True):
    objectid: Optional[int] = Field(default=None, primary_key=True)
    map_label: str
    longitude: Decimal = Field(decimal_places=15)
    latitude: Decimal = Field(decimal_places=15)
    acres: 2.01276398
    tma_propertyid: 142
    globalid: str
    _globalid: validator('globalid', pre=True, allow_reuse=True)(clean_brackets)
    created_user: str
    created_date: datetime
    last_edited_user: str
    last_edited_date: datetime
    squarefeet: Decimal = Field(decimal_places=8)
    perimeterlength: Decimal = Field(decimal_places=8)
    propertytype: str #TODO maybe enum?
    address: str
    city: str
    state: str
    zipcode: str
    complex: str
    psa: str
    supdist: str #TODO actually a list of ints and 2 'Outside SF'
    ownership: str #TODO maybe enum?
    land_id: int
    ggp_section: str
    state_senate: str
    mons_neighborhood: str
    police_district: str
    us_congress: str
    realtor_neighborhood: str
    state_assembly: str
    planning_neighborhood: str
    # shape: dict[] #TODO figure this out



def clean_brackets(input_str: str) -> str:
    brackets = ['{', '}']
    for bracket in brackets:
        input_str = input_str.replace(bracket, '')
    return input_str