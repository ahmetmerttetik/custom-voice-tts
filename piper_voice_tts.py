from piper import PiperVoice
import wave
from pathlib import Path
from pygame import mixer
from datetime import datetime
from pathlib import Path

class VoiceAssistant:
    def __init__(self, model_path, config_path):
        self.piper = PiperVoice.load(model_path, config_path)
    
    @staticmethod
    def get_timestamp():
        return datetime.now().strftime("%d%m%Y%H%M%S")
    
    def synthesize_args(self, length_scale=1.0, noise_scale=0.667, noise_w=0.8, sentence_silence=0.66):
        return {
            "length_scale": length_scale,
            "noise_scale": noise_scale,
            "noise_w": noise_w,
            "sentence_silence": sentence_silence
        }
    
    @staticmethod
    def play_sound(wav_path):
        mixer.init()
        mixer.music.load(wav_path)
        mixer.music.play()
    
    def save(self, text, synthesize_args, output_dir="."):
        output_dir = Path(output_dir)
        wav_path = output_dir / f"{self.get_timestamp()}.wav"
        
        with wave.open(str(wav_path), "wb") as wav_file:
            self.piper.synthesize(text, wav_file, **synthesize_args)
        
        return wav_path

def main():

    model_path="model_6602.onnx"
    config_path="model_6602.onnx.json"

    voice = VoiceAssistant(model_path,config_path)
    
    synth_args = voice.synthesize_args()
    
    
    text = Path("deneme.txt").read_text()
    
    
    wav_path = voice.save(text, synth_args)
    voice.play_sound(wav_path)

if __name__ == "__main__":
    main()
