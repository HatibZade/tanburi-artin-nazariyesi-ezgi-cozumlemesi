
import json, streamlit as st
from engine import compute_probability

DATA = json.load(open("data/tanburi_kucuk_artin_data.json",encoding="utf-8"))

ASIL = ['Aşîrân', 'Çargâh', 'Dügâh', 'Evc', 'Gerdâniye', 'Hüseynî', 'Irâk', 'Muhayyer', 'Nevâ', 'Rast', 'Segâh', 'Tiz Çargâh', 'Tiz Nevâ', 'Tiz Segâh', 'Yegâh']
NIM = ['Acem', 'Acem-Aşîran', 'Bayâtî', 'Buselik', 'Geveşt', 'Hicaz', 'Hisâr', 'Mahur', 'Nihâvend (Kürdî)', 'Pest Hicaz (Nerm Hicaz)', 'Sabâ', 'Sünbüle', 'Şehnaz', 'Şorizen (Nerm Bayâtî)', 'Zengûle']
ALLOWED = ['Aşîrân', 'Çargâh', 'Dügâh', 'Evc', 'Gerdâniye', 'Hüseynî', 'Irâk', 'Muhayyer', 'Nevâ', 'Rast', 'Segâh', 'Tiz Çargâh', 'Tiz Nevâ', 'Tiz Segâh', 'Yegâh', 'Acem', 'Acem-Aşîran', 'Bayâtî', 'Buselik', 'Geveşt', 'Hicaz', 'Hisâr', 'Mahur', 'Nihâvend (Kürdî)', 'Pest Hicaz (Nerm Hicaz)', 'Sabâ', 'Sünbüle', 'Şehnaz', 'Şorizen (Nerm Bayâtî)', 'Zengûle']

WEIGHTS = {
    "karar":4,
    "merkez":4,
    "agaz":3,
    "alt":2,
    "ust":2,
    "asil":3,
    "nim":2
}

st.title("Tanburi Küçük Artin – Makam Olasılık Motoru (FINAL)")

c1,c2,c3 = st.columns(3)

with c1:
    karar = st.selectbox("Karar (tam)",["—"]+ASIL)
    merkez = st.selectbox("Merkez (tam)",["—"]+ASIL)
    agaz = st.selectbox("Başlangıç civarı (tam)",["—"]+ASIL)

with c2:
    alt = st.selectbox("Alt sınır",["—"]+ALLOWED)
    ust = st.selectbox("Üst sınır",["—"]+ALLOWED)

with c3:
    asil = st.multiselect("Asıl perdeler",ASIL)
    nim = st.multiselect("Nim perdeler",NIM)

if st.button("Olasılıkları Hesapla"):
    user = {
        "karar": None if karar=="—" else karar,
        "merkez": None if merkez=="—" else merkez,
        "agaz": None if agaz=="—" else agaz,
        "alt": None if alt=="—" else alt,
        "ust": None if ust=="—" else ust,
        "asil": asil,
        "nim": nim
    }

    results=[]
    for m in DATA["makamlar"]:
        a=m.get("analysis",{})
        ref={
            "karar": a.get("karar",{}).get("perde"),
            "merkez": a.get("merkez",{}).get("perde"),
            "agaz": a.get("agaz",{}).get("perde"),
            "alt": a.get("alt_sinir",{}).get("perde"),
            "ust": a.get("ust_sinir",{}).get("perde"),
            "asil": a.get("asil_perdeler",[]),
            "nim": a.get("nim_perdeler",[])
        }
        p=compute_probability(user,ref,WEIGHTS)
        results.append((p,m["name_tr"]))

    results.sort(reverse=True)
    for p,n in results[:5]:
        st.write(f"**{n}** → %{p}")
