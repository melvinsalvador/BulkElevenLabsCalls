import requests
import csv
import os

# Constants
API_KEY = os.environ['API_KEY']
VOICE_ID = 'XrExE9yKIg1WjnnlVkGX'
API_URL = f'https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}'
GITHUB_AUDIO_BASE_URL = 'https://raw.githubusercontent.com/melvinsalvador/BulkElevenLabsCalls/main/'

def text_to_speech(input_text):
    headers = {
        'accept': 'audio/mpeg',
        'content-type': 'application/json',
        'xi-api-key': API_KEY
    }
    data = {'text': input_text}
    response = requests.post(API_URL, headers=headers, json=data)
    return response.content  # This returns the binary audio data

def save_to_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)

def main():
    results = []

    # Read the input CSV
    with open('input.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            text = row[0]

            # Get audio data
            audio_data = text_to_speech(text)
            filename = f"{text.replace(' ', '_')}.mp3"  # Replace spaces with underscores
            save_to_file(audio_data, filename)

            # Construct GitHub URL for the audio
            audio_url = GITHUB_AUDIO_BASE_URL + filename

            # Append to results
            results.append([text, audio_url])

    # Write to output CSV
    with open('output.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(results)

if __name__ == '__main__':
    main()