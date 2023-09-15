from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from typing import List, Union
from db import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import models
import schemas

# Create the database
Base.metadata.create_all(engine)

# Initialize app
app = FastAPI()

# Helper function to get database session
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.get("/")
def root():
    return "App for Stage Two of HNG Internship"

@app.post("/person", response_model=schemas.Person, status_code=status.HTTP_201_CREATED)
def create_person(person: schemas.PersonCreate, session: Session = Depends(get_session)):
    # create an instance of the Person database model
    person_db = models.Person(name=person.name)

    # add it to the session and commit it
    session.add(person_db)
    session.commit()
    session.refresh(person_db)

    # return the person object
    return person_db

@app.get("/person/{user_id}", response_model=schemas.Person)
def read_person(user_id: int, session: Session = Depends(get_session)):
    # get the person with the given id
    person = session.query(models.Person).get(user_id)

    # check if person with given id exists. If not, raise exception and return 404 not found response
    if not person:
        raise HTTPException(status_code=404, detail=f"person with id {user_id} not found")

    return person

@app.get("/person", response_model=schemas.Person)
def read_person_by_name(name: Union[str, int], session: Session = Depends(get_session)):
    # Validate that the name parameter is a string
    if not isinstance(name, str):
        raise HTTPException(status_code=400, detail="Name must be a string")

    # get the person with the given name
    person = session.query(models.Person).filter(models.Person.name == name).first()

    # check if person with given name exists. If not, raise exception and return 404 not found response
    if not person:
        raise HTTPException(status_code=404, detail=f"person with name {name} not found")

    return person

@app.put("/person/{user_id}", response_model=schemas.Person)
def update_person(user_id: int, request_data: schemas.UpdatePersonRequest, session: Session = Depends(get_session)):
    # get the person with the given id
    person = session.query(models.Person).get(user_id)

    # update person with the given name (if a person with the given id was found)
    if person:
        person.name = request_data.name
        session.commit()

    # check if person with given id exists. If not, raise exception and return 404 not found response
    if not person:
        raise HTTPException(status_code=404, detail=f"person with id {user_id} not found")

    return person

@app.delete("/person/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_person(user_id: int, session: Session = Depends(get_session)):
    # get the person with the given id
    person = session.query(models.Person).get(user_id)

    # if person with given id exists, delete it from the database. Otherwise raise 404 error
    if person:
        session.delete(person)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"person with id {user_id} not found")

    return None

@app.get("/people", response_model=List[schemas.Person])
def read_people_list(session: Session = Depends(get_session)):
    # get all persons
    people_list = session.query(models.Person).all()

    return people_list
