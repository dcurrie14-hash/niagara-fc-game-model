import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import apply_css, sidebar_brand, get_img, fig_defensive_block, fig_pressing_trap
import matplotlib.pyplot as plt

st.set_page_config(page_title="Defensive Organisation | Niagara FC", page_icon="🛡️", layout="wide")
apply_css(); sidebar_brand()

st.markdown("# DEFENSIVE ORGANISATION")
st.markdown("<div style='font-family:Oswald,sans-serif;font-size:1em;color:#E53935;letter-spacing:1px;margin-bottom:12px;'>TEAM INTENTION: Remain compact and connected while denying central penetration and forcing play into predictable wide areas.</div>", unsafe_allow_html=True)

tabs = st.tabs(["📋 Principles","🛡️ Compact Block","🔴 Press & Block Systems","⚡ Pressing Triggers"])

# ═══════════════════════════════════════════════════
# TAB 1 — PRINCIPLES
# ═══════════════════════════════════════════════════
with tabs[0]:
    st.markdown("<div style='font-family:Oswald,sans-serif;font-size:0.95em;color:#FFD700;letter-spacing:1px;margin-bottom:12px;'>STRATEGY: Protect the middle. Force play wide. Create regains in predictable areas.</div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### DEFENSIVE PRINCIPLES")
        for p, d in [
            ("DENY",               "Deny central penetration. If the ball is recoverable, press immediately. If not, recover into shape."),
            ("DIRECT",             "Force play into wide and predictable areas where pressure can be applied collectively."),
            ("BALANCE",            "Maintain team shape — the #6 protects the CB line when others press forward."),
            ("DELAY",              "If you cannot win it back immediately, delay forward progress. Buy time for recovery."),
            ("CONTROL & RESTRAINT","Be patient and organised. Win the ball back in the right moment, not desperately."),
        ]:
            st.markdown(f"<div class='card card-red'><b>{p}</b><br><small>{d}</small></div>", unsafe_allow_html=True)

        st.markdown("### CENTRE BACK PRINCIPLES")
        for item in [
            "Protect central spaces first",
            "Step aggressively to intercept",
            "Win first contacts and aerial duels",
            "Maintain compact distances to the #6",
        ]:
            st.markdown(f"<div class='card card-red'>🛡️ {item}</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("### THE #6 ROLE DEFENSIVELY")
        st.markdown("<div class='quote-block'>The #6 is the anchor of our defensive shape. When everyone else presses, she holds. When the back four steps up, she screens. When we transition, she protects. If she steps out to press, that central space must be covered immediately.</div>", unsafe_allow_html=True)
        for item in [
            "Screens the back four at all times — reads the game before pressing",
            "Holds position when #8 and #10 press forward",
            "Protects the two CBs — stays between the lines",
            "Wins second balls in central areas",
            "First to react on defensive transitions — holds the line",
            "If #6 steps out — nearest player covers the central space immediately",
            "Recognises and communicates press triggers",
        ]:
            st.markdown(f"<div class='card'>{item}</div>", unsafe_allow_html=True)

    st.divider()
    st.markdown("### DEFENSIVE BLOCK TYPES")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='card card-red'><b>🔴 HIGH PRESS</b><br><small>Shape: 4-2-4<br><br>Activated by pressing triggers. The #10 joins the front line to create a front four. The team presses aggressively to lock play to one side while the #6 screens centrally.</small></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card card-gold'><b>🟡 MID-BLOCK</b><br><small>Shape: 4-1-4-1<br><br>Default shape. Compact block. Press activated on triggers only. One presses, one covers. Protect central spaces.</small></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='card card-blue'><b>🔵 LOW BLOCK</b><br><small>Shape: 4-5-1<br><br>Protecting a lead. Player-oriented organisation. Shape first — counter immediately on regain. Stay compact and connected.</small></div>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# TAB 2 — COMPACT BLOCK
# ═══════════════════════════════════════════════════
with tabs[1]:
    st.markdown("<div class='quote-block'>The mid-block is our default defensive structure because it protects central spaces, maintains compactness, and creates opportunities to regain possession in predictable areas.</div>", unsafe_allow_html=True)
    fig = fig_defensive_block(); st.pyplot(fig, use_container_width=True); plt.close()
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Core Principles")
        for item in [
            "Defend primarily from a compact mid-block",
            "Protect central spaces first — force play wide",
            "Create regains in predictable areas",
            "Transition quickly after regains",
            "The #6 provides protection to the two centre backs",
            "The #6 provides balance when teammates press forward",
            "If #6 steps out — central space must be covered immediately",
        ]:
            st.markdown(f"<div class='card card-red'>→ {item}</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("#### Defensive Compactness")
        for item in [
            "The midfield and back line shift together to reduce spaces between units",
            "Compact distances improve pressure, cover, communication, and recovery speed",
            "Supporting defenders remain underneath pressure to protect central spaces",
            "Far-side players remain connected to maintain balance against switches",
            "The team prioritizes central protection over excessive pressure wide",
        ]:
            st.markdown(f"<div class='card'>{item}</div>", unsafe_allow_html=True)

    st.divider()
    st.markdown("### REAL GAME REFERENCES — COMPACT DEFENSIVE SHAPE")
    c1, c2 = st.columns(2)
    with c1:
        img = get_img("match_nwsl_compact_def.png")
        if img: st.image(img, caption="NWSL — compact defensive block protecting central spaces. Units connected, central spaces protected, play forced wide.", use_container_width=True)
        img = get_img("mid-block.png")
        if img: st.image(img, caption="Niagara FC — mid-block in action. Two clear defensive lines denying central penetration. Opposition forced to play in front of the block.", use_container_width=True)
        img = get_img("match_arsenal_press1.png")
        if img: st.image(img, caption="WSL Arsenal — low block defensive organisation. Front players direct play into a predictable area, cutting off central options while the team stays compact and connected behind the ball.", use_container_width=True)
    with c2:
        img = get_img("defensive_shape.png")
        if img: st.image(img, caption="Niagara FC — compact defensive shape splitting the field in half. Players deny central space, keeping play on one side and forcing the opposition into predictable areas.", use_container_width=True)
        img = get_img("10_players_compact_shape__shrink_the_field_.png")
        if img: st.image(img, caption="Niagara FC — 10 outfield players in compact defensive shape, numbered and organised. Shrink the field, protect central spaces.", use_container_width=True)
        img = get_img("10_players_compact_shape.png")
        if img: st.image(img, caption="Niagara FC — full team compact and connected. Central spaces protected and play forced into predictable wide areas.", use_container_width=True)

# ═══════════════════════════════════════════════════
# TAB 3 — PRESS & BLOCK SYSTEMS
# ═══════════════════════════════════════════════════
with tabs[2]:
    st.markdown("<div class='quote-block'>Our press is a hybrid system — player-oriented pressure with the #6 staying free to screen centrally. The front players press aggressively on triggers, the #6 protects the space in behind.</div>", unsafe_allow_html=True)
    fig = fig_pressing_trap(); st.pyplot(fig, use_container_width=True); plt.close()
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Press Behaviours")
        for item in [
            "The nearest player presses on an angle to block passing options",
            "Supporting players close spaces underneath the ball",
            "Force predictable play and create regains in advantageous areas",
            "Press collectively, not individually",
            "When the opposition GK has the ball — press front line immediately",
            "#6 stays free — screens centrally, does not commit to press",
            "If #6 steps out — nearest player covers central space immediately",
        ]:
            st.markdown(f"<div class='card card-red'>{item}</div>", unsafe_allow_html=True)

        st.markdown("#### Press Types")
        press_types = [
            ("🔴 HIGH PRESS",  "Shape: 4-2-4",   "Activated by pressing triggers. The #10 joins the front line to create a front four. The team presses aggressively to lock play to one side while the #6 screens centrally."),
            ("🟡 MID-BLOCK",   "Shape: 4-1-4-1", "Default shape. Compact block. Press activated on triggers only. One presses, one covers."),
            ("🔵 LOW BLOCK",   "Shape: 4-5-1",   "Protecting a lead. Player-oriented organisation. Shape first — counter immediately on regain."),
        ]
        for block, shape, detail in press_types:
            st.markdown(f"<div class='card'><b>{block}</b> <span style='color:#888;font-size:0.8em;'>— {shape}</span><br><small>{detail}</small></div>", unsafe_allow_html=True)

    with c2:
        st.markdown("#### Press Sequence Reference — WSL")
        img = get_img("match_arsenal_press2.png")
        if img: st.image(img, caption="Step 1 — Player-oriented press engages. Striker's pressing run forces direction. Supporting players close the space underneath.", use_container_width=True)
        img = get_img("match_arsenal_press3.png")
        if img: st.image(img, caption="Step 2 — Press maintained. Two players close simultaneously, cutting off the escape route. Team stays connected and high.", use_container_width=True)

    st.divider()
    img = get_img("Def_goal_Kick.png")
    if img: st.image(img, caption="Niagara FC — pressing high on the opposition goal kick. Front three lock short passing options while the team steps forward together.", use_container_width=True)

    st.divider()
    st.markdown("### INTERNATIONAL REFERENCES — PRESS SYSTEMS")
    c1, c2, c3 = st.columns(3)
    with c1:
        img = get_img("low_block_player_oriented.png")
        if img: st.image(img, caption="Niagara FC — #6 (circled) holds centrally while teammates press around her. She screens the space in behind, protecting the back line and maintaining defensive balance.", use_container_width=True)
    with c2:
        img = get_img("defensive_trap_weuro.png")
        if img: st.image(img, caption="WEURO — defensive trap in action. Players limit short passing options, forcing the ball back to the GK. The press has succeeded in making play predictable.", use_container_width=True)
    with c3:
        img = get_img("high_press_touch_tight.png")
        if img: st.image(img, caption="WEURO — high press touch tight. Players step to their opponents immediately, denying the short pass and forcing the long ball. Aggressive, connected, purposeful.", use_container_width=True)

# ═══════════════════════════════════════════════════
# TAB 4 — PRESSING TRIGGERS
# ═══════════════════════════════════════════════════
with tabs[3]:
    st.markdown("### PRESSING TRIGGERS")
    st.markdown("<div class='quote-block'>Every player on the team must recognise pressing triggers instantly. When the trigger fires — the nearest player presses, everyone else reacts. The #6 holds.</div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        for t in [
            "Poor first touch — ball bouncing or away from feet",
            "Back pass — opponent under pressure plays back",
            "Square pass between CBs — slow and predictable",
            "Wide player receiving facing own goal",
        ]:
            st.markdown(f"<div class='card card-red'>🔴 {t}</div>", unsafe_allow_html=True)
    with c2:
        for t in [
            "Slow circulation — opponent telegraphs next pass",
            "GK has ball — press front line immediately",
            "Long ball played — win the second ball aggressively",
            "Isolated player — no immediate support options",
        ]:
            st.markdown(f"<div class='card card-red'>🔴 {t}</div>", unsafe_allow_html=True)

    st.divider()
    st.markdown("### TRANSITION INTO DEFENCE")
    st.markdown("<div class='quote-block'>When we lose the ball — press immediately and win it back on the first action. If the press doesn't work, drop into shape immediately. If the #6 steps out to press, the space she vacates centrally must be covered immediately. Never lose defensive compactness.</div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        for item in [
            "Win it back on the first action — if not, drop into shape immediately",
            "Nearest player to ball presses — no hesitation",
            "#6 holds position — protects the back four",
            "If #6 steps out — central space covered immediately",
        ]:
            st.markdown(f"<div class='card card-red'>{item}</div>", unsafe_allow_html=True)
    with c2:
        for item in [
            "If press is broken — drop quickly into compact shape",
            "Communicate immediately — organise before they attack",
            "Back line holds a high line until the press is broken",
            "Win second balls aggressively — don't let them settle",
        ]:
            st.markdown(f"<div class='card'>{item}</div>", unsafe_allow_html=True)

    st.divider()
    img = get_img("closing_down_aggressive.png")
    if img: st.image(img, caption="Niagara FC — poor touch triggers the press. Two players press immediately, forcing play into a predictable area and creating the regain.", use_container_width=True)
