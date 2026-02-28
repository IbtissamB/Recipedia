# 🍳 Recipedia API
A professional, secure, and searchable Recipe Management API built with **Django** and **Django REST Framework**.

## 🚀 Features
- **User Authentication**: Secure registration and login with password hashing.
- **Recipe Management**: Full CRUD (Create, Read, Update, Delete) functionality.
- **Advanced Permissions**: Anyone can browse, but only the **Author** can edit or delete their own recipes.
- **Smart Search**: Search recipes by Title, Category, or Ingredients using keywords.
- **Powerful Filtering**: Refine results by Category name, Ingredient name, Cooking time, or Servings.
- **Data Validation**: Ensures all recipes include required fields and at least one ingredient.

---

## 🛠️ Tech Stack
- **Framework:** Django
- **API Toolkit:** Django REST Framework (DRF)
- **Database:** SQLite (Development)

---

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

