import streamlit as st
import modal
import json
import os

def main():
    st.title("Newsletter Dashboard")

    available_podcast_info = create_dict_from_json_files('.')

    # ... Rest of your code ...

def create_dict_from_json_files(directory):
    """Creates a dictionary of podcast information from the JSON files in the specified directory."""
    podcast_info = {}
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), 'r') as f:
            podcast_info[filename] = json.load(f)

    # Add the 'podcast_details' key to the dictionary and populate it with the podcast title.
    for filename, podcast_data in podcast_info.items():
        podcast_info[filename]['podcast_details'] = {
            'podcast_title': podcast_data['title'],
        }

    return podcast_info

def process_podcast_info(url):
    f = modal.Function.lookup("corise-podcast-project", "process_podcast")
    output = f.call(url, '/content/podcast/')
    return output

if __name__ == '__main__':
    main()

