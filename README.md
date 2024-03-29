# RIDE SHARING API

Ride Sharing API

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Prerequisites

- Python 3.8 or higher
- Django 3 or higher
- Virtualenv

## Installation

1. Clone the repository:

    bash
    git clone https://github.com/beemabeevimk/eduport_task
    

2. Navigate to the project directory:

    bash
    cd ride-sharing-api
    

3. Create a virtual environment:

    - On Windows:

        bash
        python -m venv venv
        venv\Scripts\activate
        

    - On macOS and Linux:

        bash
        python3 -m venv venv
        source venv/bin/activate
        

4. Install dependencies:

    bash
    pip install -r requirements.txt
    

## Basic Commands

### Setting Up Your Users

- To create a *superuser account*, use this command:

    bash
    python manage.py createsuperuser
    

### Running the Development Server

To run the Django development server:

```bash
python manage.py runserver