# THE WILD WORLD 

#### Video Demo: <URL HERE>

#### Description:
The Wild World is a web app that introduces wildlife and shares knowledge about the wild. Users can generate different fun facts about the wild, and the app provides free resources to learn about various animals that shape the wild. Users can also create accounts, log in, and log out on the website.

#### Features:
Here are the features included in The Wild World website:
- Users can create accounts, log in, and log out.
- The home page is an introduction to The Wild World with a welcoming hero section and a section featuring different animals to learn about.
- Users can generate fun facts about the wild.
- The website includes a section that answers the most frequently asked questions about the wild world.
- The best part is that users can search for any animal in the search bar and get detailed information about that animal, including:
  - General information about the animal
  - Description, behavior, origin, eating habits, etc.
  - A gallery of fun images related to that animal
  - Fun facts about the animal

### Stack

#### Integration with Google GenAI
To generate detailed information about animals, I used **Google GenAI** to fetch and generate data such as animal behaviors, eating habits, and other unique characteristics.

#### Pixels API
To fetch images related to the provided animal.

### Frontend:
- **Bootstrap**: 
  - Used for a responsive navbar and accordion-style questions.
  - Used to create a responsive gallery.
- **HTML**: 
  - Defines the structure of the website.
- **CSS**: 
  - Used to style the website and ensure it is responsive and visually appealing on all devices.
- **JavaScript**: 
  - Used to dynamically generate new facts.
  - Used for handling user interaction with the questions section on the home page.

### Backend:
- **Python (Flask)**: 
  - Used Flask, a Python framework, to handle requests.
- **SQLite3**: 
  - Used SQLite3 as the database to store user information.
