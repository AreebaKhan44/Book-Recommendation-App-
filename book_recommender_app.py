
import streamlit as st
import pandas as pd
import altair as alt
import joblib
from content_based_data_preprocessing import load_data, get_content_based_recommendations
from collaborative_based_data_preprocessing import get_collaborative_based_recommendations
from popularity_based_data_preprocessing import get_popular_books
from utils import set_background_image

# Title
st.title("📚Book Recommender System")

# Subtitle
st.subheader('Welcome to our book recommendation system! 📖✨')
st.write("This system provides personalized book recommendations based on your preferences.")

# Set the background image
image_url = 'https://www.lislelibrary.org/sites/default/files/assets/images/MyNextBook.jpg'
set_background_image(image_url)

# Dropdown to select filtering technique
technique = st.selectbox(
    'Select Filtering Technique',
    ['', 'Popularity-Based', 'Content-Based', 'Collaborative Filtering'],
    index=0  # Set the default selection to the empty string
)

# Load and preprocess data
merged_df = load_data()


# Show the "Recommend" button only after a technique is selected
if technique:
    top_n = st.slider("Number of Top Books to Show", min_value=1, max_value=50, value=5)

    # Input for the book title only if Content-Based is selected
    book_title = ""
    if technique == 'Content-Based':
        book_title = st.text_input("Enter a book title for content-based recommendations", "")

    if st.button('Recommend'):
        if technique == 'Popularity-Based':
            st.subheader("📊 Popularity-Based Recommendations")
            popular_books = get_popular_books(merged_df, top_n)
            if not popular_books.empty:
                # Display top books
                st.write("Top Books Based on Popularity:")
                st.dataframe(popular_books[['Book-Title', 'Book-Author', 'average_rating', 'rating_count']])

                # Optional: Visualize data with Altair
                chart = alt.Chart(popular_books.head(top_n)).mark_bar().encode(
                    x='Book-Title:N',
                    y='average_rating:Q',
                    tooltip=['Book-Title:N', 'average_rating:Q']
                ).properties(
                    title='Top Popular Books Chart'
                )
                st.altair_chart(chart, use_container_width=True)
            else:
                st.warning("No popular books available.")

        elif technique == 'Content-Based':
            st.subheader("🔍 Content-Based Recommendations")
            if book_title:
                recommended_books = get_content_based_recommendations(book_title, merged_df, num_recommendations=top_n)
                if not recommended_books.empty:
                    st.write(f"Top {top_n} Books Similar to '{book_title}':")
                    st.dataframe(recommended_books[['Book-Title']])
                else:
                    st.warning(f"No recommendations found for '{book_title}'.")
            else:
                st.warning("Please enter a book title for content-based recommendations.")

        elif technique == 'Collaborative Filtering':
            # Add text input for User ID
            user_id_input = st.text_input("Enter a User ID for recommendations")
            try:
                user_id = int(user_id_input)
                recommended_books = get_collaborative_based_recommendations(user_id, top_n)

                if not recommended_books.empty:
                    # Load merged_df to retrieve book details
                    recommended_books_details = merged_df[merged_df['ISBN'].isin(recommended_books.index)]

                    if not recommended_books_details.empty:
                        st.write(f"Top {top_n} Books Recommended for User ID {user_id}:")
                        st.dataframe(recommended_books_details[['Book-Title']])
                    else:
                        st.warning(f"No recommendations found for User ID {user_id}.")
                else:
                    st.warning("No recommendations could be generated.")
            except ValueError:
                st.warning("Please enter a valid numeric User ID.")

else:
    st.warning("Please select a filtering technique to proceed.")
