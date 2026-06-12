import os
from datetime import datetime
from uuid import uuid4

from flask import Flask, jsonify, request, send_from_directory, render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = Flask(__name__)
CORS(app)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    #return jsonify({"status": "ok", "message": "backend is running"})
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_photo():
    if "photo" not in request.files:
        return jsonify({"error": "photo file is required"}), 400

    file = request.files["photo"]
    if file.filename == "":
        return jsonify({"error": "filename is empty"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "unsupported file type"}), 400

    original_name = secure_filename(file.filename)
    ext = original_name.rsplit(".", 1)[1].lower()
    saved_name = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid4().hex[:8]}.{ext}"
    save_path = os.path.join(UPLOAD_DIR, saved_name)
    file.save(save_path)

    recorded_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    base_url = request.host_url.rstrip("/")

    return jsonify(
        {
            "message": "撮影した写真はこちらです",
            "datetime": recorded_at,
            "image_url": f"{base_url}/uploads/{saved_name}",
            "filename": saved_name,
        }
    )


@app.route("/uploads/<path:filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_DIR, filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
