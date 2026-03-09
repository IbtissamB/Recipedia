# 🍳 Recipedia API
A professional, secure and searchable Recipe Management API built with **Django** and **Django REST Framework**. Recipedia provides complete functionality for viewing and searching recipes, filtering and ordering by fields with proper authentication and authorization.

## Live Demo
**Base URL**: `https://ibtissamb.pythonanywhere.com/api/recipes/`

## Features

**Recipe Management**
- Full CRUD (Create, Read, Update, Delete) functionality.
- Search recipes by Title, Category or Ingredients using keywords.
- Refine results by Category name, Ingredient name, Cooking time or Servings.
- Filtered recipes can be ordered by ascending or descending order of cooking time or preparation time.

**User Authentication**
- User registration and login
- JWT-based authentication
- Role-based permissions (Admin vs Member)

**Data Validation**
- Two users with the same username cannot exist.
- Anyone can browse, but only the **Author** can edit or delete their own recipes.
- Ensures all recipes include required fields and at least one ingredient.

</br>

## Tech Stack
- **Framework:** Django 6.0
- **API Toolkit:** Django REST Framework (DRF) 3.16
- **Database:** SQLite (Development)
- **Authentication:** JWT (djangorestframework-simplejwt)
- **Deployment:** PythonAnywhere

</br>

## Installation & Setup

### Prerequisites
- Python 3.10+
- pip package manager
- virtualenv (recommended)

### Local Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/IbtissamB/Recipedia.git
   cd Recipedia
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run Migrations:
    ```bash
    python manage.py migrate
    ```

5. Create superuser
    ```bash
    python manage.py createsuperuser
    ```

6. Start the server:
    ```bash
    python manage.py runserver
    ```

7. Access the application
    API: http://127.0.0.1:8000/api/recipes/
    Admin Panel: http://127.0.0.1:8000/admin/

</br>

## Project Structure
``` text
Recipedia/
│
├── config/                 # Project configuration (settings, URLs, WSGI/ASGI)
│   ├── __init__.py
│   ├── asgi.py             # ASGI entry point
│   ├── settings.py         # Global project settings
│   ├── urls.py             # Root URL routing
│   ├── wsgi.py             # WSGI entry point
│   └── __pycache__/        # Compiled Python cache
│
├── recipes/                # Recipes app (core business logic)
│   ├── __init__.py
│   ├── admin.py            # Admin panel configuration
│   ├── apps.py             # App configuration
│   ├── models.py           # Database models (Recipe, Category, etc.)
│   ├── permissions.py      # Custom permission classes
│   ├── serializers.py      # DRF serializers
│   ├── tests.py            # Unit tests
│   ├── urls.py             # App-specific URL routing
│   ├── views.py            # API views
│   ├── __pycache__/        # Compiled Python cache
│   └── migrations/         # Database migration files
│       ├── __init__.py
│       ├── 0001_initial.py
│       ├── 0002_alter_recipe_options.py
│       └── __pycache__/
│
├── users/                  # Users app (authentication & profiles)
│   ├── __init__.py
│   ├── admin.py            # Admin panel configuration
│   ├── apps.py             # App configuration
│   ├── models.py           # User model 
│   ├── serializers.py      # DRF serializers for users
│   ├── tests.py            # Unit tests
│   ├── urls.py             # App-specific URL routing
│   ├── views.py            # API views (register, profile, etc.)
│   ├── __pycache__/        # Compiled Python cache
│   └── migrations/         # Database migration files
│       ├── __init__.py
│       └── __pycache__/
│
├── db.sqlite3              # Default SQLite database
├── manage.py               # Django project management script
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```
<br>

## Database Schema
```python
# Recipe Model
class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    instructions = models.TextField()
    prep_time = models.IntegerField(help_text="Time in minutes")
    cook_time = models.IntegerField(help_text="Time in minutes")
    servings = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)

# Ingredient Model
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
```
<br>

## API Endpoints

### Authentication Endpoints

| Method | Endpoint                     | Description                                   | Access  |
|--------|------------------------------|-----------------------------------------------|---------|
| POST   | `/api/users/login/`          | Exchange credentials for Access & Refresh tokens | Public  |
| POST   | `/api/users/login/refresh/`  | Use Refresh token to get a new Access token     | Public  |

## Recipes Endpoints

| Method | Endpoint             | Description                                      | Access       |
|--------|----------------------|--------------------------------------------------|--------------|
| GET    | `/api/recipes/`      | List all recipes (Supports search/filter/order)  | Public       |
| POST   | `/api/recipes/`      | Create a new recipe                              | Authenticated|
| GET    | `/api/recipes/<id>/` | View full details of a single recipe             | Public       |
| PUT/PATCH | `/api/recipes/<id>/` | Update an existing recipe                     | Author Only  |
| DELETE | `/api/recipes/<id>/` | Remove a recipe from the database                | Author Only  |       |

## Categories Endpoints

