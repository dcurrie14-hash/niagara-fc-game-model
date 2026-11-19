
import streamlit as st
import sys, os

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from utils import apply_css, sidebar_brand, get_img

st.set_page_config(
    page_title="Defensive Organisation | Niagara FC",
    page_icon="🛡️",
    layout="wide"
)

apply_css()
sidebar_brand()

st.markdown("# DEFENSIVE ORGANISATION")

st.markdown(
    "<div style='font-family:Oswald,sans-serif;font-size:1em;"
    "color:#E53935;letter-spacing:1px;margin-bottom:12px;'>"
    "OVERALL TEAM INTENTION: Remain compact and connected. Deny "
    "central penetration, influence opposition play and recognise "
    "opportunities to regain possession."
    "</div>",
    unsafe_allow_html=True
)


def tab_intention(intention, strategy):
    """Consistent red intention / gold strategy hierarchy for each tab."""
    st.markdown(
        f"<div style='font-family:Oswald,sans-serif;font-size:0.95em;"
        f"color:#E53935;letter-spacing:0.6px;margin:10px 0 8px;'>"
        f"{intention}</div>", unsafe_allow_html=True
    )
    st.markdown(
        f"<div style='font-family:Oswald,sans-serif;font-size:0.95em;"
        f"color:#F5C518;letter-spacing:0.6px;margin-bottom:16px;'>"
        f"{strategy}</div>", unsafe_allow_html=True
    )

tabs = st.tabs([
    "Principles",
    "Compact Block",
    "Press & Block Systems",
    "Pressing Triggers"
])


# ==================================================
# TAB 1 — PRINCIPLES
# ==================================================

with tabs[0]:

    tab_intention(
        "PRINCIPLES INTENTION: Protect central spaces, maintain defensive "
        "balance and collectively limit opposition attacking options.",
        "STRATEGY: Deny the middle. Direct play wide. Delay when needed. "
        "Recognise opportunities to regain possession."
    )

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("### DEFENSIVE PRINCIPLES")

        principles = [
            (
                "DENY",
                "Deny central penetration. If the ball is recoverable, "
                "press immediately. If not, recover into shape."
            ),
            (
                "DIRECT",
                "Force play into wide and predictable areas where "
                "pressure can be applied collectively."
            ),
            (
                "BALANCE",
                "Maintain team shape and protect central spaces "
                "when teammates press forward."
            ),
            (
                "DELAY",
                "If you cannot win it back immediately, delay "
                "forward progress and allow teammates to recover."
            ),
            (
                "CONTROL & RESTRAINT",
                "Be patient and organised. Recognise the right "
                "moment to press rather than chasing the ball."
            ),
        ]

        for principle, description in principles:
            st.markdown(
                f"<div class='card card-red'>"
                f"<b>{principle}</b><br>"
                f"<small>{description}</small></div>",
                unsafe_allow_html=True
            )

        st.markdown("### CENTRE BACK PRINCIPLES")

        for item in [
            "Protect central spaces first",
            "Step aggressively to intercept",
            "Win first contacts and aerial duels",
            "Maintain compact distances to the midfield",
        ]:
            st.markdown(
                f"<div class='card card-red'>{item}</div>",
                unsafe_allow_html=True
            )

    with c2:
        st.markdown("### THE #6 ROLE DEFENSIVELY")

        st.markdown(
            "<div class='quote-block'>"
            "In our 4-1-4-1 mid-block, the #6 screens in front "
            "of the back four and protects central spaces. "
            "In our 4-2-4 high press, #6 and #8 take responsibility "
            "for opposition midfielders. In either shape, if #6 "
            "steps out, a teammate must protect the space left behind."
            "</div>",
            unsafe_allow_html=True
        )

        for item in [
            "Screens the back four in the mid-block — reads the game before pressing",
            "Adjusts to the pressing structure — marks centrally in the high press",
            "Protects the centre backs and communicates central cover",
            "Wins second balls in central areas",
            "Reacts quickly in defensive transitions — protects or presses as needed",
            "If #6 steps out — nearest player covers the central space",
            "Recognises and communicates pressing triggers",
        ]:
            st.markdown(
                f"<div class='card'>{item}</div>",
                unsafe_allow_html=True
            )

    st.divider()
    st.markdown("### DEFENSIVE BLOCK TYPES")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            "<div class='card card-red'>"
            "<b>HIGH PRESS</b><br>"
            "<small>Shape: 4-2-4<br><br>"
            "The #9 and #10 engage the opposition centre backs "
            "while #7 and #11 lock onto the fullbacks. "
            "#6 and #8 control central midfield options. "
            "The #9 curves the press to deny the return pass "
            "to the goalkeeper and trap play on one side."
            "</small></div>",
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            "<div class='card card-gold'>"
            "<b>MID-BLOCK</b><br>"
            "<small>Shape: 4-1-4-1<br><br>"
            "Our default defensive structure. Stay compact "
            "and connected, protect central spaces and shift "
            "collectively towards the ball. Press on recognised "
            "triggers with supporting cover."
            "</small></div>",
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            "<div class='card card-blue'>"
            "<b>LOW BLOCK</b><br>"
            "<small>Shape: 4-5-1<br><br>"
            "Protect space closer to our goal. Maintain compact "
            "distances, defend the penalty area and remain "
            "connected. Be ready to counter on regain."
            "</small></div>",
            unsafe_allow_html=True
        )


