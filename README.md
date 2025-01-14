# Real-Time Voice Translator

## Project Overview
A real-time voice translator for cross-platform communication, designed to work 
seamlessly with various video conferencing platforms.

## Features/Goals
- Real-time voice translation
- Compatibility with Zoom, Discord, FaceTime, and other communication platforms
- User-friendly interface
- Low latency for smooth conversations

## Technologies
- Python 3.12.7
- Speech-to-text APIs (SpeechRecognition, Google Cloud Speech-to-Text, Kaldi)
- Translation APIs (to be determined)
- Audio processing tools (to be determined)

## Setup Instructions

### Prerequisites
- Python 3.12.7 or later
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/talkeridan17/Real-Time-Voice-Translator.git
cd real-time-voice-translator
```

2. Create a virtual environment:

```bash
python3 -m venv babel_env
```

3. Activate the virtual environment:
- On macOS and Linux:
  ```
  source babel_env/bin/activate
  ```
- On Windows:
  ```
  babel_env\Scripts\activate
  ```
- For Fish Shell:
  ```
  source babel_env/bin/activate.fish
  ```
- For C Shell (csh/tcsh):
  ```
  source babel_env/bin/activate.csh
  ```
- For Windows PowerShell:
  ```
  babel_env\Scripts\Activate.ps1
  ```

4. Set up the CONFIG_DIR environment variable:
- The activation script has been modified to automatically set CONFIG_DIR to
the `config` directory in the project root.

5. Install dependencies:

```bash
pip install -r requirements.txt
```

### Configuration
- Any configuration files should be placed in the `config` directory.

## Development Roadmap
1. Research and select appropriate APIs for speech recognition and translation.
2. Develop a prototype for speech recognition.
3. Implement translation functionality.
4. Integrate with audio input/output systems.
5. Develop user interface.
6. Test and optimize for latency.
7. Implement platform-specific integrations (Zoom, Discord, etc.).

## Current Progress
- Project structure set up
- Virtual environment configured
- Basic README and documentation in place
- Researching various APIs for speech recognition, reach out to Idan for details

## Challenges
- Minimizing latency for real-time translation
- Ensuring accurate speech recognition in various accents and environments
- Seamless integration with multiple communication platforms
- Handling different audio input/output configurations

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to your branch
5. Create a new Pull Request

Please ensure your code adheres to the project's coding standards and include
tests for new features.

## License

This project is licensed under the Apache License, Version 2.0. See the 
[LICENSE](LICENSE) file for details.

## Contact
Name: Idan Talker

Email: talkeridan@gmail.com

Discord: talkeridan
