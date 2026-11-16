
import streamlit as st
import sys
import os

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from utils import apply_css, sidebar_brand, get_img

st.set_page_config(
    page_title="Set Pieces | Niagara FC",
    page_icon="🎯",
    layout="wide"
)

apply_css()
sidebar_brand()

# Improve heading contrast on the dark Game Model background
st.markdown("""
<style>
[data-testid="stMain"] h2,
[data-testid="stMain"] h3,
[data-testid="stMain"] h4,
[data-testid="stMain"] h5 {
    color: #EAF2FF !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("# SET PIECES & RESTARTS")

st.markdown(
    "<div class='quote-block'>"
    "Set pieces are not a break in the game — they are another "
    "opportunity to impose ourselves on the opposition."
    "</div>",
    unsafe_allow_html=True
)

tabs = st.tabs([
    "⚽ Attacking Corners",
    "🎯 Attacking Free Kicks",
    "🛡️ Defending Set Pieces",
    "🔄 Throw-Ins & Restarts"
])


# ==================================================
# TAB 1 — ATTACKING CORNERS
# ==================================================

with tabs[0]:

    st.markdown(
        "<div class='quote-block'>"
        "Create space. Attack the delivery. React to the second ball."
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown("### CORNER PRINCIPLES")

    p1, p2, p3 = st.columns(3)

    with p1:
        st.markdown(
            "<div class='card'>"
            "⚽ <strong>Delivery & First Contact</strong><br><br>"
            "Deliver into the intended attacking area. "
            "Create space for the primary aerial target and "
            "attack the first contact with conviction."
            "</div>",
            unsafe_allow_html=True
        )

    with p2:
        st.markdown(
            "<div class='card'>"
            "⚽ <strong>Box Movement</strong><br><br>"
            "Use coordinated movements to disrupt defenders "
            "and create space. Attack complementary areas "
            "around the goalkeeper and six-yard box."
            "</div>",
            unsafe_allow_html=True
        )

    with p3:
        st.markdown(
            "<div class='card'>"
            "⚽ <strong>Second Ball & Cover</strong><br><br>"
            "Position supporting players to attack rebounds "
            "and second balls. Maintain cover outside the box "
            "to protect against counterattacks."
            "</div>",
            unsafe_allow_html=True
        )

    st.markdown(
        "<div class='card'>"
        "⚽ <strong>Short Corner</strong> — Recognise opportunities "
        "to combine quickly, create an overload or improve "
        "the angle of delivery."
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='quote-block'>"
        "Our routines may change depending on the opposition "
        "and the opportunities we identify. Our principles "
        "remain consistent: create space, attack the delivery "
        "and react to the second ball."
        "</div>",
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### NIAGARA FC IN ACTION — EXAMPLE CORNER ROUTINE")

    i1, i2 = st.columns(2)

    with i1:
        img_routine = get_img("corner_routine.png")

        if img_routine:
            st.image(
                img_routine,
                caption=(
                    "Niagara FC — Example attacking corner routine. "
                    "One variation of our attacking principles."
                ),
                use_container_width=True
            )
        else:
            st.warning("Image not found: corner_routine.png")

    with i2:
        img_nfc = get_img("attacking_corner.png")

        if img_nfc:
            st.image(
                img_nfc,
                caption=(
                    "Niagara FC — Back-post runners attack through "
                    "the six-yard box, creating space for the "
                    "primary aerial target. Supporting players "
                    "prepare for second balls and defensive transition."
                ),
                use_container_width=True
            )

    st.divider()

    st.markdown("### PROFESSIONAL REFERENCES")

    r1, r2 = st.columns(2)

    with r1:
        img_ger = get_img("Corner_att_example.png")

        if img_ger:
            st.image(
                img_ger,
                caption=(
                    "Germany Women (Olympics) — Coordinated movement "
                    "through the six-yard box creates space "
                    "for an attacking delivery."
                ),
                use_container_width=True
            )

    with r2:
        img_esp = get_img("attack_set-piece.jpg")

        if img_esp:
            st.image(
                img_esp,
                caption="Spain (Olympics) — Attacking corner sequence.",
                use_container_width=True
            )



# ==================================================
# TAB 2 — ATTACKING FREE KICKS
# ==================================================

with tabs[1]:

    st.markdown(
        "<div class='quote-block'>"
        "Make intelligent decisions — play quickly when the "
        "opportunity exists, organise when it does not."
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown("### ATTACKING FREE KICKS")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            "<div class='card'>"
            "🔴 <strong>Zones 1 & 2</strong><br><br>"
            "Recognise opportunities to restart immediately. "
            "Play forward when possible, using the first "
            "available option to progress."
            "</div>",
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            "<div class='card'>"
            "🔴 <strong>Zone 3</strong><br><br>"
            "Exploit an unorganised defence. Play forward, "
            "combine or switch quickly when the opportunity "
            "exists. If not, organise an effective delivery "
            "or attacking restart."
            "</div>",
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            "<div class='card'>"
            "🔴 <strong>Zone 4</strong><br><br>"
            "Assess the opportunity. Choose between a direct "
            "shot, a coordinated delivery or a quick combination. "
            "Attack the penalty area with purposeful movements."
            "</div>",
            unsafe_allow_html=True
        )

    st.markdown(
        "<div class='quote-block'>"
        "Think forward. Play forward. Run forward. "
        "The decision depends on the position of the ball, "
        "the organisation of the opposition and the "
        "opportunity available."
        "</div>",
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### GAME MODEL IN ACTION")

    i1, i2 = st.columns(2)

    with i1:
        img_att0 = get_img("att_free-kick.png")

        if img_att0:
            st.image(
                img_att0,
                caption="Niagara FC — Attacking free-kick shape and delivery.",
                use_container_width=True
            )

        img_att1 = get_img("att_free-kick_zone4.png")

        if img_att1:
            st.image(
                img_att1,
                caption="Niagara FC — Zone 4 attacking free-kick example.",
                use_container_width=True
            )

    with i2:
        img_att2 = get_img("quick_att_freekick_zone3.png")

        if img_att2:
            st.image(
                img_att2,
                caption=(
                    "Zone 3 — An immediate restart exploits "
                    "a disorganised defensive line."
                ),
                use_container_width=True
            )

        img_att3 = get_img("free_kick_zone3_pass.png")

        if img_att3:
            st.image(
                img_att3,
                caption=(
                    "Niagara FC — An immediate switch exploits "
                    "weak-side space before the opposition recovers."
                ),
                use_container_width=True
            )


# ==================================================
# TAB 3 — DEFENDING SET PIECES
# ==================================================

with tabs[2]:

    st.markdown(
        "<div class='quote-block'>"
        "Win the first ball. Win the second ball. Win the moment."
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown("### DEFENSIVE CORNERS")

    st.markdown(
        "<div class='quote-block'>"
        "Our defensive corner structure combines four assigned "
        "zonal responsibilities with player-oriented marking. "
        "Protect the goal, attack the first contact and "
        "react immediately to the next action."
        "</div>",
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class='card'>
        🛡️ <strong>Zones Occupied</strong><br><br>
        Four assigned positions remain occupied:<br><br>
        <strong>#3</strong> — Near-post protection<br>
        <strong>#5</strong> — Central protection<br>
        <strong>#2</strong> — Primary aerial defender;
        attacks the first contact<br>
        <strong>#9</strong> — High outlet
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(
            "<div class='card'>"
            "🛡️ <strong>Player-Oriented Marking</strong><br><br>"
            "Remaining players take responsibility for "
            "opposition attackers. Stay goal-side, track "
            "movements and remain connected. "
            "Attack the ball rather than ball-watching."
            "</div>",
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            "<div class='card'>"
            "🛡️ <strong>Short Corners</strong><br><br>"
            "The front-edge six-yard player and nearest "
            "defender react together. Apply coordinated "
            "pressure and prevent a 2v1 against our "
            "nearest defender."
            "</div>",
            unsafe_allow_html=True
        )

    st.markdown(
        "<div class='card'>"
        "🛡️ <strong>Goalkeeper Wins the Ball</strong> — "
        "Look to release #9 quickly when the counterattacking "
        "opportunity is available. Secure possession "
        "when it is not."
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='card'>"
        "🛡️ <strong>Ball Stays Live</strong> — "
        "Stay alert to rebounds and second balls. "
        "Attack the next contact, clear danger decisively "
        "and reorganise until the threat is over."
        "</div>",
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### DEFENSIVE CORNERS IN ACTION")

    i1, i2 = st.columns(2)

    with i1:
        img_shape = get_img("def_corner_shape.png")

        if img_shape:
            st.image(
                img_shape,
                caption=(
                    "Niagara FC — Defensive corner shape "
                    "with assigned zones and player-oriented marking."
                ),
                use_container_width=True
            )

    with i2:
        img_win = get_img("def_corner_strongdef_free_to_win.png")

        if img_win:
            st.image(
                img_win,
                caption=(
                    "Niagara FC — Primary aerial defender "
                    "steps from her zone to attack the first contact."
                ),
                use_container_width=True
            )

    st.divider()

    st.markdown("### DEFENSIVE FREE KICKS")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            "<div class='card'>"
            "🛡️ <strong>Zones 3 & 4</strong><br><br>"
            "Recover immediately into defensive structure.<br><br>"
            "Protect central spaces and identify threats "
            "between the lines.<br><br>"
            "Communicate, shift together and remain alert "
            "to quick restarts."
            "</div>",
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            "<div class='card'>"
            "🛡️ <strong>Zones 1 & 2</strong><br><br>"
            "Recover quickly behind the ball and organise.<br><br>"
            "The nearest player takes up a legal defensive "
            "position while teammates recover.<br><br>"
            "Recognise the possibility of a quick free kick "
            "and defend the immediate threat."
            "</div>",
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            "<div class='card'>"
            "🛡️ <strong>Zone 1 Wide — Defend as a Corner</strong>"
            "<br><br>"
            "Protect central spaces and organise for "
            "the delivery.<br><br>"
            "Attack the first ball aggressively and "
            "deny free headers in the box.<br><br>"
            "Clear danger and reorganise for the next action."
            "</div>",
            unsafe_allow_html=True
        )

    st.markdown(
        "<div class='quote-block'>"
        "Recover immediately · Protect central spaces · "
        "Communicate constantly · Attack the first ball · "
        "Win the second ball"
        "</div>",
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### DEFENSIVE FREE KICKS IN ACTION")

    d1, d2 = st.columns(2)

    with d1:
        img_def1 = get_img("def_freekick_zone1.png")

        if img_def1:
            st.image(
                img_def1,
                caption="Niagara FC — Zone 1 defensive free-kick shape.",
                use_container_width=True
            )

        img_def3 = get_img("def_freekick_zone3.png")

        if img_def3:
            st.image(
                img_def3,
                caption="Niagara FC — Compact defensive organisation.",
                use_container_width=True
            )

    with d2:
        img_def2 = get_img("def_deep_freekick_zone2.png")

        if img_def2:
            st.image(
                img_def2,
                caption=(
                    "Niagara FC — Zone 2 defensive shape, "
                    "showing compactness from another angle."
                ),
                use_container_width=True
            )

        img_def4 = get_img(
            "def_freekick_zone4_Back_in_shape.png"
        )

        if img_def4:
            st.image(
                img_def4,
                caption=(
                    "Niagara FC — Recovery into compact "
                    "defensive structure following a free kick."
                ),
                use_container_width=True
            )



# ==================================================
# TAB 4 — THROW-INS & RESTARTS
# ==================================================

with tabs[3]:

    st.markdown(
        "<div class='quote-block'>"
        "High tempo never stops. If the opportunity is on — play it."
        "</div>",
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("#### THROW-IN PRINCIPLES")

        principles = [
            "Recognise opportunities to restart before the opposition can organise",

            "Throw to feet when possible — receive, turn and play forward",

            "Create clear support angles around the ball",

            "Movement begins before the throw, not after it",

            "Nearest players provide passing options; far-side players create space",

            "In our own half, secure possession while maintaining a forward mindset",

            "In advanced Zones 3 and 4, recognise opportunities to use the throw-in as an attacking set piece",
        ]

        for item in principles:
            st.markdown(
                f"<div class='card'>⚽ {item}</div>",
                unsafe_allow_html=True
            )

    with c2:
        st.markdown("#### RESTART MENTALITY")

        mentality = [
            "Recognise when to restart quickly and when to control the moment",

            "Be organised before the restart and purposeful after it",

            "Use restarts to create advantages, not simply retain possession",

            "Make decisions based on available space, opposition organisation and supporting movements",
        ]

        for item in mentality:
            st.markdown(
                f"<div class='card card-gold'>⚽ {item}</div>",
                unsafe_allow_html=True
            )

    st.divider()

    st.markdown("### GAME MODEL IN ACTION — LONG THROW ROUTINE")

    st.markdown(
        "<div class='card'>"
        "⚽ <strong>Long Throw in Zones 3 & 4</strong><br><br>"
        "Deliver into the danger area with coordinated "
        "movements around the six-yard box. "
        "Compete for the first contact, create pressure "
        "around the goalkeeper and position supporting "
        "players to attack second balls."
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "#### EXAMPLE 1 — MIDFIELDER ATTACKS THE SECOND BALL"
    )

    img_2nd = get_img(
        "picking_up_2nd_ball_from_long_throw.png"
    )

    if img_2nd:
        st.image(
            img_2nd,
            caption=(
                "Niagara FC — A midfielder arrives late, "
                "collects the second ball and scores "
                "from the edge of the penalty area."
            ),
            use_container_width=True
        )

    st.divider()

    st.markdown(
        "#### EXAMPLE 2 — LONG THROW, FIRST CONTACT, SECOND ACTION"
    )

    st.markdown(
        "<div class='quote-block'>"
        "The first contact creates the opportunity. "
        "Our reaction to the second action finishes it."
        "</div>",
        unsafe_allow_html=True
    )

    l1, l2, l3 = st.columns(3)

    with l1:
        img_lt1 = get_img("long_throw_1.png")

        if img_lt1:
            st.image(
                img_lt1,
                caption=(
                    "1 — Long throw delivered into "
                    "the attacking area."
                ),
                use_container_width=True
            )

    with l2:
        img_lt2 = get_img("long_throw_2.png")

        if img_lt2:
            st.image(
                img_lt2,
                caption=(
                    "2 — First contact creates pressure "
                    "around the goalkeeper."
                ),
                use_container_width=True
            )

    with l3:
        img_lt3 = get_img("long_throw_3.png")

        if img_lt3:
            st.image(
                img_lt3,
                caption=(
                    "3 — Niagara FC score from "
                    "the second action."
                ),
                use_container_width=True
            )
