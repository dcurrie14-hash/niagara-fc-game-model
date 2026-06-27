import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import apply_css, sidebar_brand, get_img, fig_hz_zones, fig_channels, fig_zones_channels
import matplotlib.pyplot as plt

st.set_page_config(page_title="Pitch Geography | Niagara FC", page_icon="🗺️", layout="wide")
apply_css(); sidebar_brand()

st.markdown("# PITCH GEOGRAPHY")
st.markdown("<div class='quote-block'>Pitch geography provides players with shared reference points for positioning, support, spacing, and decision-making in every moment of the game.</div>", unsafe_allow_html=True)

tabs = st.tabs(["📏 Horizontal Zones","🔀 Vertical Channels","🗺️ Zones & Channels"])

with tabs[0]:
    fig = fig_hz_zones(); st.pyplot(fig, use_container_width=True); plt.close()
    c1, c2 = st.columns(2)
    with c1:
        for z, d in [
            ("Zone 1 — BUILD",     "Our starting point. Engage the press, create space beyond it, and progress with purpose."),
            ("Zone 2 — PROGRESS",  "Break the first line. Create overloads. Play forward whenever possible."),
            ("Zone 3 — CREATE",    "Create superiority, combine, and penetrate beyond the defensive line."),
            ("Zone 4 — FINISH",    "Attack the box with numbers. Minimum four players. Finish with conviction."),
        ]:
            st.markdown(f"<div class='card'><b>{z}</b><br><small>{d}</small></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='quote-block'>THINK FORWARD · PLAY FORWARD · RUN FORWARD<br><br>Our pitch geography tells players where to play. Our principles tell them how to play.</div>", unsafe_allow_html=True)

with tabs[1]:
    fig = fig_channels(); st.pyplot(fig, use_container_width=True); plt.close()
    c1, c2 = st.columns(2)
    with c1:
        for ch, d in [
            ("Left & Right Wide Channels", "Provide width to stretch the opposition and create space inside."),
            ("Left & Right Half Spaces",   "Primary attacking channels. Receive between the lines, combine, and penetrate forward."),
            ("Central Channel",            "The most protected area of the pitch. Penetrate centrally whenever the opportunity exists."),
        ]:
            st.markdown(f"<div class='card'><b>{ch}</b><br><small>{d}</small></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='quote-block'>Width creates space. Space creates opportunities. We use the wide channels to open the half-spaces and create opportunities to penetrate centrally.</div>", unsafe_allow_html=True)

with tabs[2]:
    fig = fig_zones_channels(); st.pyplot(fig, use_container_width=True); plt.close()
    st.markdown("<div class='quote-block'>Every zone and every channel is connected. Width creates space, movement creates overloads, and intelligent positioning creates opportunities to penetrate. Understanding how the horizontal zones and vertical channels interact allows us to attack with purpose while remaining connected as a team.</div>", unsafe_allow_html=True)