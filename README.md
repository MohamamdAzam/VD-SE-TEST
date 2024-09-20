# Django Order Management System

This is a simple Django application for managing customer orders. It allows users to add orders and view the top customers based on their spending.

## Python Programs Questions

Questions 1, 2, 4, 5, and 6 can be verified by simply running the corresponding Python files.

For question 3, we have provided all the steps necessary since this is a Django app task.

## Features

- Add new customer orders
- View top customers who have spent the most in the last 6 months
- Basic styling for a user-friendly interface

## Technologies Used

- Django
- Python
- HTML/CSS

## Installation

1. Clone the repository:
   git clone <repository-url>
   cd <repository-directory>

2. Create a virtual environment:
   python -m venv venv

3. Activate the virtual environment:
   - On Windows: venv\Scripts\activate
   - On macOS/Linux: source venv/bin/activate

4. Install the required packages:
   pip install django

5. Run database migrations:
   python manage.py migrate

6. Create a superuser to access the admin panel:
   python manage.py createsuperuser

7. Run the development server:
   python manage.py runserver

8. Access the application:
   Open your web browser and go to http://127.0.0.1:8000/orders/add-order/ to add orders or http://127.0.0.1:8000/orders/top-customers/ to view the top customers.

## Usage

- Adding Orders: Use the "Add Order" page to create new orders. You can select customers and input order details.
- View Top Customers: Navigate to the "Top Customers" page to see the list of customers who have spent the most in the last 6 months.

