import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import apply_css, sidebar_brand, get_img, fig_def_transition
import matplotlib.pyplot as plt

st.set_page_config(page_title="Defensive Transition | Niagara FC", page_icon="🔒", layout="wide")
apply_css(); sidebar_brand()

st.markdown("# DEFENSIVE TRANSITION")
st.markdown("<div style='font-family:Oswald,sans-serif;font-size:1em;color:#E53935;letter-spacing:1px;margin-bottom:12px;'>TEAM INTENTION: Win the ball back immediately on the first action — or drop into a compact defensive shape without delay.</div>", unsafe_allow_html=True)

st.markdown("<div style='font-family:Oswald,sans-serif;font-size:0.95em;color:#FFD700;letter-spacing:1px;margin-bottom:12px;'>STRATEGY: Win it back immediately if possible. If not, protect the middle and recover into shape.</div>", unsafe_allow_html=True)

fig = fig_def_transition(); st.pyplot(fig, use_container_width=True); plt.close()

c1, c2 = st.columns(2)
with c1:
    st.markdown("### COACHING DETAIL")
    for item in ["Press immediately on loss of possession — win it back on the first action",
                 "If the press does not work — drop into shape immediately, no chasing",
                 "The #6 protects the two centre backs and controls the central space",
                 "If #6 steps out to press — nearest player covers the central space immediately",
                 "Supporting players recover underneath and behind the ball",
                 "Delay forward progression and deny central penetration first",
                 "If attacking rotations leave spaces exposed — nearest players recover immediately",
                 "Players react to the moment first — positional recovery second",
                 "Once immediate danger is controlled — reorganize into team structure"]:
        st.markdown(f"<div class='card card-red'>→ {item}</div>", unsafe_allow_html=True)
    st.markdown("<div class='quote-block'>Defensive compactness and protection of central spaces take priority over positional perfection during transition moments.</div>", unsafe_allow_html=True)
with c2:
    st.markdown("### IMMEDIATE PRIORITIES")
    for priority, detail, clr in [
        ("WIN IT BACK","Press immediately — commit to winning on the first action. Nearest player leads, others support.","card-red"),
        ("DROP INTO SHAPE","If press fails — drop quickly and restore compactness. Never chase the ball.","card-orange"),
        ("PROTECT CENTRAL","Central spaces are protected before wide spaces. Force play wide.","card-gold"),
        ("#6 IS THE ANCHOR","She holds the line when everyone else presses. If she steps out — cover must be immediate.","card-blue"),
    ]:
        st.markdown(f"<div class='{clr}'><b>{priority}</b><br><small>{detail}</small></div>", unsafe_allow_html=True)
    st.markdown("<div class='quote-block'>We either win it back on the first action or we defend organised. Never disorganised.</div>", unsafe_allow_html=True)

st.divider()
st.markdown("### REAL GAME REFERENCES — DEFENSIVE TRANSITION")
st.markdown("#### Individual Defensive Transition — NFC #2 Recovery")
c1, c2 = st.columns(2)
with c1:
    img = get_img("def_trans1.png")
    if img: st.image(img, caption="Niagara FC — #2 reacts immediately after possession is lost, making a recovery sprint to get goal-side and win the ball back.", use_container_width=True)
with c2:
    img = get_img("def_trans2.png")
    if img: st.image(img, caption="Niagara FC — #2 wins the footrace and regains possession. Immediate individual defensive transition — react, recover, regain.", use_container_width=True)

st.divider()
st.markdown("#### Team Defensive Transition — Counter-Press & Drop Into Shape")
img = get_img("team_def_transition.png")
if img: st.image(img, caption="Niagara FC — #8 loses possession. Nearest players react immediately to counter-press around the ball. Others drop into a compact block, denying any forward passes. Defensive transition principle in action.", use_container_width=True)