# ==================================================
# TAB 2 — COMPACT BLOCK
# ==================================================

with tabs[1]:

    tab_intention(
        "COMPACT BLOCK INTENTION: Remain compact vertically and horizontally, "
        "protect the middle and force play into predictable wide areas.",
        "STRATEGY: Protect the middle. Stay connected. Shift together. "
        "Press when the opportunity is there."
    )

    st.markdown(
        "<div class='quote-block'>"
        "The 4-1-4-1 mid-block is our default defensive structure. "
        "We remain compact and connected, protect central spaces "
        "and shift collectively towards the ball. "
        "Our objective is to force the opposition into predictable "
        "areas where we can press and regain possession."
        "</div>",
        unsafe_allow_html=True
    )

    # NEW 4-1-4-1 DIAGRAM
    img = get_img("defensive_midblock_4141.png")

    if img:
        st.image(img, use_container_width=True)
    else:
        st.warning(
            "Image not found: defensive_midblock_4141.png"
        )

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("#### Core Principles")

        for item in [
            "Defend primarily from a compact 4-1-4-1 mid-block",
            "Protect central spaces first — force play wide",
            "Create regains in predictable areas",
            "Transition quickly after regains",
            "The #6 screens in front of the two centre backs",
            "The midfield four shift together as the ball travels",
            "If #6 steps out — central space must be covered immediately",
        ]:
            st.markdown(
                f"<div class='card card-red'>→ {item}</div>",
                unsafe_allow_html=True
            )

    with c2:
        st.markdown("#### Defensive Compactness")

        for item in [
            "The midfield and back line shift together to reduce spaces between units",
            "Compact distances improve pressure, cover, communication and recovery",
            "The nearest player applies pressure while teammates provide cover",
            "Far-side players tuck in to maintain balance against switches",
            "The #9 helps screen central passing options ahead of the midfield",
            "Protect central spaces rather than becoming stretched by wide pressure",
        ]:
            st.markdown(
                f"<div class='card'>{item}</div>",
                unsafe_allow_html=True
            )

    st.divider()
    st.markdown(
        "### REAL GAME REFERENCES — COMPACT DEFENSIVE SHAPE"
    )

    c1, c2 = st.columns(2)

    with c1:
        img = get_img("match_nwsl_compact_def.png")
        if img:
            st.image(
                img,
                caption="NWSL — compact defensive block protecting central spaces. Units stay connected and force play wide.",
                use_container_width=True
            )

        img = get_img("mid-block.png")
        if img:
            st.image(
                img,
                caption="Niagara FC — mid-block in action. Two connected defensive lines deny central penetration.",
                use_container_width=True
            )

        img = get_img("match_arsenal_press1.png")
        if img:
            st.image(
                img,
                caption="WSL Arsenal — low-block organisation. Central options are denied while the team remains compact behind the ball.",
                use_container_width=True
            )

    with c2:
        img = get_img("defensive_shape.png")
        if img:
            st.image(
                img,
                caption="Niagara FC — compact defensive shape. Players protect central spaces and keep play on one side.",
                use_container_width=True
            )

        img = get_img(
            "10_players_compact_shape__shrink_the_field_.png"
        )
        if img:
            st.image(
                img,
                caption="Niagara FC — ten outfield players organised to shrink the available playing space.",
                use_container_width=True
            )

        img = get_img("10_players_compact_shape.png")
        if img:
            st.image(
                img,
                caption="Niagara FC — full team compact and connected, protecting the middle and forcing play wide.",
                use_container_width=True
            )


