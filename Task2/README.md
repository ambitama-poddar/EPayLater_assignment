# Housing Data REST API

## Approach 1: SQLAlchemy

```markdown

This is a Flask-based REST API that handles housing data. It provides endpoints for creating housing data from a JSON file, and retrieving average sale prices, maximum sale price, minimum sale price, and average sale prices per location using SQL queries.

## Installation and Setup

1. Clone this repository.
2. Install the required dependencies:
   pip install flask flask_sqlalchemy
3. Set up your PostgreSQL database. Update the connection details in the code if necessary.
4. Start the Flask server:
   python app1.py
5. The server will start running at `http://localhost:5000`.
```

## Usage

### Create Housing Data
```markdown

- **URL:** `/housing_data`
- **Method:** POST
- **Payload:** Provide a JSON object containing the housing data in the following format:
  ```json
  {
    "data": [
      {
        "Bedrooms": 3,
        "Bathrooms": 2,
        "SquareFootage": 1500,
        "Location": "New York",
        "SalePrice": 250000
      },
      {
        "Bedrooms": 4,
        "Bathrooms": 3,
        "SquareFootage": 2000,
        "Location": "Los Angeles",
        "SalePrice": 350000
      },
      ...
    ]
  }
  ```
- **Response:** Returns a JSON object with a message indicating the success of the operation.

### Get Average Sale Price Overall

- **URL:** `/average_sale_price`
- **Method:** GET
- **Response:** Returns a JSON object with the average sale price of houses overall.

### Get Average Sale Price Per Location

- **URL:** `/average_sale_price_per_location`
- **Method:** GET
- **Response:** Returns a JSON object with the average sale price of houses per location.

### Get Maximum Sale Price

- **URL:** `/max_sale_price`
- **Method:** GET
- **Response:** Returns a JSON object with the maximum sale price of houses.

### Get Minimum Sale Price

- **URL:** `/min_sale_price`
- **Method:** GET
- **Response:** Returns a JSON object with the minimum sale price of houses.

## Approach 2: psycopg2 + SQL Queries

In this approach, the data is loaded from a JSON file and stored in a PostgreSQL database using psycopg2. SQL queries are directly executed to fetch the required information.

## Installation and Setup

1. Clone this repository. 
2. Install the required dependencies:
   pip install flask psycopg2
3. Set up your PostgreSQL database. Update the connection details in the code if necessary.
4. Start the Flask server:
   python app2.py
5. The server will start running at `http://localhost:5000`.

### Endpoints

- **POST /housing_data**: Create housing data.
- **GET /average_sale_price**: Get the average sale price of houses overall.
- **GET /average_sale_price_per_location**: Get the average sale price of houses per location.
- **GET /max_sale_price**: Get the maximum sale price of houses.
- **GET /min_sale_price**: Get the minimum sale price of houses.

## License

This project is licensed under the [MIT License](LICENSE).

```
