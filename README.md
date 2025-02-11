# 🎙Voice Assistant - Eğitilen Ses Modelini Sese Dönüştürür  

Bu proje, eğitilen ses modelini kullanarak yazılı metinleri sese dönüştüren  bir sesli asistan oluşturur. Bu tts modeli i .Metni doğal bir sesle seslendirir, bir `.wav` dosyası olarak kaydeder ve çalar.

---

## 🚀 Nasıl Kullanılır?

1. **Modeli yükle:** Piper TTS model ve ayar dosyalarını tanımlayın.
2. **Metni yükleyin:** Seslendirmek istediğiniz metni girin.
3. **Kaydedin:** Ses dosyasını `.wav` formatında oluşturun.

---

## 🛠️ Kurulum

1. **Kodları indirin:**
   ```bash
   git clone https://github.com/ahmetmerttetik/custom-voice-tts.git
   cd custom-voice-tts
   ```

2. **Bağımlılıkları yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Model dosyalarını ayarlayın:**
   - **`model_path`** ve **`config_path`** yollarını Piper TTS dosyalarınıza göre düzenleyin.
   - Okunacak metni bir `.txt` dosyasına veya string bir değere yazın.

---

## Örnek Kullanım

```python
from pathlib import Path

voice = VoiceAssistant.load(
    model_path="/home/.../model.onnx",
    config_path="/home/.../model.onnx.json"
)

synthesize_arguman = voice.synthesize_args(1, 0.667, 0.8, 0.66)

text = Path("/home/.../deneme.txt").read_text()

wav_path = voice.save(text, synthesize_arguman)

VoiceAssistant.play_sound(wav_path)
```

---

## 📂 Gereksinimler

`requirements.txt` içeriği:
```plaintext
piper-tts==0.1.0
pygame==2.5.0
```

Proje Python 3.9 sürümüm 3.10.12

