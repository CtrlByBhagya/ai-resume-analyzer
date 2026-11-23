from pathlib import Path
from flask import Flask, render_template, request
from analyzer import run_analysis

app = Flask(__name__)


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

    result = run_analysis(resume, job_description)

    return render_template("results.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
