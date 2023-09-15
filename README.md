## Documentation for API Application - for Stage 2 of HNG Internship


### Standard formats for requests and responses for eah endpoint

### Sample usage of the API 

#### Create a person

request:
                POST /person
                {
                    "name": "John Doe",
                }

response

#### Retrieve a person by name

        request:   GET /person/John%20Doe

#### Update a person's information:

    request: PUT /person/{id}
    {
        "age": 31
    }

#### Delete a person
    
    request: DELETE /person/{person_id}


### Known limitations or assumptions made



### Instructions for Local Deploy


### Instructions for Setting up on Server - Render was used
