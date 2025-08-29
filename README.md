<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>To-Do App using Flask</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; margin: 20px;">

  <h1>📝 To-Do App using Flask</h1>
  <p>
    A simple and efficient <strong>To-Do List Web Application</strong> built with <strong>Flask</strong>.<br>
    This app allows users to <strong>register, log in, and manage their tasks</strong> in an intuitive interface.
  </p>

  <p><strong>🌐 Live Demo:</strong> <a href="https://to-do-app-using-flask.onrender.com" target="_blank">
    https://to-do-app-using-flask.onrender.com
  </a></p>

  <hr>

  <h2>🚀 Features</h2>
  <ul>
    <li>🔐 User Authentication (Register/Login/Logout)</li>
    <li>📝 Create, Update, and Delete tasks</li>
    <li>✅ Mark tasks as completed</li>
    <li>💾 Persistent storage with <strong>SQLite + SQLAlchemy</strong></li>
    <li>🎨 Simple UI for easy task management</li>
    <li>🌐 Ready for deployment with <strong>Gunicorn + WSGI</strong></li>
  </ul>

  <h2>🛠️ Tech Stack</h2>
  <ul>
    <li><strong>Backend:</strong> Flask, Flask-Login, Flask-SQLAlchemy</li>
    <li><strong>Database:</strong> SQLite (default, can be changed)</li>
    <li><strong>Frontend:</strong> HTML, CSS (Jinja2 templates)</li>
    <li><strong>Deployment:</strong> Gunicorn, WSGI</li>
  </ul>

  <h2>📂 Project Structure</h2>
  <pre>
.
├── app/                  # Main application package
│   ├── __init__.py       # App factory
│   ├── models.py         # Database models
│   ├── routes.py         # Application routes
│   ├── templates/        # HTML templates
│   └── static/           # Static files (CSS, JS)
├── requirements.txt      # Dependencies
├── wsgi.py               # WSGI entry point
└── README.md             # Project documentation
  </pre>

  <h2>⚙️ Installation & Setup</h2>
  <h3>1️⃣ Clone the repository</h3>
  <pre><code>git clone https://github.com/yourusername/todo-flask-app.git
cd todo-flask-app</code></pre>

  <h3>2️⃣ Create & activate virtual environment</h3>
  <pre><code>python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows</code></pre>

  <h3>3️⃣ Install dependencies</h3>
  <pre><code>pip install -r requirements.txt</code></pre>

  <h3>4️⃣ Set up environment variables</h3>
  <p>Create a <strong>.env</strong> file in the project root and add:</p>
  <pre><code>SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///todo.db</code></pre>

  <h3>5️⃣ Run the application</h3>
  <pre><code>flask run</code></pre>
  <p>App will be available at 👉 <a href="http://127.0.0.1:5000">http://127.0.0.1:5000</a></p>

  <h2>🚀 Deployment (Gunicorn + WSGI)</h2>
  <pre><code>gunicorn --bind 0.0.0.0:8000 wsgi:app</code></pre>

  <h2>📌 Requirements</h2>
  <pre><code>Flask==3.0.3
Flask-Login==0.6.3
Flask-SQLAlchemy==3.1.1
python-dotenv==1.0.1
Werkzeug==3.0.3
gunicorn==22.0.0</code></pre>

  <h2>🤝 Contributing</h2>
  <p>Pull requests are welcome!<br>
  If you’d like to contribute, please fork the repo and submit a PR.</p>

  <h2>📜 License</h2>
  <p>This project is licensed under the <strong>MIT License</strong>.</p>

  <hr>
  <p>💡 <em>Happy Coding! Build your productivity with this To-Do app.</em></p>

</body>
</html>
