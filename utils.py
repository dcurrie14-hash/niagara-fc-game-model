"""
Niagara FC Game Model — Shared Utilities
All constants, data, CSS, pitch helpers, and diagram functions.
Import this in every page file.
"""

import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Polygon
import numpy as np
from mplsoccer import Pitch, VerticalPitch
from PIL import Image
import os

# ── COLOURS ───────────────────────────────────────────────────────────────────
BG    = "#060E18"
NAVY  = "#0D1B2A"
ROYAL = "#4169E1"
WHITE = "#F5F5F5"
RED   = "#E53935"
GOLD  = "#F5C518"
ORANGE= "#F4A261"
GRAY  = "#BDBDBD"
LBLUE = "#89B4FF"
PITCH_C = "#1a472a"
NODE  = 800

# ── IMAGE LOADER ──────────────────────────────────────────────────────────────
def get_img(filename):
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, filename)
    if os.path.exists(path):
        return Image.open(path)
    return None

# ── CSS ───────────────────────────────────────────────────────────────────────


def apply_css():
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Oswald:wght@400;600;700&family=Open+Sans:wght@400;600&display=swap');

/* ==========================================
   GLOBAL BACKGROUND & FONTS
   ========================================== */

html, body, [class*="css"] {
    font-family: 'Open Sans', sans-serif;
    background: #060E18;
}

.block-container {
    padding-top: 1.2rem;
    padding-bottom: 2rem;
    background: #060E18;
}

.stApp {
    background-color: #060E18;
}

/* ==========================================
   SIDEBAR
   ========================================== */

[data-testid="stSidebar"] {
    background: #0D1B2A !important;
    border-right: 2px solid #4169E1;
}

[data-testid="stSidebar"] * {
    color: #F5F5F5 !important;
}

/* ==========================================
   CARDS
   ========================================== */

.card,
.card-red,
.card-orange,
.card-gold,
.card-gray,
.card-blue,
.card-green {
    background: #0D1B2A;
    border-left: 4px solid #4169E1;
    padding: 10px 14px;
    margin: 5px 0;
    border-radius: 0 6px 6px 0;
    font-size: 0.87em;
    line-height: 1.6;
    color: #F5F5F5 !important;
}

.card *,
.card-red *,
.card-orange *,
.card-gold *,
.card-gray *,
.card-blue *,
.card-green * {
    color: #F5F5F5 !important;
}

.card-red {
    border-left-color: #E53935 !important;
}

.card-orange {
    border-left-color: #F4A261 !important;
}

.card-gold {
    border-left-color: #F5C518 !important;
}

.card-gray {
    border-left-color: #BDBDBD !important;
}

.card-blue {
    border-left-color: #89B4FF !important;
}

.card-green {
    border-left-color: #4CAF50 !important;
}

/* ==========================================
   IDENTITY & QUOTE BLOCKS
   ========================================== */

.identity-word {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2em;
    letter-spacing: 4px;
    color: #4169E1;
    display: block;
    line-height: 1.1;
}

.quote-block {
    border-left: 4px solid #4169E1;
    padding: 14px 20px;
    margin: 16px 0;
    font-style: italic;
    font-size: 1.05em;
    color: #BDBDBD;
    background: #0D1B2A;
    border-radius: 0 8px 8px 0;
}

/* ==========================================
   TABS
   ========================================== */

.stTabs [data-baseweb="tab-list"] {
    gap: 3px;
    background: transparent;
}

.stTabs [data-baseweb="tab"] {
    background: #0D1B2A;
    border-radius: 4px 4px 0 0;
    padding: 7px 16px;
    font-weight: 600;
    font-size: 0.83em;
    color: #A4AFBC;
    border: 1px solid #1A2E4A;
    border-bottom: none;
}

.stTabs [aria-selected="true"] {
    background: #4169E1;
    color: #FFFFFF;
    border-color: #4169E1;
}

/* ==========================================
   INPUTS & GENERAL TEXT
   ========================================== */

textarea {
    font-size: 0.84em !important;
    background: #0D1B2A !important;
    border-color: #4169E1 !important;
    color: #F5F5F5 !important;
}

p, li, small {
    color: #F5F5F5;
}

/* ==========================================
   GLOBAL HEADING STANDARDS
   ========================================== */

/* Main page headings — muted silver-grey */

h1,
.stApp [data-testid="stMain"] h1,
.stApp [data-testid="stMain"] h1 *,
.stApp [data-testid="stMain"] [data-testid="stMarkdownContainer"] h1 {
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 2.6em !important;
    font-weight: 400 !important;
    letter-spacing: 3px !important;
    color: #C1C7CE !important;
}

/* Section headings — soft silver-grey */

h2, h3, h4, h5,
.stApp [data-testid="stMain"] h2,
.stApp [data-testid="stMain"] h3,
.stApp [data-testid="stMain"] h4,
.stApp [data-testid="stMain"] h5 {
    font-family: 'Oswald', sans-serif !important;
    font-weight: 600 !important;
    letter-spacing: 1px !important;
    color: #D0D5DA !important;
}

/* Ensure headings inside Markdown containers
   follow the same standards */

.stApp [data-testid="stMain"]
[data-testid="stMarkdownContainer"] h2,

.stApp [data-testid="stMain"]
[data-testid="stMarkdownContainer"] h3,

.stApp [data-testid="stMain"]
[data-testid="stMarkdownContainer"] h4,

.stApp [data-testid="stMain"]
[data-testid="stMarkdownContainer"] h5 {
    color: #D0D5DA !important;
    font-family: 'Oswald', sans-serif !important;
}

/* ==========================================
   HIDE STREAMLIT HEADER & FOOTER
   ========================================== */

