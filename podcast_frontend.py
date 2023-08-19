import streamlit as st
import modal
import json
import os

def main():

    available_podcast_info = create_dict_from_json_files('.')

    tcol1, tcol2 = st.columns([2, 8])

    with tcol1:
        st.sidebar.image("podcast-live-icon.svg", caption="", width=50, use_column_width=False)

    # Dropdown box
    st.sidebar.subheader("Available Podcasts Feeds")
    selected_podcast = st.sidebar.selectbox("Select Podcast", options=available_podcast_info.keys())

    # User Input box
    st.sidebar.subheader("Add and Process New Podcast Feed")
    st.sidebar.markdown("<p style='margin-bottom: 5px; color:#000; font-style:italic; font-weight: bold;'>Don't Use RSS feed. Use the castbox Podcast URL</p>", unsafe_allow_html=True)

    url = st.sidebar.text_input("Spotify Podcast URL", placeholder="example: https://open.spotify.com/episode/0jbyb1Io0Ge9H0WBrhg70L")

    st.title("AMERICAN POLITICS NEWSLETTER")
    process_button = st.sidebar.button("Process Podcast Feed")
    st.sidebar.markdown("**Note**: Podcast processing can take up to 5 mins, please be patient.")

    if selected_podcast:
        podcast_info = available_podcast_info[selected_podcast]

        # Right section - Newsletter content
        st.header(":orange[Newsletter Summary]")
        st.image("podcast-mic.png", use_column_width=False)

        # ... Other parts of your code ...

    if process_button:
        podcast_info = process_podcast_info(url)

        # ... Other parts of your code ...

def create_dict_from_json_files(folder_path):
    json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
    data_dict = {}

    for file_name in json_files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            podcast_info = json.load(file)
            podcast_name = podcast_info['podcast_details']['podcast_title']
            # Process the file data as needed
            data_dict[podcast_name] = podcast_info

    return data_dict

def process_podcast_info(url):
    f = modal.Function.lookup("corise-podcast-project-full", "process_podcast")
    output = f.call(url, '/content/Podcast/')
    return output

if __name__ == '__main__':
    main()
