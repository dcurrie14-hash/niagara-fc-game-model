
import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import apply_css, sidebar_brand, get_img

st.set_page_config(
    page_title="Attacking Organisation | Niagara FC",
    page_icon="⚽",
    layout="wide"
)
apply_css()
sidebar_brand()


def show_diagram(filename, caption=None):
    img = get_img(filename)
    if img:
        st.image(img, caption=caption, use_container_width=True)
    else:
        st.warning(f"Diagram not found: {filename}")


def coaching_cards(items, style="card"):
    for item in items:
        st.markdown(
            f"<div class='card {style}'>→ {item}</div>",
            unsafe_allow_html=True
        )


st.markdown("# ATTACKING ORGANISATION")
st.markdown(
    "<div style='font-family:Oswald,sans-serif;font-size:1em;"
    "color:#1E56D6;letter-spacing:1px;margin-bottom:12px;'>"
    "TEAM INTENTION: Control and progress the ball with tempo, "
    "purpose and positional flexibility. Create opportunities "
    "to penetrate and attack quickly.</div>",
    unsafe_allow_html=True
)

tabs = st.tabs([
    "📋 Overview",
    "🔵 Zone 1 — Build",
    "🔄 Zone 2, 3 & Into 4",
    "🎯 Zone 4 — Finish",
    "🔗 Connections #9",
    "↔️ Wide Play"
])


# ==========================================================
# TAB 1 — OVERVIEW
# ==========================================================

