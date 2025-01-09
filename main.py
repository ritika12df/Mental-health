from taipy.gui import Gui
from backend import log_hydration, log_activity, log_mood, get_hydration_tip, get_activity_tip, get_mood_tip
import google.generativeai as genai

# Configure Gemini AI model
genai.configure(api_key="gemini-api-key")
model = genai.GenerativeModel("gemini-1.5-flash")

# Variables to hold user input and tips
hydration_intake = 0
hydration_goal = 2000  # Default goal in ml
hydration_progress = "0%"
activity_type = ""
activity_duration = 0
calories_burned = 0
mood = 0
stress = 0
energy = 0
hydration_tip = ""
activity_tip = ""
mood_tip = ""
daily_summary = ""

# Function to estimate calories burned using Gemini AI
def estimate_calories(activity, duration):
    prompt = f"""
    You are a fitness coach. Estimate the number of calories burned for the following activity:
    - Activity: {activity}
    - Duration: {duration} minutes
    Provide only the number of calories as output.
    """
    response = model.generate_content(prompt)
    return int(response.text.strip())

def update_hydration_progress(state):
    progress_percentage = (state.hydration_intake / state.hydration_goal) * 100
    state.hydration_progress = f"{progress_percentage:.1f}%"

# Functions to handle button clicks
def on_log_hydration(state):
    try:
        state.hydration_intake = int(state.hydration_intake)  # Ensure it's an integer
        log_hydration(state.hydration_intake)
        state.hydration_tip = get_hydration_tip(state.hydration_intake)  # Update tip
        update_hydration_progress(state)  # Update progress bar
        update_summary(state)  # Update summary after logging hydration
    except ValueError:
        state.hydration_tip = "Please enter a valid number for hydration intake."

def on_log_activity(state):
    state.calories_burned = estimate_calories(state.activity_type, state.activity_duration)
    log_activity(state.activity_type, state.activity_duration, state.calories_burned)
    state.activity_tip = get_activity_tip(state.activity_type, state.activity_duration)  # Update tip
    update_summary(state)  # Update summary after logging activity

def on_log_mood(state):
    log_mood(state.mood, state.stress, state.energy)
    state.mood_tip = get_mood_tip(state.mood, state.stress, state.energy)  # Update tip
    update_summary(state)  # Update summary after logging activity

def update_summary(state):
    state.daily_summary = f"""
     Daily Summary:  
    - Hydration: {state.hydration_intake} ml  
    - Total Calories Burned: {state.calories_burned} cal  
    - Mood Score: {state.mood}/10, Stress: {state.stress}/10, Energy: {state.energy}/10
    """    

layout = """
<style>
.taipy-button.my-style {
    border-radius: 10px;
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    font-size: 16px;
    border: none;
    cursor: pointer;
    margin-left: 10px;
}

.taipy-button.my-style:hover {
    background-color: #45a049;
    }

 /* Add spacing between form inputs */
.form-input {
    margin-bottom: 10px;
    margin-right: 20px;  
    margin-top: 10px; 
}
/* Styling for Mood, Stress, and Energy headings */
.mood-heading {
    color: #4CAF50;  /* Green for mood */
    font-weight: bold;
}

.stress-heading {
    color: #FF6347;  /* Red for stress */
    font-weight: bold;
}

.energy-heading {
    color: #FFA500;  /* Orange for energy */
    font-weight: bold;
}
</style>

# AI-powered Real-Time Health & Wellness Monitor {: .h2}

## Hydration Tracker {: .h4}
<|{hydration_intake}|input|> ml <|Log|button|on_action=on_log_hydration|class_name=my-style|>
<|{hydration_progress}|text|class=progress-box|label=Hydration Progress|>
<|{hydration_tip}|text|mode=markdown|class=tip-box|label=Hydration Tip|>

## Physical Activity Logger {: .h4}
Activity Type: <|{activity_type}|input|class_name=form-input|>
Duration (mins): <|{activity_duration}|input|class_name=form-input|>
Calories Burned: <|{calories_burned}|text|>
<|Log Activity|button|on_action=on_log_activity|class_name=my-style|>
<|{activity_tip}|text|mode=markdown|class=tip-box|label=Activity Tip|>

## Mental Well-Being Check-In {: .h4}
<|Mood (1-10):|text|class_name=mood-heading|> <|{mood}|input|class_name=form-input|>  
<|Stress (1-10):|text|class_name=stress-heading|> <|{stress}|input|class_name=form-input|>  
<|Energy (1-10):|text|class_name=energy-heading|> <|{energy}|input|class_name=form-input|>  
<|Log Mood|button|on_action=on_log_mood|class_name=my-style|>  
<|{mood_tip}|text|mode=markdown|class=tip-box|label=Mood Tip|>

## Daily Summary {: .h4}
<|{daily_summary}|text|mode=markdown|class=summary-box|>
"""
Gui(page=layout, css_file="style.css").run()

