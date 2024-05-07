import streamlit as st
import os

# Function to check if the app has already been run
def check_run_flag():
    if os.path.isfile("streamlit_run_flag.txt"):
        return False
    else:
        with open("streamlit_run_flag.txt", "w") as file:
            file.write("App has been run once.")
        return False

def main():
    if check_run_flag():
        st.write("The application has already been run once. You cannot run it again.")
        return

    st.title('Career Assessment')
    st.write("Please fill this form carefully and precisely because this data will be used for career analysis.")

    full_name = st.text_input('Full Name')

    major_options = ('Engineering (هندسة)', 'Medical (طب)', 'Computer Science (حاسبات و معلومات)', 'Sport Science (تربية رياضية)', 'Business (تجارة)')
    major = st.selectbox('Major (your college)', major_options)

    activities_options = [
        'Adapt to change or perform a variety of duties that may change',
        'Budget and handle money and records with accuracy and reliability',
        'Care about people, their needs, and their problems',
        'Concentrate for long periods without being distracted',
        'Do routine, organized, and accurate work',
        'Explore new technology',
        'Find the best way or a new way to do something',
        'Help people overcome their challenges to be at their best',
        'Have a flexible schedule',
        'Handle several responsibilities at once'
    ]
    activities = st.multiselect('Activities (Choose one or more)', activities_options)

    character_options = [
        'Adventurous',
        'Caring',
        'Competitive',
        'Creative and imaginative',
        'Creative problem-solver',
        'Decision maker',
        'Friendly',
        'Good communicator'
    ]
    character_traits = st.multiselect('What would describe you? (Choose one or more)', character_options)

    personal_traits_options = [
        'Non-judgmental',
        'Non-materialistic',
        'Optimistic',
        'Organized',
        'Pay attention to detail',
        'Persuasive',
        'Problem solver',
        'Self-confident',
        'See details in the big picture'
    ]
    personal_traits = st.multiselect('(Choose one or more) personal traits', personal_traits_options)

    stressed_out = st.radio('I get stressed out easily', ('Yes', 'No'))

    favorite_subjects_options = [
        'Biology',
        'Chemistry',
        'Computer',
        'Physics',
        'Math',
        'Foreign Language',
        'Geography',
        'History'
    ]
    favorite_subjects = st.multiselect('Favorite School Subjects (Choose one or more)', favorite_subjects_options)

    if st.button('Predict'):
        # Perform prediction or data processing here based on the collected inputs
        st.write(f"Full Name: {full_name}")
        st.write(f"Activities: {', '.join(activities)}")
        st.write(f"Character Traits: {', '.join(character_traits)}")
        st.write(f"Personal Traits: {', '.join(personal_traits)}")
        st.write(f"Stressed Out: {stressed_out}")
        st.write(f"Favorite Subjects: {', '.join(favorite_subjects)}")

if __name__ == "__main__":
    main()
