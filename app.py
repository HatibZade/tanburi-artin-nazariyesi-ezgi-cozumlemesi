
import json
import streamlit as st

st.set_page_config(page_title="Tanburi Artin – Makam Olasılık Motoru", layout="wide")

DATA_PATH = "data/tanburi_kucuk_artin_data.json"

@st.cache_data
def load():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

DATA = load()
MAKAMLAR = DATA.get("makamlar", [])

ALLOWED = ['Yegâh', 'Aşîrân', 'Irâk', 'Rast', 'Dügâh', 'Segâh', 'Çargâh', 'Nevâ', 'Hüseynî', 'Evc', 'Gerdâniye', 'Muhayyer', 'Tiz Segâh', 'Tiz Çargâh', 'Tiz Nevâ', 'Bayâtî', 'Buselik']
ASIL_CORE = ['Yegâh', 'Aşîrân', 'Irâk', 'Rast', 'Dügâh', 'Segâh', 'Çargâh', 'Nevâ', 'Hüseynî', 'Evc', 'Gerdâniye', 'Muhayyer', 'Tiz Segâh', 'Tiz Çargâh', 'Tiz Nevâ']
NIM_OPTIONS = ['Bayâtî', 'Buselik']

def uniq(seq):
    out=[]
    seen=set()
    for x in (seq or []):
        if isinstance(x,str):
            x=x.strip()
            if x and x not in seen:
                out.append(x); seen.add(x)
    return out

def overlap_score(user_list, ref_list):
    u=set(user_list or [])
    if not u:
        return 0.0
    r=set(ref_list or [])
    return len(u & r) / len(u)

def field_match(user_value, ref_value):
    if not user_value or user_value=="—" or not ref_value:
        return None
    return 1.0 if user_value == ref_value else 0.0

WEIGHTS = {
    "karar": 4,
    "merkez": 4,
    "baslangic": 3,
    "alt_sinir": 2,
    "ust_sinir": 2,
    "asil_perdeler": 3,
    "nim_perdeler": 2,
    "nazari_flags": 2,
}

st.title("Tanburi Küçük Artin – Makam Olasılık Motoru (Kilitli)")

st.markdown("""
**17'li sistem notu**
- Dik Kürdi → **Segâh**
- Dik Acem → **Evc**
- Dik Acem-Aşiran → **Irâk**
- **Şehnaz terkibinde** dik acem yerine **Evc** kullanılır.

> Sisteme yalnızca **Artin perde adlarını** gir.
""")

st.subheader("İncelenen Eser – Giriş")

c1, c2, c3 = st.columns(3, gap="large")

with c1:
    karar = st.selectbox("Karar perdesi", ["—"] + ALLOWED, index=0)
    merkez = st.selectbox("Merkez (kutb)", ["—"] + ALLOWED, index=0)
    bas1 = st.selectbox("Başlangıç civarı (1)", ["—"] + ALLOWED, index=0)
    bas2 = st.selectbox("Başlangıç civarı (2)", ["—"] + ALLOWED, index=0)

with c2:
    alt_sinir = st.selectbox("Alt sınır", ["—"] + ALLOWED, index=0)
    ust_sinir = st.selectbox("Üst sınır", ["—"] + ALLOWED, index=0)
    st.caption("Alt/üst sınır: ezginin ulaştığı en pest/en tiz perdeler.")

with c3:
    asil = st.multiselect("Asıl perdeler (tam perdeler)", ASIL_CORE)
    nim = st.multiselect("Nim perdeler (diğer perdeler)", NIM_OPTIONS)

st.markdown("#### Nazari Seyir (işaretleme)")
f1, f2, f3, f4 = st.columns(4)
with f1:
    ns_karar = st.checkbox("Karara sık dönüş")
with f2:
    ns_merkez = st.checkbox("Merkezde uzun kalış")
with f3:
    ns_ust = st.checkbox("Üst alana çıkış")
with f4:
    ns_alt = st.checkbox("Alt alana iniş")

compute = st.button("Olasılıkları Hesapla", type="primary")

def makam_ref(m):
    a = m.get("analysis", {})
    ref = {
        "karar": a.get("karar",{}).get("perde"),
        "merkez": a.get("merkez",{}).get("perde"),
        "agaz": a.get("agaz",{}).get("perde"),
        "alt_sinir": a.get("alt_sinir",{}).get("perde"),
        "ust_sinir": a.get("ust_sinir",{}).get("perde"),
    }
    seq = uniq(m.get("evidence",{}).get("seyir_sequence",[]) or [])
    ref["seq"] = seq
    ref["asil_pitches"] = [p for p in seq if p in ASIL_CORE]
    ref["nim_pitches"] = [p for p in seq if p in NIM_OPTIONS]
    return ref

