# Asiful Alam Sami — Django Portfolio

A clean personal portfolio website built with Django.

## Features

- Home / About section
- Tech stack
- Focus areas
- Project cards
- Contact and social links
- Responsive design
- Ready for deployment on Render, Railway, or any VPS

## Local Setup

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Edit Your Info

Most profile information is inside:

```text
portfolio/data.py
```

Update your real projects, links, and skills there.

## Deploy on Render

1. Push this folder to GitHub.
2. Create a new Web Service on Render.
3. Connect your GitHub repository.
4. Use:
   - Build command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - Start command: `gunicorn portfolio_project.wsgi`
5. Add environment variables:
   - `DEBUG=False`
   - `SECRET_KEY=your-secret-key`
