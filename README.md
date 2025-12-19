# Tanburi Küçük Artin – Makam/Terkib Tahlil Veri Seti (Stable, Locked)

Bu paket **tek isimli** veri dosyası kullanır; sürüm karmaşası yoktur.

## Dosyalar
- `data/tanburi_kucuk_artin_data.json` : JSON veri (Streamlit bunu okur)
- `data/tanburi_kucuk_artin_data.py` : Python modülü (DATA sözlüğü)
- `app.py` : Streamlit görüntüleyici

## Asıl perde eşleme (kilitli)
Sınıflama, yazım farklarından etkilenmemesi için normalize edilerek yapılır:
- Dügâh / Dügah / dügah -> **Dügâh** (asıl)
- Segâh / Segah -> **Segâh** (asıl)
- Çargâh / Cargah -> **Çargâh** (asıl)
vb.

Asıl perdeler kümesi (ASIL_MAP):
{
  "yegah": "Yegâh",
  "asiran": "Aşîrân",
  "irak": "Irâk",
  "rast": "Rast",
  "dugah": "Dügâh",
  "segah": "Segâh",
  "cargah": "Çargâh",
  "neva": "Nevâ",
  "huseyni": "Hüseynî",
  "evc": "Evc",
  "gerdaniye": "Gerdâniye",
  "muhayyer": "Muhayyer",
  "tiz segah": "Tiz Segâh",
  "tiz cargah": "Tiz Çargâh",
  "tiz neva": "Tiz Nevâ"
}

## Çalıştırma
```bash
pip install -r requirements.txt
streamlit run app.py
```