# ==================================================
# TAB 3 — PRESS & BLOCK SYSTEMS
# ==================================================

with tabs[2]:

    tab_intention(
        "PRESS & BLOCK SYSTEMS INTENTION: Coordinate pressure, cover and "
        "balance to disrupt opposition build-up and create regains.",
        "STRATEGY: Match pressure to the game situation. Screen passing "
        "options, direct play and move together behind the press."
    )

    st.markdown(
        "<div class='quote-block'>"
        "Our 4-2-4 high press is player-oriented and collective. "
        "The front four lock onto the opposition back four, "
        "while #6 and #8 take responsibility for central midfielders. "
        "The #9 curves the press to deny the return pass to the "
        "goalkeeper, helping trap play on one side."
        "</div>",
        unsafe_allow_html=True
    )

    # NEW 4-2-4 HIGH-PRESS DIAGRAM
    img = get_img("defensive_highpress_424.png")

    if img:
        st.image(img, use_container_width=True)
    else:
        st.warning(
            "Image not found: defensive_highpress_424.png"
        )

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("#### Press Behaviours")

        for item in [
            "The #9 curves the pressing run to deny the return pass to the goalkeeper",
            "The #10 engages the opposite centre back and limits the switch",
            "The #7 and #11 lock onto opposition fullbacks",
            "The #6 and #8 take responsibility for central midfield opponents",
            "The back four step forward and remain connected behind the press",
            "Force predictable play and create regains in advantageous areas",
            "Press collectively — everyone reacts to the movement of the ball",
            "If a player steps out, teammates adjust to provide cover and balance",
        ]:
            st.markdown(
                f"<div class='card card-red'>{item}</div>",
                unsafe_allow_html=True
            )

        st.markdown("#### Press Types")

        press_types = [
            (
                "HIGH PRESS",
                "Shape: 4-2-4",
                "Player-oriented pressure. The front four match "
                "the opposition back four, #6 and #8 control "
                "midfield opponents, and the #9 curves the press "
                "to deny the goalkeeper return and trap play wide."
            ),


            (
                "MID-BLOCK",
                "Shape: 4-1-4-1",
                "Our default defensive shape. Protect the middle, "
                "stay connected and shift collectively. "
                "Apply pressure on recognised triggers."
            ),
            (
                "LOW BLOCK",
                "Shape: 4-5-1",
                "Protect space closer to goal. Remain compact, "
                "defend the box and prepare to counter on regain."
            ),
        ]

        for block, shape, detail in press_types:
            st.markdown(
                f"<div class='card'>"
                f"<b>{block}</b> "
                f"<span style='color:#888;font-size:0.8em;'>"
                f"— {shape}</span><br>"
                f"<small>{detail}</small>"
                f"</div>",
                unsafe_allow_html=True
            )

    with c2:
        st.markdown("#### Press Sequence Reference — WSL")

        img = get_img("match_arsenal_press2.png")
        if img:
            st.image(
                img,
                caption=(
                    "Step 1 — Player-oriented press engages. "
                    "The striker's pressing run influences direction "
                    "while supporting players close passing options."
                ),
                use_container_width=True
            )

        img = get_img("match_arsenal_press3.png")
        if img:
            st.image(
                img,
                caption=(
                    "Step 2 — The press is maintained. "
                    "Supporting players close the escape routes "
                    "while the team remains connected and high."
                ),
                use_container_width=True
            )

    st.divider()

    img = get_img("Def_goal_Kick.png")
    if img:
        st.image(
            img,
            caption=(
                "Niagara FC — pressing high on the opposition goal kick. "
                "Front players deny short passing options while "
                "the team steps forward together."
            ),
            use_container_width=True
        )

    st.divider()
    st.markdown("### INTERNATIONAL REFERENCES — PRESS SYSTEMS")

    c1, c2, c3 = st.columns(3)

    with c1:
        img = get_img("low_block_player_oriented.png")
        if img:
            st.image(
                img,
                caption=(
                    "Niagara FC — the #6 holds centrally while "
                    "teammates press around her, protecting "
                    "the back line and maintaining balance."
                ),
                use_container_width=True
            )

    with c2:
        img = get_img("defensive_trap_weuro.png")
        if img:
            st.image(
                img,
                caption=(
                    "Women's EURO — defensive trap. "
                    "Players limit short passing options, "
                    "making the opposition's next action predictable."
                ),
                use_container_width=True
            )

    with c3:
        img = get_img("high_press_touch_tight.png")
        if img:
            st.image(
                img,
                caption=(
                    "Women's EURO — aggressive, connected high press. "
                    "Players engage opponents, deny short passes "
                    "and force play under pressure."
                ),
                use_container_width=True
            )


