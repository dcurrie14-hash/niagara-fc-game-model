import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import apply_css, sidebar_brand, ROYAL, NAVY, WHITE, RED, GOLD, ORANGE, LBLUE
from utils import fig_5moments, get_img
import matplotlib.pyplot as plt

st.set_page_config(page_title="Niagara FC Game Model", page_icon="🔵", layout="wide")
apply_css(); sidebar_brand()

logo = get_img("nfc.png")
c_logo, c_title = st.columns([1, 5])
with c_logo:
    if logo: st.image(logo, width=120)
with c_title:
    st.markdown("# GAME MODEL")
    st.markdown("<div style='font-family:Oswald,sans-serif;font-size:1em;letter-spacing:2px;'><span style='color:#FFFFFF;font-weight:700;'>DAVIE CURRIE</span> <span style='color:#89B4FF;'>·  NIAGARA FC OPDL  ·</span> <span style='color:#FFFFFF;font-weight:700;'>CONCACAF B LICENSE</span></div>", unsafe_allow_html=True)
    st.markdown("<div style='font-family:Oswald,sans-serif;font-size:1.1em;color:#1E56D6;letter-spacing:2px;'>INTENSITY · AGGRESSION · PURPOSE · FREEDOM WITHIN STRUCTURE</div>", unsafe_allow_html=True)

st.markdown("<div class='quote-block'>\"The only expectation is to work hard and be all in. Development is the priority, but we still compete to win. We love players that hate to lose.\"</div>", unsafe_allow_html=True)

c1, c2 = st.columns([3, 2])
with c1:
    st.markdown("### OUR FOOTBALL IDENTITY")
    for item in [
        "Aggressive and forward-thinking — high tempo in and out of possession",
        "Brave in possession — play through pressure, not away from it",
        "Compact and connected defensively — protect central spaces first",
        "Competitive in every moment — love to win, hate to lose",
        "Freedom within structure — players solve problems, not coaches",
        "Structured without becoming robotic — intelligence over patterns",
    ]:
        st.markdown(f"<div class='card'>⚡ {item}</div>", unsafe_allow_html=True)
    st.markdown("<div class='quote-block'>\"We build intelligent players who can play in any system because they understand the game, not just our game.\"</div>", unsafe_allow_html=True)
with c2:
    st.markdown("### WHAT WE VALUE")
    for v in ["Intensity","Accountability","Courage","Problem Solving","Communication","Leadership","Coachability","Resilience"]:
        st.markdown(f"<span class='identity-word'>{v}</span>", unsafe_allow_html=True)

st.divider()
st.markdown("### THE 5 MOMENTS OF THE GAME")
st.markdown("<div style='font-family:Oswald,sans-serif;font-size:0.95em;color:#89B4FF;letter-spacing:1px;margin-bottom:12px;'>The principles stay the same, even when the moment changes.</div>", unsafe_allow_html=True)

fig = fig_5moments()
st.pyplot(fig, use_container_width=True)
plt.close()

m1, m2, m3, m4, m5 = st.columns(5)
moments = [
    ("1", "IN POSSESSION",       "Control and progress the ball with tempo and purpose. Play forward whenever possible.",                                              ROYAL),
    ("2", "DEFENSIVE TRANSITION","React immediately after losing possession. Win it back on the first action or drop into shape.",                                     RED),
    ("3", "OUT OF POSSESSION",   "Remain compact and connected. Deny central penetration. Force play wide.",                                                           RED),
    ("4", "ATTACKING TRANSITION","Attack before the opponent recovers organisation. First thought is always forward.",                                                  GOLD),
    ("5", "SET PIECES",          "Set pieces are not a break in the game — they are another opportunity to impose ourselves on the opposition.",                        LBLUE),
]
for col, (num, moment, desc, clr) in zip([m1, m2, m3, m4, m5], moments):
    with col:
        st.markdown(f"""
        <div style='background:{NAVY};border-top:4px solid {clr};padding:12px;
        border-radius:6px;height:100%;'>
        <div style='color:{clr};font-weight:700;font-size:0.85em;margin-bottom:6px;'>{num}. {moment}</div>
        <div style='color:#ccc;font-size:0.8em;line-height:1.5;'>{desc}</div>
        </div>""", unsafe_allow_html=True)

st.divider()
st.markdown("### NON-NEGOTIABLES")
c1, c2 = st.columns(2)
with c1:
    for item in [
        "Win it back immediately — if not, recover into shape",
        "First thought is always forward",
        "Be brave in possession — play through pressure",
        
    ]:
        st.markdown(f"<div class='card card-red'>🔴 {item}</div>", unsafe_allow_html=True)
with c2:
    for item in [
        "Constant communication — on and off the ball",
        "Work hard and be all in — every session, every minute",
	"Fight for every second ball and loose ball",
    ]:
        st.markdown(f"<div class='card card-red'>🔴 {item}</div>", unsafe_allow_html=True)