from piper import PiperVoice
import wave
from pathlib import Path
from pygame import mixer
from datetime import datetime

class VoiceAssistant(PiperVoice):
    def __init__(self, model_path: str, config_path: str):
        super().__init__(model_path, config_path)

    @classmethod
    def load(cls, model_path: str, config_path: str):
        return cls(model_path, config_path)

    @staticmethod
    def create_unique():
        return datetime.now().strftime("%d%m%Y%H%M%S")

    def synthesize_args(self, length_scale=1, noise_scale=0.667, noise_w=0.8, sentence_silence=0.66):
        
        if isinstance(length_scale, dict):  
            return length_scale
        else:  
            return {
                "length_scale": length_scale,
                "noise_scale": noise_scale,
                "noise_w": noise_w,
                "sentence_silence": sentence_silence
            }

    @staticmethod
    def play_sound(wav_path):
        mixer.init()
        mixer.music.load(str(wav_path))
        mixer.music.play()

    def save(self, txt_file, synthesize_args, output_dir="."):
        file_name = self.create_unique()
        output_dir = Path(output_dir)
        wav_path = output_dir / f"{file_name}.wav"

        with wave.open(str(wav_path), "wb") as wav_file:
            self.synthesize(txt_file, wav_file, **synthesize_args)

        return wav_path



voice = VoiceAssistant.load(
    model_path="/home/mert/Desktop/piper/model_6602.onnx",
    config_path="/home/mert/Desktop/piper/model_6602.onnx.json"
)


synthesize_arguman = voice.synthesize_args(1, 0.667, 0.8, 0.66)


text = """Merhaba, ben Ahmet Mert TETİK."""

a = voice.save(text, synthesize_arguman)


VoiceAssistant.play_sound(a)
