# FDR Vendor Mock

`fdr-vendor-mock` is a mock microservice designed to simulate the behavior and API of a vendor system in an FDR (Financial / Report / Domain) context. It helps development and testing teams work independently by providing a fake but realistic backend vendor API without relying on live systems.

---

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Architecture](#architecture)  
- [Tech Stack](#tech-stack)  
- [Directory Structure](#directory-structure)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
  - [Running the Service](#running-the-service)  
- [Configuration](#configuration)  
- [API Endpoints](#api-endpoints)  
- [Usage](#usage)  
- [Mock Data](#mock-data)  
- [Testing](#testing)  
- [Docker Support](#docker-support)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)  

---

## Overview

The `fdr-vendor-mock` service simulates a vendor API by exposing fake endpoints, predefined data, and simple business logic. It’s especially useful for:

- Frontend development without waiting for real vendor APIs  
- Integration testing with a stable mock service  
- CI/CD pipelines to validate interactions  
- Simulating vendor failures or edge cases  

---

## Features

- RESTful mock API endpoints (GET, POST, etc.)  
- Pre-configured vendor data as JSON or in-memory structures  
- Simple logic for creating, updating, and deleting vendor records (if needed)  
- Easily extendable to simulate more complex behavior  
- Docker support for containerized development/testing  

---

## Architecture

┌────────────────────────┐
│ Client / Frontend │
└──────────┬─────────────┘
│ HTTP calls to vendor API
▼
┌────────────────────────┐
│ FDR Vendor Mock API │
│ - Receives requests │
│ - Returns mock data │
│ - Simulates behavior │
└──────────┬─────────────┘
│
▼
Mock Data (JSON / In-memory)

yaml
Copy code

---

## Tech Stack

- **Language:** Python (or language based on your implementation)  
- **Framework:** Flask / FastAPI / similar lightweight HTTP server (adjust as per your code)  
- **Data:** JSON files or in-memory mock data  
- **Containerization:** Docker  

---

## Directory Structure

Here's a typical structure (adjust if your repo is different):

fdr-vendor-mock/
├── main.py # Entry point for service
├── handlers/ # Handlers or controllers for endpoints
├── data/ # Mock JSON data / vendor records
├── config/ # Configuration (env, constants)
├── utils/ # Utility functions / helpers
├── requirements.txt # Python dependencies
└── Dockerfile # To containerize the mock service

yaml
Copy code

---

## Getting Started

### Prerequisites

- Python 3.7+  
- `pip`  
- Docker (optional)  

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/simpsonorg/fdr-vendor-mock.git
   cd fdr-vendor-mock
(Optional) Create a virtual environment and activate it:

bash
python3 -m venv venv
source venv/bin/activate
Install Python dependencies:

bash
pip install -r requirements.txt
Running the Service
Run the application:

bash
python main.py
If you’re using Flask / FastAPI, this should start the server on a default port (check your code for the exact port).

Configuration
You can configure the mock service using environment variables (or a config file) — for example:

Variable Name	Description	Default / Example
PORT	Port on which the service runs	5000
DATA_FILE	Path to mock JSON data	./data/vendors.json
LOG_LEVEL	Logging level (DEBUG, INFO, ERROR, etc.)	INFO

Example .env file:

ini
Copy code
PORT=5000
DATA_FILE=./data/vendors.json
LOG_LEVEL=DEBUG
API Endpoints
Below are example endpoints your mock service might provide (adjust based on your implementation):

Method	Path	Description
GET	/vendors	Get list of all vendor records
GET	/vendors/{id}	Get a single vendor by ID
POST	/vendors	Create a new vendor record
PUT	/vendors/{id}	Update an existing vendor
DELETE	/vendors/{id}	Delete a vendor record

Usage
You can interact with the mock vendor API using curl, Postman, or your front-end app.

Example: Create a new vendor

bash
curl -X POST http://localhost:5000/vendors \
     -H "Content-Type: application/json" \
