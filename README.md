```markdown
# Whisper Audio Transcriber

This project provides a simple yet powerful Python script to transcribe audio files (MP3, WAV, M4A, FLAC, OGG) into text using OpenAI's highly accurate Whisper model. It features a graphical user interface (GUI) for easy file selection and saves the transcribed text in a dedicated output directory.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation Guide](#installation-guide)
    - [1. Install Miniconda (Recommended)](#1-install-miniconda-recommended)
    - [2. Create and Activate Conda Environment](#2-create-and-activate-conda-environment)
    - [3. Install Required Libraries](#3-install-required-libraries)
- [Usage](#usage)
    - [1. Place the Script](#1-place-the-script)
    - [2. Run the Script](#2-run-the-script)
    - [3. GUI File Selection](#3-gui-file-selection)
- [Expected Output](#expected-output)
- [Python Code](#python-code)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Description

The `transcribe_audio_only.py` script leverages OpenAI's Whisper model for state-of-the-art speech-to-text conversion. It's designed for ease of use, allowing users to select multiple audio files through a standard file dialog. The transcription process runs offline after the initial model download, offering robust performance for various languages, including English and Persian.

## Features

-   **High Accuracy:** Utilizes OpenAI's Whisper model for superior transcription quality.
-   **Offline Operation:** After the initial model download, no internet connection is required for transcription.
-   **Multi-Language Support:** Automatically detects and transcribes various languages (e.g., English, Persian).
-   **Graphical File Selection:** Easy-to-use Tkinter-based file dialog to select one or more audio files.
-   **Batch Processing:** Supports transcribing multiple selected audio files in one go.
-   **Organized Output:** Saves each transcription as a `.txt` file in an `output` directory, named after the original audio file.
-   **Error Handling:** Basic error handling for Whisper model loading and transcription failures.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

-   **Python:** Version 3.8 or higher.
-   **Conda (Anaconda or Miniconda):** Highly recommended for managing project environments.
-   **Internet Connection:** Required for initial library and Whisper model downloads.

## Installation Guide

Follow these steps to set up your environment and install the necessary libraries.

### 1. Install Miniconda (Recommended)

Miniconda is a lightweight version of Anaconda that includes Conda, Python, and a small number of essential packages.

-   Download Miniconda from the official website: [Miniconda Installer](https://docs.conda.io/en/latest/miniconda.html)
-   Follow the installation instructions for your operating system.

### 2. Create and Activate Conda Environment

It's best practice to create a dedicated Conda environment for this project to manage its dependencies separately.

1.  **Open Anaconda Prompt (Windows) or Terminal (macOS/Linux).**
2.  Navigate to your desired project directory. For example, to `C:\Users\Raptor\Documents\Text_Generator`:
    ```bash
    cd C:\Users\Raptor\Documents
    mkdir Text_Generator
    cd Text_Generator
    ```
3.  Create a new Conda environment named `text_gen_env` with Python 3.10:
    ```bash
    conda create --name text_gen_env python=3.10
    ```
    When prompted to proceed, type `y` and press Enter.
4.  Activate the newly created environment:
    ```bash
    conda activate text_gen_env
    ```
    You should see `(text_gen_env)` at the beginning of your terminal prompt, indicating the environment is active.

### 3. Install Required Libraries

With your `text_gen_env` active, install `openai-whisper` and `jupyterlab` (optional, for interactive development):

```bash
pip install -U openai-whisper
pip install jupyterlab  # Optional, for Jupyter Notebook/Lab integration
```
The first time you run `whisper`, it will download the chosen model (e.g., 'base'), which might take some time depending on your internet speed.

## Usage

### 1. Place the Script

Save the provided Python code (see [Python Code](#python-code) section below) into a file named `transcribe_audio_only.py` within your `C:\Users\Raptor\Documents\Text_Generator` directory.

### 2. Run the Script

1.  **Open Anaconda Prompt (Windows) or Terminal (macOS/Linux).**
2.  Activate your Conda environment:
    ```bash
    conda activate text_gen_env
    ```
3.  Navigate to your project directory:
    ```bash
    cd C:\Users\Raptor\Documents\Text_Generator
    ```
4.  Run the script:
    ```bash
    python transcribe_audio_only.py
    ```

### 3. GUI File Selection

Upon running the script, a file selection dialog will appear.
-   You can select one or multiple audio files (MP3, WAV, M4A, FLAC, OGG) by holding down `Ctrl` (or `Cmd` on macOS) and clicking on the desired files.
-   Click "Open" to start the transcription process.
-   The terminal will display progress updates, including the detected language and processing time for each file.

## Expected Output

The script will:
1.  Create an `output` directory in the same location as `transcribe_audio_only.py` if it doesn't already exist.
2.  For each processed audio file, it will generate a `.txt` file with the same base name (e.g., `my_audio.mp3` will result in `my_audio.txt`).
3.  These `.txt` files, containing the transcribed text, will be saved in the `output` directory.

Example:
```
Text_Generator/
├── transcribe_audio_only.py
└── output/
    ├── my_lecture.txt
    ├── interview.txt
    └── podcast_segment.txt
```

## Troubleshooting

-   **`ModuleNotFoundError: No module named 'whisper'` or other libraries:**
    Ensure your Conda environment (`text_gen_env`) is activated and all libraries are installed correctly (`pip install -U openai-whisper` and `pip install jupyterlab`).
-   **`NameError: name 'null' is not defined`:**
    This indicates an incorrect copy-pasting of code. Ensure you have copied the entire Python script provided above and that there are no `null` values (which are not valid in Python; use `None` instead).
-   **Whisper model download issues:**
    Ensure you have a stable internet connection for the initial model download. If issues persist, try restarting the script.
-   **Jupyter Notebook/Lab not finding the kernel:**
    If you are using Jupyter and cannot find the `Python (Text Gen)` kernel, ensure `ipykernel` is installed in your environment and you've run:
    ```bash
    conda activate text_gen_env
    pip install ipykernel
    python -m ipykernel install --user --name=text_gen_env --display-name="Python (Text Gen)"
    ```
    Then, restart JupyterLab/Notebook and select the correct kernel.

## License

This project is open-source and available under the MIT License. 
```