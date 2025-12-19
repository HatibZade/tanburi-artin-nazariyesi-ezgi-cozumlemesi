# Tanburi Küçük Artin Nazariyesine Göre Makam/Terkib Tahlil Verisi

Bu repo, Tanburi Küçük Artin'in **Musikî Edvârı** metninde yer alan "**bir mızrab**" tariflerinden çıkarılmış
makam/şube ilerleyişlerini, Streamlit/Python uygulamalarında **doğrudan import edilebilir** bir veri seti olarak sunar.

## İçerik
- `data/tanburi_kucuk_artin_makam_tahlil_full_v1_3.json` : JSON veri
- `data/tanburi_kucuk_artin_makam_tahlil_full_v1_3.py` : Python modülü (DATA sözlüğü)
- `app.py` : Basit Streamlit görüntüleyici
- `requirements.txt` : Çalıştırma bağımlılıkları

## Perde Sınıflaması (v1.3)
Bu sürümde `kullanilan_perdeler` alanı ikiye ayrılır:
- `asil_perdeler`: Kullanıcı tarafından tanımlanan **asıl perde adları** kümesinde olanlar
- `nim_perdeler`: Bu kümenin dışında kalanlar

Kullanılan asıl perde adları:
- yegah, aşiran, ırak, rast, dügah, segah, çargah, neva, hüseyni, evc, gerdaniye, muhayyer, tiz segah, tiz çargah, tiz neva

## Hızlı Başlangıç (Streamlit)
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Lisans
Bu repo, **veri yapısı ve kod** açısından MIT lisansı ile sunulmuştur.
Kaynak metnin (kitabın/PDF'in) telif hakları ilgili yayıncıya aittir.
