
import streamlit as st
import sys
import os
import matplotlib.pyplot as plt

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
from utils import apply_css, sidebar_brand

st.set_page_config(
    page_title="Weekly Microcycle | Niagara FC",
    page_icon="📅",
    layout="wide"
)
apply_css()
sidebar_brand()

NAVY = "#0B192B"
BLUE = "#3478D4"
GOLD = "#E5B85C"
PALE = "#DDE9F7"

st.markdown("""
<style>
div[data-testid="stExpander"] details {
    background: #10243A !important;
    border: 1px solid #31506E !important;
    border-radius: 10px !important;
}
div[data-testid="stExpander"] details summary,
div[data-testid="stExpander"] details summary:hover,
div[data-testid="stExpander"] details[open] summary,
div[data-testid="stExpander"] details summary:focus {
    background: #173451 !important;
    color: #F4F8FF !important;
    border-radius: 9px !important;
}
div[data-testid="stExpander"] details summary *,
div[data-testid="stExpander"] details summary:hover *,
div[data-testid="stExpander"] details[open] summary * {
    color: #F4F8FF !important;
    fill: #F4F8FF !important;
}
.micro-note {
    background: #10243A;
    border-left: 4px solid #E5B85C;
    border-radius: 8px;
    padding: 15px 18px;
    margin: 12px 0;
    color: #E6F0FA;
}
.micro-quote {
    background: #10243A;
    border-left: 4px solid #3478D4;
    border-radius: 8px;
    padding: 18px 20px;
    margin: 14px 0;
    color: #F4F8FF;
}
.micro-muted {
    color: #B8CEE2;
    font-size: .92rem;
}
</style>
""", unsafe_allow_html=True)

st.title("WEEKLY MICROCYCLE")

st.markdown(
    "**Our weekly structure connects match performance, "
    "player development, physical preparation, and recovery.** "
    "The plan is adapted to match minutes, school commitments, "
    "the season phase, and individual readiness."
)

week_tab, rpe_tab, readiness_tab, fuel_tab = st.tabs([
    "📆 Week Structure",
    "📊 RPE & Training Load",
    "🌸 Female Athlete Readiness",
    "🥪 Fuel, Hydration & Recovery"
])

DAYS = [
    {
        "day": "Saturday",
        "md": "MD",
        "name": "MATCH DAY",
        "rpe": "Variable; often high",
        "plot": 9,
        "focus": "Competition and game-model execution",
        "detail": (
            "Our opportunity to apply the game model in a "
            "competitive environment. Players make decisions "
            "under pressure, manage transitions, compete in "
            "duels, and execute their roles within the team. "
            "Match demands differ by position, minutes played, "
            "and individual experience."
        ),
        "coach": (
            "Monitor minutes, match demands, injuries, and "
            "unusual fatigue. Players with limited minutes "
            "may need an appropriately planned additional stimulus."
        )
    },
    {
        "day": "Sunday",
        "md": "MD+1",
        "name": "OFF / RECOVERY",
        "rpe": "No planned team session",
        "plot": 0,
        "focus": "Recover from competition",
        "detail": (
            "No scheduled team training. Prioritize sleep, "
            "regular meals, hydration, and time away from "
            "organized football. Easy movement is optional."
        ),
        "coach": (
            "Check on knocks, soreness, illness, and wellbeing. "
            "Recovery needs vary with playing time and other activities."
        )
    },
    {
        "day": "Monday",
        "md": "MD-5",
        "name": "TECHNICAL & TACTICAL DEVELOPMENT",
        "rpe": "Suggested 5–6 / 10",
        "plot": 6,
        "focus": "Develop game-model behaviours",
        "detail": (
            "Use technical practices, positional activities, "
            "and game-based exercises to revisit learning from "
            "the match and develop the next tactical objective. "
            "Encourage quality decisions, communication, and "
            "purposeful repetitions. Adjust running volume "
            "for players who completed a full match Saturday."
        ),
        "coach": (
            "A moderate day overall. Individualize for match "
            "minutes, recovery, and school-sport demands."
        )
    },
    {
        "day": "Tuesday",
        "md": "MD-4",
        "name": "FOOTBALL-SPECIFIC PHYSICAL DEVELOPMENT",
        "rpe": "Suggested 7–9 / 10",
        "plot": 8,
        "focus": "Main planned conditioning stimulus",
        "detail": (
            "Develop high-speed running, repeated accelerations, "
            "decelerations, changes of direction, recovery runs, "
            "and the ability to repeat demanding football actions. "
            "Use progressive sprint exposures, large-space 1v1s "
            "and 2v2s, transition games, and position-related "
            "movement patterns. Football remains the context, "
            "but physical development is the main objective."
        ),
        "coach": (
            "Progress volume over time, provide adequate recovery "
            "between high-quality sprints, and do not assume "
            "small-sided games provide enough high-speed running."
        )
    },
    {
        "day": "Wednesday",
        "md": "MD-3",
        "name": "MAIN TACTICAL TRAINING",
        "rpe": "Suggested 6–8 / 10",
        "plot": 7,
        "focus": "Develop the primary game-model objective",
        "detail": (
            "Use realistic game situations, phase-of-play work, "
            "and competitive exercises to develop collective "
            "understanding. Connect units and individual roles "
            "to the week's tactical theme. Maintain purposeful "
            "intensity without repeating Tuesday's highest "
            "running volume."
        ),
        "coach": (
            "Adjust practice dimensions, repetitions, and "
            "work-to-rest ratios based on player readiness."
        )
    },
    {
        "day": "Thursday",
        "md": "MD-2",
        "name": "TACTICAL APPLICATION & MATCH PREPARATION",
        "rpe": "Suggested 4–6 / 10",
        "plot": 5,
        "focus": "Sharpen decision-making and prepare for Saturday",
        "detail": (
            "Reinforce key tactical behaviours, roles, pressing "
            "cues, attacking connections, rest defence, and set "
            "pieces. Use shorter, high-quality bouts and reduce "
            "overall volume while preserving sharpness."
        ),
        "coach": (
            "Avoid another conditioning day. Prioritize clarity, "
            "confidence, and freshness."
        )
    },
    {
        "day": "Friday",
        "md": "MD-1",
        "name": "OFF / PRE-MATCH RECOVERY",
        "rpe": "No planned team session",
        "plot": 0,
        "focus": "Arrive prepared and fresh",
        "detail": (
            "No scheduled team training. Organize kit, eat "
            "regular meals, hydrate through the day, and aim "
            "for sufficient sleep. Avoid unnecessary hard exercise."
        ),
        "coach": (
            "Check match availability and any unresolved "
            "soreness or illness."
        )
    }
]



