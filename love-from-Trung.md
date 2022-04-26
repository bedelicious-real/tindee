Some info about Backend. <br>
From Trung with love :green_heart:

# How to run backend
### <u>Installation</u>
1. Requirements: Python (version 3.x), pip.
2. Pull `master` branch & `cd backend`
3. Run `python -m venv ./venv`
4. Run `source venv/bin/activate`
5. Run `pip install -r requirements.txt`
6. Make sure `.env` & `gcp-key.json` exist in `./backend/` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <-- **[IMPORTANT]**

### <u>Run backend</u>
1. `cd backend`
2. `source venv/bin/activate`
3. run `export GOOGLE_APPLICATION_CREDENTIALS="path/to/file/gcp_key.json"`
4. `flask run --port=2020`
5. Update the value of `REACT_APP_BACKEND_HOST` in `frontend/.env` to `http://127.0.0.1:2020`


# API Reference
## **Login/Signup**
1. <u>Create new user (`/user`)</u>
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


2. <u>Login (`/user/session`)</u>
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
1. <u>Get a profile (`/profile?mentor=true|false`)</u>
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


2. <u>Get all mentors (`/profile/mentors`)</u>
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

        
3. <u>Get all mentees (`/profile/mentees`)</u>
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


4. <u>Update/ Insert a profile (`/profile?mentor=true|false`)</u>
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


5. <u>Update avatar (`/profile/avatar`)</u>
    * Method: `POST`
    * Authorization: `Bearer [token]`
    * Request body: a form containing image file
    * Response:
        * `200`: `OK`
        * `400`: `Cannot read image`
        * `500`: `We're not OK`


## **Matches**
1. <u>Mentee gets a list of matched mentors (`/matches/mentors?full=true|false`)</u>
    * Method: `GET`
    * Authorization: `Bearer [token]`
    * Response:
        * `200`: format is the same as `GET /profile/mentors`
        * `400`: `Token is expired` 
        * `400`: `Cannot verify user`
        * `500`: `We're not OK` 
2. <u>Mentor gets a list of matched mentees (`/matches/mentees?full=true|false`)</u>
    * Method: `GET`
    * Authorization: `Bearer [token]`
    * Response:
        * `200`: format is the same as `GET /profile/mentees`
        * `400`: `Token is expired` 
        * `400`: `Cannot verify user`
        * `500`: `We're not OK` 
3. <u>User 1 likes user 2 (`/matches`)</u>
    * Method: `POST`
    * Authorization: `Bearer [token]`
    * Response:
        * `200`: 
            * if MATCHED, returns `Matched`
            * otherwise, returns `Liked`
        * `400`: `Token is expired` 
        * `400`: `Cannot verify user`
        * `500`: `We're not OK` 
4. <u>User 1 unmatches/ unlikes user 2 (`/matches`)</u>
    * Method: `DELETE`
    * Authorization: `Bearer [token]`
    * Response:
        * `200`: `OK`
        * `400`: `Token is expired` 
        * `400`: `Cannot verify user`
        * `500`: `We're not OK` 

## **Search**
1. <u>Mentees search mentors (`/mentors`)</u>
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
1. <u>Get company info (`/company?name=someCompanyName`)</u>
    * Method: `GET`
    * Response:
        * `200`: 
            ```json
            {
                "name": "name of company",
                "description": "some description"
            }
            ```