import json

from datetime import datetime
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import User, Note
from . import db
from bson.objectid import ObjectId

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        note = request.form.get("note")

        if(len(note) < 1):
            flash("Note is too short!", category="error")
        else:
            new_note = Note(_id=None, user_id=current_user.get_id(), date=datetime.now(), data=note)
            db.notes.insert_one(new_note.conv_to_dict())

            flash(f"Note Added!", category="success")

    notes_cursor = db.notes.find({"user_id": current_user.get_id()})
    notes = []

    for note in notes_cursor:
        note["_id"] = str(note["_id"])
        notes.append(note)

    return render_template("home.html", user=current_user, notes=notes)

@views.route("/delete-note", methods=["POST"])
@login_required
def delete_note():
    data = json.loads(request.data)
    note_id = ObjectId(data["note_id"])
    note = db.notes.find_one(filter={"_id" : note_id})

    if note is not None:
        note = Note.conv_to_obj(note)
        if str(note.user_id) == str(current_user.get_id()):
            db.notes.delete_one({"_id": note_id})
    
    return jsonify({})