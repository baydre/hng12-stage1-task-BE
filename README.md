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

## Run Locally
Clone the repository
```bash
    git clone git@github.com:baydre/hng12-stage1-task-BE.git #ssh

    git clone https://github.com/baydre/hng12-stage1-task-BE.git #https
```
Install dependencies:
```bash
    pip install -r requirements.txt
```
Run the application:
```bash
    python3 main.py
```

## Tech Stack
- Python Flask

## Dependencies
- Flask
- Flask-CORS
- Requests
- Gunicorn

## Deployment
Deployed on [Render](https://dashboard.render.com/) and can be accessed at []()

## Authors

- [@baydre](https://github.com/baydre)

Open to coders, designers, product managers, and many more. Learn more at [HNG Internship](https://hng.tech).

## Backlinks
- [Hire Python Developers](https://hng.tech/hire/python-developers)
- [Hire C# Developers](https://hng.tech/hire/csharp-developers)
- [Hire Go Developers](https://hng.tech/hire/golang-developers)
- [Hire PHP Developers](https://hng.tech/hire/php-developers)
- [Hire Java Developers](https://hng.tech/hire/java-developers)
- [Hire Node.js Developers](https://hng.tech/hire/nodejs-developers)

## Acknowledgements
- [Numbers API for mathematical facts](http://numbersapi.com/)
- [HNG Internship Program](https://hng.tech)