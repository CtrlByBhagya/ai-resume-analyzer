
from pypdf import PdfReader
from docx import Document


def extract_text(file):
    """Extract text from an uploaded PDF or DOCX resume."""

    if file is None:
        return ""

    try:
        filename = file.filename.lower()

        # Extract text from PDF
        if filename.endswith(".pdf"):
            file.stream.seek(0)
            reader = PdfReader(file.stream)

            text = ""

            for page in reader.pages:
                text += (page.extract_text() or "") + "\n"

            return text.strip()

        # Extract text from DOCX
        elif filename.endswith(".docx"):
            file.stream.seek(0)
            document = Document(file.stream)

            text = ""

            # Extract paragraphs
            for paragraph in document.paragraphs:
                text += paragraph.text + "\n"

            # Extract tables
            for table in document.tables:
                for row in table.rows:
                    for cell in row.cells:
                        text += cell.text + "\n"

            return text.strip()

        # Unsupported file format
        else:
            return ""

    except Exception as e:
        print("Extraction Error:", e)
        return ""
