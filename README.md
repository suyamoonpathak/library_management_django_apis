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
cd library_management_django_apis/library_management_system/
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

-- Log in as the default PostgreSQL superuser (e.g., 'postgres')
```bash
sudo -u postgres psql
```

#### Create a User

When the PostgreSQL command prompt or terminal opens, and enter the following commands to create a new user (replace 'suyamoon' with your desired username and 'password' with your desired password)
```sql
CREATE USER suyamoon WITH PASSWORD 'password';
```

#### Create a database (e.g., "library_management_system").
```sql
CREATE DATABASE library_management_system;
```
#### Grant all privileges on the database to the newly created user
```sql
GRANT ALL PRIVILEGES ON DATABASE library_management_system TO suyamoon;
```
#### Exit the PostgreSQL prompt
```sql
\q
```

### 7. Create .env File

Create a file named `.env` in the project directory (library_management_system). Copy the contents from `.env example` and adjust the names if you changed them in the previous step.

### 8. Run the Django App

Run the following commands to apply migrations and start the Django development server:

```bash
python manage.py migrate
python manage.py runserver
```

### 9. Access Swagger API Documentation

Visit [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) in your web browser to explore the API documentation.

Congratulations! You've successfully set up and run the Library Management System on your local machine.

# API Authentication

Before you start using the Library Management System APIs, you need to create an account and obtain a JWT (JSON Web Token) for authentication. Follow these steps:

## 1. Signup

- **Endpoint:** `POST http://localhost:8000/library/signup/`
- **Body (raw > JSON):**
  ```json
  {
      "username": "your_username",
      "password": "your_password"
  }
  ```

After successfully signing up, you will receive a success code 201.

## 2. Login

- **Endpoint:** `POST http://localhost:8000/library/login/`
- **Body (raw > JSON):**
  ```json
  {
      "username": "your_username",
      "password": "your_password"
  }
  ```

After a successful login, you will receive three values. You will need the "access" token. Copy the value.

To use this token for further API requests in tools like Postman:

1. Navigate to the "Authorization" tab.
2. Select "Bearer Token" as the **Type** of authorization from the drop down menu.
3. Paste the "access" token you received after logging in into the "Token" field on the right.


# Other API Endpoints

Now that you have successfully obtained your JWT token, you can explore the Library Management System APIs. **Note that the token expires every 2 hours.** So, you may have to keep generating a new token every two hours from your last visit. Below are the API endpoints along with the required parameters and constraints:

## 1. User APIs:

### Create a New User
- **Endpoint:** `POST http://localhost:8000/library/users/`
- **Body (raw > JSON):**
  ```json
  {
    "Name": "Suyamoon",
    "Email": "suyamoonpathak@gmail.com",
    "MembershipDate": "2024-01-02"
  }
  ```
  - Constraints: The "Email" must be unique.

### List All Users
- **Endpoint:** `GET http://localhost:8000/library/users/`

### Get User by ID
- **Endpoint:** `GET http://localhost:8000/library/users/{id}/`
  - Replace `{id}` with the actual **UserID**.

## 2. Book APIs:

### Add a New Book
- **Endpoint:** `POST http://localhost:8000/library/books/`
- **Body (raw > JSON):**
  ```json
  {
    "Title": "The Alchemist: Paulo Coelho",
    "ISBN": "9280060834838",
    "PublishedDate": "2023-02-02",
    "Genre": "Drama"
  }
  ```
  - Constraints: The "ISBN" must be unique and lesser than or equal to 13 characters.

### List All Books
- **Endpoint:** `GET http://localhost:8000/library/books/`

### Get Book by ID
- **Endpoint:** `GET http://localhost:8000/library/books/{id}/`
  - Replace `{id}` with the actual **BookID**.

### Update Book Attributes
- **Endpoint:** `PUT http://localhost:8000/library/books/{id}/`
  - Replace `{id}` with the actual **BookID**.
- **Body (JSON):**
  ```json
  {
    "Title": "The Alchemist (Updated)",
    "ISBN": "9280060834838",
    "PublishedDate": "2023-02-02",
    "Genre": "Drama"
  }
  ```
  - Constraints: The "ISBN" must be unique and lesser than or equal to 13 characters.

## 3. BookDetails APIs:

### Add New Book Details
- **Endpoint:** `POST http://localhost:8000/library/bookdetails/`
- **Body (JSON):**
  ```json
  {
      "NumberOfPages": 208,
      "Publisher": "HarperTorch",
      "Language": "English",
      "BookID": 1
  }
  ```
  - Constraints: You can't add details again to a book that already has details. Update the values using PUT. You can only add BookDetails if you have a BookID. You can't create BookDetails without a Book.

### List All Book Details
- **Endpoint:** `GET http://localhost:8000/library/bookdetails/`

### Get Book Details by ID
- **Endpoint:** `GET http://localhost:8000/library/bookdetails/{id}/`
  - Replace `{id}` with the actual **DetailsID**.

### Update Book Details
- **Endpoint:** `PUT http://localhost:8000/library/bookdetails/{id}/`
  - Replace `{id}` with the actual **DetailsID**.
- **Body (JSON):**
  ```json
  {
      "NumberOfPages": 208,
      "Publisher": "Sajha Prakashan",
      "Language": "Nepali (Dubbed)",
      "BookID": 1
  }
  ```

## 4. BorrowedBooks APIs:

### Borrow a Book
- **Endpoint:** `POST http://localhost:8000/library/borrowedbooks/`
- **Body (JSON):**
  ```json
  {
      "BorrowDate": "2023-01-02",
      "ReturnDate": "2023-01-15",
      "UserID": 1,
      "BookID": 2
  }
  ```
  - Constraints: BorrowDate can't be in the past compared to ReturnDate. ReturnDate must not be more than a month from BorrowDate.

### Return a Book
- **Endpoint:** `PUT http://localhost:8000/library/borrowedbooks/{id}/`
  - Replace `{id}` with the actual BorrowedBooks **id**.
- **Body (JSON):**
  ```json
  {
      "ReturnDate": "2023-01-10"
  }
  ```
  - Constraints: Date passed in the parameter can't be in the past compared to BorrowDate. If the Date Passed in the parameter is in the future compared to ReturnDate (set while borrowing the book), then a fine of Rs. 10 per day is charged.

### List All Borrowed Books
- **Endpoints:**
  - `GET http://localhost:8000/library/borrowedbooks/`
  - `GET http://localhost:8000/library/borrowedbooks/all`

### List Currently Borrowed Books
- **Endpoint:** `GET http://localhost:8000/library/borrowedbooks/current`

### Get Borrowed Book by ID
- **Endpoint:** `GET http://localhost:8000/library/borrowedbooks/{id}/`
  - Replace `{id}` with the actual BorrowedBooks **id**.


