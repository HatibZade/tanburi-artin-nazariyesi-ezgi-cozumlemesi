import json
import streamlit as st

st.set_page_config(page_title="Tanburi Küçük Artin - Makam Tahlil", layout="wide")

DATA_PATH = "data/tanburi_kucuk_artin_makam_tahlil_full_v1.json"

@st.cache_data
def load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

DATA = load_data()
makamlar = DATA.get("makamlar", [])

st.title("Tanburi Küçük Artin Nazariyesine Göre Makam/Terkib Tahlilleri")
st.caption("Kaynak: Musikî Edvârı (\"bir mızrab\" seyir dizileri)")

left, right = st.columns([1, 2], gap="large")

with left:
    q = st.text_input("Ara (makam adı / id)", "")
    filtered = makamlar
    if q.strip():
        ql = q.lower()
        filtered = [m for m in makamlar if ql in (m.get("name_tr","").lower()) or ql in (m.get("id","").lower())]
    st.write(f"Toplam kayıt: {len(filtered)} / {len(makamlar)}")

    names = [f'{m.get("name_tr","(adsız)")}  —  {m.get("id","")}' for m in filtered]
    idx = st.selectbox("Kayıt seç", list(range(len(names))), format_func=lambda i: names[i] if names else "(yok)", disabled=(len(names)==0))

with right:
    if makamlar and filtered:
        m = filtered[idx]
        a = m.get("analysis", {})
        st.subheader(m.get("name_tr","(adsız)"))
        c1, c2, c3 = st.columns(3)
        c1.metric("Âgâz", a.get("agaz", {}).get("perde", "—"))
        c2.metric("Merkez", a.get("merkez", {}).get("perde", "—"))
        c3.metric("Karar", a.get("karar", {}).get("perde", "—"))

        c4, c5 = st.columns(2)
        c4.metric("Alt sınır", a.get("alt_sinir", {}).get("perde", "—"))
        c5.metric("Üst sınır", a.get("ust_sinir", {}).get("perde", "—"))

        st.markdown("### Kullanılan perdeler")
        kp = a.get("kullanilan_perdeler", {})
        st.write("**Tam:**", ", ".join(kp.get("tam", [])) or "—")
        st.write("**Nim:**", ", ".join(kp.get("nim", [])) or "—")

        st.markdown("### Seyir (bir mızrab)")
        st.code(" → ".join(m.get("evidence", {}).get("seyir_sequence", [])) or "—", language="text")

        with st.expander("Ham kayıt (JSON)"):
            st.json(m)
    else:
        st.info("Gösterilecek kayıt yok.")
