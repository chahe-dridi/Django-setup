# Django Setup

This project is a Django web application example.

## Requirements
- Python 3.9.10 (Download from: https://www.python.org/downloads/release/python-3910/)
- Django 4.2

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/chahe-dridi/Django-setup.git
   cd Django-setup
   ```

2. **Create and activate a virtual environment (recommended):**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies:**
   ```sh
   pip install django==4.2
   ```

4. **Run migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Start the development server:**
   ```sh
   python manage.py runserver
   ```

6. **Access the app:**
   - Visit [http://localhost:8000/event/hello/](http://localhost:8000/event/hello/) for the hello view.
   - Visit [http://localhost:8000/event/bonjour/](http://localhost:8000/event/bonjour/) for the bonjour view.

## Project Structure
- `Event/` - Django app containing views and templates
- `Template/` - Contains HTML templates (e.g., `Template/event/hello.html`)
- `manage.py` - Django project management script

## Notes
- Make sure you are using Python 3.9.10 for compatibility.
- If you need to install Python 3.9.10, download it from the [official Python website](https://www.python.org/downloads/release/python-3910/).
