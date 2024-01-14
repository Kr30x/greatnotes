from flask import Flask, send_from_directory
import random
import os

app = Flask(__name__)

def scan_directory(directory_path):
    result = {}

    try:
        # List all files and directories in the given path
        entries = os.listdir(directory_path)
        for entry in entries:
            # Create full path to the entry
            full_path = os.path.join(directory_path, entry)

            # Check if the entry is a directory
            if os.path.isdir(full_path):
                # If it's a directory, recursively scan it
                result[entry] = {'type': 'Folder', 'name': entry, 'content': scan_directory(full_path)}
            else:
                result[entry] = {'type': 'File', 'name': entry}

    except Exception as e:
        print(f"Error scanning directory: {e}")


    return result

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)


@app.route("/get_folder/<path:path>")
def get_folder(path):
    print('scanning', path)
    return os.listdir(path)


if __name__ == "__main__":
    app.run(debug=True)
