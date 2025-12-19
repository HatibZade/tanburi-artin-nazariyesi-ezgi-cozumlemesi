import json, os, streamlit as st

st.set_page_config(page_title="Tanburi Küçük Artin – 17'li Sistem", layout="wide")

DATA_PATH = "data/tanburi_kucuk_artin_data.json"

@st.cache_data
def load_data(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

DATA = load_data(DATA_PATH)
makamlar = DATA.get("makamlar", [])

st.title("Tanburi Küçük Artin Nazariyesine Göre Makam / Terkib Analizi")
st.markdown("""
**Ses sistemi:** 17'li sistem  
**Nazariyeci:** Tanburi Küçük Artin  

### Önemli Nazari Not
- Dik Kürdi → **Segâh**
- Dik Acem → **Evc**
- Dik Acem-Aşiran → **Irâk**
- **Şehnaz terkibinde** dik acem yerine **Evc** kullanılır.

> Sisteme yalnızca **Artin perde adlarını** giriniz.
""")

left, right = st.columns([1,2])

with left:
    q = st.text_input("Ara (makam / terkib)")
    filtered = [m for m in makamlar if q.lower() in m.get("name_tr","").lower()] if q else makamlar
    idx = st.selectbox("Seç", range(len(filtered)), format_func=lambda i: filtered[i].get("name_tr",""))

with right:
    if filtered:
        m = filtered[idx]
        a = m.get("analysis", {})
        st.subheader(m.get("name_tr",""))
        st.write("**Karar:**", a.get("karar",{}).get("perde","—"))
        st.write("**Merkez:**", a.get("merkez",{}).get("perde","—"))
        kp = a.get("kullanilan_perdeler",{})
        st.write("**Asıl perdeler:**", ", ".join(kp.get("asil_perdeler",[])) or "—")
        st.write("**Nim perdeler:**", ", ".join(kp.get("nim_perdeler",[])) or "—")
