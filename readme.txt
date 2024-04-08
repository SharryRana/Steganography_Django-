# Image Uploader Application

## Introduction
This README file provides instructions on how to set up and run the Image Uploader Application on your local machine.

## Prerequisites
Before proceeding with the installation, ensure you have the following installed:
- Python (latest version): [Download Python](https://www.python.org/downloads/)
- Django: Install using `pip install django`
- XAMPP Server (latest version) for SQL database: [Download XAMPP](https://www.apachefriends.org/download.html)
- Required Python packages: 
  - Pillow: Install using `pip install pillow`
  - mysqlclient: Install using `pip install mysqlclient`
  
## Installation Steps
1. Install Python: 
   - Download and install Python from the [official website](https://www.python.org/downloads/)
   - Make sure to check the option to add Python to your system PATH during installation.

2. Install Django:
   - Open your command prompt or terminal.
   - Run the command `pip install django` to install Django.

3. Install XAMPP Server:
   - Download and install XAMPP Server from the [official website](https://www.apachefriends.org/download.html).
   - Follow the installation instructions provided on the website.

4. Create Database:
   - Once XAMPP is installed, start the XAMPP control panel.
   - Start the Apache and MySQL services.
   - Open your browser and navigate to `http://localhost/phpmyadmin/`.
   - Create a new database named `image_audio_text_upload`.

5. Install Required Python Packages:
   - Open your command prompt or terminal.
   - Run the following commands:
     ```
     pip install pillow
     pip install mysqlclient
     ```

6. Project Setup:
   - Download the project files and unzip them.
   - Open the project in your preferred code editor (e.g., VSCode, Sublime Text).

7. Run Migrations:
   - In your code editor's terminal, navigate to the project directory.
   - Run the following commands:
     ```
     python manage.py makemigrations
     python manage.py migrate
     ```

8. Run the Server:
   - After migrating the database, run the following command to start the server:
     ```
     python manage.py runserver
     ```

9. Access the Application:
   - Once the server is running, open your web browser.
   - Navigate to `http://127.0.0.1:8000/` to access the Image Uploader Application.

## Conclusion
You have successfully set up the Image Uploader Application on your local machine. 
If you encounter any issues during the installation process, please refer to the troubleshooting section in the project documentation.

---
Note: Replace `python` with `python3` if `python` command doesn't work for you, depending on your Python installation.