with week_tab:
    st.subheader("Saturday Match Microcycle")
    st.caption(
        "MD = match day. This schedule is a planning framework, "
        "not a rigid prescription for every player or every week."
    )

    for d in DAYS:
        with st.expander(
            f"{d['day']} · {d['md']} — {d['name']}",
            expanded=(d["day"] == "Tuesday")
        ):
            st.markdown(f"**Primary focus:** {d['focus']}")
            st.markdown(f"**Planned effort:** {d['rpe']}")
            st.write(d["detail"])
            st.info("Coaching consideration: " + d["coach"])

    st.markdown("### Tuesday: Position-Specific Conditioning")
    st.write(
        "All players need a broad physical foundation. "
        "Positional activities add specific movement demands "
        "without restricting players to one type of movement."
    )

    positions = {
        "Wide forwards & outside backs": (
            "Longer accelerations, overlaps, wide-channel runs, "
            "recovery sprints, repeated runs behind, and crossing "
            "after a high-speed action. Example: attack a wide "
            "channel, deliver a cross, then react to a turnover "
            "and recover toward your own goal."
        ),
        "#6 / holding midfielders": (
            "Frequent scanning, short accelerations, lateral "
            "covering movements, receiving and turning under "
            "pressure, and recovery into central spaces. "
            "Example: intercept, connect a forward pass, shift "
            "to protect the centre, and recover after a turnover."
        ),
        "#8 and #10 midfielders": (
            "Repeated short movements and turns plus longer "
            "box-to-box supporting runs, pressing actions, "
            "and transitions. Example: receive between lines, "
            "turn, support the attack, then recover into midfield."
        ),
        "Centre-backs": (
            "Explosive steps to engage, lateral adjustments, "
            "turning to recover, duels, and longer sprints "
            "into space behind. Example: step to intercept, "
            "react to a ball over the top, turn, sprint, "
            "and defend a 1v1."
        ),
        "Strikers": (
            "Curved pressing runs, explosive movements across "
            "defenders, runs in behind, repeated accelerations, "
            "and finishing after intense efforts. Example: "
            "press, reset, attack depth, and finish."
        )
    }

    for name, desc in positions.items():
        with st.expander(name):
            st.write(desc)

    st.markdown(
        "<div class='micro-note'>"
        "<b>Session design:</b> Prepare movement quality first; "
        "include progressive high-speed running with sufficient "
        "rest; use positional stations and competitive games; "
        "adjust total work to players' training history. "
        "Reduce or reshape conditioning as the season progresses."
        "</div>",
        unsafe_allow_html=True
    )


