# Flask Request Logger

A simple Flask-based Python script that logs HTTP requests made to a web server. It captures the client's IP address, HTTP method, and requested path, printing them to the console. The server responds with a "Logged" message and a 200 status code for all requests.

## Features
- Logs HTTP requests (GET, POST, PUT, DELETE, PATCH, OPTIONS) with client IP, method, and path.
- Supports dynamic routing for any path.
- Lightweight and easy to deploy.
- Runs on a customizable host and port.

## Prerequisites
- **Python Version**: Python 3.6 or higher.
- **Dependencies**:
  - `Flask` (web framework for handling HTTP requests)

## Installation
1. Clone or download the script to your local machine.
2. Install the required dependency:
   ```bash
   pip install flask
