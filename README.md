# Voice Assistant - Metni Sese Dönüştürür  

Bu proje, Piper ses modeli tarafından önceden eğitilmiş eğitim dosyalarının çalıştırılmasını sağlar. 
Projenin temel amacı, verilen metni sese dönüştürmek ve bu yapının farklı projelere kolay bir şekilde entegre edilebilmesini sağlamaktır. 
Sistem, offline ve hızlı bir şekilde çalışır. 
Kullanıcı isterse kendi sesini Piper ses modeli ile eğitip kişisel bir asistan oluşturabilir.

---

## 🛠️ Kurulum

1.
   ```bash
   git clone https://github.com/ahmetmerttetik/custom-voice-tts.git
   cd custom-voice-tts
   ```

2.
   ```bash
   python -m venv venv
   ```
3.
  ```bash
   source venv/bin/activate
   ```
   
 4.  
   ```bash
   pip install -r requirements.txt
   ```

5.
   - **`model_path`** ve **`config_path`** yollarını Piper TTS dosyalarınıza göre düzenleyin.
   - Okunacak metni bir `.txt` dosyasına yazın veya string bir değere atayın.

---

## Örnek Kullanım

```python
from voiceAssistant import VoiceAssistant
from pathlib import Path

def main():

    model_path="model_6602.onnx"
    config_path="model_6602.onnx.json"

    voice = VoiceAssistant(model_path,config_path)
    
    synth_args = voice.synthesize_args()
    
    
    text = Path("deneme.txt").read_text() # veya text = "Merhaba dünya"
    
    wav_path = voice.save(text, synth_args)
    voice.play_sound(wav_path)

if __name__ == "__main__":
    main()
```

---
