from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .models import Project, Todo
from . import db

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))
    return render_template("index.html")

@main_bp.route("/dashboard")
@login_required
def dashboard():
    projects = Project.query.filter_by(user_id=current_user.id).all()
    simple_tasks = (
        Todo.query.filter_by(user_id=current_user.id, project_id=None)
        .order_by(Todo.due_date.asc().nulls_last(), Todo.due_time.asc().nulls_last(), Todo.id)
        .all()
    )
    return render_template("dashboard.html", projects=projects, tasks=simple_tasks)

@main_bp.route("/project/<int:project_id>")
@login_required
def view_project(project_id):
    project = Project.query.filter_by(id=project_id, user_id=current_user.id).first_or_404()
    return render_template("project.html", project=project)

@main_bp.route("/project/add", methods=["POST"])
@login_required
def add_project():
    name = request.form.get("name", "").strip()
    if not name:
        flash("Project name required.", "danger")
        return redirect(url_for("main.dashboard"))
    p = Project(name=name, user_id=current_user.id)
    db.session.add(p)
    db.session.commit()
    flash("Project created.", "success")
    return redirect(url_for("main.dashboard"))

@main_bp.route("/project/<int:project_id>/delete", methods=["POST"])
@login_required
def delete_project(project_id):
    project = Project.query.filter_by(id=project_id, user_id=current_user.id).first_or_404()
    db.session.delete(project)
    db.session.commit()
    flash("Project deleted.", "info")
    return redirect(url_for("main.dashboard"))

def _parse_date_time(form):
    date_str = form.get("date") or None
    time_str = form.get("time") or None
    due_date = datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else None
    due_time = datetime.strptime(time_str, "%H:%M").time() if time_str else None
    return due_date, due_time

@main_bp.route("/task/add", methods=["POST"])
@login_required
def add_task():
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    project_id = request.form.get("project_id")
    project_id = int(project_id) if project_id else None
    due_date, due_time = _parse_date_time(request.form)
    if not title:
        flash("Title is required.", "danger")
        return redirect(request.referrer or url_for("main.dashboard"))
    if project_id is not None:
        Project.query.filter_by(id=project_id, user_id=current_user.id).first_or_404()
    todo = Todo(
        title=title,
        description=description,
        user_id=current_user.id,
        project_id=project_id,
        due_date=due_date,
        due_time=due_time,
    )
    db.session.add(todo)
    db.session.commit()
    flash("Task added.", "success")
    return redirect(request.referrer or url_for("main.dashboard"))

@main_bp.route("/task/<int:task_id>/toggle", methods=["POST"])
@login_required
def toggle_task(task_id):
    todo = Todo.query.filter_by(id=task_id, user_id=current_user.id).first_or_404()
    todo.completed = not todo.completed
    db.session.commit()
    flash("Updated.", "success")
    return redirect(request.referrer or url_for("main.dashboard"))

@main_bp.route("/task/<int:task_id>/delete", methods=["POST"])
@login_required
def delete_task(task_id):
    todo = Todo.query.filter_by(id=task_id, user_id=current_user.id).first_or_404()
    pid = todo.project_id
    db.session.delete(todo)
    db.session.commit()
    flash("Deleted.", "info")
    if pid:
        return redirect(url_for("main.view_project", project_id=pid))
    return redirect(request.referrer or url_for("main.dashboard"))

@main_bp.route("/task/<int:task_id>/edit", methods=["GET", "POST"])
@login_required
def edit_task(task_id):
    todo = Todo.query.filter_by(id=task_id, user_id=current_user.id).first_or_404()
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        due_date, due_time = _parse_date_time(request.form)
        if not title:
            flash("Title is required.", "danger")
            return redirect(url_for("main.edit_task", task_id=task_id))
        todo.title = title
        todo.description = description
        todo.due_date = due_date
        todo.due_time = due_time
        db.session.commit()
        flash("Task updated.", "success")
        return redirect(url_for("main.view_project", project_id=todo.project_id) if todo.project_id else url_for("main.dashboard"))
    return render_template("edit_task.html", todo=todo)
