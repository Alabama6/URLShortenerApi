# URL Shortener API Project

This is a simple project that provides URL shortening functionality through an API built with Django REST Framework.

## Features

- Shorten a long URL and generate a short URL.
- Expand a short URL and redirect to the original URL.

## Requirements

To run this project locally, you need to have the following installed:

- Python 3.x
- Django
- Django REST Framework

## Installation

1. Clone the repository to your local machine:
```
git clone <repository-url>
```
2. Navigate to the project directory:
```commandline
cd url_shortener
```
3. Create a virtual environment (optional but recommended):
```
python -m venv venv
```
4. Activate the virtual environment:
Windows: `venv\Scripts\activate`
macOS/Linux: `source venv/bin/activate`


5. Install the project dependencies:
```
pip install -r requirements.txt
```

6. Run the database migrations:
```commandline
python manage.py makemigrations
python manage.py migrate
```

7. Start the development server:
```
python manage.py runserver
```
## Usage

- To shorten a URL, make a POST request to the `/shrt/` endpoint with a `url` field containing the target URL. You will receive a response with the shortened URL.
- To expand a short URL, make a GET request to the `/shrt/<short_code>/` endpoint, where `<short_code>` is the shortened part of the URL. You will receive a redirect response to the original URL.

## Testing the API

You can test the API using cURL. Here are some example commands:

- Shorten a URL:
```
curl -X POST -H "Content-Type: application/json" -d '{"original_url": "http://example.com"}' http://localhost:8000/shrt/
```

- Expand a short URL:
```
curl -H "Accept: application/json" http://localhost:8000/shrt/<short_code>/
```
Replace `<short_code>` with the actual shortened code obtained from the previous step.
