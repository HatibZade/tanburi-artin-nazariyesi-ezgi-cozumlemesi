
import json
import streamlit as st
import unicodedata
import re

st.set_page_config(page_title="Tanburi Artin Makam Analizi", layout="wide")

DATA_PATH = "data/tanburi_kucuk_artin_data.json"

@st.cache_data
def load():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

DATA = load()
makamlar = DATA.get("makamlar", [])
ASIL_MAP = (DATA.get("classification", {}).get("asil_map") or {})

def norm_key(s: str) -> str:
    s = s.strip().lower()
    s = s.replace("ı","i").replace("İ","i")
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = s.translate(str.maketrans({"ğ":"g","ş":"s","ç":"c","ö":"o","ü":"u"}))
    s = re.sub(r"[^\w\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

ASIL_KEYS = set(ASIL_MAP.keys())

def is_asil(perde: str) -> bool:
    return norm_key(perde) in ASIL_KEYS

# Build options dynamically from dataset
all_pitches = []
seen = set()
for m in makamlar:
    seq = (m.get("evidence", {}).get("seyir_sequence") or [])
    for p in seq:
        if isinstance(p, str):
            p2 = p.strip()
            if p2 and p2 not in seen:
                all_pitches.append(p2)
                seen.add(p2)

asil_options = list(ASIL_MAP.values())
nim_options = []
nim_seen=set()
for p in all_pitches:
    if not is_asil(p):
        k = norm_key(p)
        if k not in nim_seen:
            nim_seen.add(k)
            nim_options.append(p)

nim_options = sorted(nim_options, key=lambda x: norm_key(x))
boundary_options = ["—"] + asil_options + nim_options

st.title("Tanburi Küçük Artin'e Göre Makam / Terkib Analizi (17'li Sistem)")

st.markdown("""
**Önemli Nazari Not (17'li sistem)**
- Dik Kürdi → **Segâh**
- Dik Acem → **Evc**
- Dik Acem-Aşiran → **Irâk**
- **Şehnaz terkibinde** dik acem yerine **Evc** kullanılır.

> Sisteme yalnızca **Artin perde adlarını** giriniz (görselde “dik …” duyuyorsan yukarıdaki dönüşümü uygula).
""")

st.subheader("İncelenen Eser – Giriş Bilgileri")

c1, c2, c3 = st.columns(3, gap="large")

with c1:
    karar = st.selectbox("Karar perdesi", boundary_options, index=0)
    merkez = st.selectbox("Merkez (kutb)", boundary_options, index=0)

with c2:
    bas1 = st.selectbox("Başlangıç civarı (1)", boundary_options, index=0)
    bas2 = st.selectbox("Başlangıç civarı (2)", boundary_options, index=0)
    alt_sinir = st.selectbox("Alt sınır", boundary_options, index=0)
    ust_sinir = st.selectbox("Üst sınır", boundary_options, index=0)

with c3:
    asil = st.multiselect("Asıl perdeler (tam perdeler)", asil_options)
    nim = st.multiselect("Nim perdeler (diğer perdeler)", nim_options)

st.markdown("#### Nazari Seyir (işaretleme)")
ns1, ns2, ns3, ns4 = st.columns(4)
with ns1:
    ns_karar = st.checkbox("Karara sık dönüş")
with ns2:
    ns_merkez = st.checkbox("Merkezde uzun kalış")
with ns3:
    ns_ust = st.checkbox("Üst alana çıkış")
with ns4:
    ns_alt = st.checkbox("Alt alana iniş")

st.divider()
st.subheader("Makam Olasılıkları")

st.info("Bu sürümde puanlama/olasılık motoru **taslak**. Giriş alanları artık tam kapsamlı. İstersen bir sonraki adımda gerçek puanlama motorunu ekleyelim.")

st.write("Örnek çıktı (demo):")
st.write("- Hicaz → %78")
st.write("- Uşşak → %54")
st.write("- Şehnaz → %41")

st.divider()
st.subheader("Detay Paneli – Tanburi Artin Örnek Seyirleri")

makam_ad = st.selectbox("Makam seç", [m.get("name_tr","") for m in makamlar])

for m in makamlar:
    if m.get("name_tr","") == makam_ad:
        st.markdown("**Perde Sıralaması (Artin örnek seyri):**")
        seq = m.get("evidence",{}).get("seyir_sequence",[]) or []
        st.code(" → ".join(seq) if seq else "—", language="text")
        break
