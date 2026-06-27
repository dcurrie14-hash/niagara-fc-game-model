import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import apply_css, sidebar_brand, get_img
from utils import fig_zone1, fig_zone23, fig_connections_9, fig_zone4_women, fig_wide_play
import matplotlib.pyplot as plt

st.set_page_config(page_title="Attacking Organisation | Niagara FC", page_icon="⚽", layout="wide")
apply_css(); sidebar_brand()

st.markdown("# ATTACKING ORGANISATION")
st.markdown("<div style='font-family:Oswald,sans-serif;font-size:1em;color:#1E56D6;letter-spacing:1px;margin-bottom:12px;'>TEAM INTENTION: Control and progress the ball with tempo, purpose, and positional flexibility while creating opportunities to penetrate and attack quickly.</div>", unsafe_allow_html=True)

tabs = st.tabs(["📋 Overview","🔵 Zone 1 — Build","🔄 Zone 2, 3 & Into 4","🎯 Zone 4 — Finish","🔗 Connections #9","↔️ Wide Play"])

with tabs[0]:
    st.markdown("<div style='font-family:Oswald,sans-serif;font-size:0.95em;color:#FFD700;letter-spacing:1px;margin-bottom:12px;'>STRATEGY: Play forward whenever possible. Break lines quickly. Attack before the opposition can recover organisation.</div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### CORE PRINCIPLES")
        for item in ["Play forward whenever possible","Break lines quickly",
                     "Support underneath, beside, and beyond the ball",
                     "Use movement to disrupt defensive references",
                     "Create overloads around the ball",
                     "Stretch defensive compactness horizontally and vertically",
                     "Attack before the opponent can recover organisation",
                     "Encourage creativity and problem solving"]:
            st.markdown(f"<div class='card'>→ {item}</div>", unsafe_allow_html=True)
        st.markdown("<div class='quote-block'>The best way to disrupt defensive lines is to engage the first line of pressure.</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("### REAL GAME REFERENCES")
        img = get_img("match_d1f_forward_run.png")
        if img: st.image(img, caption="D1 Féminine — midfielder identifies the forward pass. #25 times the run beyond the defensive line. PLAY FORWARD. RUN FORWARD.", use_container_width=True)
        img = get_img("match_wsl_front3.png")
        if img: st.image(img, caption="WSL — distances and dispersal between the front three as midfielders progress with the ball. Width and depth maintained.", use_container_width=True)
    st.divider()
    img = get_img("Attacking_pic.png")
    if img: st.image(img, caption="Niagara FC — attacking organisation in practice. The RB (🔴) progresses play forward, the #10 (🔵) supports underneath the #9 (🟡), and the weak-side #11 (🔹) rotates centrally to create an overload around the ball. The #7 (🟡) and #9 (🟡) maintain depth and penetration. This demonstrates our principle of players occupying useful spaces rather than remaining fixed in positions.", use_container_width=True)
    img = get_img("match_nfc_attacking_shape.png")
    if img: st.image(img, caption="Niagara FC — attacking organisation in practice. The #7 (🟣) attacks with the ball while the #9 (🟣) provides a central reference point and the #11 (🟣) maintains width and depth. The #8 and #10 (🟡) support beyond the striker, creating multiple forward passing options and opportunities to penetrate. This demonstrates our principles of width, depth, support, and positional flexibility in possession.", use_container_width=True)

with tabs[1]:
    st.markdown("**Team Intention:** Create overloads against the first line of pressure to progress through, around, or beyond the opponent.")
    fig = fig_zone1(); st.pyplot(fig, use_container_width=True); plt.close()
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### Coaching Detail")
        for item in ["The goalkeeper is used as an extra outfield player to create numerical superiority",
                     "Centre backs begin inside the box to increase passing angles and stretch the pressing line",
                     "One centre back may play into the goalkeeper before splitting to disrupt pressing references",
                     "Midfielders rotate underneath and between lines to create forward passing options",
                     "High players pin defenders to create space between lines",
                     "Fullbacks adjust height depending on pressure and available space",
                     "Players are encouraged to drive forward if pressure creates open space"]:
            st.markdown(f"<div class='card'>{item}</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("#### On The Ball")
        for item in ["Players scan before receiving to identify forward options early",
                     "Forward passes are prioritized over unnecessary circulation",
                     "Players are encouraged to eliminate defenders through passing or dribbling",
                     "The objective is to commit defenders before exploiting the spaces they leave behind",
                     "Quick combinations are encouraged to break pressure",
                     "Recognize moments to play beyond the press early",
                     "Tempo of circulation should manipulate the opponent"]:
            st.markdown(f"<div class='card card-blue'>{item}</div>", unsafe_allow_html=True)
    with c3:
        st.markdown("#### Off The Ball")
        for item in ["Supporting players create angles underneath, beside, and beyond the ball",
                     "Movements are dynamic rather than positional to disrupt defensive references",
                     "Midfielders rotate to create overloads and passing lanes",
                     "Furthest players maintain width and depth to stretch compactness",
                     "Nearest players connect quickly around the ball to support second actions",
                     "Fullbacks adjust width and height depending on the positioning of the winger",
                     "High players remain connected to threaten space behind the defence"]:
            st.markdown(f"<div class='card card-gold'>{item}</div>", unsafe_allow_html=True)
    st.divider()
    st.markdown("### REAL GAME REFERENCES — ZONE 1")
    c1, c2 = st.columns(2)
    with c1:
        img = get_img("Build_up_from_GK.png")
        if img: st.image(img, caption="Niagara FC — GK stands on the ball to invite the press. As the opposition commits to pressing, space opens for our midfielders to receive between the lines.", use_container_width=True)
        img = get_img("short_gk_build.png")
        if img: st.image(img, caption="Niagara FC — CB takes the goal kick short to the GK, creating numerical superiority against the high press. The GK now has time and options to decide — short, long, or switch.", use_container_width=True)
    with c2:
        img = get_img("Goal_Kick_Option_to_go_long.png")
        if img: st.image(img, caption="Niagara FC — goal kick option to go long. Two options from the same situation — short to build or long to exploit. The opposition cannot predict which is coming.", use_container_width=True)

with tabs[2]:
    st.markdown("**Team Intention:** Advance the ball with tempo while creating central support and penetration opportunities.")
    st.markdown("<div class='quote-block'>The goal is never to stay in Zone 2 or 3 — it's to move through them as quickly as possible. Play forward, run forward, break lines.</div>", unsafe_allow_html=True)
    fig = fig_zone23(); st.pyplot(fig, use_container_width=True); plt.close()
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### Coaching Detail")
        for item in ["Combine centrally to attract pressure and create spaces beyond",
                     "Use third-man combinations to break lines",
                     "Create overloads around the ball",
                     "Encourage forward runs beyond the ball",
                     "Switch play when central spaces become overloaded",
                     "Attack weak-side spaces quickly after circulation"]:
            st.markdown(f"<div class='card'>{item}</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("#### On The Ball")
        for item in ["Receive on the half-turn whenever possible",
                     "Play forward quickly when space opens",
                     "Eliminate defenders through passing or dribbling",
                     "Attack defenders aggressively when isolated",
                     "Recognize moments to accelerate or secure possession",
                     "Encourage penetrative passes before the defensive structure is organized",
                     "Take the risk to play through lines — this is what takes our game to the next level"]:
            st.markdown(f"<div class='card card-blue'>{item}</div>", unsafe_allow_html=True)
    with c3:
        st.markdown("#### Off The Ball")
        for item in ["Constant movement around the ball",
                     "Support underneath, beside, and beyond",
                     "Forward runs beyond the back line create depth",
                     "Opposite side players remain connected for switches",
                     "Players adjust positions dynamically to create overloads",
                     "Arrivals into support spaces should be timed rather than static"]:
            st.markdown(f"<div class='card card-gold'>{item}</div>", unsafe_allow_html=True)
    st.divider()
    st.markdown("### REAL GAME REFERENCES — ZONE 2, 3 & INTO 4")
    c1, c2 = st.columns(2)
    with c1:
        img = get_img("3rd_man_run_z2-3.jpg")
        if img: st.image(img, caption="NWSL — third-man combination in Zone 2 & 3. Ball played in, combination breaks the first line, third player runs beyond.", use_container_width=True)
        img = get_img("match_wsl_cm_penetrate1.png")
        if img: st.image(img, caption="WSL — simple option is available but the midfielder takes the risk to play the penetrating pass through the line. That decision is what takes our game to the next level.", use_container_width=True)
        img = get_img("attacking_the_half_space.png")
        if img: st.image(img, caption="Niagara FC — wide player receives in the right wide channel and plays into the striker cutting into the half space. Width in the wide channel creates the opportunity in the half space.", use_container_width=True)
    with c2:
        img = get_img("3rd_man_comb_z2-3.jpg")
        if img: st.image(img, caption="NWSL — continuation of the combination, third player runs beyond into the space created, exploiting the defensive line.", use_container_width=True)
        img = get_img("match_wsl_cm_penetrate2.png")
        if img: st.image(img, caption="WSL — the penetrating pass rewards the forward runner, stretching the defense and creating space in behind.", use_container_width=True)
        img = get_img("match_wsl_third_man.png")
        if img: st.image(img, caption="WSL — third-man combination penetrating from Zone 3 into Zone 4, bypassing the defensive line.", use_container_width=True)
    img = get_img("match_d1f_zone23_fb.png")
    if img: st.image(img, caption="D1 Féminine — switch of play to the fullback providing width on the opposite side, creating a new attack from Zone 3 into Zone 4.", use_container_width=True)

with tabs[3]:
    st.markdown("**Team Intention:** Create and finish high-quality chances through aggressive penetration, dynamic movement, and sustained attacking pressure.")
    st.markdown("<div class='quote-block'>When the ball reaches the end line, the game is won or lost by the quality of runs and the timing of arrivals. Minimum 4 attack the box — every time.</div>", unsafe_allow_html=True)
    img = get_img("zone4_cutback_diagram.png")
    if img: st.image(img, use_container_width=True)
    st.divider()
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### Core Principles")
        for item in ["Attack with speed and aggression",
                     "Minimum of four players attack the box",
                     "Create movement across the defensive line",
                     "Sustain attacks through second actions and recycled possession",
                     "Attack spaces with timing and momentum",
                     "Ball carrier attacks the end line — forces defenders to commit"]:
            st.markdown(f"<div class='card'>{item}</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("#### Cutback Options")
        for item, clr in [("① #9 — near post cutback between 6-yd box and PK spot","card-gold"),
                           ("② #11 — longer ball to back post far side","card-blue"),
                           ("③ #10 — cutback to PK spot central","card-orange"),
                           ("④ #8 — arrives late at top of the D","card-red"),
                           ("#2 — overlapping support as extra option","card-red")]:
            st.markdown(f"<div class='{clr}'>→ {item}</div>", unsafe_allow_html=True)
    with c3:
        st.markdown("#### Women's Football Data")
        for stat, clr in [("Cutbacks are the #1 source — 28% of goals","card-gold"),
                           ("70% of goals from central areas inside the box","card-red"),
                           ("Transitions within 8 seconds = 22% of goals","card-red"),
                           ("Low crosses and driven balls = 20%","card-red"),
                           ("Combinations and one-twos = 15%","card-red")]:
            st.markdown(f"<div class='{clr}'>★ {stat}</div>", unsafe_allow_html=True)
    st.divider()
    st.markdown("### REAL GAME REFERENCES — ZONE 4")
    c1, c2 = st.columns(2)
    with c1:
        img = get_img("4_in_the_box.png")
        if img: st.image(img, caption="NWSL — wide player delivers from the right channel into a box with multiple runners arriving simultaneously. Back post and central zones occupied. Minimum 4 in the box principle in action.", use_container_width=True)
        img = get_img("match_wsl_striker_run.png")
        if img: st.image(img, caption="WSL — striker breaks the defensive line to go through on goal. Timed run, not static positioning.", use_container_width=True)
    with c2:
        img = get_img("match_wsl_zone4_box.png")
        if img: st.image(img, caption="WSL — striker central in the frame of goal, wide forward arriving at back post. Two attacking threats simultaneously.", use_container_width=True)
        img = get_img("match_wsl_third_man.png")
        if img: st.image(img, caption="WSL — third-man combination penetrating from Zone 3 into Zone 4, bypassing the defensive line.", use_container_width=True)
    img = get_img("womens_goals_scored.png")
    if img: st.image(img, caption="Women's Football Goal Analysis — evidence base for our Zone 4 principles.", use_container_width=True)

with tabs[4]:
    st.markdown("**Team Intention:** Create immediate support structures around the striker to prevent isolation and sustain attacks.")
    fig = fig_connections_9(); st.pyplot(fig, use_container_width=True); plt.close()
    c1, c2 = st.columns(2)
    with c1:
        for item in ["When playing forward, one midfielder must connect underneath or beyond the #9 as quickly as possible",
                     "Immediate support prevents isolation and sustains attacks",
                     "If immediate midfield support is unavailable, the opposite side winger moves centrally to connect",
                     "As the opposite winger moves inside, the opposite fullback provides width and depth",
                     "The nearest players connect centrally while the furthest maintain width and balance",
                     "Rotations should create support structures without sacrificing transition balance"]:
            st.markdown(f"<div class='card'>{item}</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='quote-block'>The #9 is our first outlet. When the long ball is played, she wins it, holds it with back to goal, and connects — giving our runners time to arrive. The #9 should never be isolated.</div>", unsafe_allow_html=True)
        img = get_img("holdup_9.png")
        if img: st.image(img, caption="Niagara FC — long ball played into #9 who holds with back to goal. #7 provides immediate support underneath, #11 makes the run beyond in behind — three connections in one moment.", use_container_width=True)
        img = get_img("match_d1f_reims_9_connections.png")
        if img: st.image(img, caption="D1 Féminine — #9 holds centrally, #8 & #10 arrive underneath and beyond, wide forwards stretch in behind.", use_container_width=True)

with tabs[5]:
    st.markdown("**Team Intention:** Attack the wide channels aggressively, isolate defenders in 1v1 situations, reach the end line, and deliver cutbacks into the box.")
    st.markdown("<div class='quote-block'>Width stretches the defence. The end line creates panic. The cutback is the finish. This is our preferred wide attack sequence.</div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        for item in ["Wide players attack defenders aggressively in 1v1 situations",
                     "Attack the end line to create cutback opportunities",
                     "Deliver early crosses before the defence is fully organized",
                     "Combine quickly around the wide channel to create overloads",
                     "Opposite side attackers attack weak-side spaces aggressively",
                     "Minimum 4 players in the box before the delivery"]:
            st.markdown(f"<div class='card'>{item}</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='quote-block'>Cutbacks are the #1 source of goals in women's football. When the ball goes wide, every available player attacks the box. Minimum 4 must arrive before the delivery.</div>", unsafe_allow_html=True)
    st.divider()
    st.markdown("### REAL GAME REFERENCES — WIDE PLAY")
    c1, c2 = st.columns(2)
    with c1:
        img = get_img("wide_play1.png")
        if img: st.image(img, caption="Australia vs France — wide player receives in the right wide channel, isolates the defender and drives at pace toward the end line.", use_container_width=True)
        img = get_img("isolate_1v1_wide_play.png")
        if img: st.image(img, caption="Niagara FC — wide player isolated in a 1v1 in the wide channel with no cover. The instruction is simple — attack, drive at them, and win the duel.", use_container_width=True)
    with c2:
        img = get_img("wide_play2.png")
        if img: st.image(img, caption="Australia vs France — the cutback is delivered into the box with multiple players arriving. Width created the chance, the cutback finished it.", use_container_width=True)
        img = get_img("wide_cutback_goal.png")
        if img: st.image(img, caption="Niagara FC — wide player drives into the half space toward the end line and provides the cutback. The movement creates the chance.", use_container_width=True)