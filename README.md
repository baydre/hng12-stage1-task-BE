# Number Classification API

## Overview
A Flask-based API that provides detailed mathematical properties and fun facts about a given number.

## Features
- Determines if a number is prime
- Checks if a number is perfect
- Identifies Armstrong numbers
- Calculates digit sum
- Retrieves a fun math fact about the number

## API Endpoint
```http
GET /api/classify-number?number={your_number}
```

## Response Example
```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number..."
}
```

## Setup
Clone the repository
```bash
    git clone <repository>
```
Install dependencies:
```bash
    pip install flask flask-cors requests
```
Run the application:
```bash
    python main.py
```

## Dependencies
- Flask
- Flask-CORS
- Requests
- Gunicorn

## Deployment
Deployed on [Your Deployment Platform]

## Acknowledgements
- Numbers API for mathematical facts
- HNG Internship Program