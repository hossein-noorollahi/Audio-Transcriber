import whisper
import os
import time
import tkinter as tk
from tkinter import filedialog

# Function to create the output directory
def create_output_directory(dir_name="output"):
    """
    Creates the output directory if it doesn't already exist.
    """
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    return dir_name

# Function to transcribe an audio file
def transcribe_audio_file(file_path, model, output_dir):
    """
    Processes an audio file and saves its transcription to the output directory.
    """
    print("-" * 50)
    print(f"[PROCESS] Starting transcription for: {os.path.basename(file_path)}")
    
    # Extract base filename for output text file
    base_filename = os.path.splitext(os.path.basename(file_path))[0]
    output_txt_path = os.path.join(output_dir, f"{base_filename}.txt")

    # Check if the file has already been processed
    if os.path.exists(output_txt_path):
        print(f"[SKIP] File {os.path.basename(file_path)} has already been transcribed. Skipping.")
        return

    print("[INFO] Transcribing audio with Whisper...")
    start_time = time.time()
    
    try:
        # Perform speech recognition directly on the audio file
        # fp16=False for better CPU compatibility and to avoid potential errors on some systems
        result = model.transcribe(file_path, fp16=False) 
        transcribed_text = result['text']
        detected_language = result.get('language', 'N/A')
        
        end_time = time.time()
        print(f"[SUCCESS] Transcription completed in {end_time - start_time:.2f} seconds.")
        print(f"[INFO] Detected language: {detected_language}")

        # Save the transcribed text to a .txt file
        with open(output_txt_path, 'w', encoding='utf-8') as f:
            f.write(transcribed_text)
        print(f"[SAVE] Transcription successfully saved to {output_txt_path}.")

    except Exception as e:
        print(f"[ERROR] An error occurred during Whisper processing: {e}")

# Main function of the program
def main():
    """
    Main function that opens the file selection dialog and starts the transcription process.
    """
    # Create the main Tkinter window (which remains hidden)
    root = tk.Tk()
    root.withdraw() # Hides the main window

    # Open file selection dialog for audio files only
    print("Please select your audio files...")
    file_paths = filedialog.askopenfilenames(
        title="Select Audio Files",
        filetypes=(
            ("Audio Files", "*.mp3 *.wav *.m4a *.flac *.ogg"), # Common audio formats
            ("All Files", "*.*") # Option to show all files
        )
    )

    if not file_paths:
        print("No files selected. Program terminated.")
        return

    print(f"\n[INFO] {len(file_paths)} file(s) selected for processing.")
    
    # Load the Whisper model
    # Available models: 'tiny', 'base', 'small', 'medium', 'large'
    # 'base' offers a good balance between speed and accuracy for most cases.
    # For higher accuracy, consider 'medium' or 'large' (requires more RAM and processing time).
    print("[INFO] Loading Whisper model (may take a while the first time)...")
    try:
        model = whisper.load_model("base")
        print("[SUCCESS] Whisper model loaded successfully.")
    except Exception as e:
        print(f"[FATAL ERROR] Unable to load Whisper model: {e}")
        print("Please ensure you have an internet connection and Whisper is correctly installed.")
        return

    # Create the output directory
    output_directory = create_output_directory()

    # Process each selected file
    for file_path in file_paths:
        transcribe_audio_file(file_path, model, output_directory)
    
    print("\n[COMPLETE] All operations finished.")
    print(f"Transcriptions are saved in the '{output_directory}' folder.")


# Ensure the code runs only when executed directly
if __name__ == "__main__":
    main()