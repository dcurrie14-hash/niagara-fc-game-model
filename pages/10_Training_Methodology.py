
import streamlit as st
import sys
import os

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from utils import apply_css, sidebar_brand, get_img

st.set_page_config(
    page_title="Training Philosophy | Niagara FC",
    page_icon="🏃",
    layout="wide"
)

apply_css()
sidebar_brand()

# ==========================================
# PAGE-SPECIFIC STYLING
# ==========================================

st.markdown("""
<style>
[data-testid="stMain"] h1,
[data-testid="stMain"] h2,
[data-testid="stMain"] h3,
[data-testid="stMain"] h4 {
    color: #F2F5FA !important;
}

[data-testid="stMain"] .stTabs button {
    white-space: nowrap;
}

.training-kicker {
    color: #FFD700;
    font-family: Oswald, sans-serif;
    font-size: 0.95rem;
    letter-spacing: 0.8px;
    margin: 18px 0 10px;
}

.training-note {
    color: #B9C8D8;
    font-size: 0.91rem;
    line-height: 1.65;
}

.training-small {
    color: #AFC0D2;
    font-size: 0.85rem;
    line-height: 1.6;
}

.training-rule {
    border-top: 1px solid #28405D;
    margin: 20px 0;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# PAGE INTRODUCTION
# ==========================================

st.markdown("# TRAINING PHILOSOPHY & PRACTICE DESIGN")

st.markdown(
    "<div class='quote-block'>"
    "The game drives the training. "
    "The objective determines the methodology."
    "</div>",
    unsafe_allow_html=True
)

st.markdown(
    "My approach to training is flexible. The method I choose depends "
    "on the game problem, the needs of the players and where we are "
    "within our periodisation cycle. What remains consistent is the "
    "environment I want to create: purposeful, challenging, competitive "
    "and enjoyable, with players actively involved in making decisions."
)

tabs = st.tabs([
    "Coaching Approach",
    "Practice Design",
    "On the Training Ground"
])

# ==========================================
# TAB 1 — COACHING APPROACH
# ==========================================

with tabs[0]:

    st.markdown("### WHAT STAYS CONSISTENT")

    st.markdown(
        "I want players to train with energy and purpose. "
        "They should be challenged to recognise information, "
        "make decisions and solve problems, rather than simply "
        "reproduce movements they've been shown."
    )

    c1, c2 = st.columns(2, gap="medium")

    with c1:
        st.markdown(
            "<div class='card card-blue'>"
            "<b>Tempo & Engagement</b><br><br>"
            "Purposeful activity, meaningful repetition and "
            "minimal unnecessary downtime. Players should "
            "be actively involved in the session."
            "</div>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<div class='card'>"
            "<b>Decision-Making</b><br><br>"
            "Practices should give players information to "
            "recognise and decisions to make. The aim is "
            "understanding, not simply completing an exercise."
            "</div>",
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            "<div class='card card-gold'>"
            "<b>Competition</b><br><br>"
            "Opposition, pressure and meaningful challenges "
            "help players develop the ability to perform "
            "when the game becomes difficult."
            "</div>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<div class='card'>"
            "<b>Enjoyment</b><br><br>"
            "Players should enjoy the challenge of training. "
            "Competition, improvement and enjoyment "
            "should support one another."
            "</div>",
            unsafe_allow_html=True
        )

    st.markdown("### OUR TRAINING ENVIRONMENT")

    st.markdown(
        "Development is a shared responsibility. "
        "Coaches are responsible for creating worthwhile "
        "learning opportunities. Players are responsible "
        "for how they approach them."
    )

    c1, c2 = st.columns(2, gap="medium")

    with c1:
        st.markdown("#### WHAT WE PROVIDE")
        st.markdown(
            "<div class='card card-blue'>"
            "Purposeful sessions connected to our Game Model.<br><br>"
            "Appropriate challenge and meaningful repetition.<br><br>"
            "Opportunities to make decisions and solve problems.<br><br>"
            "Feedback, support and room to make mistakes.<br><br>"
            "An environment where players can compete and enjoy football."
            "</div>",
            unsafe_allow_html=True
        )

    with c2:
        st.markdown("#### WHAT WE EXPECT")
        st.markdown(
            "<div class='card card-gold'>"
            "<b>Be All In.</b><br><br>"
            "Arrive ready to train and be fully engaged.<br><br>"
            "Compete with intensity and purpose.<br><br>"
            "Challenge yourself and your teammates.<br><br>"
            "Be coachable and respond to feedback.<br><br>"
            "Take responsibility for your own development."
            "</div>",
            unsafe_allow_html=True
        )

    st.markdown(
        "<div class='quote-block'>"
        "Being all in doesn't mean being perfect. "
        "It means being committed to the work, "
        "responding to mistakes and making the most "
        "of every opportunity to improve."
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown("### WHAT CHANGES")

    st.markdown(
        "The structure of training is not fixed. I may use "
        "Whole–Part–Whole, a progressive practice, a functional "
        "exercise or a larger game depending on what the players "
        "need. The level of physical intensity, complexity "
        "and coaching intervention also changes across the "
        "training cycle."
    )

    st.markdown(
        "<div class='card'>"
        "<b>The principle is simple:</b> select the approach "
        "that best serves the objective, rather than forcing "
        "every objective into the same approach."
        "</div>",
        unsafe_allow_html=True
    )



# ==========================================
# TAB 2 — PRACTICE DESIGN
# ==========================================

with tabs[1]:

    st.markdown("### FROM THE GAME TO THE TRAINING GROUND")

    st.markdown(
        "Session design begins with what I observe in matches "
        "and training. I identify the problem, consider what "
        "players need to understand, then select a practice "
        "that gives them opportunities to work through it."
    )

    for heading, detail, style in [
        (
            "1. IDENTIFY THE GAME PROBLEM",
            "What are players struggling to recognise or execute? "
            "Is the issue technical, tactical, physical or a "
            "combination of factors?",
            "card-blue"
        ),
        (
            "2. ESTABLISH THE LEARNING OBJECTIVE",
            "What should players recognise, decide or do "
            "more effectively? The objective should connect "
            "to our Game Model and be observable in a match.",
            "card"
        ),
        (
            "3. SELECT THE PRACTICE",
            "Choose the numbers, space, opposition, format "
            "and conditions that best represent the problem "
            "and provide appropriate repetition.",
            "card"
        ),
        (
            "4. CONSIDER THE TRAINING CYCLE",
            "Adjust the physical load, complexity and "
            "duration according to the stage of periodisation, "
            "proximity to matches and player readiness.",
            "card"
        ),
        (
            "5. OBSERVE AND ADAPT",
            "Are players recognising the right information "
            "and making better decisions? Adjust the practice "
            "or intervention when the learning isn't occurring.",
            "card-gold"
        )
    ]:
        st.markdown(
            f"<div class='card {style}' style='margin-bottom:8px;'>"
            f"<b>{heading}</b><br><br>{detail}</div>",
            unsafe_allow_html=True
        )

    st.markdown("### CHOOSING THE METHODOLOGY")

    st.markdown(
        "I don't follow one methodology for every session. "
        "Different problems call for different approaches, "
        "and the same objective may require a different "
        "approach depending on the group or stage of the season."
    )

    with st.expander("Whole–Part–Whole"):
        st.markdown(
            "Players experience a problem within a game, "
            "work on a more specific element when necessary, "
            "then return to a larger game to apply what "
            "they've learned. Useful when I want players "
            "to recognise a problem in its full context "
            "before increasing repetition of a particular moment."
        )

    with st.expander("Progressive Practice"):
        st.markdown(
            "A practice develops through planned progressions "
            "in numbers, space, opposition or complexity. "
            "I use this when players need to establish "
            "understanding and confidence before dealing "
            "with more demanding game situations."
        )

    with st.expander("Whole / Game-Based Practice"):
        st.markdown(
            "A larger or more complete game allows players "
            "to experience realistic relationships, transitions "
            "and decisions. This can help me assess their "
            "understanding or challenge them to apply "
            "principles in a less controlled environment."
        )

    with st.expander("Functional and Isolated Practice"):
        st.markdown(
            "Some moments benefit from focused repetition "
            "with fewer players or more specific conditions. "
            "This might involve a positional relationship, "
            "a technical action or set-piece organisation. "
            "The aim is to transfer that learning back "
            "into the game."
        )

    st.markdown("### USING CONSTRAINTS")

    st.markdown(
        "Constraints are one of the tools I use to shape "
        "the learning environment. Changing the space, "
        "numbers, rules or scoring conditions can encourage "
        "players to recognise particular opportunities "
        "without prescribing every solution."
    )

    st.markdown(
        "<div class='card card-blue'>"
        "<b>Example — Attacking Organisation</b><br><br>"
        "If players are circulating possession without "
        "recognising opportunities to play forward, "
        "I might create a directional game that rewards "
        "breaking lines. The challenge is to recognise "
        "when the forward option is available, not to "
        "force a forward pass every time."
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='card'>"
        "<b>Example — Defensive Organisation</b><br><br>"
        "If our defensive unit is becoming disconnected, "
        "I might adjust the playing area or opposition "
        "structure to create more frequent situations "
        "where players must recognise when to press, "
        "cover and recover into compact positions."
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='card'>"
        "<b>Example — Attacking Transition</b><br><br>"
        "To encourage our 'play forward, run forward' "
        "principle, I might reward quick attacking "
        "actions after regaining possession. "
        "The objective is to recognise and exploit "
        "the opportunity before the opposition recovers "
        "its organisation."
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='quote-block'>"
        "A constraint is only useful if it helps create "
        "the learning we're looking for. If players "
        "begin forcing actions or the practice loses "
        "its connection to the game, I adjust it."
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown("### COACHING INTERVENTIONS")

    st.markdown(
        "I vary how and when I intervene. Sometimes "
        "players benefit from being allowed to play "
        "and discover solutions. At other times, "
        "a question, a brief demonstration or direct "
        "instruction can help move the learning forward. "
        "The decision depends on what I'm observing "
        "and what the players need."
    )

    with st.expander("Practice design reference — SCORE"):
        st.markdown(
            "SCORE provides a useful check when reviewing "
            "the quality of a training activity:"
        )

        for label, detail in [
            ("Soccer Problem", "Is the practice connected to a real game problem?"),
            ("Challenge", "Are players appropriately challenged?"),
            ("Opposition", "Does opposition provide useful information and pressure?"),
            ("Realism", "Can the learning transfer to the game?"),
            ("Enjoyment", "Are players engaged and motivated to participate?")
        ]:
            st.markdown(f"**{label}** — {detail}")



# ==========================================
# TAB 3 — ON THE TRAINING GROUND
# ==========================================

with tabs[2]:

    st.markdown("### TRAINING IN PRACTICE")

    st.markdown(
        "The examples below illustrate different ways "
        "I use training activities to develop specific "
        "moments within our Game Model. "
        "They are examples, not fixed session templates. "
        "The organisation and conditions can change "
        "depending on the players and the objective."
    )

    # ======================================
    # PRACTICAL EXAMPLE
    # ======================================

    st.markdown("### EXAMPLE — CHANGING THE POINT OF ATTACK")

    st.markdown(
        "<div class='card card-blue'>"
        "<b>Game Moment</b><br>"
        "Attacking Organisation — Zones 2 & 3"
        "<br><br>"
        "<b>Game Problem</b><br>"
        "Players are forcing possession into congested "
        "central areas rather than recognising space "
        "available on the opposite side."
        "<br><br>"
        "<b>Learning Objective</b><br>"
        "Recognise when and why to change the point "
        "of attack to create a better opportunity "
        "to play forward."
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown("#### ONE POSSIBLE SESSION APPROACH")

    st.markdown(
        "For this problem, I might use a "
        "Whole–Part–Whole structure. "
        "The players first experience the problem "
        "in a game, then work within a practice "
        "that creates more opportunities to recognise "
        "the switch before returning to a larger game."
    )

    c1, c2, c3 = st.columns(3, gap="medium")

    with c1:
        st.markdown(
            "<div class='card card-blue'>"
            "<b>1 — EXPERIENCE</b><br><br>"
            "<b>3v3+2 Four-Goal Game</b><br><br>"
            "Players experience pressure and "
            "multiple attacking options. "
            "Observe whether they recognise "
            "when to move the ball away "
            "from congestion."
            "</div>",
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            "<div class='card card-gold'>"
            "<b>2 — DEVELOP</b><br><br>"
            "<b>4v4+3 Switching Game</b><br><br>"
            "Supporting players create repeated "
            "opportunities to move the opposition "
            "and find space on the far side. "
            "Focus on recognising the moment "
            "rather than switching automatically."
            "</div>",
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            "<div class='card'>"
            "<b>3 — APPLY</b><br><br>"
            "<b>8v8+2 Directional Game</b><br><br>"
            "Return to a larger game with "
            "more realistic relationships. "
            "Observe whether players can "
            "recognise and use switching "
            "opportunities independently."
            "</div>",
            unsafe_allow_html=True
        )

    st.markdown("#### WHAT I'M LOOKING FOR")

    st.markdown(
        "<div class='card'>"
        "Are players scanning before receiving?<br><br>"
        "Do they recognise when the opposition "
        "has overloaded one side?<br><br>"
        "Can they move the ball quickly to "
        "the available space?<br><br>"
        "Do supporting players adjust their "
        "positions to create passing options?<br><br>"
        "Most importantly, do they recognise "
        "when to switch and when to continue "
        "playing forward?"
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='quote-block'>"
        "The success of the session isn't measured "
        "by how many times players switch the ball. "
        "It's whether they recognise when the "
        "switch creates an advantage and can "
        "make that decision in a match."
        "</div>",
        unsafe_allow_html=True
    )

    st.divider()

    # ======================================
    # SESSION DIAGRAMS
    # ======================================

    st.markdown("### SESSION EXAMPLES")

    st.markdown(
        "Different game moments require different "
        "training environments. These diagrams "
        "illustrate some of the practice formats "
        "used to challenge specific decisions "
        "and relationships."
    )

    st.markdown("#### ATTACKING ORGANISATION")

    img = get_img("8v6_Runs_behind.png")

    if img:
        c1, c2 = st.columns([1.2, 1], gap="large")

        with c1:
            st.image(
                img,
                use_container_width=True
            )

        with c2:
            st.markdown("#### 8v6 — RUNS BEHIND")

            st.markdown(
                "**Game Moment:** Attacking Organisation, "
                "Zones 3 & 4."
            )

            st.markdown(
                "Developing the recognition and timing "
                "of forward runs to penetrate the "
                "opposition's defensive line."
            )

            st.markdown(
                "**Coaching Focus**"
            )

            st.markdown(
                "Recognise space behind the line, "
                "coordinate the passer and runner, "
                "and time movements to create "
                "forward passing opportunities."
            )

    st.divider()

    st.markdown("#### TRANSITION TO ATTACK")

    img = get_img("Counter_Attack_in_Final_third.png")

    if img:
        c1, c2 = st.columns([1.2, 1], gap="large")

        with c1:
            st.image(
                img,
                use_container_width=True
            )

        with c2:
            st.markdown("#### COUNTER ATTACK — FINAL THIRD")

            st.markdown(
                "**Game Moment:** Transition to Attack."
            )

            st.markdown(
                "Creating opportunities to attack "
                "before the opposition can recover "
                "its defensive organisation."
            )

            st.markdown("**Coaching Focus**")

            st.markdown(
                "Recognise the forward option, "
                "support with immediate forward runs, "
                "and attack available space with purpose."
            )

    st.divider()

    st.markdown("#### DEFENSIVE ORGANISATION")

    img = get_img("8v8_Pressing_Half_Field.png")

    if img:
        c1, c2 = st.columns([1.2, 1], gap="large")

        with c1:
            st.image(
                img,
                use_container_width=True
            )

        with c2:
            st.markdown("#### 8v8 — HALF-FIELD PRESSING")

            st.markdown(
                "**Game Moment:** Defensive Organisation."
            )

            st.markdown(
                "Developing the team's ability "
                "to recognise pressing opportunities "
                "and apply pressure as a connected unit."
            )

            st.markdown("**Coaching Focus**")

            st.markdown(
                "Recognise pressing triggers, "
                "coordinate pressure and cover, "
                "and maintain compactness behind "
                "the players engaging the ball."
            )

    st.divider()

    st.markdown("#### DEFENSIVE TRANSITION")

    img = get_img("Phase_of_Play_8v8_counter.png")

    if img:
        c1, c2 = st.columns([1.2, 1], gap="large")

        with c1:
            st.image(
                img,
                use_container_width=True
            )

        with c2:
            st.markdown("#### PHASE OF PLAY — 8v8 COUNTER")

            st.markdown(
                "**Game Moment:** Defensive Transition."
            )

            st.markdown(
                "Challenging players to react immediately "
                "when possession is lost and respond "
                "to the developing attacking threat."
            )

            st.markdown("**Coaching Focus**")

            st.markdown(
                "Immediate reaction, pressure on the ball, "
                "supporting cover and recognition "
                "of when to counter-press or recover."
            )

    st.divider()

    st.markdown("### REFLECTING ON THE SESSION")

    st.markdown(
        "After training, I consider whether the "
        "practice created the intended problems "
        "and whether the players demonstrated "
        "improved recognition, decisions and execution. "
        "Those observations help inform the next "
        "session and the wider training cycle."
    )

    st.markdown(
        "<div class='quote-block'>"
        "The purpose of training is not to perfect "
        "the exercise. It is to improve the player "
        "and their understanding of the game."
        "</div>",
        unsafe_allow_html=True
    )
