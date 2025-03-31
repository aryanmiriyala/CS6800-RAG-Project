import os
import json

# Path to the directory containing JSON files
json_directory = './DATAR/release_related/all_jsons/'

# New directory for saving the extracted files
extracted_directory = './Extracted-Files/'

# Create the new directory if it doesn't exist
if not os.path.exists(extracted_directory):
    os.makedirs(extracted_directory)

# Iterate through all JSON files in the directory
for filename in os.listdir(json_directory):
    if filename.endswith('.json'):
        file_path = os.path.join(json_directory, filename)
        
        # Create output file path in the new 'Extracted_files' directory
        output_file = os.path.join(extracted_directory, f"{filename.replace('.json', '')}-extracted.json")
        
        # List to store extracted data
        data_list = []
        
        # Read the JSON file
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                json_data = json.load(f)
                
                # Check if the data is a list or a dictionary
                if isinstance(json_data, list):
                    for entry in json_data:
                        data_list.append({
                            'filename': filename,
                            # 'release_data': entry.get('release_data', []),
                            'published_at': entry.get('published_at', entry.get('release_data', {}).get('published_at', 'N/A')),
                            'google_play_reviews': entry.get('google_play_reviews', [])
                        })
                elif isinstance(json_data, dict):
                    data_list.append({
                        'filename': filename,
                        # 'release_data': json_data.get('release_data', []),
                        'published_at': json_data.get('published_at', json_data.get('release_data', {}).get('published_at', 'N/A')),
                        'google_play_reviews': json_data.get('google_play_reviews', [])
                    })

                # Save extracted data to the new directory
                with open(output_file, 'w', encoding='utf-8') as f_out:
                    json.dump(data_list, f_out, ensure_ascii=False, indent=4)
                print(f"Extraction complete. Data saved to {output_file}")
                
            except json.JSONDecodeError as e:
                print(f"Error reading {filename}: {e}")
