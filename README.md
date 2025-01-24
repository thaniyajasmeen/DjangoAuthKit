# DjangoAuthKit Application 

This is a Django-based web application that implements user authentication and management. The project provides essential features such as login, signup, password management, and restricted access based on user authentication.

---

## Features

1. **User Authentication**
   - Login using email or username and password.
   - Sign up with email verification (optional, can be added later).

2. **Pages Included**
   - **Login Page**: Login functionality with links to sign up or reset password.
   - **Sign Up Page**: New user registration with username, email, and password.
   - **Forgot Password Page**: Email-based password reset functionality.
   - **Change Password Page**: Change the password for logged-in users.
   - **Dashboard**: Personalized user dashboard available only after login.
   - **Profile Page**: Displays user details (username, email, etc.).

3. **Access Restriction**
   - Certain pages (like Dashboard and Profile) are restricted to authenticated users only.

---

## Pages and Functionalities

### 1. **Login Page**
   - Fields: Username/Email, Password.
   - Links: Sign Up, Forgot Password.

### 2. **Sign Up Page**
   - Fields: Username, Email, Password, Confirm Password.
   - Link to return to the Login page.

### 3. **Forgot Password Page**
   - Field: Email.
   - Button to send password reset instructions via email.

### 4. **Change Password Page**
   - Fields: Old Password, New Password, Confirm Password.
   - Accessible only by logged-in users.

### 5. **Dashboard**
   - Displays a greeting message: "Hi, username!"
   - Links to:
     - Profile Page.
     - Change Password Page.
     - Logout.

### 6. **Profile Page**
   - Displays:
     - Username.
     - Email.
     - Date Joined.
     - Last Updated.
   - Links:
     - Dashboard.
     - Logout.

---

## Requirements

1. **Python** (Version 3.x)
2. **Django** (Latest version recommended)
3. Email setup for the password reset functionality.

---

## Installation Instructions

1) Git Clone :
2) cd
3) Create and activate a virtual environment:
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
4) Apply database migrations:
python manage.py migrate
5) Run the development server:
python manage.py runserver
6) Access the application: Open your browser and navigate to http://127.0.0.1:8000/.

**Contributing**
Contributions are welcome! Feel free to fork the repository and submit pull requests.

**Contact**
For questions or feedback, feel free to reach out at jazzthaniya51@gmail.com.



  
