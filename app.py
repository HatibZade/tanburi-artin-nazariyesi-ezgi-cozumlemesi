
import json, streamlit as st

st.set_page_config(page_title="Tanburi Artin – Makam Olasılık Motoru", layout="wide")

DATA = json.load(open("data/tanburi_kucuk_artin_data.json", encoding="utf-8"))

ASIL_CORE = ['Aşîrân', 'Dügâh', 'Evc', 'Gerdâniye', 'Hüseynî', 'Irâk', 'Muhayyer', 'Nevâ', 'Rast', 'Segâh', 'Tiz Nevâ', 'Tiz Segâh', 'Tiz Çargâh', 'Yegâh', 'Çargâh']
NIM_OPTIONS = ['Acem', 'Acem-Aşîran', 'Bayâtî', 'Buselik', 'Geveşt', 'Hicaz', 'Hisâr', 'Mahur', 'Nihâvend (Kürdî)', 'Pest Hicaz (Nerm Hicaz)', 'Sabâ', 'Sünbüle', 'Zengûle', 'Şehnaz', 'Şorizen (Nerm Bayâtî)']
ALLOWED = ['Aşîrân', 'Dügâh', 'Evc', 'Gerdâniye', 'Hüseynî', 'Irâk', 'Muhayyer', 'Nevâ', 'Rast', 'Segâh', 'Tiz Nevâ', 'Tiz Segâh', 'Tiz Çargâh', 'Yegâh', 'Çargâh', 'Acem', 'Acem-Aşîran', 'Bayâtî', 'Buselik', 'Geveşt', 'Hicaz', 'Hisâr', 'Mahur', 'Nihâvend (Kürdî)', 'Pest Hicaz (Nerm Hicaz)', 'Sabâ', 'Sünbüle', 'Zengûle', 'Şehnaz', 'Şorizen (Nerm Bayâtî)']

st.title("Tanburi Küçük Artin – Makam Olasılık Motoru (Kilitli)")

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

st.caption("Perde listeleri alfabetik sıralıdır. Nim perdeler Artin listesine göredir.")