with tabs[0]:
    st.markdown(
        "<div style='font-family:Oswald,sans-serif;font-size:0.95em;"
        "color:#FFD700;letter-spacing:1px;margin-bottom:12px;'>"
        "STRATEGY: Play forward whenever possible. Break lines "
        "quickly. Attack space before the opposition can "
        "recover organisation.</div>",
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("### CORE PRINCIPLES")
        coaching_cards([
            "Think forward, play forward, run forward",
            "Break lines through passing, dribbling or movement",
            "Support underneath, beside and beyond the ball",
            "Engage defenders to create space elsewhere",
            "Create overloads without sacrificing width and depth",
            "Use movement to disrupt defensive organisation",
            "Recognise when to accelerate or retain possession",
            "Encourage creativity, courage and problem solving"
        ])

        st.markdown(
            "<div class='quote-block'>"
            "Engage pressure to create space. Recognise the "
            "opportunity, play forward and support the next action."
            "</div>",
            unsafe_allow_html=True
        )

    with c2:
        st.markdown("### REAL GAME REFERENCES")

        show_diagram(
            "match_d1f_forward_run.png",
            "D1 Féminine — midfielder identifies the forward pass. "
            "#25 times the run beyond the defensive line. "
            "PLAY FORWARD. RUN FORWARD."
        )

        show_diagram(
            "match_wsl_front3.png",
            "WSL — distances and dispersal between the front "
            "three as midfielders progress with the ball. "
            "Width and depth maintained."
        )

    st.divider()

    show_diagram(
        "Attacking_pic.png",
        "Niagara FC — attacking organisation in practice. "
        "The RB progresses play forward, the #10 supports "
        "underneath the #9, and the weak-side #11 rotates "
        "centrally to create an overload. The #7 and #9 "
        "maintain depth. Players occupy useful spaces rather "
        "than remaining fixed in positions."
    )

    show_diagram(
        "match_nfc_attacking_shape.png",
        "Niagara FC — the #7 attacks with the ball, the #9 "
        "provides a central reference point and the #11 "
        "maintains width and depth. The #8 and #10 support "
        "the attack, creating multiple forward options."
    )


# ==========================================================
# TAB 2 — ZONE 1: BUILD
# ==========================================================

with tabs[1]:
    st.markdown(
        "**Team Intention:** Attract and manipulate the first "
        "line of pressure to progress through, around or beyond it."
    )

    show_diagram("ao_zone1_build.png")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("#### Coaching Detail")
        coaching_cards([
            "Use the goalkeeper as an additional passing option "
            "to create numerical superiority",
            "Centre backs split to stretch the opposition press",
            "Invite pressure when it creates space to exploit",
            "The #6 adjusts position to offer a passing lane "
            "or create space for another midfielder",
            "Fullbacks adjust width and height in response "
            "to the press",
            "High players occupy defenders and threaten "
            "space beyond the pressing line",
            "Recognise when to play short, switch or go long"
        ])

    with c2:
        st.markdown("#### On The Ball")
        coaching_cards([
            "Scan early to recognise pressure and forward options",
            "Receive with an open body shape where possible",
            "Engage the pressing player before releasing the ball",
            "Prioritise forward passes when the opportunity exists",
            "Eliminate defenders through passing or dribbling",
            "Use quick combinations to escape pressure",
            "Change the tempo to exploit spaces created by the press"
        ], "card-blue")

    with c3:
        st.markdown("#### Off The Ball")
        coaching_cards([
            "Create clear passing angles and appropriate distances",
            "Provide options underneath, beside and beyond",
            "Rotate to open passing lanes, not simply to exchange positions",
            "Maintain width and depth to stretch the opposition",
            "Support the next action after the first line is broken",
            "Adjust positions in response to the ball and pressure",
            "Prepare to compete for second balls when playing beyond"
        ], "card-gold")

    st.divider()
    st.markdown("### REAL GAME REFERENCES — ZONE 1")

    c1, c2 = st.columns(2)

    with c1:
        show_diagram(
            "Build_up_from_GK.png",
            "Niagara FC — GK stands on the ball to invite the press. "
            "As the opposition commits, space opens for midfielders "
            "to receive between the lines."
        )

        show_diagram(
            "short_gk_build.png",
            "Niagara FC — CB takes the goal kick short to the GK, "
            "creating numerical superiority against the high press. "
            "The GK can now decide to play short, long or switch."
        )

    with c2:
        show_diagram(
            "Goal_Kick_Option_to_go_long.png",
            "Niagara FC — goal kick option to go long. "
            "From the same starting situation, we can build "
            "short or exploit space beyond the press."
        )



# ==========================================================
# TAB 3 — ZONES 2 & 3: PROGRESS AND CREATE
# ==========================================================

with tabs[2]:
    st.markdown(
        "**Team Intention:** Progress with tempo and purpose. "
        "Break defensive lines, create superiority and recognise "
        "opportunities to penetrate Zone 4."
    )

    st.markdown(
        "<div class='quote-block'>"
        "THINK FORWARD · PLAY FORWARD · RUN FORWARD. "
        "Exploit opportunities to break lines quickly. "
        "When the forward option is unavailable, move the "
        "opposition to create a better one."
        "</div>",
        unsafe_allow_html=True
    )

    show_diagram("ao_zone23_progress.png")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("#### Coaching Detail")
        coaching_cards([
            "Engage defenders to create space between and beyond lines",
            "Use third-player combinations to eliminate pressure",
            "Create numerical or positional superiority around the ball",
            "Encourage forward runs that threaten the defensive line",
            "Recognise opportunities to switch play when central spaces close",
            "Exploit weak-side spaces before the opposition can shift",
            "Maintain connections behind the ball to sustain the attack"
        ])

    with c2:
        st.markdown("#### On The Ball")
        coaching_cards([
            "Scan before receiving to identify the next action",
            "Receive on the half-turn when possible",
            "Play forward when a teammate can receive advantageously",
            "Break lines through passes, carries or combinations",
            "Attack isolated defenders with confidence",
            "Recognise when to accelerate and when to retain possession",
            "Be brave enough to attempt penetrative passes"
        ], "card-blue")

    with c3:
        st.markdown("#### Off The Ball")
        coaching_cards([
            "Support underneath, beside and beyond the ball",
            "Time forward runs to threaten space behind the defensive line",
            "Use rotations to create useful spaces and passing angles",
            "Maintain width and depth while connecting centrally",
            "Opposite-side players prepare for switches and penetration",
            "Create third-player options through coordinated movement",
            "Adjust positions as the ball and opposition move"
        ], "card-gold")

    st.divider()
    st.markdown("### REAL GAME REFERENCES — ZONE 2, 3 & INTO 4")

    c1, c2 = st.columns(2)

    with c1:
        show_diagram(
            "3rd_man_run_z2-3.jpg",
            "NWSL — third-player combination in Zones 2 and 3. "
            "The ball is played in, the first line is broken, "
            "and the third player runs beyond."
        )

        show_diagram(
            "match_wsl_cm_penetrate1.png",
            "WSL — a simple option is available, but the midfielder "
            "recognises the opportunity to play through the line. "
            "A brave forward decision creates penetration."
        )

        show_diagram(
            "attacking_the_half_space.png",
            "Niagara FC — wide player receives in the right channel "
            "and connects with the striker moving into the half-space. "
            "Width creates the opportunity to penetrate inside."
        )

    with c2:
        show_diagram(
            "3rd_man_comb_z2-3.jpg",
            "NWSL — continuation of the combination. "
            "The third player exploits the space created "
            "beyond the defensive line."
        )

        show_diagram(
            "match_wsl_cm_penetrate2.png",
            "WSL — the penetrating pass rewards the forward runner, "
            "stretching the defence and exploiting space behind."
        )

        show_diagram(
            "match_wsl_third_man.png",
            "WSL — third-player combination progresses from "
            "Zone 3 into Zone 4, bypassing the defensive line."
        )

    show_diagram(
        "match_d1f_zone23_fb.png",
        "D1 Féminine — switch of play finds the opposite fullback "
        "providing width, creating a new opportunity to progress "
        "from Zone 3 into Zone 4."
    )


# ==========================================================
# TAB 4 — ZONE 4: FINISH
# ==========================================================

with tabs[3]:
    st.markdown(
        "**Team Intention:** Create and finish high-quality chances "
        "through penetration, coordinated attacking runs and "
        "effective occupation of the penalty area."
    )

    st.markdown(
        "<div class='quote-block'>"
        "When we penetrate Zone 4, the timing and quality of our "
        "movements determine the opportunity. Attack the box "
        "with purpose, arrive in complementary spaces and "
        "be ready for the next action."
        "</div>",
        unsafe_allow_html=True
    )

    # Final approved diagram:
    # #3 to #8 to #11, with #11 delivering the cutback
    # and the back line supporting around halfway.
    show_diagram("ao_zone4_finish.png")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("#### Core Principles")
        coaching_cards([
            "Penetrate Zone 4 with speed, purpose and aggression",
            "Create separation through movement across the defensive line",
            "Attack the near-post, central and far-post spaces",
            "Time arrivals to meet the delivery rather than waiting in the box",
            "Recognise when to cross early or reach the end line",
            "Maintain supporting players for second balls and recycled attacks",
            "Keep defensive balance behind the attack to protect transitions"
        ])

    with c2:
        st.markdown("#### Attacking the Box")
        coaching_cards([
            "#9 — threaten the space in front of goal and attack the delivery",
            "#7 — attack the far-post space or arrive centrally as play develops",
            "#10 — arrive around the penalty spot as a cutback option",
            "#8 — time a later arrival near the edge of the penalty area",
            "#11 — recognise the cutback, low delivery or individual finish",
            "Attack different spaces rather than all running towards the ball",
            "Adjust runs to the ball carrier's position and body shape"
        ], "card-gold")

    with c3:
        st.markdown("#### Decision Making")
        coaching_cards([
            "Recognise the goalkeeper's and defenders' positions",
            "Cut back into space when defenders are recovering towards goal",
            "Choose the delivery based on the movement of teammates",
            "Use early crosses when the defence is exposed",
            "Attack rebounds and second balls with anticipation",
            "Recycle possession when a clear finishing option is unavailable",
            "Prepare immediately for defensive transition if possession is lost"
        ], "card-blue")

    st.divider()
    st.markdown("### REAL GAME REFERENCES — ZONE 4")

    c1, c2 = st.columns(2)

    with c1:
        show_diagram(
            "4_in_the_box.png",
            "NWSL — wide delivery with multiple runners arriving "
            "in complementary areas of the penalty box. "
            "Central and far-post spaces are occupied."
        )

        show_diagram(
            "match_wsl_striker_run.png",
            "WSL — striker times the run to break the defensive "
            "line and create a chance on goal."
        )

    with c2:
        show_diagram(
            "match_wsl_zone4_box.png",
            "WSL — striker provides a central threat while a "
            "wide forward arrives at the far post. "
            "Two different spaces are attacked simultaneously."
        )

        show_diagram(
            "match_wsl_third_man.png",
            "WSL — third-player combination penetrates from "
            "Zone 3 into Zone 4, bypassing the defensive line."
        )

    # Existing women's football analysis graphic retained.
    # Any statistics shown in this image should be checked
    # against their original source before being presented
    # as established findings.
    show_diagram(
    "ao_zone4_finishing_insights.png",
        "Women's World Cup 2023 — finishing locations, "
"the second six-yard box and goals assisted by crosses. "
"Source: England Football Learning."



# ==========================================================
# TAB 5 — CONNECTIONS AROUND #9
# ==========================================================

with tabs[4]:
    st.markdown(
        "**Team Intention:** Create immediate support around the "
        "#9 to connect midfield with the attack, prevent isolation "
        "and threaten space beyond the defensive line."
    )

    st.markdown(
        "<div class='quote-block'>"
        "PLAY FORWARD. CONNECT. RUN FORWARD. "
        "The #9 provides a central reference point, while "
        "supporting players create options underneath, "
        "beside and beyond the ball."
        "</div>",
        unsafe_allow_html=True
    )

    show_diagram("ao_connections9.png")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("### COACHING DETAIL")

        coaching_cards([
            "Recognise opportunities to play forward into the #9",
            "The #9 secures possession and connects with supporting players",
            "The #8 provides immediate support underneath the striker",
            "The #10 stays close enough to combine or receive beyond",
            "The #7 and #11 threaten space behind the defensive line",
            "Support the next action as soon as the forward pass is played",
            "Use third-player combinations to penetrate beyond pressure",
            "Maintain width and defensive balance as players move to connect"
        ])

    with c2:
        st.markdown("### KEY RELATIONSHIPS")

        for title, detail, style in [
            (
                "#6 → #9",
                "Recognise the forward passing opportunity and "
                "find the striker when she can receive or compete.",
                "card-blue"
            ),
            (
                "#9 + #8",
                "The #8 supports underneath to receive a layoff, "
                "secure the second ball or continue the attack.",
                "card-gold"
            ),
            (
                "#9 + #10",
                "The #10 stays connected to combine quickly "
                "and exploit space around the striker.",
                "card-blue"
            ),
            (
                "#7 + #11",
                "Wide forwards threaten space beyond the defence, "
                "stretching the opposition and creating depth.",
                "card-gold"
            )
        ]:
            st.markdown(
                f"<div class='card {style}'>"
                f"<b>{title}</b><br>"
                f"<small>{detail}</small></div>",
                unsafe_allow_html=True
            )

        st.markdown(
            "<div class='quote-block'>"
            "The #9 should never be isolated. "
            "When we play forward, the next movement is just "
            "as important as the pass."
            "</div>",
            unsafe_allow_html=True
        )

    st.divider()
    st.markdown("### REAL GAME REFERENCES — CONNECTIONS #9")

    c1, c2 = st.columns(2)

    with c1:
        show_diagram(
            "holdup_9.png",
            "Niagara FC — long ball played into the #9, "
            "who holds possession with her back to goal. "
            "#7 provides immediate support underneath while "
            "#11 threatens space beyond."
        )

    with c2:
        show_diagram(
            "match_d1f_reims_9_connections.png",
            "D1 Féminine — #9 provides a central reference point. "
            "#8 and #10 connect around the striker while "
            "wide forwards threaten space behind."
        )


# ==========================================================
# TAB 6 — WIDE PLAY
# ==========================================================

with tabs[5]:
    st.markdown(
        "**Team Intention:** Create and exploit wide attacking "
        "opportunities through isolation, combinations, "
        "penetration and effective delivery."
    )

    st.markdown(
        "<div class='quote-block'>"
        "ISOLATE · COMBINE · PENETRATE · DELIVER. "
        "Width stretches the opposition and creates space. "
        "Recognise when to attack the defender, combine "
        "with support or deliver into the penalty area."
        "</div>",
        unsafe_allow_html=True
    )

    show_diagram("ao_wide_play.png")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("### COACHING DETAIL")

        coaching_cards([
            "Create opportunities to isolate defenders in 1v1 situations",
            "Attack isolated defenders with speed and confidence",
            "Use overlapping and underlapping runs to create 2v1s",
            "Combine quickly to penetrate the wide channel or half-space",
            "Recognise opportunities to attack the end line",
            "Deliver early when the opposition is exposed",
            "Use cutbacks when teammates arrive into space inside the box",
            "Opposite-side attackers threaten the far-post area",
            "Maintain supporting positions for second balls and transitions"
        ])

    with c2:
        st.markdown("### DECISION MAKING")

        for title, detail, style in [
            (
                "ISOLATE",
                "Can we create a 1v1 and encourage the wide "
                "player to attack the defender?",
                "card-blue"
            ),
            (
                "COMBINE",
                "If the defender has support, can we create "
                "an overload through an overlap, underlap "
                "or quick combination?",
                "card-gold"
            ),
            (
                "PENETRATE",
                "Can we exploit the space behind the fullback "
                "or attack through the half-space?",
                "card-blue"
            ),
            (
                "DELIVER",
                "Recognise the best option: early cross, "
                "low delivery, cutback or individual finish.",
                "card-gold"
            )
        ]:
            st.markdown(
                f"<div class='card {style}'>"
                f"<b>{title}</b><br>"
                f"<small>{detail}</small></div>",
                unsafe_allow_html=True
            )

        st.markdown(
            "<div class='quote-block'>"
            "The delivery is determined by the position "
            "of the ball, the defenders and the timing "
            "of our attacking runs."
            "</div>",
            unsafe_allow_html=True
        )

    st.divider()
    st.markdown("### REAL GAME REFERENCES — WIDE PLAY")

    c1, c2 = st.columns(2)

    with c1:
        show_diagram(
            "wide_play1.png",
            "Australia vs France — wide player receives in "
            "the right channel, isolates the defender and "
            "drives towards the end line."
        )

        show_diagram(
            "isolate_1v1_wide_play.png",
            "Niagara FC — wide player isolated in a 1v1 "
            "with no immediate defensive cover. "
            "Attack the defender and exploit the space."
        )

    with c2:
        show_diagram(
            "wide_play2.png",
            "Australia vs France — the wide player delivers "
            "a cutback with multiple teammates arriving "
            "in the penalty area."
        )

        show_diagram(
            "wide_cutback_goal.png",
            "Niagara FC — wide player drives into the "
            "half-space towards the end line and provides "
            "a cutback. Penetration and movement create "
            "the finishing opportunity."
        )
