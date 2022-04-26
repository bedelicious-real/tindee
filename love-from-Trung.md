Some info about Backend

# How to run backend
### Installation
1. Requirements: Python (version 3.x), pip.
2. Pull `master` branch & `cd backend`
3. Run `python -m venv ./venv`
4. Run `pip install -r requirements.txt`
5. Make sure `.env` & `gcp-key.json` exist [IMPORTANT]

### Run backend
1. `cd backend`
2. `flask run --port=2020`
3. Update the value of `REACT_APP_BACKEND_HOST` in `frontend/.env` to `http://127.0.0.1:2020`


# API Reference
## **Login/Signup**
1. Create new user (`/user`)
    * Method: `POST`
    * Request body:
        ```json
        {
            "email": "a@x.com",
            "first": "First Name",
            "last": "Last Name",
            "pwd": "Password"
        }
        ```
    * Response:
        * `200`: a string as token for user
        * `400`: `User already existed` 
        * `500`: `We're not OK` 


2. Login (`/user/session`)
    * Method: `POST`
    * Request body:
        ```[json]
        {
            "email": "a@x.com",
            "pwd": "Password"
        }
        ```
    * Response:
        * `200`: a string as token for user
        * `400`: `Wrong password` 
        * `500`: `We're not OK` 


## **Profile**
1. Get a profile (`/profile?mentor=true|false`)
    * Method: `GET`
    * Authorization: `Bearer [token]`
    * Response:
        * `200`: 
            if `mentor=true`:
            ```json
            {
                "email": "a@x.com",
                "first-name": "First",
                "last-name": "Last",
                "image-url": "http://url-to-image.com/image.jpg",
                "years": 1,
                "offers": ["Offer 1", "Offer 2"],
                "concentration": ["Field 1", "Field 2"],
                "organization": "Twiiter"
            }
            ```
            if `mentor=false`
            ```json
            {
                "email": "a@x.com",
                "first-name": "First",
                "last-name": "Last",
                "image-url": "http://url-to-image.com/image.jpg",
                "organization": "CWRU",
                "status": "Student",
                "level": "High School",
                "intro": "Some description about mentee"
            }
            ```
        * `400`: `Token is expired` 
        * `400`: `Cannot verify user`
        * `500`: `We're not OK` 


2. Get all mentors (`/profile/mentors`)
    * Method: `GET`
    * Authorization: `Bearer [token]`
    * Response:
        * `200`: 
            ```json
            [ { mentor_1 }, { mentor_2 }]
            ```
            *note: format of `mentor_1`... is the same as `GET /profile?mentor=true`
        * `400`: `Token is expired` 
        * `400`: `Cannot verify user`
        * `500`: `We're not OK` 

        
3. Get all mentees (`/profile/mentees`)
    * Method: `GET`
    * Authorization: `Bearer [token]`
    * Response:
        * `200`: 
            ```json
            [ { mentee_1 }, { mentee_2 }]
            ```
            *note: format of `mentee_1`... is the same as `GET /profile?mentor=false`
        * `400`: `Token is expired` 
        * `400`: `Cannot verify user`
        * `500`: `We're not OK` 


4. Update/ Insert a profile (`/profile?mentor=true|false`)
    * Method: `POST`
    * Authorization: `Bearer [token]`
    * Request body:
        if `mentor=true`
        ```json
        {
            "email": "a@x.com",
            "first-name": "First",
            "last-name": "Last",
            "image-url": "http://url-to-image.com/image.jpg",
            "years": 1,
            "offers": ["Offer 1", "Offer 2"],
            "concentration": ["Field 1", "Field 2"],
            "organization": "Twiiter",
            "org_description": "Description of organization"  // <-- IMPORTANT
        }
        ```
        if `mentor=false`
        ```json
        {
            "email": "a@x.com",
            "first-name": "First",
            "last-name": "Last",
            "image-url": "http://url-to-image.com/image.jpg",
            "organization": "CWRU",
            "status": "Student",
            "level": "High School",
            "intro": "Some description about mentee"
        }
        ```
    * Response:
        * `200`: `OK`
        * `400`: `Token is expired` 
        * `400`: `Cannot verify user`
        * `500`: `We're not OK` 


5. Update avatar (`/profile/avatar`)
    * Method: `POST`
    * Authorization: `Bearer [token]`
    * Request body: a form containing image file
    * Response:
        * `200`: `OK`
        * `400`: `Cannot read image`
        * `500`: `We're not OK`


## **Matches**
1. Mentee gets a list of matched mentors (`/matches/mentors?full=true|false`)
    * Method: `GET`
    * Authorization: `Bearer [token]`
    * Response:
        * `200`: format is the same as `GET /profile/mentors`
        * `400`: `Token is expired` 
        * `400`: `Cannot verify user`
        * `500`: `We're not OK` 
2. Mentor gets a list of matched mentees (`/matches/mentees?full=true|false`)
    * Method: `GET`
    * Authorization: `Bearer [token]`
    * Response:
        * `200`: format is the same as `GET /profile/mentees`
        * `400`: `Token is expired` 
        * `400`: `Cannot verify user`
        * `500`: `We're not OK` 
3. User 1 likes user 2 (`/matches`)
    * Method: `POST`
    * Authorization: `Bearer [token]`
    * Response:
        * `200`: 
            * if MATCHED, returns `Matched`
            * otherwise, returns `Liked`
        * `400`: `Token is expired` 
        * `400`: `Cannot verify user`
        * `500`: `We're not OK` 
4. User 1 unmatches/ unlikes user 2 (`/matches`)
    * Method: `DELETE`
    * Authorization: `Bearer [token]`
    * Response:
        * `200`: `OK`
        * `400`: `Token is expired` 
        * `400`: `Cannot verify user`
        * `500`: `We're not OK` 

## **Search**
1. Mentees search mentors (`/mentors`)
    * Method: `POST`
    * Authorization: `Bearer [token]`
    * Request body: 
        ```json
        [
            {
                "type": "first-name",
                "value": "some value"
            }, 
            {
                "type": "offers",
                "value": ["Offer 1", "Offer 2"]
            }, 
            {
                "type": "concentration",
                "value": ["Field 1", "Field 2", "Field 3"]
            }, 
            ...
        ]
        ```
        * note: there are 4 types: `first-name`, `last-name`, `offers`, `concentration`
    * Response:
        * `200`: format is the same as `GET /profile/mentors`
        * `400`: `Token is expired` 
        * `400`: `Cannot verify user`
        * `500`: `We're not OK` 

## **Company**
1. Get company info (`/company?name=someCompanyName`)
    * Method: `GET`
    * Response:
        * `200`: 
            ```json
            {
                "name": "name of company",
                "description": "some description"
            }
            ```