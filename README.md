# flask-weather-api-with-TDD Documentation

The Flask Weather Application is a simple web application that provides weather data for cities. It allows users to retrieve, create, update, and delete weather information using HTTP requests.

## Installation

To run the Flask Weather Application, follow these steps:

1. Clone the project repository from GitHub:
   ```
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```
   cd flask-weather-app
   ```
3. Set up a virtual environment (optional but recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Starting the Application

To start the Flask Weather Application, run the following command in the project directory:
```
python app.py
```
This will start the Flask development server, and the application will be accessible at `http://localhost:5000`.

### API Endpoints

The Flask Weather Application provides the following API endpoints:

#### GET /weather/<city>

Retrieves the weather information for a specific city.

- Method: GET
- Path: `/weather/<city>`
- Parameters:
  - `<city>`: The name of the city (string)
- Response:
  - 200 OK: Returns the weather information for the specified city as a JSON object.
  - 404 Not Found: If the specified city is not found.

#### POST /weather

Creates new weather data for a city.

- Method: POST
- Path: `/weather`
- Request Body:
  - JSON object containing the following fields:
    - `city`: The name of the city (string)
    - `temperature`: The temperature in Celsius (integer)
    - `weather`: The weather description (string)
- Response:
  - 201 Created: Returns the created weather data as a JSON object.
  - 400 Bad Request: If the specified city already has weather data.

#### PUT /weather/<city>

Updates the weather data for a specific city.

- Method: PUT
- Path: `/weather/<city>`
- Parameters:
  - `<city>`: The name of the city (string)
- Request Body:
  - JSON object containing the fields to be updated:
    - `temperature` (optional): The updated temperature in Celsius (integer)
    - `weather` (optional): The updated weather description (string)
- Response:
  - 200 OK: Returns the updated weather data as a JSON object.
  - 404 Not Found: If the specified city is not found.

#### DELETE /weather/<city>

Deletes the weather data for a specific city.

- Method: DELETE
- Path: `/weather/<city>`
- Parameters:
  - `<city>`: The name of the city (string)
- Response:
  - 200 OK: Returns a message confirming the deletion.
  - 404 Not Found: If the specified city is not found.

### Examples

#### Example: Retrieving Weather Data

To retrieve the weather data for a city, send a GET request to `/weather/<city>`, where `<city>` is the name of the city.

Request:
```
GET /weather/New York
```
Response:
```json
{
  "temperature": 20,
  "weather": "Sunny"
}
```

#### Example: Creating Weather Data

To create new weather data for a city, send a POST request to `/weather` with the weather data in the request body.

Request:
```
POST /weather
Content-Type: application/json

{
  "city": "Chicago",
  "temperature": 18,
  "weather": "Cloudy"
}
```
Response:
```json
{
  "city": "Chicago",
  "temperature": 18,
  "weather": "Cloudy"
}
```

#### Example: Updating Weather Data

To update the weather data for a city, send a PUT request to `/weather/<city>` with the updated weather data in the request body.

Request:
```
PUT /weather/Seattle
Content-Type: application/json

{
  "temperature": 22,
  "weather": "Sunny"
}
```
Response:
```json
{
  "temperature": 22,
  "weather": "Sunny"
}
```

#### Example: Deleting Weather Data

To delete the weather data for a city, send a DELETE request to `/weather/<city>`, where `<city>` is the name of the city.

Request:
```
DELETE /weather/Austin
```
Response:
```json
{
  "message": "Weather data for Austin deleted"
}
```

## Testing

The Flask Weather Application includes unit tests to ensure the correctness of its functionality. To run the tests, use the following command in the project directory:
```
pytest
```

The tests cover the functionality of all endpoints, including retrieving weather data, creating new weather data, updating weather data, and deleting weather data.

## Conclusion

The Flask Weather Application provides a simple and lightweight solution for managing weather data for cities. It allows users to retrieve, create, update, and delete weather information using HTTP requests. By following the Test-Driven Development (TDD) approach, the application was developed incrementally and tested thoroughly to ensure its functionality.

Feel free to explore and customize the application further based on your needs.


