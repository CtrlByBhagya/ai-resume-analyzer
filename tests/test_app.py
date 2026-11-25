import io # io module provides tools for working with input and output
from app import app # imports the flask application object from projects's app.py

def post(data):  # .post sends an HTTP POST request
    return app.test_client().post(  # creates a simulated browser client
        "/analyze",  # the route we are testing
        data=data,   # sends the form information
        content_type="multipart/form-data"  # multipart/form-data is the content type used when submitting forms containing file uploads.
    )

def test_empty_form_shows_error():

    #  response stores the response returned by our flask application
    response = post({"job_description": "x"})  # simulating a user submitting the form with a job description but without uploading a resume.

    assert b"Please upload a resume." in response.data  # b prefix creates bytes literal and is used so because flask's response data is stored as bytes not a regular python string.


def test_wrong_file_type_shows_error():  # tests an unsupported file
    response = post({
        "resume": (io.BytesIO(b"x"), "resume.exe"),
        "job_description": "python"
    })

    assert b"Only PDF or DOCX" in response.data # response.data contains HTML response sent back by flask.

def test_valid_upload_reaches_results(): # tests a valid upload request
    response = post({
        "resume": (io.BytesIO(b"x"), "resume.pdf"), # io.BytesIO(b"x") creates a fake file memory and resume.pdf gives uploaded file an allowed extension,so it passes the extension validation.
        "job_description": "python"
    })

    assert response.status_code == 200 # http status code 200 means the request was succesfully processed.