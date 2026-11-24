from pathlib import Path
from flask import Flask, render_template, request
from analyzer import run_analysis

app = Flask(__name__)

app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():

    resume = request.files.get("resume")
    job_description = request.form.get("job_description","").strip()


    if resume is None or resume.filename =="":
        return render_template("index.html",error="Please upload a resume.")

    if Path(resume.filename).suffix.lower() not in {".pdf", ".docx"}:
        return render_template(
            "index.html",
            error="Only PDF or DOCX files are allowed."
        )

    if not job_description:
        error_message = "Please enter a job description."
        return render_template("index.html", error=error_message)

    # the analyzer processes the two passing arguments and returns a dictionary in result
    result = run_analysis(resume, job_description)

    # render_template() tells flask to:
    # 1. find the results.html inside the templates folder.
    # 2. pass the python variable result into that HTML template.
    # 3. render the template into an HTML response and send it to the browser.
    return render_template("results.html", result=result)

@app.errorhandler(413)
def file_too_large(error):
    return render_template(
        "index.html",
        error = "Your upload is too large. Please upload a file smaller than 5 MB"
    ) , 413


if __name__ == "__main__":
    app.run(debug=True)
