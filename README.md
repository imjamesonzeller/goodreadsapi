# Goodreads API

This project provides a simple API to retreive your current read from Goodreads in a formatted manner. It uses Flask as the web framework and allows users to send a GET request. The API returns a JSON object that contains a string that is their current read's title and author. ex: "Lightlark by Alex Aster"

## Features

- **Current Read Retrieval**: Requests webpage of specific Goodreads user and uses beautiful soup to find string with current read information.
- **GET Method**: Accepts `GET` requests for a simple, 15 word, word search.
- **JSON Response**: Returns a JSON object representing the generated word search grid along with the words that are contained.

## Requirements

- Python 3.x
- Flask
- `requests` (for testing)
- `flask_cors` (for enabling CORS)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/imjamesonzeller/goodreadsapi.git
cd goodreadsapi
```

### 2. Install Dependencies

You can install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

Alternatively, install Flask and CORS manually:

```bash
pip install Flask flask_cors
```

### 3. Modify URL to specific Goodreads user.

In current_read.py modify the url variable (Line 5) to match the desired Goodread's user's URL.

### 4. Run the Flask API Server

Start the Flask server by running the following command:

```bash
python app.py
```

By default, the API will be available at `http://localhost:5001`. If you want to deploy it to a different IP or port, you can modify the `app.run()` call in `app.py`.

### `GET /get_current_read`

This endpoint returns your current read formatted.

#### Request

- **URL**: `/get_current_read`
- **Method**: `GET`

#### Response

The response will be a JSON object containing your current read.

Example response:

```json
{
  'attrs': "Lightlark by Alex Aster"
}
```

#### Error Responses

- **400 Bad Request**: If an invalid request is sent.

- **404 Not Found**: If the endpoint is incorrect or unavailable.
  
- **500 Internal Server Error**: If there is a server-side error.

## Testing the API

You can test the API using a tool like **Postman** or **cURL**. Here's how to do it with **cURL**:

### Example cURL Request for POST:

```bash
curl -X GET http://localhost:5001/get_current_read \
     -H "Content-Type: application/json" \
```

If successful, you'll receive a JSON response with the attributes of your current read.

### Example Python Test Script

You can also test the API with the following Python script using the `requests` library:

```python
import requests
import json

# URL of your Flask API endpoint
url = 'http://localhost:5001/get_current_read'

# Send the POST request to the Flask API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Current read retrieved successfully!")
    print(json.dumps(response.json(), indent=2))
else:
    print(f"Error: {response.status_code}")
    print(response.text)
```

### Dependencies for Testing

If you're testing the API using Python, you'll need to install the `requests` library:

```bash
pip install requests
```

## Code Explanation

### `app.py`

The Flask API is defined in `app.py`. The key parts of the code are:

- **CORS**: This is enabled to allow cross-origin requests, which is particularly useful if you're hosting the API and front-end on different domains.
  
- **GET `/get_current_read`**: The main endpoint where users can request their current read from Goodreads.

# Self-Hosting & Deployment

This Good Reads API is self-hosted on my home server using Docker. It is used privatly for updating the current read on my website.

### Hosting with Docker

To make the API available, I’ve containerized the application using Docker. 

## Conclusion

The Word Search API is a fun and simple tool to see your Goodreads current read. This project demonstrates my ability to work with both backend technologies, as well as my familiarity with Docker and cloud-based hosting.

Feel free to see it in use on the website or directly interact with the API by cloning it!

## License

This project is open source and available under the MIT License.