footer, header {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# ── SIDEBAR BRANDING ──────────────────────────────────────────────────────────
def sidebar_brand():
    with st.sidebar:
        st.markdown("""
<div style='text-align:center;padding:20px 0 12px;'>
    <div style='font-size:2em;'>🔵</div>
    <div style='font-family:Bebas Neue,sans-serif;font-size:1.4em;letter-spacing:4px;color:#4169E1;margin-top:4px;'>GAME MODEL</div>
    <div style='font-family:Oswald,sans-serif;font-size:0.9em;color:#F5F5F5;letter-spacing:2px;margin-top:4px;'>DAVIE CURRIE</div>
    <div style='font-size:0.7em;color:#4169E1;letter-spacing:2px;margin-top:2px;'>NIAGARA FC  ·  OPDL</div>
    <div style='margin-top:6px;font-size:0.72em;color:#89B4FF;letter-spacing:1px;font-style:italic;'>Intensity · Aggression · Purpose</div>
</div>
<hr style='border:none;border-top:1px solid #4169E1;margin:0 0 8px;'>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# DATA
# ══════════════════════════════════════════════════════════════════════════════

FORMATIONS = {
    "1-4-3-3": {
        "pos":[(5,40,"1"),(27,10,"2"),(24,28,"4"),(24,52,"5"),(27,70,"3"),
               (50,22,"8"),(42,40,"6"),(53,58,"10"),(85,10,"7"),(90,40,"9"),(85,70,"11")],
        "roles":{
            "#1 — Goalkeeper":
                "Ball-playing goalkeeper. Create numerical superiority during build-up, organise the defensive line, protect space behind the defence, and initiate attacks quickly with purposeful distribution.",
            "#2 — Right Back":
                "Recognise when to provide width and when to underlap. Support the winger to create overloads, attack forward when opportunities arise, and recover quickly to protect wide areas during transitions.",
            "#3 — Left Back":
                "Recognise when to provide width and when to underlap. Support the winger to create overloads, attack forward when opportunities arise, and recover quickly to protect wide areas during transitions.",
            "#4 & #5 — Centre Backs":
                "Ball-playing defenders. Build from inside the box, step forward with the ball whenever possible to create numerical superiority, protect central spaces, organise the defensive line, and break lines with forward passes.",
            "#6 — Defensive Midfielder":
                "Connect the team in possession by creating passing angles and supporting underneath the ball. Protect central spaces, screen the defensive line, and provide balance during attacking and defensive transitions.",
            "#8 — Box-to-Box Midfielder":
                "Connect underneath and beyond the #9. Arrive late into attacking areas, create overloads around the ball, support combination play, and contribute immediately during transitions.",
            "#10 — Attacking Midfielder":
                "Operate between the lines to connect midfield and attack. Receive in advanced spaces, create overloads around the ball, support the #9, arrive in scoring areas, and react immediately after possession is lost.",
            "#7 — Right Winger":
                "Provide width to stretch the opposition before recognising moments to attack inside. Eliminate defenders 1v1, combine with supporting players, and create or finish goal-scoring opportunities.",
            "#11 — Left Winger":
                "Provide width to stretch the opposition before recognising moments to attack inside. Eliminate defenders 1v1, combine with supporting players, and create or finish goal-scoring opportunities.",
            "#9 — Striker":
                "Occupy the opposition centre backs, initiate the press from the front, provide a forward outlet during transition, connect teammates into attack, and make penetrating runs beyond the defensive line.",
        }
    },
    "1-4-1-4-1": {
        "pos":[(5,40,"1"),(22,10,"2"),(20,28,"4"),(20,52,"5"),(22,70,"3"),
               (35,40,"6"),
               (52,15,"7"),(52,30,"8"),(52,50,"10"),(52,65,"11"),
               (75,40,"9")],
        "roles":{
            "#1 — Goalkeeper":
                "Organise the defensive block, communicate constantly with the back four, and distribute quickly on regain to launch the counter-attack.",
            "#2 — Right Back":
                "Maintain defensive width on the right side, stay connected to the centre backs, and recover immediately on transition. Contribute forward only when the moment is clearly on.",
            "#3 — Left Back":
                "Maintain defensive width on the left side, stay connected to the centre backs, and recover immediately on transition. Contribute forward only when the moment is clearly on.",
            "#4 & #5 — Centre Backs":
                "Protect central spaces, win first contacts and aerial duels, organise the defensive line, and deny penetration through the middle. Step aggressively to intercept when the opportunity is clear.",
            "#6 — Defensive Midfielder":
                "Screen the back four at all times. Hold central positions, protect the space in front of the defensive line, and provide the balance that allows the midfield four to press around her.",
            "#8 — Right Central Midfielder":
                "Drop into the midfield line and stay compact. Press aggressively on triggers, protect the right half space, stay connected to #6 and #7, and contribute to counter-attacks immediately on regain.",
            "#10 — Left Central Midfielder":
                "Drop into the midfield line and stay compact. Press aggressively on triggers, protect the left half space, stay connected to #6 and #11, and contribute to counter-attacks immediately on regain.",
            "#7 — Right Wide Midfielder":
                "Stay narrow and compact — protect the right half space, not the wide channel. Press the ball carrier when play enters your zone and stay connected to the defensive block.",
            "#11 — Left Wide Midfielder":
                "Stay narrow and compact — protect the left half space, not the wide channel. Press the ball carrier when play enters your zone and stay connected to the defensive block.",
            "#9 — Striker":
                "Lead the press from the front to initiate the defensive block. Limit opposition build-up options, force play into predictable areas, and be ready to exploit transitions immediately on regain.",
        }
    },
    "1-4-4-2": {
        "pos":[(5,40,"1"),(27,10,"2"),(24,28,"4"),(24,52,"5"),(27,70,"3"),
               (57,10,"7"),(54,28,"8"),(54,52,"10"),(57,70,"11"),(88,28,"9"),(88,52,"9")],
        "roles":{
            "#1 — Goalkeeper":
                "Organise the defensive structure, distribute with purpose, and act as an additional outfield option during build-up.",
            "#2 — Right Back":
                "Provide width on the right, combine with #7 to create overloads, and recover quickly on transition.",
            "#3 — Left Back":
                "Provide width on the left, combine with #11 to create overloads, and recover quickly on transition.",
            "#4 & #5 — Centre Backs":
                "Ball-playing defenders. Protect central spaces, win duels, organise the defensive line, and play forward whenever the opportunity is on.",
            "#7 — Right Midfielder":
                "Stay wide to stretch the opposition, deliver early crosses, press aggressively from the front, and track back to support defensively.",
            "#8 — Right Central Midfielder":
                "Win second balls, connect between the lines, press on triggers, and arrive into the box from deep positions.",
            "#10 — Left Central Midfielder":
                "Win second balls, connect between the lines, press on triggers, and arrive into the box from deep positions.",
            "#11 — Left Midfielder":
                "Stay wide to stretch the opposition, deliver early crosses, press aggressively from the front, and track back to support defensively.",
            "#9 & #9 — Strikers":
                "Combine in pairs, press from the front to initiate the defensive block, provide forward outlets during transition, and support each other in and out of possession.",
        }
    },
}

PROFILES = {
    "#1 — Goalkeeper": {
        "scores": [4.0, 4.5, 3.5, 4.5, 5.0],
        "intro": (
            "The goalkeeper is our extra outfield player and the starting point "
            "of our attacking organisation. She protects the goal, supports "
            "possession, manages the space behind the defensive line and "
            "organises teammates. She must be brave, composed and decisive, "
            "recognising when to build, play forward or relieve pressure."
        ),
        "attrs": {
            "Technical": [
                "Receives and controls the ball with a first touch that prepares the next action",
                "Distributes accurately with both feet over short, medium and long distances",
                "Uses appropriate passing technique to break lines, switch play or find a forward",
                "Demonstrates effective handling, footwork and shot-stopping technique",
                "Claims, punches or redirects crosses using appropriate technique",
                "Executes quick and accurate distribution after regaining possession"
            ],
            "Tactical": [
                "Creates passing angles and supports numerical superiority during build-up",
                "Recognises when to play through pressure, switch play or use a longer forward pass",
                "Adjusts starting position to manage space behind the defensive line",
                "Recognises when to sweep, hold position or engage an attacker",
                "Anticipates crosses, through balls and second-ball situations",
                "Identifies opportunities to initiate attacking transitions before opponents recover",
                "Organises defensive positioning and responds to changes in the opposition's shape"
            ],
            "Physical": [
                "Explosive over short distances when attacking loose balls or closing down attackers",
                "Agile and coordinated when changing direction and making saves",
                "Develops the jumping ability and strength needed for aerial challenges",
                "Recovers quickly between repeated goalkeeping actions",
                "Maintains physical readiness throughout the match"
            ],
            "Mental & Social": [
                "Remains composed and makes clear decisions under pressure",
                "Responds positively to mistakes and prepares for the next action",
                "Communicates early, clearly and consistently",
                "Demonstrates courage in possession and in defensive situations",
                "Maintains concentration during extended periods without involvement",
                "Takes responsibility and leads through actions and communication"
            ],
            "NFC Non-Negotiables": [
                "Be available to support possession and offer a passing option",
                "Recognise the forward option first; choose the pass that best progresses the attack",
                "Be brave and purposeful when playing out under pressure",
                "Manage the space behind the defensive line and act decisively",
                "Communicate early and organise the defensive unit",
                "React immediately to changes of possession and prepare the next action"
            ]
        }
    },

    "#2 & #3 — Fullbacks": {
        "scores": [3.5, 4.5, 4.5, 4.0, 4.5],
        "intro": (
            "Fullbacks connect our defensive and attacking organisation. "
            "They provide width when required, support combinations and "
            "recognise opportunities to overlap or underlap. They must "
            "understand when to advance, when to support underneath and "
            "when to remain in a position of defensive balance."
        ),
        "attrs": {
            "Technical": [
                "Receives with a positive first touch that creates time or space",
                "Passes accurately in short combinations and across longer distances",
                "Delivers quality crosses and cutbacks from wide attacking areas",
                "Combines effectively using one-touch and two-touch passing",
                "Defends 1v1 situations with controlled footwork and appropriate tackling technique",
                "Protects possession and plays effectively when pressured near the touchline"
            ],
            "Tactical": [
                "Recognises the wide forward's position to decide whether to overlap, underlap or support underneath",
                "Provides width when needed without occupying the same space as a teammate",
                "Recognises when to advance and when to maintain defensive balance",
                "Supports forward passing options and creates useful passing angles",
                "Anticipates space behind the defensive line when the team attacks",
                "Recovers quickly and protects dangerous spaces during defensive transition",
                "Moves centrally to connect with centre backs when the team defends",
                "Recognises when to press the wide player and when to delay or protect space"
            ],
            "Physical": [
                "Repeatedly performs high-intensity attacking and defensive runs",
                "Develops acceleration and recovery speed over short and medium distances",
                "Competes effectively in physical duels in wide areas",
                "Changes direction quickly when defending or supporting combinations",
                "Maintains the physical capacity to repeat quality actions throughout the match"
            ],
            "Mental & Social": [
                "Demonstrates discipline when deciding whether to advance or hold",
                "Communicates consistently with the wide forward, midfielders and centre backs",
                "Competes confidently in 1v1 defensive situations",
                "Responds immediately when possession changes",
                "Shows resilience after being beaten or making a mistake"
            ],
            "NFC Non-Negotiables": [
                "Recognise when to provide width, overlap, underlap or support underneath",
                "Advance with purpose while maintaining awareness of defensive balance",
                "React immediately on losing possession and recover towards dangerous space",
                "Stay connected to the centre backs and protect central areas when defending",
                "Compete in wide defensive duels and prevent easy penetration",
                "Communicate and coordinate movements with nearby teammates"
            ]
        }
    },

    "#4 & #5 — Centre Backs": {
        "scores": [4.0, 4.5, 4.5, 4.5, 5.0],
        "intro": (
            "Centre backs provide the foundation of our defensive structure "
            "and attacking build-up. They must be confident progressing the "
            "ball, aggressive when defending and intelligent in managing "
            "space, depth and cover. They lead the defensive unit through "
            "their positioning, decisions and communication."
        ),
        "attrs": {
            "Technical": [
                "Receives and passes confidently under pressure",
                "Plays accurate forward passes that break lines and find teammates between lines",
                "Switches play or finds forward runners with appropriate longer passes",
                "Uses effective first-touch and ball-carrying technique to escape pressure",
                "Competes strongly in aerial challenges and defensive duels",
                "Demonstrates controlled tackling, blocking and interception technique"
            ],
            "Tactical": [
                "Creates useful passing angles with the goalkeeper and defensive partners",
                "Recognises opportunities to carry forward or pass through opposition lines",
                "Identifies when to step into midfield and when to maintain the defensive line",
                "Protects central spaces and directs opponents away from dangerous areas",
                "Manages defensive depth and anticipates runs behind a higher line",
                "Maintains cover and balance when a defensive teammate presses",
                "Recognises pressing triggers and coordinates pressure with nearby players",
                "Adjusts positioning in response to the ball, opponents and teammates",
                "Organises the defensive line during open play and defensive transitions"
            ],
            "Physical": [
                "Competes strongly in aerial and ground duels",
                "Develops acceleration and recovery speed to defend space behind",
                "Uses strength and balance effectively when protecting the penalty area",
                "Changes direction efficiently when responding to attacking movement",
                "Maintains physical readiness and repeat-action quality throughout the match"
            ],
            "Mental & Social": [
                "Remains calm and composed when building under pressure",
                "Communicates clearly and organises teammates",
                "Takes pride in defending and competing for the ball",
                "Shows courage when stepping forward or defending isolated situations",
                "Responds positively to setbacks and maintains concentration",
                "Leads through consistent standards and responsible decisions"
            ],
            "NFC Non-Negotiables": [
                "Be available in build-up and look to progress the ball forward",
                "Protect central spaces and prevent easy penetration",
                "Step forward decisively when the pressing opportunity is on",
                "Provide cover and manage space behind teammates who press",
                "Stay connected to the defensive unit and communicate constantly",
                "Compete aggressively for first balls and react to second balls"
            ]
        }
    },

    "#6 — Defensive Midfielder": {
        "scores": [4.0, 5.0, 4.0, 5.0, 5.0],
        "intro": (
            "The #6 connects defence and attack while providing balance "
            "and protecting central spaces. She must recognise when to "
            "offer a forward passing option, when to support underneath "
            "and when to remain behind the ball. Her positional "
            "intelligence allows teammates to attack and press with confidence."
        ),
        "attrs": {
            "Technical": [
                "Receives under pressure with an open body shape and effective first touch",
                "Passes accurately over short and medium distances with either foot",
                "Executes forward passes that break lines and connect attacking players",
                "Protects possession and uses appropriate turns to escape pressure",
                "Carries the ball forward when space is available",
                "Uses controlled tackling and interception technique to regain possession"
            ],
            "Tactical": [
                "Provides passing angles between the defensive and attacking lines",
                "Recognises when to remain central, drop deeper or move to create a passing lane",
                "Identifies forward options before receiving the ball",
                "Maintains defensive balance when teammates advance",
                "Screens central passing lanes and protects space in front of the centre backs",
                "Recognises when to step forward to press and when to hold or provide cover",
                "Adjusts positioning to the team's pressing or mid-block structure",
                "Anticipates second balls and positions to regain possession",
                "Supports attacking transitions without leaving central spaces unnecessarily exposed"
            ],
            "Physical": [
                "Covers ground efficiently to support both attacking and defensive actions",
                "Accelerates quickly to close space and compete for loose balls",
                "Competes effectively in midfield duels",
                "Demonstrates balance and strength when protecting possession",
                "Repeats high-quality actions throughout the match"
            ],
            "Mental & Social": [
                "Remains composed when receiving in congested areas",
                "Demonstrates patience and discipline in positional decisions",
                "Communicates and helps organise teammates around the ball",
                "Anticipates situations and takes responsibility before danger develops",
                "Makes clear decisions quickly under pressure",
                "Responds positively to mistakes and maintains focus"
            ],
            "NFC Non-Negotiables": [
                "Be available to connect the defensive and attacking units",
                "Look forward before receiving and progress the ball when possible",
                "Protect central spaces and maintain defensive balance",
                "Recognise when to press and ensure space behind is covered",
                "Anticipate and compete for second balls",
                "Communicate and organise teammates in possession and out of possession"
            ]
        }
    },

    "#8 & #10 — Central Midfielders": {
        "scores": [4.5, 4.5, 4.5, 4.0, 4.5],
        "intro": (
            "Our #8 and #10 connect midfield to attack, create forward "
            "options and influence the game between opposition lines. "
            "They must recognise when to support underneath, receive "
            "between lines, run beyond the forwards or arrive in scoring "
            "positions. Their roles may differ within the formation, "
            "but both require creativity, intelligence and defensive responsibility."
        ),
        "attrs": {
            "Technical": [
                "Receives on the half-turn and prepares to play forward",
                "Controls and protects the ball in tight spaces under pressure",
                "Executes penetrating passes and combinations through opposition lines",
                "Uses one-touch passing, wall passes and third-player combinations",
                "Carries the ball forward to eliminate opponents or create advantages",
                "Finishes effectively from central areas and late runs into the penalty area",
                "Uses accurate passing and appropriate weight of delivery to create chances"
            ],
            "Tactical": [
                "Recognises pockets of space between opposition midfield and defensive lines",
                "Provides passing options underneath, alongside or beyond the #9",
                "Identifies when to receive to feet and when to run beyond the defensive line",
                "Recognises opportunities for third-player movements and combinations",
                "Coordinates movements with wide forwards and the striker to avoid occupying the same space",
                "Times forward runs to arrive in dangerous areas rather than standing in them",
                "Understands when to maintain midfield balance and when to join the attack",
                "Recognises pressing triggers and coordinates pressure with the forwards",
                "Recovers quickly and tracks dangerous midfield runners during defensive transitions",
                "Anticipates second balls and positions to regain possession"
            ],
            "Physical": [
                "Repeatedly supports attacking and defensive actions",
                "Accelerates into space and changes direction quickly",
                "Competes effectively in midfield challenges",
                "Develops the endurance to make repeated supporting and penetrating runs",
                "Maintains physical intensity and quality throughout the match"
            ],
            "Mental & Social": [
                "Shows courage and creativity when receiving under pressure",
                "Demonstrates a desire to create and score goals",
                "Makes decisions based on the movement of teammates and opponents",
                "Communicates and connects players across midfield and attack",
                "Competes for loose balls and reacts positively to setbacks",
                "Balances attacking ambition with defensive responsibility"
            ],
            "NFC Non-Negotiables": [
                "Create forward passing options between and beyond opposition lines",
                "Look to play forward or combine to break lines whenever possible",
                "Recognise when to support underneath and when to run beyond",
                "Time movements into the penalty area to create scoring opportunities",
                "Press together with teammates and react immediately when possession is lost",
                "Compete for second balls and recover to protect central spaces"
            ]
        }
    },

    "#7 & #11 — Wide Forwards": {
        "scores": [4.5, 3.5, 5.0, 4.0, 4.5],
        "intro": (
            "Wide forwards stretch and unbalance the opposition through "
            "their positioning, movement and direct attacking play. "
            "They must recognise when to stay wide, attack a defender, "
            "combine with teammates or run into space behind. "
            "They contribute goals and chances while remaining "
            "committed to pressing and defensive recovery."
        ),
        "attrs": {
            "Technical": [
                "Uses a positive first touch to attack space or prepare the next action",
                "Dribbles confidently and effectively in 1v1 situations",
                "Changes speed and direction to eliminate defenders",
                "Delivers accurate crosses and cutbacks from dangerous wide areas",
                "Finishes effectively from wide and central attacking positions",
                "Combines through short passes, lay-offs and third-player actions",
                "Protects possession when isolated or under pressure"
            ],
            "Tactical": [
                "Recognises when to provide width and when to move inside",
                "Identifies opportunities to isolate and attack defenders 1v1",
                "Times runs behind the defensive line to exploit space",
                "Coordinates movement with the fullback to create overlaps and underlaps",
                "Recognises when to attack the penalty area as the opposite-side forward",
                "Identifies opportunities to combine rather than force an individual action",
                "Prioritises effective cutbacks and ground deliveries when appropriate in Zone 4",
                "Recognises pressing triggers and coordinates pressure on opposition defenders",
                "Recovers to support the fullback and protect wide spaces when required"
            ],
            "Physical": [
                "Demonstrates acceleration and speed to attack defenders and space behind",
                "Changes direction explosively to create separation",
                "Uses strength and balance to protect the ball in wide areas",
                "Repeats attacking runs, pressing actions and defensive recoveries",
                "Maintains high-intensity contributions throughout the match"
            ],
            "Mental & Social": [
                "Demonstrates courage and confidence in attacking 1v1 situations",
                "Maintains a positive, forward-thinking attacking mentality",
                "Shows resilience after losing possession or missing opportunities",
                "Recognises when to be direct and when to involve teammates",
                "Competes consistently in attacking and defensive moments",
                "Takes responsibility for creating and finishing chances"
            ],
            "NFC Non-Negotiables": [
                "Provide width or attack inside at the appropriate moment",
                "Recognise opportunities to attack defenders and space behind",
                "Play forward with purpose and support combinations when needed",
                "Attack the penalty area when the ball is delivered from the opposite side",
                "Press with teammates and react immediately when possession is lost",
                "Recover and support the fullback when defensive balance requires it"
            ]
        }
    },

    "#9 — Striker": {
        "scores": [4.0, 4.5, 4.5, 4.5, 5.0],
        "intro": (
            "The #9 provides a central attacking reference point, "
            "connects teammates and threatens the opposition's defensive line. "
            "She must recognise when to hold possession, combine, "
            "run behind or attack the penalty area. Without the ball, "
            "she helps initiate the press and sets the standard "
            "for collective defensive effort."
        ),
        "attrs": {
            "Technical": [
                "Receives and protects the ball with defenders applying pressure",
                "Uses an effective first touch when receiving with back to goal",
                "Combines quickly through lay-offs, wall passes and third-player actions",
                "Finishes effectively using different techniques and from varied situations",
                "Competes for aerial balls and controls or redirects forward passes",
                "Uses appropriate ball-striking technique to finish crosses and cutbacks",
                "Secures possession long enough to bring supporting teammates into play"
            ],
            "Tactical": [
                "Provides a central forward option during build-up and attacking transitions",
                "Recognises when to check towards the ball and when to run behind",
                "Occupies centre backs and creates space for attacking teammates",
                "Connects midfielders and forwards through intelligent link play",
                "Times movements to attack crosses, cutbacks and rebounds",
                "Recognises when to secure possession and when to release runners quickly",
                "Coordinates pressing actions and directs opponents towards team pressure",
                "Anticipates second balls and attacking opportunities around the penalty area",
                "Adjusts positioning to remain a forward threat without becoming isolated"
            ],
            "Physical": [
                "Competes effectively against physical defenders",
                "Develops acceleration to threaten space behind the defensive line",
                "Uses strength and balance to protect possession",
                "Competes confidently in aerial challenges",
                "Repeats pressing actions, forward runs and attacking movements",
                "Maintains physical intensity throughout the match"
            ],
            "Mental & Social": [
                "Demonstrates confidence and composure in scoring situations",
                "Competes willingly in physical challenges",
                "Responds positively to missed chances and setbacks",
                "Works selflessly to create opportunities for teammates",
                "Communicates and coordinates movements with attacking players",
                "Leads through effort, attitude and defensive commitment"
            ],
            "NFC Non-Negotiables": [
                "Provide a central forward option and threaten space behind",
                "Recognise when to secure possession, combine or release the ball forward",
                "Attack the penalty area with purposeful movement",
                "Occupy defenders and create space for supporting runners",
                "Initiate and coordinate pressing actions with teammates",
                "Compete for first and second balls and react immediately to transitions"
            ]
        }
    }
}

CYCLE_PHASES = {
    "🔵  Menstrual  (Days 1–5)": {
        "color":"#4472C4","bg":"#101d36",
        "energy":"Lower — fatigue more noticeable",
        "intensity":"Low – Medium",
        "focus":"Recovery · Mobility · Light Technical Work",
        "tips":["Reduce high-intensity volume — quality over quantity","Prioritise technical clarity and decision-making work",
                "Allow extra warm-up and cool-down time","Check in individually — comfort and open communication first",
                "Excellent time for video review and tactical understanding","Iron-rich nutrition and hydration are important this phase"],
        "avoid":"Heavy conditioning, high-volume sprinting, maximum strength work"
    },
    "🟢  Follicular  (Days 6–13)": {
        "color":"#70AD47","bg":"#0f2416",
        "energy":"Rising — motivation and strength building",
        "intensity":"High",
        "focus":"Strength · Speed · High-Intensity Conditioning",
        "tips":["Best window for high-intensity conditioning and fitness work","Introduce new patterns — players more receptive and motivated",
                "Push pressing, duelling, and explosive movement work","Ideal for complex tactical concepts — brain and body are ready",
                "Strength peaks this phase — capitalise on it","Competitive intensity in training is well tolerated"],
        "avoid":"Nothing — this is the peak training window, use it"
    },
    "🟡  Ovulation  (Day ~14)": {
        "color":"#FFC000","bg":"#2e2200",
        "energy":"Peak — coordination and power at highest",
        "intensity":"High  ⚠️  (monitor joints)",
        "focus":"Skill Work · Fast-Paced Drills · Game Scenarios",
        "tips":["Best window for peak performance sessions","Joint laxity slightly increased — thorough warm-up essential",
                "Ideal for small-sided games and high-speed decision-making","Teamwork and communication drills work excellently here",
                "Monitor closely for injury risk — ligaments slightly looser","Emphasise strength work in warm-up to protect joints"],
        "avoid":"Skipping the warm-up — injury risk is elevated this phase"
    },
    "🟠  Luteal  (Days 15–28)": {
        "color":"#ED7D31","bg":"#2a1400",
        "energy":"Dipping — fatigue and body temperature may rise",
        "intensity":"Medium",
        "focus":"Technique · Set Pieces · Strategy · Controlled Training",
        "tips":["Maintain quality over quantity in session design","Tactical and technical sessions are excellent this phase",
                "Hydration and nutrition more critical — body temp elevated","Great phase for set piece rehearsal and video analysis",
                "Increase recovery focus — sleep, stretching, foam rolling","Be attentive to mood and energy — check in as a group"],
        "avoid":"Excessive volume, back-to-back high-intensity sessions"
    }
}

DAYS = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
MICRO_SCHEDULE = {
    "Sunday": {
        "icon": "⚽", "title": "Match Day", "rpe": "RPE 10", "color": RED,
        "desc": "Compete and apply the game model within a competitive environment.",
    },
    "Monday": {
        "icon": "🔄", "title": "MD+1 — Recovery & Reflection", "rpe": "RPE 2-3", "color": LBLUE,
        "desc": "Light movement, recovery strategies, video review, and reflection. The priority is physical and mental recovery following competition.",
    },
    "Tuesday": {
        "icon": "😴", "title": "MD+2 — Off", "rpe": "RPE 0", "color": "#555",
        "desc": "Full recovery day to allow players to recharge physically and mentally.",
    },
    "Wednesday": {
        "icon": "🔥", "title": "MD+3 — Main Training", "rpe": "RPE 8-9", "color": RED,
        "desc": "Highest load of the week. The primary game moment and tactical objective are developed through game-based activities aligned with our game model. Larger player numbers, realistic game scenarios, and competitive football actions are used to challenge players physically, technically, tactically, and cognitively.",
    },
    "Thursday": {
        "icon": "🧠", "title": "MD-3 — Tactical Application", "rpe": "RPE 6-7", "color": GOLD,
        "desc": "Reinforce and apply the principles introduced on Wednesday. Activities are designed to increase repetitions of key moments while maintaining realism and decision-making. Session load may be adjusted based on player readiness, school sport commitments, and fixture congestion.",
    },
    "Friday": {
        "icon": "⚽", "title": "MD-2 — Optional Technical Training", "rpe": "RPE 4-5", "color": LBLUE,
        "desc": "Optional individual development session focused on technical confidence, ball mastery, finishing, position-specific work, and individual skill development. Attendance is optional to support appropriate load management.",
    },
    "Saturday": {
        "icon": "😴", "title": "MD-1 — Off", "rpe": "RPE 0", "color": "#555",
        "desc": "Recovery and mental preparation for competition.",
    },
}
# ══════════════════════════════════════════════════════════════════════════════
# PITCH HELPERS
# ══════════════════════════════════════════════════════════════════════════════

def make_pitch(figsize=(14,8)):
    p = Pitch(pitch_type='statsbomb', pitch_color=PITCH_C, line_color='white',
              linewidth=1.8, goal_type='box', corner_arcs=True)
    fig, ax = p.draw(figsize=figsize)
    fig.patch.set_facecolor(BG)
    return fig, ax, p

def draw_channels(ax):
    ch_data = [(0,18,RED,0.07),(18,30,GOLD,0.07),(30,50,ROYAL,0.06),(50,62,GOLD,0.07),(62,80,RED,0.07)]
    for y1,y2,clr,alph in ch_data:
        rect = mpatches.Rectangle((0,y1),120,y2-y1,facecolor=clr,alpha=alph,edgecolor='none',zorder=1)
        ax.add_patch(rect)
    for y in [18,30,50,62]:
        ax.axhline(y=y,color='white',alpha=0.15,lw=0.8,linestyle='--')
    for lbl,yc,clr in [("WIDE",9,RED),("HALF\nSPACE",24,GOLD),("CENTRAL",40,ROYAL),("HALF\nSPACE",56,GOLD),("WIDE",71,RED)]:
        ax.text(122,yc,lbl,color=clr,fontsize=6.5,ha='left',va='center',fontweight='bold',alpha=0.7)

def pl(ax, x, y, lbl, color=ROYAL):
    ax.scatter(x, y, s=NODE, c=color, edgecolors='white', linewidths=2.5, zorder=5)
    ax.annotate(lbl,(x,y),fontsize=9,ha='center',va='center',
                color='white',fontweight='bold',zorder=6)

def opp(ax, x, y, lbl=""):
    ax.scatter(x, y, s=500, c=RED, edgecolors='white', linewidths=1.5, zorder=4, alpha=0.85)
    if lbl:
        ax.annotate(lbl,(x,y),fontsize=7.5,ha='center',va='center',color='white',fontweight='bold',zorder=5)

def arr(ax, p, xs, ys, xe, ye, color=ROYAL, w=2.5, hw=7, hl=6):
    p.arrows(xs,ys,xe,ye,ax=ax,color=color,width=w,headwidth=hw,headlength=hl,zorder=3,alpha=0.9)

def flood(ax, x1, y1, x2, y2, color, alpha=0.18, lw=1.5, ls='--'):
    rect = mpatches.Rectangle((x1,y1),x2-x1,y2-y1,
                               facecolor=color,alpha=alpha,
                               edgecolor=color,linewidth=lw,linestyle=ls,zorder=2)
    ax.add_patch(rect)

def zlabels(ax, H=80):
    for x in (30,60,90):
        ax.axvline(x=x,color='white',alpha=0.12,lw=1,linestyle='--')
    for lbl,xc in [("Z1",15),("Z2",45),("Z3",75),("Z4",105)]:
        ax.text(xc,H+2,lbl,color='white',alpha=0.3,fontsize=8,ha='center',va='bottom')

# ══════════════════════════════════════════════════════════════════════════════
# DIAGRAM FUNCTIONS
# ══════════════════════════════════════════════════════════════════════════════

def fig_hz_zones():
    fig,ax,p = make_pitch(figsize=(14,8))
    draw_channels(ax)
    for i,(clr,alph) in enumerate([('#1a3a6a',0.2),('#1a4a2a',0.15),('#3a2a0a',0.15),('#3a0a0a',0.15)]):
        flood(ax,i*30,0,(i+1)*30,80,clr,alpha=alph,ls='-')
    for x in (30,60,90): ax.axvline(x=x,color='white',alpha=0.5,lw=2)
    for lbl,xc,clr in [("ZONE 1\nBUILD PHASE",15,LBLUE),("ZONE 2\nPROGRESS",45,ROYAL),
                        ("ZONE 3\nCREATE",75,GOLD),("ZONE 4\nFINISH",105,RED)]:
        ax.text(xc,75,lbl,color=clr,fontsize=12,ha='center',va='center',fontweight='bold',alpha=0.9)
    banner = mpatches.Rectangle((0,36),120,8,facecolor=ROYAL,alpha=0.85,zorder=4)
    ax.add_patch(banner)
    ax.text(60,40,"THINK FORWARD  ·  PLAY FORWARD  ·  RUN FORWARD",
            color='white',fontsize=12,ha='center',va='center',fontweight='bold',zorder=5,fontfamily='monospace')
    ax.set_title("Pitch Geography — Horizontal Zones",color=WHITE,fontsize=14,fontweight='bold',pad=8)
    fig.patch.set_facecolor(BG); plt.tight_layout(); return fig

def fig_channels():
    fig,ax,p = make_pitch(figsize=(14,8))
    ch_data = [((0,18),RED,"LEFT\nWIDE\nCHANNEL"),
               ((18,30),GOLD,"LEFT\nHALF\nSPACE"),
               ((30,50),ROYAL,"CENTRAL\nCHANNEL"),
               ((50,62),GOLD,"RIGHT\nHALF\nSPACE"),
               ((62,80),RED,"RIGHT\nWIDE\nCHANNEL")]
    alphas = [0.15,0.15,0.18,0.15,0.15]
    for i,((y1,y2),clr,name) in enumerate(ch_data):
        flood(ax,0,y1,120,y2,clr,alpha=alphas[i],ls='-')
        if y2 < 80:
            ax.axhline(y=y2,color='white',alpha=0.45,lw=1.5,linestyle='--')
        ax.text(60,(y1+y2)/2,name,color=clr,fontsize=11,ha='center',va='center',fontweight='bold',alpha=0.9)
    ax.annotate("Edge of 6-yd box",(2,31),fontsize=8,color=WHITE,alpha=0.7)
    ax.annotate("Edge of 18-yd box",(2,19),fontsize=8,color=WHITE,alpha=0.7)
    ax.set_title("Pitch Geography — Vertical Channels",color=WHITE,fontsize=14,fontweight='bold',pad=8)
    fig.patch.set_facecolor(BG); plt.tight_layout(); return fig

def fig_zones_channels():
    fig = plt.figure(figsize=(18,10))
    fig.patch.set_facecolor(BG)

    ax_left = fig.add_axes([0.0, 0.0, 0.22, 1.0])
    ax_left.set_facecolor(NAVY); ax_left.axis('off')
    ax_left.text(0.5, 0.96, "HORIZONTAL\nZONES", transform=ax_left.transAxes,
                 fontsize=11, ha='center', va='top', color=WHITE, fontweight='bold',
                 fontfamily='monospace')
    zone_info = [
        (LBLUE, "ZONE 1", "BUILD-UP",
         ["GK as extra player","CBs split wide","#6 drops between lines","Patience with purpose"]),
        (ROYAL, "ZONE 2", "PROGRESS",
         ["Break first line","Create overloads","Drive forward","Third-man combinations"]),
        (GOLD,  "ZONE 3", "CREATE",
         ["Half-space combinations","Penetrate the last line","Switch when overloaded","Forward runs beyond"]),
        (RED,   "ZONE 4", "FINISH",
         ["Min. 4 attack the box","Near/central/back post","Attack end line","Cutbacks — 28% of goals"]),
    ]
    y_positions = [0.72, 0.52, 0.32, 0.10]
    for (clr, z, sub, pts), yp in zip(zone_info, y_positions):
        rect = mpatches.FancyBboxPatch((0.05, yp), 0.90, 0.18,
               boxstyle="round,pad=0.02", facecolor=clr, alpha=0.25,
               edgecolor=clr, linewidth=1.5, transform=ax_left.transAxes, zorder=2)
        ax_left.add_patch(rect)
        ax_left.text(0.10, yp+0.155, f"{z}", transform=ax_left.transAxes,
                     fontsize=11, color=clr, fontweight='bold', va='top')
        ax_left.text(0.10, yp+0.128, sub, transform=ax_left.transAxes,
                     fontsize=9, color=WHITE, va='top', alpha=0.8)
        for i, pt in enumerate(pts):
            ax_left.text(0.10, yp+0.098-i*0.024, f"• {pt}", transform=ax_left.transAxes,
                         fontsize=8, color=WHITE, va='top', alpha=0.75)

    ax_right = fig.add_axes([0.78, 0.0, 0.22, 1.0])
    ax_right.set_facecolor(NAVY); ax_right.axis('off')
    ax_right.text(0.5, 0.96, "VERTICAL\nCHANNELS", transform=ax_right.transAxes,
                  fontsize=11, ha='center', va='top', color=WHITE, fontweight='bold',
                  fontfamily='monospace')
    ch_info = [
        (RED,   "WIDE CHANNELS",
         ["Fullbacks & wide forwards","Stretch compactness","Attack end line","Deliver early crosses"]),
        (GOLD,  "HALF SPACES",
         ["Most dangerous zone","Cut inside from wide","Midfielders arrive late","Create combinations"]),
        (ROYAL, "CENTRAL CORRIDOR",
         ["Highest protection","Highest reward","Penetrate through middle","#6 screens centrally"]),
    ]
    y_positions_r = [0.62, 0.38, 0.12]
    for (clr, ch, pts), yp in zip(ch_info, y_positions_r):
        rect = mpatches.FancyBboxPatch((0.05, yp), 0.90, 0.22,
               boxstyle="round,pad=0.02", facecolor=clr, alpha=0.25,
               edgecolor=clr, linewidth=1.5, transform=ax_right.transAxes, zorder=2)
        ax_right.add_patch(rect)
        ax_right.text(0.10, yp+0.195, ch, transform=ax_right.transAxes,
                      fontsize=11, color=clr, fontweight='bold', va='top')
        for i, pt in enumerate(pts):
            ax_right.text(0.10, yp+0.155-i*0.034, f"• {pt}", transform=ax_right.transAxes,
                          fontsize=8, color=WHITE, va='top', alpha=0.75)

    ax_pitch = fig.add_axes([0.22, 0.08, 0.56, 0.88])
    p = Pitch(pitch_type='statsbomb', pitch_color=PITCH_C, line_color='white',
              linewidth=1.5, goal_type='box', corner_arcs=True)
    p.draw(ax=ax_pitch)
    ax_pitch.set_facecolor(PITCH_C)

    for i,(clr,alph) in enumerate([('#1a3a6a',0.3),('#1a4a2a',0.25),('#3a2a0a',0.25),('#3a0a0a',0.25)]):
        rect = mpatches.Rectangle((i*30,0),30,80,facecolor=clr,alpha=alph,zorder=1)
        ax_pitch.add_patch(rect)
    for x in (30,60,90):
        ax_pitch.axvline(x=x,color='white',alpha=0.6,lw=1.5)

    for lbl,xc,clr in [("Z1",15,LBLUE),("Z2",45,ROYAL),("Z3",75,GOLD),("Z4",105,RED)]:
        ax_pitch.text(xc,40,lbl,color=clr,fontsize=16,ha='center',va='center',
                      fontweight='bold',alpha=0.9,zorder=4)

    for y1,y2,clr,alph in [(0,18,RED,0.1),(18,30,GOLD,0.1),(30,50,ROYAL,0.08),(50,62,GOLD,0.1),(62,80,RED,0.1)]:
        rect = mpatches.Rectangle((0,y1),120,y2-y1,facecolor=clr,alpha=alph,zorder=2)
        ax_pitch.add_patch(rect)
    for y in [18,30,50,62]:
        ax_pitch.axhline(y=y,color='white',alpha=0.3,lw=1,linestyle='--')

    for lbl,yc,clr in [("WIDE",9,RED),("HALF\nSPACE",24,GOLD),("CENTRAL\nCORRIDOR",40,ROYAL),
                        ("HALF\nSPACE",56,GOLD),("WIDE",71,RED)]:
        ax_pitch.text(122,yc,lbl,color=clr,fontsize=7,ha='left',va='center',
                      fontweight='bold',alpha=0.85)

    ax_pitch.annotate('',xy=(115,75),xytext=(5,75),
                      arrowprops=dict(arrowstyle='->,head_width=0.8,head_length=2',
                                     color=GOLD,lw=2.5))
    ax_pitch.text(60,77,"ATTACKING ORGANISATION →",color=GOLD,fontsize=8,
                  ha='center',fontweight='bold',alpha=0.9)

    ax_pitch.annotate('',xy=(5,5),xytext=(115,5),
                      arrowprops=dict(arrowstyle='->,head_width=0.8,head_length=2',
                                     color=LBLUE,lw=2.5))
    ax_pitch.text(60,3,"← DEFENSIVE ORGANISATION",color=LBLUE,fontsize=8,
                  ha='center',fontweight='bold',alpha=0.9)

    fig.text(0.50, 0.98, "PITCH GEOGRAPHY — HORIZONTAL ZONES & VERTICAL CHANNELS",
             ha='center', va='top', fontsize=14, color=WHITE, fontweight='bold',
             fontfamily='monospace')
    fig.text(0.50, 0.94, "NIAGARA FC  ·  GAME MODEL",
             ha='center', va='top', fontsize=9, color=LBLUE, alpha=0.8,
             fontfamily='monospace')

    plt.tight_layout(rect=[0,0,1,0.93])
    return fig

def fig_formation(name):
    fig,ax,p = make_pitch()
    draw_channels(ax)
    for x,y,lbl in FORMATIONS[name]["pos"]: pl(ax,x,y,lbl)
    ax.set_title(f"{name}  —  Team Shape",color=WHITE,fontsize=14,fontweight='bold',pad=8)
    plt.tight_layout(); return fig

def fig_zone1():
    fig,ax,p = make_pitch(figsize=(14,8))
    draw_channels(ax)
    for x,y in [(44,22),(44,40),(44,58),(56,12),(56,68),(62,30),(62,50),(70,40),(75,15),(75,65)]:
        opp(ax,x,y)
    for x,y,l in [(5,40,"1"),(18,14,"4"),(18,66,"5"),(28,5,"2"),(28,75,"3"),
                  (36,40,"6"),(58,20,"8"),(58,60,"10"),(80,40,"9"),(70,7,"7"),(70,73,"11")]:
        pl(ax,x,y,l)
    kw=dict(w=2.5,hw=7,hl=6)
    arr(ax,p,5,40,18,14,GOLD,**kw); arr(ax,p,18,14,36,40,GOLD,**kw)
    arr(ax,p,36,40,58,20,ROYAL,**kw)
    arr(ax,p,58,20,70,7,GOLD,w=2.8,hw=8,hl=7)
    arr(ax,p,22,30,18,14,LBLUE,w=1.5,hw=5,hl=4)
    arr(ax,p,22,50,18,66,LBLUE,w=1.5,hw=5,hl=4)
    ax.annotate("① GK = extra outfield player",(3,55),fontsize=10,color=GOLD,fontweight='bold')
    ax.annotate("② CBs split to stretch press",(10,2),fontsize=10,color=WHITE,alpha=0.9,fontweight='bold')
    ax.annotate("③ #6 drops between lines",(34,44),fontsize=10,color=WHITE,alpha=0.9,fontweight='bold')
    ax.annotate("④ Penetrating pass breaks line",(60,9),fontsize=10,color=GOLD,fontweight='bold')
    zlabels(ax)
    ax.set_title("Zone 1 — Build-Up: GK + Split CBs + Dropping #6",color=WHITE,fontsize=13,fontweight='bold',pad=8)
    plt.tight_layout(); return fig

def fig_zone23():
    fig,ax,p = make_pitch(figsize=(14,8))
    draw_channels(ax)
    for x,y in [(55,15),(55,30),(55,50),(55,65),(68,22),(68,40),(68,58),(80,30),(80,50),(85,40)]:
        opp(ax,x,y)
    for x,y,l in [(5,40,"1"),(38,8,"2"),(36,24,"4"),(36,56,"5"),(38,72,"3"),
                  (42,40,"6"),(60,22,"8"),(60,58,"10"),(82,40,"9"),(72,8,"7"),(72,72,"11")]:
        pl(ax,x,y,l)
    ax.scatter(60,22,s=300,c=GOLD,marker='*',zorder=8)
    kw=dict(w=2.5,hw=7,hl=6)
    arr(ax,p,60,22,82,40,ROYAL,**kw)
    arr(ax,p,82,40,75,52,ROYAL,w=2.2,hw=6,hl=5)
    arr(ax,p,60,58,78,50,GOLD,**kw)
    arr(ax,p,60,22,72,72,GOLD,w=2,hw=6,hl=5)
    arr(ax,p,60,22,75,15,ORANGE,w=2,hw=6,hl=5)
    flood(ax,52,18,88,62,ROYAL,alpha=0.06,ls='-')
    ax.annotate("Combine centrally\nto attract pressure",(68,25),fontsize=10,color=ROYAL,fontweight='bold')
    ax.annotate("Third-man combination",(78,53),fontsize=10,color=GOLD,fontweight='bold')
    ax.annotate("Switch when overloaded",(73,74),fontsize=10,color=GOLD,fontweight='bold')
    ax.annotate("Forward run beyond",(78,12),fontsize=10,color=ORANGE,fontweight='bold')
    zlabels(ax)
    ax.set_title("Zone 2 & 3 — Central Combinations + Third-Man + Switch of Play",color=WHITE,fontsize=13,fontweight='bold',pad=8)
    plt.tight_layout(); return fig

def fig_connections_9():
    fig,ax,p = make_pitch(figsize=(14,8))
    draw_channels(ax)
    for x,y in [(78,10),(78,25),(78,40),(78,55),(78,70),(90,30),(90,50)]:
        opp(ax,x,y)
    for x,y,l in [(5,40,"1"),(25,12,"2"),(22,28,"4"),(22,52,"5"),(25,68,"3"),
                  (42,40,"6"),(62,24,"8"),(62,56,"10"),(85,40,"9"),(72,8,"7"),(72,72,"11")]:
        pl(ax,x,y,l)
    kw=dict(w=2.5,hw=7,hl=6)
    arr(ax,p,62,24,85,40,GOLD,w=2.8,hw=8,hl=7)
    arr(ax,p,62,24,80,33,ROYAL,**kw)
    arr(ax,p,72,8,82,28,ORANGE,w=2.2,hw=6,hl=5)
    arr(ax,p,25,12,55,7,LBLUE,w=2,hw=6,hl=5)
    arr(ax,p,62,56,88,52,GOLD,**kw)
    ax.scatter(75,40,s=350,c=GOLD,marker='o',edgecolors='white',lw=2,zorder=8)
    ax.annotate("⚽ BALL",(75,35),fontsize=10,color=GOLD,fontweight='bold',ha='center')
    ax.annotate("① #8 connects underneath #9",(50,30),fontsize=10,color=ROYAL,fontweight='bold')
    ax.annotate("② #7 moves centrally if isolated",(58,18),fontsize=10,color=ORANGE,fontweight='bold')
    ax.annotate("③ #2 provides width as #7 moves in",(5,2),fontsize=10,color=LBLUE,fontweight='bold')
    ax.annotate("④ #10 runs beyond #9",(89,57),fontsize=10,color=GOLD,fontweight='bold')
    zlabels(ax)
    ax.set_title("Connections Around the #9 — Immediate Support Prevents Isolation",color=WHITE,fontsize=13,fontweight='bold',pad=8)
    plt.tight_layout(); return fig

def fig_zone4_women():
    p2 = VerticalPitch(half=True, pitch_type='statsbomb', pitch_color=PITCH_C,
                       line_color='white', linewidth=1.8, goal_type='box')
    fig, ax = p2.draw(figsize=(10,12))
    fig.patch.set_facecolor(BG)
    for x,y in [(112,22),(112,35),(112,48),(112,60),(116,30),(116,45),(108,38),(105,52)]:
        opp(ax,x,y)
    pl(ax,120,68,"7")
    pl(ax,113,55,"9")
    pl(ax,110,40,"10")
    pl(ax,112,22,"11")
    pl(ax,100,40,"8")
    pl(ax,118,60,"2")
    ax.scatter(120,68,s=200,c=GOLD,marker='o',edgecolors='white',lw=1.5,zorder=9)
    flood(ax,113,48,120,65,GOLD,alpha=0.2,lw=1.5,ls='-')
    ax.annotate("CUTBACK\nZONE",(116,56),fontsize=9,color=GOLD,ha='center',fontweight='bold')
    kw=dict(w=2.8,hw=8,hl=7)
    arr(ax,p2,120,68,113,55,GOLD,**kw)
    arr(ax,p2,120,68,112,22,ROYAL,**kw)
    arr(ax,p2,120,68,110,40,ORANGE,w=2.5,hw=7,hl=6)
    arr(ax,p2,120,68,100,40,WHITE,w=2,hw=6,hl=5)
    ax.annotate("① #9 — near post cutback",(85,58),fontsize=10,color=GOLD,fontweight='bold')
    ax.annotate("② #11 — back post far side",(85,20),fontsize=10,color=ROYAL,fontweight='bold')
    ax.annotate("③ #10 — PK spot",(85,42),fontsize=10,color=ORANGE,fontweight='bold')
    ax.annotate("④ #8 — top of the D",(85,35),fontsize=10,color=WHITE,fontweight='bold')
    ax.annotate("MIN. 4 ATTACK THE BOX",(90,75),fontsize=10,ha='center',color=RED,fontweight='bold')
    ax.set_title("Zone 4 — End Line Options · Cutback Zones · Box Occupation",
                 color=WHITE,fontsize=13,fontweight='bold',pad=10)
    plt.tight_layout(); return fig

def fig_wide_play():
    p2 = VerticalPitch(half=True, pitch_type='statsbomb', pitch_color=PITCH_C,
                       line_color='white', linewidth=1.8, goal_type='box')
    fig, ax = p2.draw(figsize=(10,12))
    fig.patch.set_facecolor(BG)
    for y1,y2,clr,alph in [(0,18,RED,0.07),(18,30,GOLD,0.07),(30,50,ROYAL,0.06),(50,62,GOLD,0.07),(62,80,RED,0.07)]:
        rect = mpatches.Rectangle((60,y1),60,y2-y1,facecolor=clr,alpha=alph,edgecolor='none',zorder=1)
        ax.add_patch(rect)
    for x,y in [(116,62),(112,55),(112,40),(112,25),(108,48),(105,35)]:
        opp(ax,x,y)
    pl(ax,120,65,"7")
    flood(ax,114,50,120,68,GOLD,alpha=0.2,lw=2,ls='-')
    ax.annotate("CUTBACK\nZONE",(117,59),fontsize=9,color=GOLD,ha='center',fontweight='bold')
    pl(ax,116,52,"9")
    pl(ax,112,38,"10")
    pl(ax,110,22,"11")
    pl(ax,103,38,"8")
    pl(ax,119,58,"2")
    ax.scatter(120,65,s=220,c=GOLD,marker='o',edgecolors='white',lw=1.5,zorder=9)
    kw=dict(w=2.8,hw=8,hl=7)
    arr(ax,p2,120,65,116,52,GOLD,**kw)
    arr(ax,p2,120,65,112,38,ORANGE,w=2.5,hw=7,hl=6)
    arr(ax,p2,120,65,110,22,ROYAL,**kw)
    arr(ax,p2,120,65,103,38,WHITE,w=2,hw=6,hl=5)
    ax.annotate("① #9 — near post cutback",(85,55),fontsize=10,color=GOLD,fontweight='bold')
    ax.annotate("② #10 — PK spot cutback",(85,40),fontsize=10,color=ORANGE,fontweight='bold')
    ax.annotate("③ #11 — back post far side",(85,23),fontsize=10,color=ROYAL,fontweight='bold')
    ax.annotate("④ #8 — arrives top of the D",(85,35),fontsize=10,color=WHITE,fontweight='bold')
    ax.set_title("Wide Play — Attack End Line · Cutback Options · Box Occupation",
                 color=WHITE,fontsize=13,fontweight='bold',pad=10)
    plt.tight_layout(); return fig

def fig_defensive_block():
    fig,ax,p = make_pitch(figsize=(14,8))
    draw_channels(ax)
    for x,y in [(100,40),(88,18),(88,40),(88,62),(75,10),(75,30),(75,50),(75,70),(62,24),(62,56),(50,40)]:
        opp(ax,x,y)
    flood(ax,34,7,68,73,ROYAL,alpha=0.08,lw=2,ls='--')
    flood(ax,34,25,68,55,ROYAL,alpha=0.12,lw=1,ls='-')
    pl(ax,34,34,"4")
    pl(ax,34,46,"5")
    pl(ax,36,22,"2")
    pl(ax,36,58,"3")
    pl(ax,50,26,"8")
    pl(ax,50,54,"10")
    pl(ax,50,40,"6")
    pl(ax,63,22,"7")
    pl(ax,62,40,"9")
    pl(ax,63,58,"11")
    pl(ax,5,40,"1")
    ax.annotate("← COMPACT BLOCK →",(49,76),fontsize=11,ha='center',color=GOLD,fontweight='bold')
    ax.annotate("PROTECT CENTRAL SPACES FIRST",(35,2),fontsize=10,ha='center',color=ROYAL,alpha=0.9,fontweight='bold')
    ax.annotate("FORCE WIDE →",(82,40),fontsize=10,ha='center',color=RED,alpha=0.9,fontweight='bold',rotation=90)
    ax.annotate("CBs — central channel",(5,34),fontsize=9,color=LBLUE,fontweight='bold')
    ax.annotate("FBs — inside half spaces",(5,22),fontsize=9,color=ROYAL,fontweight='bold')
    ax.annotate("#8/#10 — half space/central edge",(5,54),fontsize=9,color=ROYAL,fontweight='bold')
    ax.set_title("Defensive Organisation — Compact Mid-Block",color=WHITE,fontsize=13,fontweight='bold',pad=8)
    plt.tight_layout(); return fig

def fig_pressing_trap():
    fig,ax,p = make_pitch(figsize=(14,8))
    draw_channels(ax)
    for x,y in [(108,65),(96,18),(96,40),(96,62),(80,10),(80,28),(80,52),(80,70),(68,24),(68,56),(54,40)]:
        opp(ax,x,y)
    ax.scatter(108,65,s=550,c=RED,edgecolors=GOLD,lw=2.5,zorder=4,alpha=0.9)
    flood(ax,80,54,112,80,GOLD,alpha=0.15,lw=2,ls='--')
    ax.annotate("PRESS TRAP ZONE",(96,74),fontsize=10,ha='center',color=GOLD,fontweight='bold')
    flood(ax,62,24,80,56,RED,alpha=0.08,lw=1,ls='-')
    ax.annotate("BLOCK\nCENTRAL",(71,40),fontsize=9,ha='center',color=RED,alpha=0.8,fontweight='bold')
    for x,y,l in [(5,40,"1"),(62,10,"2"),(60,28,"4"),(60,52,"5"),(62,70,"3"),
                  (72,18,"8"),(70,40,"6"),(72,62,"10"),(82,22,"7"),(86,40,"9"),(82,58,"11")]:
        pl(ax,x,y,l)
    kw=dict(w=2.8,hw=8,hl=7)
    arr(ax,p,86,40,100,55,RED,**kw)
    arr(ax,p,82,58,90,62,RED,**kw)
    arr(ax,p,72,62,88,65,ORANGE,w=2,hw=6,hl=5)
    ax.annotate("TRIGGER: Wide pass → Press on ANGLE",(72,84),fontsize=10,ha='center',color=GOLD,fontweight='bold')
    ax.annotate("BACK LINE STAYS HIGH — NO GAPS",(40,84),fontsize=9,ha='center',color=ROYAL,fontweight='bold')
    ax.set_title("High Press — Hybrid Player-Oriented Press · #6 Screens · Back Line Stays Compact",color=WHITE,fontsize=12,fontweight='bold',pad=8)
    plt.tight_layout(); return fig

def fig_att_transition():
    fig,ax,p = make_pitch(figsize=(14,8))
    draw_channels(ax)
    ax.scatter(45,40,s=450,c=GOLD,marker='*',zorder=9)
    ax.annotate("REGAIN",(45,44),fontsize=10,ha='center',color=GOLD,fontweight='bold')
    for x,y in [(48,35),(48,42),(48,48),(52,38),(52,44),(55,30),(55,50),(60,40)]:
        opp(ax,x,y)
    for x,y,l in [(5,40,"1"),(26,14,"2"),(24,30,"4"),(24,50,"5"),(26,66,"3"),
                  (45,40,"6"),(50,22,"8"),(50,58,"10"),(55,10,"7"),(58,40,"9"),(55,70,"11")]:
        pl(ax,x,y,l)
    kw=dict(w=2.8,hw=8,hl=7)
    arr(ax,p,45,40,58,40,GOLD,**kw)
    arr(ax,p,58,40,85,40,GOLD,w=2.5,hw=7,hl=6)
    arr(ax,p,55,10,95,8,ROYAL,**kw)
    arr(ax,p,55,70,95,72,ROYAL,**kw)
    arr(ax,p,50,22,75,28,ORANGE,w=2,hw=6,hl=5)
    arr(ax,p,50,58,75,52,ORANGE,w=2,hw=6,hl=5)
    ax.annotate("① Find #9 immediately",(60,44),fontsize=10,color=GOLD,fontweight='bold')
    ax.annotate("② #7 & #11 run in behind",(70,10),fontsize=10,color=ROYAL,fontweight='bold')
    ax.annotate("③ #8 & #10 support",(62,30),fontsize=10,color=ORANGE,fontweight='bold')
    ax.annotate("DECISION: 1 SECOND",(85,82),fontsize=11,ha='center',color=GOLD,fontweight='bold')
    zlabels(ax)
    ax.set_title("Attacking Transition — Compact to Win It. Direct to Attack It.",
                 color=WHITE,fontsize=13,fontweight='bold',pad=8)
    plt.tight_layout(); return fig

def fig_def_transition():
    fig,ax,p = make_pitch(figsize=(14,8))
    draw_channels(ax)

    # Ball lost just inside opposition half — central area
    ax.scatter(65,40,s=550,c=GOLD,marker='*',zorder=9)
    ax.annotate("BALL\nLOST",(65,33),fontsize=9,ha='center',color=GOLD,fontweight='bold')

   # Opposition 4-4-2 — proper shape
    # Back four
    for x,y in [(55,8),(55,28),(55,52),(55,72)]:
        opp(ax,x,y)
    # Midfield four — two central threatening between our lines
    for x,y in [(65,40),(68,38),(47,33),(47,47)]:
        opp(ax,x,y)
    # Two strikers — threatening between our lines centrally
    for x,y in [(80,33),(80,47)]:
        opp(ax,x,y)

    # NFC players — spread in 4-3-3 attacking shape when ball is lost
    for x,y,l in [(5,40,"1"),(35,10,"2"),(32,26,"4"),(32,54,"5"),(35,70,"3"),
                  (55,22,"8"),(58,40,"6"),(55,58,"10"),(75,8,"7"),(78,40,"9"),(75,72,"11")]:
        pl(ax,x,y,l)

    # #8 and nearest player counter-press immediately (RED arrows toward ball)
    arr(ax,p,55,22,63,37,RED,w=2.8,hw=8,hl=7)
    arr(ax,p,58,40,63,40,RED,w=2.8,hw=8,hl=7)

    # #6 holds centrally — short arrow showing she stays (GOLD)
    arr(ax,p,58,40,55,40,GOLD,w=2,hw=6,hl=5)

    # Fullbacks tuck in toward central block (ROYAL)
    arr(ax,p,35,10,38,22,ROYAL,w=2,hw=6,hl=5)
    arr(ax,p,35,70,38,58,ROYAL,w=2,hw=6,hl=5)

    # CBs hold and tighten (ROYAL)
    arr(ax,p,32,26,35,32,ROYAL,w=2,hw=6,hl=5)
    arr(ax,p,32,54,35,48,ROYAL,w=2,hw=6,hl=5)

    # Wide forwards drop into block (LBLUE)
    arr(ax,p,75,8,62,20,LBLUE,w=2,hw=6,hl=5)
    arr(ax,p,75,72,62,60,LBLUE,w=2,hw=6,hl=5)

    # #9 drops to close space centrally (LBLUE)
    arr(ax,p,78,40,65,40,LBLUE,w=2,hw=6,hl=5)

    # #10 — drops into block (ROYAL)
    arr(ax,p,55,58,55,50,ROYAL,w=2,hw=6,hl=5)

    # Compact block zone shading
    flood(ax,35,18,65,62,ROYAL,alpha=0.08,lw=2,ls='--')

    ax.annotate("① Counter-press immediately",(40,82),fontsize=10,color=RED,fontweight='bold')
    ax.annotate("② #6 holds centrally",(40,76),fontsize=10,color=GOLD,fontweight='bold')
    ax.annotate("③ Team drops into compact block",(40,70),fontsize=10,color=ROYAL,fontweight='bold')

    zlabels(ax)
    ax.set_title("Defensive Transition — Counter-Press or Drop Into Shape. Never Disorganised.",
                 color=WHITE,fontsize=13,fontweight='bold',pad=8)
    plt.tight_layout(); return fig

def fig_corner():
    import matplotlib.patches as mpatches
    from matplotlib.patches import FancyArrow
    import numpy as np

    fig, ax = plt.subplots(figsize=(6, 9))
    fig.patch.set_facecolor(NAVY)

    pitch = VerticalPitch(
        pitch_type="statsbomb",
        pitch_color="#1a5c35",
        line_color=WHITE,
        half=False,
        goal_type="box",
        linewidth=1.5,
    )
    pitch.draw(ax=ax)

    def add_arrow(x1, y1, x2, y2, col=GOLD):
        dx, dy = x2 - x1, y2 - y1
        ax.add_patch(FancyArrow(
            x1, y1, dx, dy,
            width=0.08, head_width=0.7, head_length=0.6,
            fc=col, ec=col, length_includes_head=True, zorder=8
        ))

    # ── Ball + corner taker — LEFT corner ────────────────
    ax.scatter(2, 120, s=90, color=WHITE, zorder=9, marker='o')
    ax.text(4, 117.5, "CK", color=WHITE, fontsize=7.5,
            ha='left', va='top', fontweight='bold')
    pl(ax, 2, 120, "7")

    # ── GK stays at own end ───────────────────────────────
    pl(ax, 40, 10, "1")

    # ── Holding centrally near halfway ────────────────────
    pl(ax, 37, 66, "5")
    pl(ax, 41, 66, "9")
    pl(ax, 55, 64, "3")

    # ── Left side — approaching box ───────────────────────
    pl(ax, 25, 90, "2")     # wide left, makes near-post run
    pl(ax, 35, 97, "10")    # just outside box, left

    # ── Top of D / outside box ───────────────────────────
    pl(ax, 55, 101, "4")    # right of D
    pl(ax, 40, 100, "6")    # top of D — 2nd ball

    # ── In box — far post side (RIGHT in VP) ─────────────
    pl(ax, 62, 110, "8")
    pl(ax, 66, 108, "11")

    # ── Opposition ───────────────────────────────────────
    opp(ax, 40, 120, "")    # GK
    opp(ax, 20, 116, "")    # near post cover
    opp(ax, 32, 113, "")    # central box
    opp(ax, 42, 113, "")    # penalty spot area
    opp(ax, 58, 115, "")    # right box
    opp(ax, 63, 113, "")    # right box far
    opp(ax, 44, 105, "")    # outside box cover
    opp(ax, 38, 99,  "")    # D edge

    # ── Run Arrows ───────────────────────────────────────
    add_arrow(25, 90,  22, 114)    # #2  → near post run
    add_arrow(62, 110, 57, 115)    # #8  → toward goal
    add_arrow(66, 108, 68, 114)    # #11 → back post

    # ── Delivery arc — LEFT corner into near post area ───
    t  = np.linspace(0, 1, 80)
    xs = (1-t)**2 * 2  + 2*(1-t)*t * 12 + t**2 * 30
    ys = (1-t)**2 * 120 + 2*(1-t)*t * 121 + t**2 * 117
    ax.plot(xs, ys, color=WHITE, lw=1.8, ls='--', zorder=5, alpha=0.85)
    add_arrow(xs[-4], ys[-4], xs[-1], ys[-1], col=WHITE)

    # ── Annotations ──────────────────────────────────────
    ax.text(40, 97, "2ND BALL", color=GOLD,
            fontsize=7, ha='center', fontweight='bold', va='top',
            bbox=dict(boxstyle='round,pad=0.2', fc=NAVY, ec=GOLD, alpha=0.7))

    ax.set_title("Attacking Corner — NFC Routine",
                 color=WHITE, fontsize=10, fontweight="bold", pad=8)

    blue_p  = mpatches.Patch(color=ROYAL,     label="NFC")
    red_p   = mpatches.Patch(color="#E53935", label="Opposition")
    gold_p  = mpatches.Patch(color=GOLD,      label="Run")
    white_p = mpatches.Patch(color=WHITE,     label="Delivery")
    ax.legend(handles=[blue_p, red_p, gold_p, white_p],
              loc="lower left", facecolor=NAVY,
              labelcolor=WHITE, fontsize=7, framealpha=0.8)

    fig.tight_layout()
    return fig

def fig_freekick():
    """Attacking free kick diagram — wall, runners, delivery options, shot arc."""
    import matplotlib.patches as mpatches

    fig, ax = plt.subplots(figsize=(6, 9))
    fig.patch.set_facecolor(NAVY)

    pitch = VerticalPitch(
        pitch_type="statsbomb",
        pitch_color="#1a5c35",
        line_color=WHITE,
        half=False,
        goal_type="box",
        linewidth=1.5,
    )
    pitch.draw(ax=ax)
    draw_channels(ax)

    # ── Arrow helper ─────────────────────────────────────
    def run_arrow(x1, y1, x2, y2, rad=0.0, color=GOLD, lw=1.8):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(
                        arrowstyle="-|>",
                        color=color,
                        lw=lw,
                        mutation_scale=14,
                        connectionstyle=f"arc3,rad={rad}",
                    ))

    # ── Ball position — central FK ~23 yards out ─────────
    FK_X, FK_Y = 40, 97
    ax.scatter(FK_X, FK_Y, s=100, color=WHITE, zorder=9, marker='o')
    ax.text(FK_X - 2.5, FK_Y, "FK", color=WHITE,
            fontsize=7.5, ha='right', va='center', fontweight='bold')

    # ── Defensive Wall ───────────────────────────────────
    # 4-player wall, slightly offset from centre (covering near post)
    wall_xs = [33, 36, 39, 42]
    wall_y  = 104
    for wx in wall_xs:
        opp(ax, wx, wall_y, "")
    # Wall bracket label
    ax.annotate("", xy=(42.8, wall_y), xytext=(32.2, wall_y),
                arrowprops=dict(arrowstyle="<->", color="#AAAAAA", lw=1))
    ax.text(37.5, wall_y + 1.8, "Wall", color="#AAAAAA",
            fontsize=6.5, ha='center', va='bottom')

    # ── Extra opposition (covering runners) ──────────────
    opp(ax, 50, 112, "")   # penalty spot zone
    opp(ax, 36, 113, "")   # near post / GK side
    opp(ax, 56, 115, "")   # far post
    opp(ax, 45, 107, "")   # blocking shooting lane
    opp(ax, 42, 118, "")   # GK (between posts)
    opp(ax, 28, 116, "")   # near post cover

    # ── NFC Players over the ball ────────────────────────
    pl(ax, FK_X,     FK_Y, "10")  # shooter / main deliverer
    pl(ax, FK_X + 3, FK_Y, "8")   # dummy runner / second option

    # ── NFC Runners ──────────────────────────────────────
    pl(ax, 30, 109, "9")    # near post run
    pl(ax, 48, 109, "11")   # far post run
    pl(ax, 54, 106, "7")    # back post / wide arrival
    pl(ax, 40, 99,  "6")    # top of D — 2nd ball
    pl(ax, 65, 103, "2")    # wide option / switch
    pl(ax, 18, 106, "3")    # far-side width
    pl(ax, 35, 104, "4")    # defensive cover
    pl(ax, 25, 107, "5")    # defensive cover

    # ── Movement Arrows ──────────────────────────────────
    # #9 — near post curl run
    run_arrow(30, 109, 28, 115, rad=0.2)

    # #11 — penalty spot surge
    run_arrow(48, 109, 46, 115, rad=-0.15)

    # #7 — diagonal far post run
    run_arrow(54, 106, 56, 114, rad=-0.2)

    # #8 dummy run (decoy — dashed feel, lighter)
    run_arrow(FK_X + 3, FK_Y, FK_X + 6, FK_Y + 5,
              rad=0.1, color="#AAAAAA", lw=1.2)

    # ── Delivery Options ─────────────────────────────────
    # Option A — Shot bending around wall (WHITE arc)
    ax.annotate("", xy=(36, 119.5), xytext=(FK_X, FK_Y),
                arrowprops=dict(
                    arrowstyle="-|>",
                    color=WHITE,
                    lw=2.0,
                    mutation_scale=13,
                    connectionstyle="arc3,rad=-0.28",
                ))

    # Option B — Cross/delivery to far post (#7 run, GOLD dashed feel)
    ax.annotate("", xy=(55, 116), xytext=(FK_X, FK_Y),
                arrowprops=dict(
                    arrowstyle="-|>",
                    color=GOLD,
                    lw=1.6,
                    mutation_scale=12,
                    connectionstyle="arc3,rad=0.18",
                ))

    # ── Option Labels ─────────────────────────────────────
    ax.text(26, 110, "A: Bend\naround wall", color=WHITE,
            fontsize=6.5, ha='center', va='center', linespacing=1.3,
            bbox=dict(boxstyle='round,pad=0.25', fc=NAVY, ec=WHITE, alpha=0.75))

    ax.text(62, 108, "B: Cross\nto far post", color=GOLD,
            fontsize=6.5, ha='left', va='center', linespacing=1.3,
            bbox=dict(boxstyle='round,pad=0.25', fc=NAVY, ec=GOLD, alpha=0.75))

    # ── #6 Role Label ─────────────────────────────────────
    ax.text(40, 96, "2ND BALL", color=GOLD,
            fontsize=7, ha='center', fontweight='bold', va='top',
            bbox=dict(boxstyle='round,pad=0.2', fc=NAVY, ec=GOLD, alpha=0.7))

    # ── Quick Restart Nudge ───────────────────────────────
    ax.text(40, 73, "⚡ First look: quick restart",
            color="#AAAAAA", fontsize=7, ha='center', va='center',
            fontstyle='italic',
            bbox=dict(boxstyle='round,pad=0.3', fc=NAVY, ec="#555555", alpha=0.6))

    # ── Title & Legend ────────────────────────────────────
    ax.set_title("Attacking Free Kick — NFC Routine",
                 color=WHITE, fontsize=10, fontweight="bold", pad=8)

    blue_p  = mpatches.Patch(color=ROYAL,     label="NFC")
    red_p   = mpatches.Patch(color="#E53935", label="Opposition / Wall")
    white_p = mpatches.Patch(color=WHITE,     label="Option A — Shot")
    gold_p  = mpatches.Patch(color=GOLD,      label="Option B — Cross / Run")
    ax.legend(handles=[blue_p, red_p, white_p, gold_p],
              loc="lower left", facecolor=NAVY,
              labelcolor=WHITE, fontsize=7, framealpha=0.8)

    fig.tight_layout()
    return fig

def fig_pentagon(position):
    cats  = ["Technical","Tactical","Physical","Mental &\nSocial","NFC Non-\nNegotiables"]
    vals  = PROFILES[position]["scores"]
    N     = 5
    angles= [n/N*2*np.pi for n in range(N)]+[0]
    vplot = vals+vals[:1]
    fig,ax= plt.subplots(figsize=(7,7),subplot_kw=dict(polar=True))
    fig.patch.set_facecolor(BG); ax.set_facecolor('#0a1520')
    ax.set_theta_offset(np.pi/2); ax.set_theta_direction(-1)
    for ring in [1,2,3,4,5]:
        ax.plot(np.linspace(0,2*np.pi,100),[ring]*100,'-',color='#1a2e4a',lw=0.8,zorder=0)
    ax.plot(angles,vplot,'o-',lw=3,color=ROYAL,zorder=5)
    ax.fill(angles,vplot,alpha=0.25,color=ROYAL)
    for angle,val in zip(angles[:-1],vals):
        ax.scatter(angle,val,s=120,color=ROYAL,zorder=6,edgecolors='white',lw=1.5)
        ax.annotate(f"{val:.1f}",(angle,val+0.28),fontsize=9.5,ha='center',color=GOLD,fontweight='bold',zorder=7)
    ax.set_xticks(angles[:-1]); ax.set_xticklabels(cats,size=10,color=WHITE,fontweight='600')
    ax.set_ylim(0,5.5); ax.set_yticks([1,2,3,4,5]); ax.set_yticklabels(['1','2','3','4','5'],size=7.5,color='#555')
    ax.grid(color='#1a2e4a',lw=0.8); ax.spines['polar'].set_color('#1a2e4a')
    ax.set_title(f"Target Profile — {position}",size=13,color=WHITE,fontweight='bold',pad=20)
    plt.tight_layout(); return fig

def fig_5moments():
    fig, ax = plt.subplots(figsize=(12, 8))
    fig.patch.set_facecolor(BG); ax.set_facecolor(BG); ax.axis('off')

    boxes = [
        ("IN\nPOSSESSION",       0.04, 0.58, 0.28, 0.32, ROYAL),
        ("ATTACKING\nTRANSITION",0.68, 0.58, 0.28, 0.32, GOLD),
        ("DEFENSIVE\nTRANSITION",0.04, 0.14, 0.28, 0.32, RED),
        ("OUT OF\nPOSSESSION",   0.68, 0.14, 0.28, 0.32, "#C62828"),
    ]
    for label, x, y, w, h, clr in boxes:
        rect = mpatches.FancyBboxPatch((x,y),w,h,
               boxstyle="round,pad=0.015",
               facecolor=clr,edgecolor='white',linewidth=2,
               zorder=3,transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(x+w/2,y+h/2,label,transform=ax.transAxes,
                fontsize=13,ha='center',va='center',
                color='white',fontweight='bold',zorder=4)

    rect = mpatches.FancyBboxPatch((0.04,0.02),0.92,0.09,
           boxstyle="round,pad=0.015",
           facecolor=NAVY,edgecolor=GOLD,linewidth=2.5,
           zorder=3,transform=ax.transAxes)
    ax.add_patch(rect)
    ax.text(0.50,0.065,"SET PIECES",transform=ax.transAxes,
            fontsize=13,ha='center',va='center',
            color=GOLD,fontweight='bold',zorder=4)

    logo = get_img("nfc.png")
    if logo:
        newax = fig.add_axes([0.42,0.38,0.16,0.22])
        newax.imshow(logo)
        newax.axis('off')

    ax.annotate('',xy=(0.68,0.74),xytext=(0.32,0.74),
                xycoords='axes fraction',
                arrowprops=dict(arrowstyle='->,head_width=0.4,head_length=0.02',
                               color=GOLD,lw=3))
    ax.annotate('',xy=(0.82,0.14+0.32),xytext=(0.82,0.58),
                xycoords='axes fraction',
                arrowprops=dict(arrowstyle='->,head_width=0.4,head_length=0.02',
                               color=RED,lw=3))
    ax.annotate('',xy=(0.32,0.30),xytext=(0.68,0.30),
                xycoords='axes fraction',
                arrowprops=dict(arrowstyle='->,head_width=0.4,head_length=0.02',
                               color=ROYAL,lw=3))
    ax.annotate('',xy=(0.18,0.58),xytext=(0.18,0.46),
                xycoords='axes fraction',
                arrowprops=dict(arrowstyle='->,head_width=0.4,head_length=0.02',
                               color=GOLD,lw=3))

    ax.annotate('',xy=(0.68,0.60),xytext=(0.45,0.50),
                xycoords='axes fraction',
                arrowprops=dict(arrowstyle='->,head_width=0.3,head_length=0.02',
                               color=GRAY,lw=2,alpha=0.6))
    ax.annotate('',xy=(0.32,0.60),xytext=(0.55,0.50),
                xycoords='axes fraction',
                arrowprops=dict(arrowstyle='->,head_width=0.3,head_length=0.02',
                               color=GRAY,lw=2,alpha=0.6))
    ax.annotate('',xy=(0.68,0.40),xytext=(0.45,0.50),
                xycoords='axes fraction',
                arrowprops=dict(arrowstyle='->,head_width=0.3,head_length=0.02',
                               color=GRAY,lw=2,alpha=0.6))
    ax.annotate('',xy=(0.32,0.40),xytext=(0.55,0.50),
                xycoords='axes fraction',
                arrowprops=dict(arrowstyle='->,head_width=0.3,head_length=0.02',
                               color=GRAY,lw=2,alpha=0.6))

    ax.set_xlim(0,1); ax.set_ylim(0,1)
    plt.tight_layout(); return fig

def fig_microcycle_timeline():
    days   = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    icons  = ["⚽","🔄","😴","🔥","🧠","⚽","😴"]
    labels = ["Match","Recovery","Off","Main Training","Tactical Application","Optional Technical","Off"]
    rpe    = [10, 2.5, 0, 8.5, 6.5, 4.5, 0]
    colors = [RED, LBLUE, "#555", RED, GOLD, LBLUE, "#555"]

    fig, ax = plt.subplots(figsize=(14, 5))
    fig.patch.set_facecolor(NAVY); ax.set_facecolor(NAVY)

    x = list(range(7))
    ax.plot(x, rpe, '-', color="#444", lw=2.5, zorder=1)

    for xi, yi, clr in zip(x, rpe, colors):
        size = 260 + yi * 35
        ax.scatter(xi, yi, s=size, color=clr, zorder=5, edgecolors='white', linewidths=2)

    for i, (day, icon, lbl, yi, clr) in enumerate(zip(days, icons, labels, rpe, colors)):
        ax.text(i, yi + 2.0, day, ha='center', color='white', fontsize=13, fontweight='bold')
        ax.text(i, yi + 1.0, icon, ha='center', fontsize=18)
        rpe_txt = f"RPE {yi:g}" if yi > 0 else "OFF"
        ax.text(i, yi - 1.6, rpe_txt, ha='center', color=clr, fontsize=10.5, fontweight='bold')
        ax.text(i, yi - 2.4, lbl, ha='center', color='#bbb', fontsize=8.5)

    ax.set_ylim(-4, 14)
    ax.set_xlim(-0.6, 6.6)
    ax.axis('off')
    plt.tight_layout()
    return fig
