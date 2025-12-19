
import json
import streamlit as st

st.set_page_config(page_title="Tanburi Artin – Makam Olasılık Motoru", layout="wide")

DATA = json.load(open("data/tanburi_kucuk_artin_data.json", encoding="utf-8"))

ASIL_CORE = ['Yegâh', 'Aşîrân', 'Irâk', 'Rast', 'Dügâh', 'Segâh', 'Çargâh', 'Nevâ', 'Hüseynî', 'Evc', 'Gerdâniye', 'Muhayyer', 'Tiz Segâh', 'Tiz Çargâh', 'Tiz Nevâ']
NIM_OPTIONS = ['Şorizen (Nerm Bayâtî)', 'Pest Hicaz (Nerm Hicaz)', 'Geveşt', 'Zengûle', 'Nihâvend (Kürdî)', 'Buselik', 'Sabâ', 'Hicaz', 'Bayâtî', 'Hisâr', 'Acem', 'Mahur', 'Şehnaz', 'Sünbüle']
ALLOWED = ['Yegâh', 'Aşîrân', 'Irâk', 'Rast', 'Dügâh', 'Segâh', 'Çargâh', 'Nevâ', 'Hüseynî', 'Evc', 'Gerdâniye', 'Muhayyer', 'Tiz Segâh', 'Tiz Çargâh', 'Tiz Nevâ', 'Şorizen (Nerm Bayâtî)', 'Pest Hicaz (Nerm Hicaz)', 'Geveşt', 'Zengûle', 'Nihâvend (Kürdî)', 'Buselik', 'Sabâ', 'Hicaz', 'Bayâtî', 'Hisâr', 'Acem', 'Mahur', 'Şehnaz', 'Sünbüle']

st.title("Tanburi Küçük Artin – Makam Olasılık Motoru (Kilitli)")

st.markdown("""
**Tanburi Küçük Artin – 17’li Sistem**
Bu uygulamada **nim perdeler**, Artin’in tarif ettiği adlarla
**isim isim** tanımlıdır.  
Liste dışında nim perde **yoktur**.
""")

st.subheader("İncelenen Eser – Giriş")

c1, c2, c3 = st.columns(3)

with c1:
    karar = st.selectbox("Karar (tam)", ["—"] + ASIL_CORE)
    merkez = st.selectbox("Merkez (tam)", ["—"] + ASIL_CORE)
    bas1 = st.selectbox("Başlangıç civarı 1 (tam)", ["—"] + ASIL_CORE)
    bas2 = st.selectbox("Başlangıç civarı 2 (tam)", ["—"] + ASIL_CORE)

with c2:
    alt = st.selectbox("Alt sınır (tam + nim)", ["—"] + ALLOWED)
    ust = st.selectbox("Üst sınır (tam + nim)", ["—"] + ALLOWED)

with c3:
    asil = st.multiselect("Asıl Perdeler (tam)", ASIL_CORE)
    nim = st.multiselect("Nim Perdeler (Artin)", NIM_OPTIONS)

st.info("Nim perdeler (Artin): " + " • ".join(NIM_OPTIONS))
