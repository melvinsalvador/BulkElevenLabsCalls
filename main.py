import requests
import csv

# Constants
API_KEY = 'e3545a7fb96eb44e47a174060673fa7a'
VOICE_ID = 'XrExE9yKIg1WjnnlVkGX'
API_URL = f'https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}'
GITHUB_AUDIO_BASE_URL = 'https://raw.githubusercontent.com/melvin-ck/coaching/main/'

def text_to_speech(input_text):
    headers = {
        'accept': 'audio/mpeg',
        'content-type': 'application/json',
        'xi-api-key': API_KEY
    }
    data = {
        'text': input_text
    }
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
            filename = f"{text}.mp3"
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