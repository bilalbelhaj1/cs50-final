from google import genai
import requests
from flask import redirect, session
from functools import wraps
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash

# generate informations about any animal
def general_informations(animal):
    # prompt to pass to the moodle to generate the content
    prompt = f"""
      Generate a Python dictionary that contains the following information for an animal:
        1. general informations like (name, kingdom, class, family, locations, lifespan, prey if the animal is a predator)
        2. **Behavior**: A description of the {animal}'s behavior (e.g., how it behaves in the wild, social structure, etc.).
        3. **Origin**: The {animal}'s geographic origin or habitat (e.g., native region or continent).
        4. **Description**: A short description of the {animal}, including its physical characteristics and general appearance.
        5. **Eating Habits**: A description of the {animal}'s diet (e.g., carnivore, herbivore, omnivore, specific foods it eats).
        6. **Fun Facts**: A list of 5 fun facts about the {animal} 
        7. **Questions and Answers about {animal}**: A list of 4 dictionaries, each containing a question and its answer

    The dictionary should be structured as follows:
    animal_data = {{
        "general_information" : {{
            "name",
            "kingdom",
            "class",
            "family",
            "locations",
            "lifespan",
            "prey",
        }}
        "behavior": "Description of the animal's behavior...",
        "origin": "Where the animal is from...",
        "description": "Physical characteristics and general appearance...",
        "eating_habits": "Diet and eating habits...",
        "general_informations" : [
            "Scientific Name, Lifespan, etc."
        ],
        "fun_facts": [
            "Fact 1",
            "Fact 2",
            "Fact 3",
            "Fact 4",
            "Fact 5"
        ],
        "questions_and_answers": [
            {{"question": "Question 1", "answer": "Answer 1"}},
            {{"question": "Question 2", "answer": "Answer 2"}},
            {{"question": "Question 3", "answer": "Answer 3"}},
            {{"question": "Question 4", "answer": "Answer 4"}}
        ]
    }}
    """
    
    client = genai.Client(api_key="AIzaSyBtMJCJH36QrIigc7VlKPh0esO39pv3MwA")
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    
    # Get the text response from the generated content
    data = response.text
    # Clean the response text 
    cleaned_response = data.strip("```python\n").strip("```")
    
    # Execute the cleaned response in the global scope
    global_scope = globals()
    try:
        # executing the return response to get a dictionary 
        exec(cleaned_response, global_scope)
        return animal_data
    except Exception as e:
        return None


# get tthe animal images 
def get_animal_images(animal):
    api_key = "wKFJGAvf2KuiXWDU8RYMiRVQvZkQlYVXZ1THIgWhCw1ISKdBpRLo1PP7"
    url = f'https://api.pexels.com/v1/search?query={animal} animal&per_page=5'
    headers = {'Authorization': api_key}

    response = requests.get(url, headers=headers)

    # check if we get back a response
    if response.status_code == 200:
        # get the images from the response
        images = response.json()['photos']

        # create a liste of the return images
        photos = []
        for img in images:
            photos.append(img["src"]["large"])
        return photos
    else:
        return None


def get_animal_information(animal):
    # get the data about the animal
    animal_general_description = general_informations(animal)
    if not animal_general_description:
        return None
    
    # get images about the correspond animal
    gallery = get_animal_images(animal)
    images = []
    # if there is no provide image return the default
    if not animal_general_description:
        images[0] = "https://www.aputf.org/wp-content/uploads/2015/06/default-placeholder1-1024x1024-960x540.png"
    else:
        images = gallery
    #combine all the data 
    animal_general_description["gallery"] = images

    return animal_general_description


# check if the username already exists
def check_user(username):
    conn = sqlite3.connect("wilddb.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    rows = cursor.fetchall()
    conn.close()
    if len(rows) > 0:
        return True
    return False


# check if the email already exists
def check_email(email):
    conn = sqlite3.connect("wilddb.db")
    cursor = conn.cursor()

    cursor.execute("""
           SELECT * FROM users WHERE email = ?
""", (email, ))
    rows = cursor.fetchall()

    conn.close()
    if len(rows) > 0:
        return True
    return False


# register the user
def add_user(username, email, password):

    # generate a hash password to store in the database
    hash = generate_password_hash(password, method='scrypt', salt_length=16)

    conn = sqlite3.connect("wilddb.db")
    cursor = conn.cursor()
    try:
        # insert the new user to the database
        cursor.execute("INSERT INTO users(username, email, hash) VALUES(?, ?, ?)", (username, email, hash))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(e)
        return False


# validate the user data
def check_user_info(username, password):
    conn = sqlite3.connect("wilddb.db")
    cursor = conn.cursor()

    # validate the username
    cursor.execute("SELECT * FROM users WHERE username = ?", (username, ))
    rows = cursor.fetchall()
    if len(rows) == 0:
        return "user_not"
    else:
        hash = rows[0][2]

        # validate the password
        if not check_password_hash(hash, password, ):
            return "not_pass"
        
        # if the user exists return it's id and username
        return [rows[0][0], rows[0][1]]

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function
