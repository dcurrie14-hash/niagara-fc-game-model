import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import apply_css, sidebar_brand, get_img, fig_att_transition
import matplotlib.pyplot as plt

st.set_page_config(page_title="Attacking Transition | Niagara FC", page_icon="⚡", layout="wide")
apply_css(); sidebar_brand()

st.markdown("# ATTACKING TRANSITION")
st.markdown("<div style='font-family:Oswald,sans-serif;font-size:1em;color:#F5C518;letter-spacing:1px;margin-bottom:12px;'>TEAM INTENTION: Attack quickly before the opponent can recover defensive organisation.</div>", unsafe_allow_html=True) 

st.markdown("<div style='font-family:Oswald,sans-serif;font-size:0.95em;color:#FFD700;letter-spacing:1px;margin-bottom:12px;'>STRATEGY: Attack immediately. Play forward before the opposition can recover organisation.</div>", unsafe_allow_html=True)

fig = fig_att_transition(); st.pyplot(fig, use_container_width=True); plt.close()

c1, c2 = st.columns(2)
with c1:
    st.markdown("### COACHING DETAIL")
    for item in ["Immediate forward thought after regain — decision made within one second",
                 "On regain, look to find #7, #9, or #11 immediately — attack before the opposition can recover their shape",
                 "#9 must secure contact, hold the ball with her back to goal, and connect with runners",
                 "Wide players sprint in behind immediately — provide width and depth",
                 "Fullbacks provide immediate width as the team transitions forward",
                 "Attack before the opposition defensive structure recovers",
                 "Support underneath, beyond, and ahead of the ball",
                 "Commit runners forward aggressively — arrive in numbers",
                 "If immediate penetration is not available, secure possession and restart the attack"]:
        st.markdown(f"<div class='card card-gold'>→ {item}</div>", unsafe_allow_html=True)
with c2:
    for w in ["FAST.","DIRECT.","AGGRESSIVE."]:
        st.markdown(f"<span class='identity-word'>{w}</span>", unsafe_allow_html=True)
    st.markdown("<div class='quote-block'>Compact to win it. Direct to attack it.</div>", unsafe_allow_html=True)

st.divider()
st.markdown("### REAL GAME REFERENCES — ATTACKING TRANSITION")
c1, c2 = st.columns(2)
with c1:
    img = get_img("LB_providing_width_on_AT.png")
    if img: st.image(img, caption="Niagara FC — attacking transition in practice. The #8 wins the second ball and immediately switches play to the fullback, who provides width on the transition. This demonstrates our principles of immediate forward thought, quick ball circulation, and attacking before the opposition can recover their defensive organisation.", use_container_width=True)
    img = get_img("attacking_transition1.png")
    if img: st.image(img, caption="WEURO — Germany win possession and immediately play forward. Two runners sprint in behind simultaneously, attacking before Austria can recover their defensive shape.", use_container_width=True)
with c2:
    img = get_img("Attacking_transitions2.png")
    if img: st.image(img, caption="NWSL — possession won and play switched immediately to exploit width. Runner sprints beyond on the far side — attack before the defence recovers.", use_container_width=True)