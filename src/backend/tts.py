__author__ = "Idan Talker"
__version__ = "2.0.0"
__maintainer__ = "Idan Talker"
__email__ = ["talkeridan@gmail.com"]
__status__ = "Production"

from gtts import gTTS
import os
import tempfile
import platform
import subprocess
from typing import Optional

class TextToSpeech:
    """
    A modular text-to-speech converter class that synthesizes text into spoken audio.
    Handles different platforms and provides clean interfaces for integration.

    Args:
        lang (str): ISO language code (default: 'en')
        slow (bool): Use slow speed synthesis (default: False)
    """
    def __init__(self, lang: str = 'en', slow: bool = False):
        self.lang = lang
        self.slow = slow
        self.temp_files = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cleanup()

    def synthesize(self, text: str) -> bytes:
        """
        Converts text to speech audio data in MP3 format.

        Args:
            text (str): Input text to synthesize

        Returns:
            bytes: Audio data in MP3 format
        """
        tts = gTTS(text=text, lang=self.lang, slow=self.slow)
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
            tts.save(fp.name)
            self.temp_files.append(fp.name)
            with open(fp.name, 'rb') as audio_file:
                return audio_file.read()

    def speak(self, text: str) -> None:
        """
        Synthesizes text and plays it immediately through system speakers.

        Args:
            text (str): Text to speak aloud
        """
        audio_data = self.synthesize(text)
        self._play_audio(audio_data)

    def save_to_file(self, text: str, filename: str) -> None:
        """
        Saves synthesized speech to an MP3 file.

        Args:
            text (str): Text to synthesize
            filename (str): Output filename (.mp3 extension recommended)
        """
        tts = gTTS(text=text, lang=self.lang, slow=self.slow)
        tts.save(filename)

    def _play_audio(self, audio_data: bytes) -> None:
        """
        Internal method to play audio from bytes data.
        Creates temporary file and uses platform-specific players.
        """
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
            fp.write(audio_data)
            fp.flush()
            self._system_play(fp.name)
            os.unlink(fp.name)

    def _system_play(self, filepath: str) -> None:
        """Platform-specific audio playback implementation."""
        system = platform.system()
        try:
            if system == "Windows":
                os.startfile(filepath)
            elif system == "Darwin":  # macOS
                subprocess.run(["afplay", filepath], check=True)
            else:  # Linux and other UNIX-like systems
                subprocess.run(["aplay", filepath], check=True)
        except (subprocess.CalledProcessError, OSError) as e:
            raise RuntimeError(f"Audio playback failed: {str(e)}") from e

    def cleanup(self) -> None:
        """Remove any temporary files created during synthesis."""
        for filepath in self.temp_files:
            try:
                os.unlink(filepath)
            except FileNotFoundError:
                pass
        self.temp_files = []