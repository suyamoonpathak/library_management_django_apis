# Project Setup and Run Guide

Welcome to the Library Management System! Follow these step-by-step instructions to set up and run the project on your local machine.

## Prerequisites

Before you begin, make sure you have the following installed:

- [Git](https://git-scm.com/downloads)
- [Python](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)

## Steps

### 1. Clone the Repository

Open your terminal (command prompt) and navigate to the directory where you want to store the project. Run the following command:

```bash
git clone https://github.com/suyamoonpathak/library_management_django_apis
```

### 2. Extract the Zip

If you downloaded a zip file, extract its contents to a folder.

### 3. Create a Virtual Environment

Navigate into the project directory:

```bash
cd library-management-system
```

Create a virtual environment:

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### On Windows:

```bash
venv\Scripts\activate
```

#### On macOS/Linux:

```bash
source venv/bin/activate
```

### 5. Install Dependencies

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

### 6. Setup PostgreSQL Database

- Install PostgreSQL and create a user (e.g., "suyamoon") with the password "password."
- Create a database (e.g., "library_management_system").

### 7. Create .env File

Create a file named `.env` in the project directory. Copy the contents from `.env example` and adjust the names if you changed them in the previous step.

### 8. Run the Django App

Run the following commands to apply migrations and start the Django development server:

```bash
python manage.py migrate
python manage.py runserver
```

### 9. Access Swagger API Documentation

Visit [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) in your web browser to explore the API documentation.

Congratulations! You've successfully set up and run the Library Management System on your local machine. If you have any issues, feel free to reach out for help.
