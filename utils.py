import streamlit  as st

# st.image(image_path, use_column_width=True)
def set_background_image(image_url):
    """
    Set the background image of the Streamlit app with a blur effect,
    and style the content for enhanced readability with a semi-transparent overlay behind the text.
    """
    st.markdown(
        f"""
        <style>
        /* Apply styles to the whole app */
        .stApp {{
            position: relative;
            overflow: hidden;
            height: 100vh;
            margin: 0;
            padding: 0;
            background: transparent; /* Ensure no background color interferes */
        }}

        /* Create a full-screen blurred background */
        .stApp::before {{
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            filter: blur(2px); /* Apply blur effect */
            z-index: -1; /* Ensure the background is behind other elements */
        }}

        /* Style titles, subheadings, and text */
        h1, h2, h3 {{
              background-color: rgba(255, 165, 0, 0.5); /* Semi-transparent orange background */
              padding: 10px 20px; /* Add padding around the text */
              border-radius: 10px; /* Rounded corners for a smoother look */
              color: #FFFFFF; /* White text color for high contrast */
              display: inline-block; /* Shrink to fit the text content */
              font-family: 'Georgia', serif; /* Apply Georgia font */
              font-weight: bold; /* Bold text for titles */
              text-align: center; /* Center-align the text */
              margin: 20px 0; /* Add vertical space between titles */
              text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7); /* Add text shadow for better readability */
              position: relative; /* Prevent overflow */
              z-index: 1; /* Ensure proper layering */
              white-space: nowrap; /* Prevent text from wrapping and expanding the background */
          }}

        p {{
            color: #FFFFFF; /* Set paragraph and label text color to white */
            font-size: 16px; /* Increase the font size for better readability */
            background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent background for text */
            padding: 5px 15px; /* Add some padding */
            border-radius: 8px; /* Add rounded corners */
            display: inline-block; /* Shrink to fit the text content */
            position: relative; /* Prevent overflow */
            z-index: 1; /* Ensure proper layering */

        }}

        /* Make sure surrounding containers have transparent backgrounds */
        .stContainer {{
              background-color: transparent !important; /* Remove any container background */
              padding: 0 !important; /* Remove unnecessary padding */
              margin: 0 !important; /* Remove unnecessary margins */

          }}

        /* Fix for button backgrounds */
        .stButton>button {{
            background-color: #4CAF50; /* Green background */
            display: inline-block; /* Shrink to fit the text content */
            color: white; /* White text */
            font-size: 18px; /* Increase font size */
            padding: 10px 24px; /* Add padding */
            border-radius: 8px; /* Rounded corners */
            border: none; /* Remove border */
        }}

        /* Style selectbox (dropdown) */
        .stSelectbox, .stMultiSelect {{
            z-index: 1; /* Ensure selectbox appears above the background */
            background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent background */
            display: inline-block; /* Shrink to fit the text content */
            border-radius: 8px; /* Rounded corners */
            color: #FFFFFF; /* White text color */
        }}

        /* Style slider */
        .stSlider {{
            background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent background for slider text */
            padding: 5px 10px; /* Padding for text readability */
            border-radius: 8px; /* Rounded corners */
            font-size: 16px; /* Adjust font size */
            font-weight: bold; /* Bold text */
            position: relative; /* Prevent overflow */
            z-index: 1; /* Ensure slider appears above the background */
            color: #FFFFFF; /* White text on sliders */
            max-width: 100%; /* Ensure the text doesn't overflow the slider container */
            white-space: normal; /* Allow text wrapping within the slider */
            word-wrap: break-word; /* Break words if too long */
        }}

        </style>
        """,
        unsafe_allow_html=True
    )
