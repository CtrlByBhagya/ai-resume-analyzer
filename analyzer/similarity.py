from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def similarity_score(resume_text, job_text):
    """Return a similarity score between 0 and 1."""

    # .strip() removes leading and trailing whitespace.
    # 'not' checks whether the value is empty.
    if not resume_text.strip() or not job_text.strip():
        return 0.0

    documents = [resume_text, job_text]

    # creating an object of the Tfidfvectorizer class
    # a tool created which will convert text into TF-IDF values
    vectorizer = TfidfVectorizer()

    # fit_transform() performs two operations:
    # fit: learns the vocabulary and calculates IDF weights.
    # transform: converts both documents into numerical TF-IDF vectors.
    # handle cases where the documents contain no valid tokens.
    try:
        tfidf_matrix = vectorizer.fit_transform(documents)
    except ValueError:
        return 0.0

    # tfidf_matrix[0:1] selects the first document's vector (resume).
    # tfidf_matrix[1:2] selects the second document's vector (job description).
    # cosine_similarity() compares their numerical representation.
    # [0][0] extracts the actual similarity number from the returned 2D result
    score = cosine_similarity(tfidf_matrix[0:1],tfidf_matrix[1:2])[0][0]

    return float(score)
