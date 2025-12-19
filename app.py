
import json, streamlit as st

st.set_page_config(page_title="Tanburi Artin Makam Analizi", layout="wide")

DATA_PATH = "data/tanburi_kucuk_artin_data.json"

@st.cache_data
def load():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

DATA = load()
makamlar = DATA.get("makamlar", [])

st.title("Tanburi Küçük Artin'e Göre Makam / Terkib Analizi (17'li Sistem)")

st.markdown("""
**Önemli Nazari Not**
- Dik Kürdi → **Segâh**
- Dik Acem → **Evc**
- Dik Acem-Aşiran → **Irâk**
- **Şehnaz terkibinde** dik acem yerine **Evc** kullanılır.
""")

st.subheader("İncelenen Eser – Giriş Bilgileri")

col1, col2, col3 = st.columns(3)

with col1:
    karar = st.selectbox("Karar perdesi", ["—","Dügâh","Rast","Nevâ"])
    merkez = st.selectbox("Merkez (kutb)", ["—","Nevâ","Hüseynî","Dügâh"])

with col2:
    alt_alan = st.selectbox("Alt alan", ["—","Rast–Dügâh","Dügâh–Segâh"])
    ust_alan = st.selectbox("Üst alan", ["—","Nevâ–Muhayyer","Hüseynî–Gerdâniye"])

with col3:
    asil = st.multiselect("Asıl perdeler", ["Dügâh","Segâh","Nevâ","Hüseynî","Evc"])
    nim = st.multiselect("Nim perdeler", ["Acem","Saba","Zirgüle"])

st.divider()
st.subheader("Makam Olasılıkları")

st.info("⚠️ Puanlama algoritması bu sürümde demo amaçlıdır.")

st.write("Hicaz → %78")
st.write("Uşşak → %54")
st.write("Şehnaz → %41")

st.divider()
st.subheader("Detay Paneli – Tanburi Artin Örnek Seyirleri")

makam_ad = st.selectbox("Makam seç", [m.get("name_tr","") for m in makamlar])

for m in makamlar:
    if m.get("name_tr","") == makam_ad:
        st.markdown("**Perde Sıralaması (Artin örnek seyri):**")
        seq = m.get("evidence",{}).get("seyir_sequence",[])
        st.code(" → ".join(seq) if seq else "—")
        break
