# The Profile App (Resume)

The Profile App (Resume) is a web application that allows users to create and share their resumes online. Users can add their skills, certificates, personal profile picture, short description, and detailed description to their resumes. Each user gets a unique website link where their resume is hosted, making it easy to share with others. Recipients of the link can view all the skills, certificates, and details of the sender. The sender can update their resume at any time, and these changes are instantly reflected in the shared link after the recipient refreshes the webpage.

## Installation

To run the project, follow these steps:

1. Activate the virtual environment:
  ./venv/Scripts/activate
2. Navigate to the project folder:
  cd MyProject
3. Run the Django server:
  python manage.py runserver
4. Access the project using the provided link.

## Project Structure

The project directory structure includes:

- `venv/`: Virtual environment folder.
- `MyProject/`: Main project folder.
  - `myapp/`: Django application folder.
    - `migrations/`: Folder containing migration files.
    - `models.py`, `views.py`, `urls.py`: Files for app functionality.
  - `src/`: Project settings folder.
    - `settings.py`, `urls.py`, etc.: Project settings files.
  - `static/`: Folder for static files like CSS and images.
    - `profile_pics/`: Folder for user-uploaded profile pictures.
    - `certificates/`: Folder for user-uploaded certificates.
    - CSS files.
  - `templates/`: Folder containing HTML templates.
    - HTML files for webpage navigation.
- `db.sqlite3`: SQLite database file.
- `manage.py`: Django management script.


## Security

Every user-created profile is password-protected, ensuring that only authorized users can edit their resumes.

## Contact

For questions or feedback, contact:

- Name: Arpit Dara
- Phone: +91 9650257467
- Email: arpitdara2003@gmail.com
