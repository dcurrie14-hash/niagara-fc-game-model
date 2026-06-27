import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import apply_css, sidebar_brand, fig_formation, FORMATIONS
import matplotlib.pyplot as plt

st.set_page_config(page_title="Systems & Formations | Niagara FC", page_icon="📐", layout="wide")
apply_css(); sidebar_brand()

st.markdown("# SYSTEMS & FORMATIONS")
st.markdown("<div class='quote-block'>The formation organises the team. Our principles give players the freedom to solve problems, adapt to the game, and make intelligent decisions.</div>", unsafe_allow_html=True)
st.markdown("<div class='card' style='margin-bottom:1rem;'>These are role profiles rather than fixed positions. Responsibilities change according to the moment, but our principles remain constant.</div>", unsafe_allow_html=True)

c1, _ = st.columns([1, 3])
with c1: sel = st.selectbox("Formation", list(FORMATIONS.keys()))
fig = fig_formation(sel); st.pyplot(fig, use_container_width=True); plt.close()

st.divider()
st.markdown("### ROLE DESCRIPTIONS")
cols = st.columns(3)
for i, (role, desc) in enumerate(FORMATIONS[sel]["roles"].items()):
    with cols[i % 3]:
        st.markdown(f"<div class='card'><b>{role}</b><br><small>{desc}</small></div>", unsafe_allow_html=True)