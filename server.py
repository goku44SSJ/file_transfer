from flask import Flask, request, render_template_string
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
      body { font-family: sans-serif; padding: 50px; text-align: center; background: #f4f4f4; }
      input[type=file] { margin: 20px; }
      button { padding: 10px 20px; font-size: 16px; }
    </style>
  </head>
  <body>
    <h2>Upload a File to Laptop</h2>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="file" required>
      <br>
      <button type="submit">Upload</button>
    </form>
    <p>{{ message }}</p>
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
            message = f"✅ File '{file.filename}' uploaded successfully!"
    return render_template_string(HTML_PAGE, message=message)

if __name__ == "__main__":
    app.run(port=5000)
