# Tanburi Küçük Artin Nazariyesine Göre Makam/Terkib Tahlil Verisi

Bu repo, Tanburi Küçük Artin'in **Musikî Edvârı** metninde yer alan "**bir mızrab**" tariflerinden çıkarılmış
makam/şube ilerleyişlerini, Streamlit/Python uygulamalarında **doğrudan import edilebilir** bir veri seti olarak sunar.

## İçerik
- `data/tanburi_kucuk_artin_makam_tahlil_full_v1.json` : JSON veri
- `data/tanburi_kucuk_artin_makam_tahlil_full_v1.py` : Python modülü (DATA sözlüğü)
- `app.py` : Basit Streamlit görüntüleyici
- `requirements.txt` : Çalıştırma bağımlılıkları

## Veri Şeması (özet)
Her kayıt şu alanları içerir:
- `name_tr`, `id`
- `evidence.seyir_sequence` : "bir mızrab" perde dizisi
- `analysis.agaz`, `analysis.merkez`, `analysis.karar`
- `analysis.alt_sinir`, `analysis.ust_sinir`
- `analysis.kullanilan_perdeler.tam|nim`

> Not: Artin metninde Âgâz/Merkez/Karar/Alt–Üst sınır başlıkları sistematik şekilde verilmediği için bu alanlar,
yalnızca dizilerin başlangıç–bitiş ve tekrar/yoğunluk özelliklerinden türetilmiştir (repo içindeki dosyalarda notlar var).

## Hızlı Başlangıç (Streamlit)
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Python'da Kullanım

### Python modülü
```python
from data.tanburi_kucuk_artin_makam_tahlil_full_v1 import DATA

print(len(DATA["makamlar"]))
print(DATA["makamlar"][0]["name_tr"])
```

### JSON
```python
import json

with open("data/tanburi_kucuk_artin_makam_tahlil_full_v1.json", "r", encoding="utf-8") as f:
    DATA = json.load(f)

print(len(DATA["makamlar"]))
```

## Lisans
Bu repo, **veri yapısı ve kod** açısından MIT lisansı ile sunulmuştur.
Kaynak metnin (kitabın/PDF'in) telif hakları ilgili yayıncıya aittir.
