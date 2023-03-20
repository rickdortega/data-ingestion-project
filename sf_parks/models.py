import json
from datetime import datetime
from typing import Optional, Dict
from decimal import Decimal
from sqlmodel import Field, SQLModel, create_engine
from pydantic import validator, condecimal



class FilmLocations(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: Optional[str]  
    release_year: Optional[int] 
    locations: Optional[str]
    address: Optional[str]
    production_company: Optional[str]  
    director: Optional[str]
    writer: Optional[str] #TODO handle NA case id=9
    actor_1: Optional[str]
    actor_2: Optional[str]
    actor_3: Optional[str]

    @validator('writer')
    def split_writers(input_str: str) -> str:
        str_without_and = input_str.replace('&', '')
        str_list = [s.strip() for s in str_without_and.split(',')]
        return json.dumps(str_list)

class ParkScores(SQLModel, table=True):
    park_id: Optional[int] = Field(default=None, primary_key=True)
    psa: str  
    park: str 
    fq: str  
    score: condecimal() = Field()

class PrivateOpenSpaces(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    popos_address: str
    hours: Optional[str]
    type: Optional[str] 
    landscaping: Optional[str] 
    seating_no: Optional[str]
    food_service: Optional[str] 
    art: Optional[str] 
    restrooms: Optional[str] 
    accessibility: Optional[str] 
    location: Optional[str]
    year: Optional[int] 
    description: Optional[str]
    hours_type: Optional[str] 
    subject_to_downtown_pln: Optional[str]
    signage: Optional[str]
    block_num: Optional[int] 
    lot_num: Optional[int] 
    parcel_num: Optional[int] 
    latitude: Optional[str]
    longitude: Optional[str]
    sf_find_neighborhoods: Optional[int]
    current_police_districts: Optional[int]
    current_supervisor_districts: Optional[int]
    analysis_neighborhoods: Optional[int]
    

class Properties(SQLModel, table=True):
    objectid: Optional[int] = Field(default=None, primary_key=True)
    map_label: Optional[str]
    longitude: Optional[str]
    latitude: Optional[str]
    acres: condecimal() = Field()
    tma_propertyid: int
    globalid: Optional[str]
    created_user: Optional[str]
    created_date: datetime
    last_edited_user: Optional[str]
    last_edited_date: datetime
    squarefeet: condecimal() = Field()
    perimeterlength: condecimal() = Field()
    propertytype: Optional[str] #TODO maybe enum?
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zipcode: Optional[str]
    complex: Optional[str]
    psa: Optional[str]
    supdist: Optional[str] #TODO actually a list of ints and 2 'Outside SF'
    ownership: Optional[str] #TODO maybe enum?
    land_id: Optional[int]
    ggp_section: Optional[str]
    state_senate: Optional[str]
    mons_neighborhood: Optional[str]
    police_district: Optional[str]
    us_congress: Optional[str]
    realtor_neighborhood: Optional[str]
    state_assembly: Optional[str]
    planning_neighborhood: Optional[str]
    # shape: dict[] #TODO figure this out
    
    @validator('globalid')
    def clean_brackets(input_str: str) -> str:
        brackets = ['{', '}']
        for bracket in brackets:
            input_str = input_str.replace(bracket, '')
        return input_str