# ==================================================
# TAB 4 — PRESSING TRIGGERS
# ==================================================

with tabs[3]:

    tab_intention(
        "PRESSING TRIGGERS INTENTION: Recognise opposition vulnerability "
        "and react collectively to restrict options and regain possession.",
        "STRATEGY: Recognise the cue. Press at the right angle. "
        "Close nearby options. Protect the space behind the press."
    )

    st.markdown("### PRESSING TRIGGERS")

    st.markdown(
        "<div class='quote-block'>"
        "Every player must recognise pressing triggers immediately. "
        "When a trigger appears, the player best positioned applies pressure "
        "and teammates react together. We close passing options, "
        "protect central spaces and make the opposition's next "
        "action predictable."
        "</div>",
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:
        for trigger in [
            "Poor first touch — ball bouncing or away from feet",
            "Back pass — opponent under pressure plays backwards",
            "Square pass between centre backs — slow and predictable",
            "Wide player receiving while facing their own goal",
        ]:
            st.markdown(
                f"<div class='card card-red'>{trigger}</div>",
                unsafe_allow_html=True
            )

    with c2:
        for trigger in [
            "Slow circulation — opponent telegraphs the next pass",
            "Goalkeeper preparing a short pass — front four coordinate the press",
            "Long ball played — compete for first contact and win the second ball",
            "Isolated player — no immediate support options",
        ]:
            st.markdown(
                f"<div class='card card-red'>{trigger}</div>",
                unsafe_allow_html=True
            )

    st.markdown("### PRESSING TRIGGER — COLLECTIVE RESPONSE")

    img = get_img("pressing_triggers.png")
    if img:
        st.image(img, use_container_width=True)
    else:
        st.warning("Image not found: pressing_triggers.png")

    st.divider()

    img = get_img("closing_down_aggressive.png")
    if img:
        st.image(
            img,
            caption=(
                "Niagara FC — a poor first touch triggers immediate "
                "pressure. Two players close the ball carrier, "
                "forcing play into a predictable area and "
                "creating an opportunity to regain possession."
            ),
            use_container_width=True
        )
