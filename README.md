
<p align="center">
  <img src="assets/banne.png" alt="Banner" width="100%">
</p>

# Python Multi-Service API Client

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![REST API](https://img.shields.io/badge/REST-API-success)
![JSON](https://img.shields.io/badge/JSON-Data-orange)
![Automation](https://img.shields.io/badge/Automation-Python-blueviolet)
![GitHub](https://img.shields.io/badge/Open%20Source-GitHub-black?logo=github)

A Python automation project demonstrating API integration, JSON processing, structured data storage, and robust error handling using multiple public APIs.

A beginner-friendly Python automation project that demonstrates how to communicate with multiple external APIs, process JSON responses, store structured data, and implement basic error handling.

This project was developed as part of my AI Automation Engineering learning journey.

---

## Project Overview

This application communicates with three independent public APIs:

- Weather API
- Currency Exchange API
- Cryptocurrency API

The application:

- Sends HTTP GET requests
- Receives API responses
- Parses JSON data
- Extracts required information
- Saves processed data into JSON files
- Handles common API failures gracefully

---

## Features

- Multi-API Integration
- JSON Parsing
- Nested JSON Processing
- Structured Data Extraction
- JSON File Storage
- HTTP Communication
- Basic Error Handling
- Modular Project Structure

---

## Project Structure

```text
Python-Multi-Service-API-Client/
│
├── apis/
│   ├── weather.py
│   ├── currency.py
│   └── crypto.py
│
├── output/
│   ├── weather.json
│   ├── currency.json
│   └── crypto.json
│
├── config/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## Technologies Used

- Python
- Requests
- JSON
- REST APIs

---

## APIs Used

- wttr.in
- Open Exchange Rates API (open.er-api.com)
- CoinGecko API

---

## Learning Outcomes

Through this project I practiced:

- Python API communication
- HTTP GET requests
- JSON parsing
- Nested JSON processing
- Error handling
- Data serialization
- Modular Python programming

---

## Future Improvements

- Environment variable integration
- Logging
- Retry mechanism
- API authentication
- Docker support
- Unit testing

---

## Author

Abdul Qadeer

AI Automation Engineering Learning Journey