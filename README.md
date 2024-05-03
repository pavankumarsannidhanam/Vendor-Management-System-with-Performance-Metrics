# Vendor Management System

This project is a Vendor Management System implemented using Django and Django REST Framework.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/your_repository.git
   cd your_repository 
2. Install Dependencies:
   ```bash
  pip install -r requirements

3. Apply migrations:
   ```bash
   python manage.py migrate

4. Run the development server:
   ```bash
   python manage.py runserver

5. Access the API endpoints in your browser or using tools like Postman:
   ```bash
   Vendor API: http://localhost:8000/api/vendors/
   Purchase Order API: http://localhost:8000/api/purchase_orders/
   Vendor Performance Endpoint: http://localhost:8000/api/vendors/{vendor_id}/performance/
   Acknowledge Purchase Order Endpoint: http://localhost:8000/api/purchase_orders/{po_id}/acknowledge/

