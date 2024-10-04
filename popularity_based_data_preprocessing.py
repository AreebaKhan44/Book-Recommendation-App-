
import streamlit as st
import pandas as pd

# Caching the data loading to improve performance
# To ensures that the caching mechanism aligns with the latest Streamlit API guidelines.
@st.cache_data  # used for caching data processing functions.
def load_data():
    """Load the merged dataset with book details and ratings."""
    merged_df = pd.read_csv('/content/drive/MyDrive/BRS/datasets/pre-processed-merged-data/merged_df.csv')
    return merged_df

def calculate_popularity(merged_df):
    """Calculate book popularity based on ratings."""
    # Group by 'ISBN' to calculate the mean rating and count of ratings
    book_popularity = merged_df.groupby('ISBN').agg({
        'Book-Rating': ['mean', 'count']
    })
    book_popularity.columns = ['average_rating', 'rating_count']
    return book_popularity

def merge_with_popularity(books, book_popularity):
    """Merge book data with popularity scores."""
    # Merge book details with popularity metrics, keeping only the unique book details
    books_with_popularity = books.drop_duplicates(subset='ISBN').merge(book_popularity, on='ISBN', how='left')
    books_with_popularity['popularity_score'] = books_with_popularity['rating_count'] * books_with_popularity['average_rating']
    return books_with_popularity

def get_popular_books(merged_df, top_n):
    """Get the top N most popular books."""
    # Calculate popularity
    book_popularity = calculate_popularity(merged_df)
    # Extract book details
    books = merged_df[['ISBN', 'Book-Title', 'Book-Author']]
    # Merge with book details
    books_with_popularity = merge_with_popularity(books, book_popularity)
    # Sort by popularity score and get top N books
    popular_books = books_with_popularity.sort_values(by='popularity_score', ascending=False).head(top_n)
    return popular_books

# Usage Get and display popular books
if __name__ == "__main__":
    # Load data
    merged_df = load_data()

    # Get top 5 popular books
    top_n = 5
    top_books = get_popular_books(merged_df, top_n)

    # Display the top books
    print(top_books[['Book-Title', 'Book-Author', 'average_rating', 'rating_count']])
