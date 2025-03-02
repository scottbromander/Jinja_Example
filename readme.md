# FastAPI + Jinja2 Example

This is a simple FastAPI project that demonstrates **server-side rendering with Jinja2**, handling **form submissions**, and serving **static files (CSS)**. The app allows users to select different categories of fruits and dynamically updates the page content.

## 📌 Features

- 🌐 **FastAPI-powered web application**
- 🎨 **Jinja2 templates for dynamic HTML rendering**
- 📩 **Form handling using FastAPI**
- 🔥 **Lightweight and easy to extend**

---

## 🚀 Getting Started

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/fastapi-jinja-example.git
cd fastapi-jinja-example
```

### 2. Set Up a Virtual Environment

Create and activate a virtual environment:

Windows (Command Prompt)

```sh
python -m venv venv
venv\Scripts\activate
```

Mac/Linux (Terminal)

```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependancies

```sh
pip install fastapi uvicorn jinja2 python-multipart
```

### 4. Run the FastAPI Server

```sh
python server.py
```

## 🎨 How It Works

1. The homepage (/) displays a form and a default fruit list.
2. The user selects a fruit category from the dropdown.
3. When the form is submitted, FastAPI processes the request and re-renders the page dynamically.
4. Jinja2 is used for template rendering, and CSS styles the page.

## Project Structure

```
fastapi_project/
│-- venv/              # Virtual environment (ignored in Git)
│-- templates/         # HTML templates
│   ├── index.html     # Homepage basically
│-- static/            # Static files (CSS)
│   ├── styles.css     # Styling for the web app
│-- server.py          # FastAPI server
│-- .gitignore         # Ignore unnecessary files
│-- README.md          # Project documentation
```

## 🖥️ Usage

1. Visit http://127.0.0.1:8000/ in your browser.
2. Select a fruit category and click "Get Fruits".
3. The page updates dynamically using server-side rendering (SSR).

## 📌 Requirements

- Python 3.8+
- FastAPI, Jinja2, Uvicorn
- A web browser (Chrome, Firefox, etc.)