def compute_score(user, ref):
    raw = 0.0
    maxw = 0.0

    for key, w in [("karar", WEIGHTS["karar"]), ("merkez", WEIGHTS["merkez"])]:
        m = field_match(user.get(key), ref.get(key))
        if m is not None:
            raw += m*w
            maxw += w

    # başlangıç civarı
    ref_start = ref.get("agaz") or (ref.get("seq")[:1][0] if ref.get("seq") else None)
    if user.get("bas1")!="—" or user.get("bas2")!="—":
        maxw += WEIGHTS["baslangic"]
        hit = 0.0
        if ref_start:
            hit = 1.0 if (user.get("bas1")==ref_start or user.get("bas2")==ref_start) else 0.0
        raw += hit*WEIGHTS["baslangic"]

    for key, w in [("alt_sinir", WEIGHTS["alt_sinir"]), ("ust_sinir", WEIGHTS["ust_sinir"])]:
        m = field_match(user.get(key), ref.get(key))
        if m is not None:
            raw += m*w
            maxw += w

    if user.get("asil"):
        maxw += WEIGHTS["asil_perdeler"]
        raw += overlap_score(user["asil"], ref.get("asil_pitches")) * WEIGHTS["asil_perdeler"]

    if user.get("nim"):
        maxw += WEIGHTS["nim_perdeler"]
        raw += overlap_score(user["nim"], ref.get("nim_pitches")) * WEIGHTS["nim_perdeler"]

    flags = {
        "ns_karar": user.get("ns_karar"),
        "ns_merkez": user.get("ns_merkez"),
        "ns_ust": user.get("ns_ust"),
        "ns_alt": user.get("ns_alt"),
    }
    if any(flags.values()):
        maxw += WEIGHTS["nazari_flags"]
        seq = ref.get("seq") or []
        ref_flags = {
            "ns_karar": (ref.get("karar") in seq[-3:]) if ref.get("karar") else False,
            "ns_merkez": (ref.get("merkez") in seq) if ref.get("merkez") else False,
            "ns_ust": (ref.get("ust_sinir") in seq) if ref.get("ust_sinir") else False,
            "ns_alt": (ref.get("alt_sinir") in seq) if ref.get("alt_sinir") else False,
        }
        checked = [k for k,v in flags.items() if v]
        agree = sum(1 for k in checked if ref_flags.get(k))
        raw += (agree/len(checked) if checked else 0.0) * WEIGHTS["nazari_flags"]

    return (raw/maxw)*100.0 if maxw else 0.0

if compute:
    user = {
        "karar": karar, "merkez": merkez,
        "bas1": bas1, "bas2": bas2,
        "alt_sinir": alt_sinir, "ust_sinir": ust_sinir,
        "asil": asil, "nim": nim,
        "ns_karar": ns_karar, "ns_merkez": ns_merkez, "ns_ust": ns_ust, "ns_alt": ns_alt
    }

    results = []
    for m in MAKAMLAR:
        ref = makam_ref(m)
        score_val = compute_score(user, ref)
        results.append((score_val, m, ref))

    results.sort(key=lambda x: x[0], reverse=True)

    st.subheader("Sonuçlar (Top 10)")
    for score_val, m, ref in results[:10]:
        with st.expander(f"{m.get('name_tr','(adsız)')} — %{score_val:.1f}"):
            st.write("**Referans (Artin tahlili)**")
            st.write("- Karar:", ref.get("karar") or "—")
            st.write("- Merkez:", ref.get("merkez") or "—")
            st.write("- Âgâz:", ref.get("agaz") or "—")
            st.write("- Alt sınır:", ref.get("alt_sinir") or "—")
            st.write("- Üst sınır:", ref.get("ust_sinir") or "—")

            st.write("**Perde Sıralaması (Artin örnek seyri)**")
            st.code(" → ".join(ref.get("seq") or []) or "—", language="text")

            st.write("**Eser girdin (özet)**")
            st.write("- Karar:", karar)
            st.write("- Merkez:", merkez)
            st.write("- Başlangıç civarı:", ", ".join([x for x in [bas1, bas2] if x!="—"]) or "—")
            st.write("- Alt/Üst:", f"{alt_sinir} / {ust_sinir}")
            st.write("- Asıl perdeler:", ", ".join(asil) or "—")
            st.write("- Nim perdeler:", ", ".join(nim) or "—")
else:
    st.caption("Makam olasılıklarını görmek için bilgileri girip **Olasılıkları Hesapla**'ya bas.")
