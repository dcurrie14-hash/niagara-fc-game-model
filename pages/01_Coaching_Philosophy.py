import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import apply_css, sidebar_brand, get_img
st.set_page_config(page_title="Coaching Philosophy | Niagara FC", page_icon="🧠", layout="wide")
apply_css(); sidebar_brand()
st.markdown("# COACHING PHILOSOPHY")
st.markdown("<div class='quote-block'>\"We need to create enthusiasm for the game.\"</div>", unsafe_allow_html=True)

img = get_img("team_pic.jpeg")
if img:
    st.image(img, use_container_width=True)

st.divider()

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("### COACHING ENVIRONMENT")
    for item in [
        "Safe, demanding, and supportive",
        "High standards without fear of mistakes",
        "Encourage player ownership and leadership",
        "Develop players through realistic football situations",
        "Create enthusiasm for the game — players who love playing will always develop faster",
    ]:
        st.markdown(f"<div class='card'>✔ {item}</div>", unsafe_allow_html=True)
with c2:
    st.markdown("### COACHING BEHAVIOURS")
    for item in [
        "Guided discovery and questioning over direct instruction",
        "Detail without over-coaching",
        "Coach the problem, not just the action",
        "Use constraints to guide learning and shape behaviour",
        "Constant links between training and game moments",
        "Encourage players to adapt rather than memorise patterns",
    ]:
        st.markdown(f"<div class='card card-blue'>✔ {item}</div>", unsafe_allow_html=True)
with c3:
    st.markdown("### LEARNING ENVIRONMENT")
    for item in [
        "Mistakes are accepted as part of growth",
        "Players are encouraged to take risks",
        "Decision-making is valued over positional perfection",
        "Players have freedom to make decisions within our playing principles",
        "Players learn to recognise and solve game problems independently",
    ]:
        st.markdown(f"<div class='card card-gold'>✔ {item}</div>", unsafe_allow_html=True)
st.divider()
st.markdown("### WHAT WE WANT TO DEVELOP")
st.markdown("<div class='quote-block'>Football development should challenge, excite, and develop intelligent competitors who love the game.</div>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("#### Football Intelligence")
    for item in [
        "Understand the game",
        "Solve problems independently",
        "Make intelligent decisions",
        "Adapt to different situations",
    ]:
        st.markdown(f"<div class='card'>→ {item}</div>", unsafe_allow_html=True)
with c2:
    st.markdown("#### Character")
    for item in [
        "Embrace accountability",
        "Compete relentlessly",
        "Maintain intensity in every moment",
    ]:
        st.markdown(f"<div class='card card-red'>→ {item}</div>", unsafe_allow_html=True)
with c3:
    st.markdown("#### Mindset")
    for item in [
        "Play with courage and confidence",
        "Love the game",
        "Embrace risk — mistakes are part of the process",
    ]:
        st.markdown(f"<div class='card card-gold'>→ {item}</div>", unsafe_allow_html=True)
