# Bookmarks

Bookmarks is a Django-based social website project focused on user accounts and profiles. Users can register, sign in, manage their account details, and access a personal dashboard. The project also has configuration for Google OAuth sign-in and stores profile photos and dates of birth.

## Features

- User registration with password confirmation and unique email validation
- Sign-in using a username or email address
- Authenticated user dashboard
- Account profile editing, including a profile photo and date of birth
- Django's built-in logout, password change, and password reset views
- Google OAuth 2.0 authentication support
- PostgreSQL database and user-uploaded media support

The Images and People navigation items are currently placeholders.

## Technology

- Python
- Django
- PostgreSQL
- Pillow for profile image handling
- `social-auth-app-django` for Google OAuth

Dependencies are listed in [`requirements.txt`](requirements.txt).

## Project layout

```text
bookmarks/              Django project and application
  manage.py             Django management entry point
  bookmarks/            Project settings and root URL configuration
  account/              Account, profile, authentication, and templates
requirements.txt        Python dependencies
```

## Requirements

- Python compatible with the Django version in `requirements.txt`
- PostgreSQL
- Google OAuth credentials if you want to enable Google sign-in

## Local setup

Run these commands from the repository root in PowerShell:

1. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install the project dependencies:

   ```powershell
   python -m pip install --upgrade pip
   pip install -r .\requirements.txt
   ```

3. Create a PostgreSQL database and a user with access to it. Then create a local `.env` file in the repository root with the following values:

   ```dotenv
   DB_NAME=your_database_name
   DB_USER=your_database_user
   DB_PASSWORD=your_database_password
   DB_HOST=localhost
   DB_PORT=5432
   GOOGLE_OAUTH2_KEY=your_google_oauth_client_id
   GOOGLE_OAUTH2_SECRET=your_google_oauth_client_secret
   ```

   The database settings are required to start the application. Google OAuth values are required when using the Google authentication backend. Create an OAuth 2.0 Web application in Google Cloud and add this authorized redirect URI:

   ```text
   http://localhost:8000/social-auth/complete/google-oauth2/
   ```

   Keep real credentials in your local `.env` file; do not commit secrets or OAuth client-secret files.

4. Apply database migrations and start the development server:

   ```powershell
   python .\bookmarks\manage.py migrate
   python .\bookmarks\manage.py runserver
   ```

5. Open <http://127.0.0.1:8000/account/> in your browser. You can register at <http://127.0.0.1:8000/account/register/>.

## Useful URLs

| URL | Description |
| --- | --- |
| `/account/` | Dashboard (sign-in required) |
| `/account/register/` | Create an account |
| `/account/login/` | Sign in |
| `/account/logout/` | Sign out |
| `/account/edit/` | Edit account and profile information (sign-in required) |
| `/account/password_change/` | Change password (sign-in required) |
| `/social-auth/` | Social authentication routes |
| `/admin/` | Django administration |

Password reset emails use Django's console email backend in the current settings, so reset messages are written to the development server's console rather than sent by an email provider.

## Tests and checks

From the repository root, run Django's tests and system checks with:

```powershell
python .\bookmarks\manage.py test
python .\bookmarks\manage.py check
```

## Production note

The included settings are for development, not production. Before deploying, configure a secret key through a secure environment variable, turn off `DEBUG`, set appropriate allowed hosts and HTTPS/security settings, and configure production email and media storage.
