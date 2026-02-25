import os
import uuid
from flask import (
    Blueprint,
    render_template,
    request,
    session,
    current_app
)
from werkzeug.utils import secure_filename

from app.utils.image_handler import process_image
from app.utils.celebrity_detector import CelebrityDetector
from app.utils.qa_engine import QAEngine

main = Blueprint("main", __name__)

celebrity_detector = CelebrityDetector()
qa_engine = QAEngine()


# Allowed image extensions
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@main.route("/", methods=["GET", "POST"])
def index():

    celebrity_info = session.get("celebrity_info", {})
    image_filename = session.get("image_filename", "")
    answer = ""

    if request.method == "POST":

        if "image" in request.files:

            image_file = request.files["image"]

            if image_file and allowed_file(image_file.filename):

                try:
                    # Process image (face detection etc.)
                    img_bytes, face_box = process_image(image_file)

                    if face_box is None:
                        session.clear()
                        return render_template(
                            "index.html",
                            celebrity_info={"full_name": "No face detected"},
                            image_filename="",
                            answer=""
                        )

                    # Create upload folder if not exists
                    upload_folder = os.path.join(
                        current_app.root_path,
                        "static",
                        "uploads"
                    )
                    os.makedirs(upload_folder, exist_ok=True)

                    # Generate secure unique filename
                    filename = secure_filename(f"{uuid.uuid4().hex}.jpg")
                    file_path = os.path.join(upload_folder, filename)

                    # Save image
                    with open(file_path, "wb") as f:
                        f.write(img_bytes)

                    # Identify celebrity
                    celebrity_info, celebrity_name = celebrity_detector.identify(img_bytes)

                    # Store ONLY small data in session
                    session["celebrity_info"] = celebrity_info
                    session["celebrity_name"] = celebrity_name
                    session["image_filename"] = filename

                    image_filename = filename

                except Exception:
                    session.clear()
                    return render_template(
                        "index.html",
                        celebrity_info={"full_name": "Error processing image"},
                        image_filename="",
                        answer=""
                    )

        elif "question" in request.form:

            user_question = request.form.get("question")
            celebrity_name = session.get("celebrity_name")

            if not celebrity_name:
                answer = "Please detect a celebrity first."
            else:
                answer = qa_engine.ask_about_celebrity(
                    celebrity_name,
                    user_question
                )

    return render_template(
        "index.html",
        celebrity_info=celebrity_info,
        image_filename=image_filename,
        answer=answer
    )