# Ecommerce Project

This project is a simple ecommerce application that allows users to buy and sell products online. The project uses Python as the programming language and MySQL as the database.

## Features

The project has the following features:

- Users can create an account, login, and reset their password.
- Users can view all the products available in the database.
- Users can add products to their cart and place orders.
- Users can view their orders and track their status.
- Users can create and view their address details.
- Admins can login and manage the products in the database.

## Installation

To run this project, you need to have Python 3 and MySQL installed on your system. You also need to install the following Python packages:

- mysql-connector-python
- settings
- db
- auth
- inner_section
- admin

You can install them using the command:

`pip install -r requirements.txt`

## Usage

To start the project, you need to run the main.py file using the command:

`python main.py`

The project will connect to the MySQL database using the settings in the settings.py file. You can change them according to your configuration.

The project will then display a menu with the following options:

1. Login
2. Admin Login
3. Create Account
4. Reset Password
5. Exit

You can choose any option by entering the corresponding number.

If you choose to login or create an account, you will be asked to enter your email and password. If you choose to reset your password, you will be asked to enter your email and a verification code that will be sent to your email.

If you login successfully, you will enter the inner section of the project, where you will see another menu with the following options:

1. View All Products
2. View Orders
3. Add Product To Cart
4. View Products In My Cart
5. Place Orders In Cart
6. Create Address
7. View Address
8. Logout

You can choose any option by entering the corresponding number.

If you have any further questions or need assistance with anything else, feel free to ask!