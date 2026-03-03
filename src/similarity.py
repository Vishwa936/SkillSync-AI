from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_text, job_description_text):
    """
    Calculates cosine similarity between resume and job description using TF-IDF.
    Returns similarity score (0-100).
    """

    documents = [resume_text, job_description_text]

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    score = float(similarity[0][0]) * 100

    return round(score, 2)