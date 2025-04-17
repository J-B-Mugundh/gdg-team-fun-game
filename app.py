import streamlit as st
import random
import google.generativeai as genai
from PIL import Image

# Configure Gemini API
genai.configure(api_key="AIzaSyAqPYE72UoSojB5KewKPYTpelAsYaoDIF8")
model = genai.GenerativeModel("gemini-2.0-flash")

# People list
people = [
    "Mugundh", "Vijai", "Thasneem", "Aishwariya", "Kavya", "Usha", "Saravana",
    "Shanmukha", "Kanishka", "Vijayadarshini", "Bharanidharan", "Maanasa", "Neelavathy",
    "Ravishankar", "Santhosh", "Badri", "Lokesh", "Sivaranjini", "Tamil Selvan", "Vignesh"
]

# App layout
st.set_page_config(page_title="GDG MIT Fun Time", layout="centered")

# Header image
st.image("GDG-Community-Page-banner.jpg", use_container_width=True)

# Title
st.markdown("<h2 style='text-align: center;'>🎉 GDG MIT - Fun Time 🎉</h2>", unsafe_allow_html=True)

if st.button("Pick Participants 🎲"):
    asker, answerer = random.sample(people, 2)
    st.success(f"🙋‍♂️ **{asker}** will ask the question!")
    st.info(f"🧍‍♀️ **{answerer}** will answer it!")

    # Ask Gemini for Truth/Dare suggestions
    prompt = """
    Give me a list of 5 fun "Truth" questions and 5 fun "Dare" challenges suitable for a casual college group game.
    Make sure they are light-hearted, creative, and not embarrassing or inappropriate.
    """

    response = model.generate_content(prompt)
    suggestions = response.text

    st.markdown("---")
    st.subheader("💡 Suggested Questions:")
    st.markdown(suggestions)

