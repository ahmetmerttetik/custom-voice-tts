# Voice Assistant - Metni Sese Dönüştürür  

Bu proje, eğitilen ses modelini kullanarak yazılı metinleri sese dönüştüren  bir sesli asistan modülüdür.

---

Bu proje Ubuntu'da ve diğer dağıtımlarda için yapıldı.  

---

## 🛠️ Kurulum

1.
   ```bash
   git clone https://github.com/ahmetmerttetik/custom-voice-tts.git
   cd custom-voice-tts
   ```

2.
   ```bash
   pip install -r requirements.txt
   ```

3.
   - **`model_path`** ve **`config_path`** yollarını Piper TTS dosyalarınıza göre düzenleyin.
   - Okunacak metni bir `.txt` dosyasına veya string bir değere yazın.

---

## Örnek Kullanım

```python
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
```

---

## 📂 Gereksinimler

`requirements.txt` içeriği:
```plaintext
piper-tts==0.1.0
pygame==2.5.0
```

Python sürümüm 3.10.12

