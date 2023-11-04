from flask import Flask, request, jsonify
import os
from aeneas.executetask import ExecuteTask
from aeneas.task import Task
import json 
import re

from flask_cors import CORS  # Import CORS from the flask_cors extension

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})  # Allow requests from http://localhost:3000


# Define a sample function that processes JSON data
def process_data(data):
    print(data)
    audio = data['audio']
    transcription = data['transcription']
    language = data['language']
    
    # Assuming you have a 'data.txt' file with text content
    with open("inputs/"+transcription, 'r') as text_file:
        text_content = text_file.read()

    # Initialize an empty string to store the formatted text
    formatted_text = ''

    # Split the text into sentences based on comma or full stop
    sentences = [sentence.strip() for sentence in re.split(r'[,\.]', text_content)]

    # Iterate through each sentence
    for sentence in sentences:
        if sentence:  # Check if the sentence is not empty
            # Format the sentence by adding a new line after each sentence
            formatted_text += sentence + '\n'

    # # Write the formatted text to a new text file (e.g., output.txt)
    with open('output.txt', 'w', encoding='utf-8') as txt_file:
        txt_file.write(formatted_text)

    audio_file_path = os.path.abspath("inputs/"+audio)
    text_file_path = os.path.abspath("output.txt")
    output_sync_map_path = os.path.abspath("output.json")

    # Call the align_audio_text function with the file paths
    align_audio_text(audio_file_path, text_file_path, output_sync_map_path, language)

    # Read the output sync map file and write it back with utf-8 encoding
    with open(output_sync_map_path, 'r', encoding='utf-8') as json_file:
        sync_map = json.load(json_file)
    with open(output_sync_map_path, 'w', encoding='utf-8') as json_file:
        json.dump(sync_map, json_file, ensure_ascii=False, indent=4)
    return f"Processed data: {data}"


def align_audio_text(audio_file, text, output_sync_map, language):
    config_string = "task_language="+language+"|is_text_type=plain|os_task_file_format=json"
    # config_string = "task_language=eng|is_text_type=plain|os_task_file_format=json"
    task = Task(config_string=config_string)
    task.audio_file_path_absolute = audio_file
    task.text_file_path_absolute = text
    task.sync_map_file_path_absolute = output_sync_map

    executor = ExecuteTask(task)
    executor.execute()
    task.output_sync_map_file()

# Define an API endpoint that accepts JSON data in the request body
@app.route('/api/process', methods=['POST'])
def process_endpoint():
    try:
    # Get the JSON data   
        data = request.get_json()
        if data is None:
            return jsonify({'error': 'Invalid JSON data'}), 400
        result = process_data(data)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
