# Number Classification API

## Overview
The **Number Classification API** is a simple web service built with **Python Flask** that classifies a number based on various mathematical properties. It returns information such as whether the number is prime, perfect, Armstrong, even, odd, and its digit sum. Additionally, it fetches a fun fact related to the number from the **Numbers API**.

### **Features:**
- Classify numbers based on mathematical properties.
- Fetch a fun fact for the number.
- Returns responses in a well-structured JSON format.

## API Endpoint

### `GET /api/classify-number?number={number}`

- **Parameter:** `number` (Required) — The number to classify. It can be a positive or negative integer.

#### **Response Format (200 OK)**

```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### **Response Format (400 Bad Request)**

```json
{
  "number": "alphabet",
  "error": true
}
```

### Properties in the Response:

**is_prime**: Boolean indicating whether the number is prime.
**is_perfect**: Boolean indicating whether the number is a perfect number.
**properties**: A list containing the number's mathematical properties such as "odd", "even", "armstrong".
**digit_sum**: Sum of the digits of the number.
**fun_fact**: A fun fact related to the number fetched from the Numbers API.

### Requirements
The following packages are required to run the project:

Flask==2.0.1
requests==2.26.0
To install the requirements, simply run:

```bash
pip install -r requirements.txt
```

### Setting Up Locally
#### Clone the repository:

```bash
git clone https://github.com/your-username/number-classification-api
```

#### Navigate into the project directory:

```bash
cd number-classification-api
```

#### Set up and activate the virtual environment:

```bash
python -m venv venv
source venv/Scripts/activate  # On Windows, use `source venv/Scripts/activate`
```

#### Install the dependencies:

```bash
pip install -r requirements.txt
```
#### Run the Flask app:

```bash
flask run
```

The API will be running at http://127.0.0.1:5000/.

### Deployment
The API can be deployed to any platform that supports Python, such as Heroku, AWS, or Google Cloud.

### Testing the API
You can test the API by sending a GET request to the endpoint with a number as a query parameter. Example:

```bash
curl "http://127.0.0.1:5000/api/classify-number?number=371"
```

You should receive a response like this:

```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```
### Contributing
Contributions are welcome! If you have an idea to improve the API or find any issues, feel free to fork the repository and submit a pull request.







