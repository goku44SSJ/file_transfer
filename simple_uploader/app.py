from flask import Flask, request, render_template_string, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

HTML_PAGE = """
<!doctype html>
<html>
  <head>
    <title>Simple File Upload</title>
    <style>
      body { font-family: sans-serif; text-align: center; padding: 50px; background: #f5f5f5; }
      input[type=file] { margin: 20px; }
      button { padding: 10px 20px; font-size: 16px; cursor: pointer; }
      a { text-decoration: none; color: blue; }
    </style>
  </head>
  <body>
    <h2>Upload a File</h2>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="file" required>
      <br>
      <button type="submit">Upload</button>
    </form>
    <p>{{ message }}</p>
    <hr>
    <h3>Uploaded Files</h3>
    {% if files %}
      <ul style="list-style:none;">
        {% for f in files %}
          <li><a href="/uploads/{{ f }}" target="_blank">{{ f }}</a></li>
        {% endfor %}
      </ul>
    {% else %}
      <p>No files uploaded yet.</p>
    {% endif %}
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def upload_file():
    message = ""
    if request.method == "POST":
        file = request.files.get("file")
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            message = f"✅ Uploaded: {file.filename}"
    files = os.listdir(UPLOAD_FOLDER)
    return render_template_string(HTML_PAGE, message=message, files=files)

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
