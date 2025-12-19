import json,streamlit as st
st.title('Tanburi Artin – Clean')
DATA=json.load(open('data/tanburi_kucuk_artin_data.json',encoding='utf-8'))
for m in DATA['makamlar']:
 st.subheader(m.get('name_tr',''))
 st.code(' → '.join(m.get('evidence',{}).get('seyir_sequence',[])) or '—')