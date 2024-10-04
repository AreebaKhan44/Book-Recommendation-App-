
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.decomposition import TruncatedSVD
import numpy as np
import joblib
import os

# Function to get collaborative-based recommendations
def get_collaborative_based_recommendations(user_id, top_n=5):
    # Load preprocessed data
    utility_matrix = joblib.load('/content/drive/MyDrive/BRS/App/pkl/utility_matrix.pkl')
    predicted_df = joblib.load('/content/drive/MyDrive/BRS/App/pkl/predicted_df.pkl')

    # Get the predicted ratings for the user
    user_ratings = predicted_df.loc[user_id]

    # Filter out books already rated by the user
    known_ratings = utility_matrix.loc[user_id]
    unrated_books = user_ratings[known_ratings == 0]

    # Sort and recommend the top N books
    recommendations = unrated_books.sort_values(ascending=False).head(top_n)

    return recommendations

# Usage
# Recommend books for a specific user_id
user_id = 277427  # Example User ID
top_n = 5  # Number of top recommendations
recommended_books = get_collaborative_based_recommendations(user_id, top_n)
print(f"Recommended books for user {user_id}:\n{recommended_books}")
