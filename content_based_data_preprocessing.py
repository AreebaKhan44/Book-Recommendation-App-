
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

@st.cache_data
def load_data():
    """
    Load the merged dataset with book details and ratings.
    """
    try:
        merged_df = pd.read_csv('/content/drive/MyDrive/BRS/datasets/pre-processed-merged-data/merged_df.csv')
        return merged_df
    except FileNotFoundError:
        st.error("File not found. Please check the file path.")
        return pd.DataFrame()  # Return an empty DataFrame in case of error

def compute_tfidf_matrix(text_data):
    """
    Compute the TF-IDF matrix from the given text data.
    """
    tfidf_vectorizer = TfidfVectorizer(analyzer='word', ngram_range=(2, 2), min_df=1, stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(text_data)
    return tfidf_matrix, tfidf_vectorizer

def get_content_based_recommendations(query, merged_df, num_recommendations=5):
    """
    Recommend books based on a query using content-based filtering.
    """
    if merged_df.empty:
        st.warning("No data available for recommendations.")
        return pd.DataFrame()
    else:
        # Preprocess the books data
        # For now, using only title
        merged_df['combined_text'] = merged_df['Book-Title']

        # Compute the TF-IDF matrix
        tfidf_matrix, tfidf_vectorizer = compute_tfidf_matrix(merged_df['combined_text'])

        # Transform the query using the same vectorizer
        query_tfidf = tfidf_vectorizer.transform([query])

        # Compute cosine similarity
        cosine_sim = linear_kernel(query_tfidf, tfidf_matrix)

        # Get indices of the most similar books
        sim_scores = list(enumerate(cosine_sim[0]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the top 'num_recommendations' recommendations
        recommended_indices = [i[0] for i in sim_scores[:num_recommendations]]

        # Extract book details for recommendations
        recommendations = merged_df.iloc[recommended_indices]

        return recommendations[['Book-Title']]

# # Usage
# if __name__ == "__main__":
#     # Load books data
#     merged_df = load_data()

#     # Example query
#     query = 'The Testament'
#     recommended_books = get_content_based_recommendations(query, merged_df, num_recommendations=5)
#     print("Recommended Books:")
#     print(recommended_books)
