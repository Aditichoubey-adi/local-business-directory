# Local Business Directory (Django Web App)

This project is a **Local Business Directory** web application built using the Django framework. Its purpose is to allow users to browse, search, and manage listings of local businesses. It includes key functionalities such as user authentication, business categorization, and the display of detailed business information.

## Table of Contents
- [About The Project](#about-the-project)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Future Enhancements](#future-enhancements)
- [License](#license)
- [Contact](#contact)

## About The Project

This is a **Local Business Directory** web application built with Django and Python. It allows users to browse, search, and manage local business listings. The application provides robust functionalities for user authentication, categorizing businesses, and displaying detailed business information.

## Features

* **User Authentication:** Seamless Register, Login, and Logout functionality for users.
* **Business Listing:** Users can add new business details including Name, Address, Phone Number, Description, and an optional Image, categorized appropriately.
* **Business Management:** Authenticated users can view, edit, and delete their own business listings.
* **Category Management:** Businesses are organized into different categories for easy navigation.
* **Search Functionality:** Efficiently search for businesses by name or description.
* **Responsive Design:** User-friendly interface built with Bootstrap, ensuring a good experience on various devices.

## Technologies Used

* **Backend:**
    * Python (Programming Language)
    * Django (Web Framework)
    * SQLite (Database for local development)
    * Gunicorn (WSGI HTTP Server for production deployment)
* **Frontend:**
    * HTML (Structure)
    * CSS (Styling)
    * Bootstrap (CSS Framework for responsive design)
    * Django Template Language (DTL for dynamic content rendering)
* **Version Control:**
    * Git
    * GitHub

## Getting Started

To get a local copy of this project up and running on your machine, follow these simple steps.

### Prerequisites

Make sure you have Python installed on your system. It's highly recommended to use a virtual environment for dependency management.

* Python 3.x
* pip (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Aditichoubey-adi/local-business-directory.git](https://github.com/Aditichoubey-adi/local-business-directory.git)
    cd local-business-directory
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```
3.  **Install project dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Apply database migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5.  **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts in the terminal to set up your desired username, email, and password for the admin panel.

## Usage

1.  **Run the Django development server:**
    ```bash
    python manage.py runserver
    ```
2.  Open your web browser and navigate to `http://127.0.0.1:8000/`.
3.  From the homepage, you can:
    * Register a new user account or log in with an existing one.
    * Add new businesses through the user interface (after logging in) or manage existing ones via the Django admin panel at `http://127.0.0.1:8000/admin/` (if logged in as a superuser).
    * Browse through the list of businesses and utilize the search functionality.

## Deployment

This project is deployed live on the internet using **Render**, a cloud application platform.

**Live Demo:** [https://local-business-directory-pkhz.onrender.com/](https://local-business-directory-pkhz.onrender.com/)


## Contact

Your Name - [jchoubey609@gmail.com]
Project Link: [https://github.com/Aditichoubey-adi/local-business-directory](https://github.com/Aditichoubey-adi/local-business-directory)

   