| Method | Endpoint                        | Description                          | Access        |
|--------|---------------------------------|--------------------------------------|---------------|
| GET    | `/api/recipes/categories/`      | List all available categories        | Public        |
| POST   | `/api/recipes/categories/`      | Add a new category                   | Authenticated |
| GET    | `/api/recipes/categories/<id>/` | View a specific category's details   | Public        |
| DELETE | `/api/recipes/categories/<id>/` | Delete a category                    | Admin/Author  |

## User Management Endpoints

| Method | Endpoint              | Description                          | Access        |
|--------|-----------------------|--------------------------------------|---------------|
| POST   | `/api/users/register/`| Create a new user account            | Public        |
| GET    | `/api/users/profile/` | View details of the logged-in user   | Authenticated |

<br>

## What do the Endpoints do?
- **Authentication**: These endpoints are used to manage your JSON Web Tokens (JWT).
- **Recipes**: The core of your application where users interact with the recipe database.
- **Categories**: Used to group recipes (e.g., Breakfast, Dessert, Indian).
- **Ingredients**: The building blocks used in the many-to-many relationship with recipes.
- **User Management**: Endpoints related to account creation and user profiles.


## Search & Filter Examples
- Search by keyword: ?search=pasta
- Filter by Category Name: ?category__name=Italian
- Filter by Ingredient: ?ingredients__name=chicken
- Filter by Cook Time (Max 30 mins): ?cook_time__lte=30
- Sort by Prep Time: ?ordering=prep_time

## Validation & Security
- Author Lock: The IsAuthorOrReadOnly custom permission ensures data integrity and prevents "Recipe Sabotage."
    - A normal user can see (GET) every recipe.
    - A normal user can delete (DELETE) only their own recipes.
    - A Superuser can usually delete anything via the Django Admin panel.
- Field Validation: Recipes cannot be saved without a Title, Instructions, or at least one Ingredient.

<br>

## Common Error Examples in Recipedia

**Example of a 400 Bad Request (Missing Field):**
``` json
{
    "title": ["This field is required."],
    "category": ["Invalid pk \"99\" - object does not exist."]
}
```
**Example of a 403 Forbidden (Permission Error):**
```json
{
    "detail": "You do not have permission to perform this action."
}
```

</br>

## Recipedia API: Expected Responses

Standard HTTP status codes and what they mean for your project.

| Status Code | Label              | What it means for your project                          | Example Scenario                                                                 |
|-------------|--------------------|----------------------------------------------------------|---------------------------------------------------------------------------------|
| 200         | OK                 | Success — Data retrieved or updated successfully.        | Sending a GET to `/api/recipes/` or a PATCH to your own recipe.                 |
| 201         | Created            | Success — A new entry was added to the database.         | Sending a POST to `/api/recipes/` with valid title, category, and ingredients.  |
| 204         | No Content         | Success — Deletion was successful.                       | Sending a DELETE to `/api/recipes/5/` while logged in as the author.            |
| 400         | Bad Request        | Data Error — The JSON you sent is missing or malformed.  | Sending a recipe without a title or using a non-existent category ID.           |
| 401         | Unauthorized       | Auth Error — Your JWT token is missing or expired.       | Trying to add an ingredient without pasting your token into the Bearer field.   |
| 403         | Forbidden          | Security Block — You aren't the author of this recipe.   | Logged in as `ibtissam` but trying to DELETE a recipe created by `Health_Guru`. |
| 404         | Not Found          | URL Error — That recipe ID or endpoint doesn't exist.    | Trying to GET a recipe at `/api/recipes/999/` that hasn't been created.         |
| 405         | Method Not Allowed | Action Error — Wrong HTTP method for the endpoint.       | Trying to POST a new recipe to `/api/recipes/1/` (IDs only accept GET/PUT/DELETE). |

<br>

## Troubleshooting

If you encounter issues while testing the API, check these common solutions:

### 1. Token Errors (`401 Unauthorized` / `token_not_valid`)
* **Problem:** Your access token has expired (default is 5 minutes).
* **Fix:** Use the `/api/users/login/refresh/` endpoint to get a new access token using your refresh token, or simply log in again.
* **Note:** Ensure the header in Postman is set to `Authorization: Bearer <your_token>`.

### 2. Permission Denied (`403 Forbidden`)
* **Problem:** You are trying to Edit (`PUT/PATCH`) or Delete a recipe you didn't create.
* **Fix:** Check the `author` field of the recipe. You must be logged in as that specific user to modify it.

### 3. Database Errors (`no such table`)
* **Problem:** You've added new features (like Categories) but the database hasn't updated.
* **Fix:** Run `python manage.py makemigrations` and `python manage.py migrate` in your terminal.

### 4. Slash Issues (`404 Not Found`)
* **Problem:** Django is strict about trailing slashes.
* **Fix:** Ensure your URL ends with a `/`. (e.g., use `/api/recipes/` instead of `/api/recipes`).