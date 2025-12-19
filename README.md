# Tanburi Küçük Artin – Makam/Terkib Tahlil Veri Seti (Clean)

Bu repo **tek isimli** veri dosyası kullanır; sürüm karmaşası yoktur.

## Dosyalar
- `data/tanburi_kucuk_artin_data.json` : JSON veri (Streamlit bunu okur)
- `data/tanburi_kucuk_artin_data.py` : Python modülü (DATA sözlüğü)
- `app.py` : Streamlit görüntüleyici

## Perde sınıflaması
- **Asıl perdeler** (kullanıcı tanımı): yegah, aşiran, ırak, rast, dügah, segah, çargah, neva, hüseyni, evc, gerdaniye, muhayyer, tiz segah, tiz çargah, tiz neva
- Bu listenin dışında kalanlar: **Nim perdeler**

## Çalıştırma
```bash
pip install -r requirements.txt
streamlit run app.py
```
