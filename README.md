# Project Documentation

## Overview
This project is a RESTful API for a note-taking application developed using Node.js, Express, and MongoDB. The purpose of the project is to provide a backend service for managing and persisting notes with functionalities to create, retrieve, and delete notes. The frontend is built using React to ensure scalability, readability, and modularity of the frontend code. The notes are hosted and kept in a MongoDB database to ensure that the notes do not disappear after refreshing the page. Express.js and Node.js are used to frame the backend API and facilitate communication between the server and client. 

## Technologies used

### Frontend

The front end is created using Javascript (ES6), HTML, and CSS. React framework is used for its virtual DOM and performance optimization and its reusable components, which can enhance code reusability and codability. React also allows easy integration with other frontend and backend technologies to ensure the connection from the client to the server is stable. 

### Database

MongoDB is used as the database to store the notes. Storing notes in the backend is critical because it ensures that notes user entered will not be removed after refreshing or reopening the page. MongoDB is notable for its high speed and availability, its Atlas function which allows a simple and free setup and database connection, and its flexibility in terms of note structure. Compared to SQL, MongoDB allows for highly diverse and flexible data and allows building the webpage faster. 

### Backend

Express.js and Node.js are used for the backend development of this note-taking webpage. They are used to establish a server for MongoDB database connection and building API endpoints, which handle adding, retrieving, and deleting notes efficiently using RESTful API conventions and methodologies. The backend ensures that what user inputs and modifies gets transmitted to the database, and any changes in the database are accurately and promptly reflected back to the client. The backend serves as a crucial connection between the client and the server, ensuring their interactions and sent and reflected as expected. 

## File Structure
The project structure is organized as follows:
- `/backend`: Contains the server-side code
  - `/models`: Defines the data models (e.g., `Note` model)
  - `/routes`: Handles different API routes for note operations
- `/public`:
- `/src`:

The backend and frontend code are separated for best practices, and modifications in one shall in general not impact the other. 

## Key Components
### Models
The `Note` model represents a note entity in the database with fields `title` and `content`.

### Routes
- `POST /`: Creates a new note
- `GET /`: Retrieves all notes
- `DELETE /:id`: Deletes a note by ID


## API Endpoints
### POST /
- Creates a new note
- Request Body:

{
"title": "Note Title",
"content": "Note Content"
}

- Response (201 - Created):

{
"_id": "note_id",
"title": "Note Title",
"content": "Note Content"
}


### GET /
- Retrieves all notes
- Response (200 - OK): Array of all notes

### DELETE /:id
- Deletes a note by ID
- Response (200 - OK): Deleted note object

## Running the Project
To run the project locally:
1. Clone the repository from GitHub.
2. Install dependencies using `npm install`.
3. Ensure that the command is currently in the backend folder by  `cd backend/` if necessary.
4. Start the server with `` or `node server.js`.
5. The server will run on `http://localhost:3000`.

## Dependencies
The project uses the following dependencies:
- Express: Web framework for Node.js
- Mongoose: MongoDB object modeling tool
- Body-parser: Parse incoming request bodies in a middleware



## Testing
You can test the API endpoints using tools like Postman. The API endpoints documented above can all be tested:

- POST
- GET
- DELETE

## Author
Haolin Guo

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