with rpe_tab:
    st.subheader("RPE & Training Load")

    st.write(
        "RPE (rating of perceived exertion) describes how hard "
        "a player feels a session was, typically on a 0–10 scale. "
        "These figures are illustrative planning guides, not "
        "measured results or fixed targets for every player."
    )

    fig, ax = plt.subplots(figsize=(10, 3.6))
    fig.patch.set_facecolor(NAVY)
    ax.set_facecolor(NAVY)

    colours = [
        GOLD if d["day"] == "Saturday"
        else BLUE if d["day"] == "Tuesday"
        else "#6685A8"
        for d in DAYS
    ]

    ax.bar(
        [d["day"][:3] for d in DAYS],
        [d["plot"] for d in DAYS],
        color=colours
    )

    ax.set_ylim(0, 10)
    ax.set_ylabel("Illustrative RPE (0–10)", color=PALE)
    ax.tick_params(colors=PALE)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#6B86A3")
    ax.grid(axis="y", alpha=0.15, color="white")
    ax.set_axisbelow(True)

    fig.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

    st.caption(
        "Off days are shown at zero only to illustrate the "
        "weekly rhythm. Match-day 9 is an example, not a "
        "measurement. Actual effort varies by player."
    )

    st.markdown(
        "**Session RPE and training load are different.** "
        "One simple monitoring method is session RPE multiplied "
        "by session duration in minutes. For example, "
        "RPE 7 × 75 minutes = 525 arbitrary units. "
        "This is a monitoring tool, not a safety threshold."
    )

    st.markdown(
        "**Ask players:** How hard was today's session? "
        "How recovered do you feel? Any soreness, illness, "
        "poor sleep, or additional school-sport demands? "
        "Use responses to guide conversations and adjustments, "
        "not to punish players for reporting fatigue."
    )

    st.markdown(
        "<div class='micro-note'>"
        "<b>Coaching principle:</b> Tuesday is the main planned "
        "physical-development day, not a requirement to exhaust "
        "players. Wednesday's tactical quality and Saturday's "
        "match performance still matter. Progress workloads "
        "and adapt when schedules become congested."
        "</div>",
        unsafe_allow_html=True
    )



with readiness_tab:
    st.subheader("Female Athlete Readiness & Recovery")

    st.markdown(
        "<div class='micro-quote'>"
        "<b>Voices from the Women's Game</b><br><br>"
        "England internationals Leah Williamson and Beth Mead "
        "have spoken publicly about reducing stigma and making "
        "conversations about periods more comfortable in football."
        "<br><br><span class='micro-muted'>"
        "<a href='https://www.westeurope.englandfootball.com/articles/2025/Mar/08/leah-williamson-beth-mead-international-womens-day-20250308' "
        "target='_blank' style='color:#9CC9FF;'>"
        "Read their England Football discussion (2025)"
        "</a></span></div>",
        unsafe_allow_html=True
    )

    st.write(
        "Menstrual health is part of athlete health. Experiences "
        "differ between players and can vary from month to month. "
        "Coaches should not assume that every player performs "
        "better or worse in a particular cycle phase, or "
        "prescribe intensity from calendar dates alone."
    )

    with st.expander("What players might experience", expanded=True):
        st.write(
            "Some players experience cramps, headaches, fatigue, "
            "disrupted sleep, digestive symptoms, or mood changes. "
            "Others have few symptoms. Ask about individual "
            "readiness and what support would help, without "
            "requiring players to disclose cycle details."
        )

    with st.expander("How we respond in training"):
        st.markdown("""
- Maintain high expectations with sensible individual support.
- Provide access to water, toilets, and period products.
- Adjust volume, recovery, or exercises when appropriate.
- Avoid automatic restrictions based on menstrual phase.
- Encourage medical advice for persistent or severe symptoms.
""")

    with st.expander("Menstrual health, fuelling & RED-S"):
        st.write(
            "Irregular or absent periods, persistent fatigue, "
            "recurrent injuries, and poor recovery can be signs "
            "that deserve medical assessment. Low energy "
            "availability can affect health and performance. "
            "Players need enough food to support growth, "
            "school, training, and matches. Coaches should "
            "not diagnose or publicly discuss athlete health."
        )

    with st.expander("Professional football and research"):
        st.markdown("""
**England Football:** [Leah Williamson and Beth Mead discuss periods and stigma](https://www.westeurope.englandfootball.com/articles/2025/Mar/08/leah-williamson-beth-mead-international-womens-day-20250308)

**FIFPRO:** [Research on gynaecological health in professional women's football](https://www.fifpro.org/en/articles/2025/02/new-fifpro-research-delivers-key-findings-on-gynaecological-health-of-womens-players)

**IOC:** [Consensus statement on Relative Energy Deficiency in Sport](https://bjsm.bmj.com/content/57/17/1073)
""")

    st.caption(
        "General education, not individualized medical advice. "
        "Cycle tracking, if used, should be voluntary, "
        "private, and athlete-led."
    )


