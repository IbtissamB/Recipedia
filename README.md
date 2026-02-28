# 🍳 Recipedia API
A professional, secure, and searchable Recipe Management API built with **Django** and **Django REST Framework**.

## 🚀 Features
- **User Authentication**: Secure registration and login with password hashing.
- **Recipe Management**: Full CRUD (Create, Read, Update, Delete) functionality.
- **Advanced Permissions**: Anyone can browse, but only the **Author** can edit or delete their own recipes.
- **Smart Search**: Search recipes by Title, Category, or Ingredients using keywords.
- **Powerful Filtering**: Refine results by Category name, Ingredient name, Cooking time, or Servings.
- **Data Validation**: Ensures all recipes include required fields and at least one ingredient.

</br>

## 🛠️ Tech Stack
- **Framework:** Django
- **API Toolkit:** Django REST Framework (DRF)
- **Database:** SQLite (Development)

</br>

## 📥 Installation & Setup

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

5. Start the server:
    ```bash
    python manage.py runserver
    ```
    Visit the API at http://127.0.0.1:8000/api/recipes/

</br>

## 🛣️ API Endpoints

### 👤 Users
| Method | Endpoint                  | Description            |
|--------|---------------------------|------------------------|
| POST   | `/api/users/register/`    | Create a new account   |


### 📖 Recipes
| Method | Endpoint              | Description                                |
|--------|-----------------------|--------------------------------------------|
| GET    | `/api/recipes/`        | List all recipes (Search & Filter enabled) |
| POST   | `/api/recipes/`        | Create a new recipe (Login required)       |
| GET    | `/api/recipes/<id>`    | View details of a specific recipe          |
| PUT    | `/api/recipes/<id>`    | Edit a recipe (Author only)                |
| DELETE | `/api/recipes/<id>`    | Delete a recipe (Author only)              |

### 📁 Categories
| Method | Endpoint              | Description                   |
|--------|-----------------------|-------------------------------|
| GET    | `/api/categories/`    | List all available categories |


</br>

## 🔍 Search & Filter Examples
- Search by keyword: ?search=pasta

- Filter by Category Name: ?category__name=Italian

- Filter by Ingredient: ?ingredients__name=chicken

- Filter by Cook Time (Max 30 mins): ?cook_time__lte=30

- Sort by Prep Time: ?ordering=prep_time

</br>

## 🛡️ Validation & Security
- Author Lock: The IsAuthorOrReadOnly custom permission ensures data integrity.

- Field Validation: Recipes cannot be saved without a Title, Instructions, or at least one Ingredient.