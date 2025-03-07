# The Wild World

## Video Demo: [https://youtu.be/YJLQ5xCWr4Q]

## Description
The Wild World is a web app that introduces wildlife and shares knowledge about the wild. Users can generate different fun facts about wildlife, and the app provides free resources to learn about various animals. Users can also create accounts, log in, and log out on the website.

I chose to make this project because I have always been fascinated by wildlife. Since I was a kid, I loved watching documentaries about nature and animals. So, when given the opportunity to build a web app, I wanted to create something I love—something that allows people to gain knowledge and explore the amazing creatures that rule the wild.

## Features
The Wild World website includes the following features:
- Users can create accounts, log in, and log out.
- The home page introduces The Wild World with a welcoming hero section and a section featuring different animals to learn about.
- Users can generate fun facts about wildlife.
- A section answers the most frequently asked questions about the wild world.
- Users can search for any animal in the search bar and get detailed information, including:
  - General information about the animal.
  - Description, behavior, origin, eating habits, etc.
  - A gallery of fun images related to that animal.
  - Fun facts about the animal.

## Project Structure
This is an overview of the key files and what they do:

### Backend Files
- **`app.py`**: The main Flask application that handles requests and serves responses.
- **`helpers.py`**: Contains helper functions such as making API requests to fetch images from the Pexels API and generating animal information using Google GenAI. Also handles user authentication by connecting to the SQLite database.
- **`wilddb.db`**: SQLite database used to store user information.

### Frontend Files
- **`templates/layout.html`**: The base template that includes the navbar, footer, and general structure of the website.
- **`templates/index.html`**: The home page that users see when they first visit the website.
- **`templates/search.html`**: Displays search results for an animal.
- **`templates/register.html`** & **`templates/login.html`**: Templates for user registration and login pages.

## Technologies Used

### Backend:
- **Python (Flask)**: Handles server-side logic and request processing.
- **SQLite3**: Database used for storing user information.

### Frontend:
- **HTML**: Defines the structure of the web pages.
- **CSS**: Styles the website and ensures responsiveness.
- **Bootstrap**:
  - Used for a responsive navbar and accordion-style FAQ section.
  - Used to create a responsive gallery.
- **JavaScript**:
  - Dynamically generates new fun facts.
  - Handles user interactions with the FAQ section on the home page.

### APIs Used:
- **Google GenAI**: Used to fetch and generate detailed information about animals, including behavior, eating habits, and unique characteristics.
- **Pexels API**: Used to fetch high-quality images related to the provided animal.
