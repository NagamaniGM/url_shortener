# URL Shortener

A simple Flask-based URL shortener with SQLite database.

## Features
- Shortens long URLs into unique short links
- Stores data in SQLite database (`urls.db`)
- Redirects users when the short link is visited
- Random 6-character short code generation

## Getting started

### Prerequisites
- Python 3.8+ installed

### Install dependencies
```bash
pip install flask
```

### Run locally
```bash
python app.py
```
Then open http://localhost:5000 in your browser.

## Project structure
```
url_shortener/
├─ app.py
└─ urls.db  (auto-created on first run)
```

## How it works
- On the home page, submit a long URL.
- The app creates a random 6-character code and stores the mapping in SQLite.
- Visiting `http://localhost:5000/<code>` redirects to the long URL.

## License
MIT