with fuel_tab:
    st.subheader("Fuel, Hydration & Recovery")

    st.write(
        "You don't need expensive supplements or a perfect "
        "diet. You need enough food, regular fluids, and a "
        "realistic plan for school days and evening training."
    )

    training_time = st.radio(
        "Choose your training start time",
        ["5:30 PM", "7:00 PM"],
        horizontal=True
    )

    if training_time == "5:30 PM":
        plan = [
            (
                "Before school",
                "Breakfast: cereal and milk, oatmeal and fruit, "
                "or eggs on toast."
            ),
            (
                "Mid-morning",
                "School snack: fruit, yogurt, cheese and crackers, "
                "or a granola bar."
            ),
            (
                "Lunch",
                "Eat a substantial lunch: sandwich, wrap, or "
                "leftovers, plus fruit and water."
            ),
            (
                "3:15–3:45 PM",
                "Pre-training snack: bagel with jam, banana and "
                "pretzels, or applesauce and crackers."
            ),
            (
                "5:30 PM",
                "Training: bring a full water bottle and "
                "drink during breaks."
            ),
            (
                "After training",
                "Dinner: pasta, rice bowl, burrito, eggs and "
                "toast, or another substantial family meal."
            )
        ]
    else:
        plan = [
            (
                "Before school",
                "Breakfast: cereal and milk, oatmeal and fruit, "
                "or eggs on toast."
            ),
            (
                "Mid-morning",
                "School snack: fruit, yogurt, cheese and crackers, "
                "or a granola bar."
            ),
            (
                "Lunch",
                "Eat a substantial lunch: sandwich, wrap, or "
                "leftovers, plus fruit and water."
            ),
            (
                "4:30–5:00 PM",
                "Early dinner or substantial snack: chicken "
                "wrap, pasta, rice bowl, or bagel with yogurt."
            ),
            (
                "6:15–6:30 PM",
                "Optional small top-up if hungry: banana, "
                "applesauce, or crackers."
            ),
            (
                "7:00 PM",
                "Training: bring water and drink during breaks."
            ),
            (
                "After training",
                "Recovery meal or snack: leftovers, sandwich "
                "and milk, or yogurt, granola, and fruit."
            )
        ]

    for when, what in plan:
        st.markdown(f"**{when}** — {what}")

    st.caption(
        "Flexible examples, not strict meal times. "
        "Adjust for appetite, digestion, training duration, "
        "and individual needs."
    )

    st.markdown("### Easy, Realistic Snacks")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
- Banana + granola bar
- Bagel with jam
- Applesauce pouch + pretzels
- Turkey or cheese wrap
""")

    with c2:
        st.markdown("""
- Yogurt + granola (keep chilled)
- Crackers + cheese
- Nut-free trail mix where school rules permit
- Chocolate milk + banana after training
""")

    st.markdown("### Water Bottle Habit")

    st.markdown("""
- Bring a refillable bottle to school and drink regularly.
- Refill it through the day rather than catching up at training.
- Bring enough water for the session and take drink breaks.
- Needs vary with bottle size, weather, sweat, and individual factors. There is no universal two-bottle rule.
""")

    st.markdown("### Match-Day & Halftime Fuel")

    st.write(
        "Eat a familiar carbohydrate-rich meal beforehand, "
        "with enough time to digest. At halftime, a small "
        "amount of easily digested carbohydrate, such as a "
        "banana, applesauce, fruit snacks, or wine gums, "
        "may help during demanding matches. Wine gums are "
        "an option, not a requirement, and do not replace "
        "regular meals or water. Avoid trying new foods "
        "for the first time on match day."
    )

    st.markdown("### After Training: Recover for Tomorrow")

    st.markdown("""
- Eat a meal containing carbohydrates and protein.
- Have a snack first if dinner will be delayed.
- Chocolate milk is convenient, but ordinary food works too.
- Teenagers generally need 8–10 hours of sleep.
- Take persistent fatigue, dizziness, or illness seriously.
""")

    st.markdown(
        "<div class='micro-note'>"
        "<b>For parents:</b> Keep it simple. An extra packed "
        "snack, a filled water bottle, and leftovers ready "
        "to reheat can make evening training much easier. "
        "Food should support growing athletes, not become "
        "another source of pressure."
        "</div>",
        unsafe_allow_html=True
    )

    st.caption(
        "General sports nutrition education for adolescents. "
        "Individual needs vary. Consult a qualified sports "
        "dietitian or healthcare professional for personal "
        "concerns. Avoid caffeinated energy drinks and "
        "unnecessary supplements."
    )
