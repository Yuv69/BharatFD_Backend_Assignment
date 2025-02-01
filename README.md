# FAQ App for BharatFD

A Django-based FAQ (Frequently Asked Questions) application for managing and displaying common questions and answers effectively.

## 🚀 Features

- Add, edit, and delete FAQs via the admin panel
- Display FAQs dynamically on the frontend
- Simple, clean, and responsive design

---

## 📦 Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/bharatfd.git
cd bharatfd
```

### 2. Create a Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Linux/Mac
env\Scripts\activate   # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser
```bash
python manage.py createsuperuser
```

### 6. Run the Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/faq/` to see the FAQ app in action.

---

## 📡 API Usage Examples

### 1. Get All FAQs
**Endpoint:** `GET /faq/`

**Response:**
```json
[
  {
    "id": 1,
    "question": "What is BharatFD?",
    "answer": "BharatFD is a platform for ..."
  },
  {
    "id": 2,
    "question": "How to use the FAQ app?",
    "answer": "Simply navigate to the FAQ section ..."
  }
]
```

### 2. Admin Panel
- Access: `http://127.0.0.1:8000/admin/`
- Use your superuser credentials to manage FAQs.

---

## 🤝 Contribution Guidelines

1. **Fork the repository** and create your branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. **Make your changes** and commit:
   ```bash
   git add .
   git commit -m "feat: Add new FAQ feature"
   ```
3. **Push your branch** to GitHub:
   ```bash
   git push origin feature/your-feature-name
   ```
4. **Open a Pull Request** and describe your changes.

### 📝 Commit Message Convention
- `feat:` Add new feature
- `fix:` Bug fixes
- `docs:` Documentation changes
- `refactor:` Code refactoring without changing functionality
- `test:` Adding or updating tests

Example:
```bash
git commit -m "feat: Add multilingual FAQ model"
git commit -m "fix: Improve translation caching"
git commit -m "docs: Update README with API examples"
```

---

## 🗂️ Folder Structure
```
├── bharatfd
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── faq
│   ├── migrations/
│   ├── templates/faq/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── manage.py
└── README.md
```

---



