import sqlite3
import google.generativeai as genai

# Configure the Gemini AI model
genai.configure(api_key="gemini-api-key")
model = genai.GenerativeModel("gemini-1.5-flash")

hydration_goal = 2000  # Default goal in ml

def log_hydration(intake):
    conn = sqlite3.connect("wellness.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO hydration (date, intake) VALUES (CURRENT_DATE, ?)", (intake,))
    conn.commit()
    conn.close()

def log_activity(activity_type, duration, calories):
    conn = sqlite3.connect("wellness.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO activity (date, activity_type, duration, calories) VALUES (CURRENT_DATE, ?, ?, ?)", 
                   (activity_type, duration, calories))
    conn.commit()
    conn.close()

def log_mood(mood, stress, energy):
    conn = sqlite3.connect("wellness.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO mood (date, mood, stress, energy) VALUES (CURRENT_DATE, ?, ?, ?)", 
                   (mood, stress, energy))
    conn.commit()
    conn.close()

# AI Tip Generation Functions
def get_hydration_tip(intake):
    if intake < hydration_goal:
        prompt = f"""
        You are a virtual wellness coach. The user has logged {intake} ml of water intake today, which is below the recommended daily fluid intake of {hydration_goal} ml. Provide a motivational tip emphasizing the importance of staying hydrated for physical performance, mental clarity, and energy levels. Suggest simple ways to increase hydration. Keep it under 200 words and highlight key points using **bold** text.
        """
    else:
        prompt = f"""
        You are a virtual wellness coach. The user has logged {intake} ml of water intake today, meeting or exceeding the recommended daily intake of {hydration_goal} ml. Provide a positive reinforcement tip, mentioning the benefits of adequate hydration and encouraging the user to maintain their good habit. Use bold text for key points and keep it under 200 words.
        """
    response = model.generate_content(prompt)
    return response.text.strip()

def get_activity_tip(activity_type, duration):
    prompt = f"""
    You are a fitness coach helping users improve their physical well-being through personalized guidance. The user has logged a physical activity in their real-time wellness tracker:
    
    **Activity type:** {activity_type}
    **Duration:** {duration} minutes
    
    Provide a detailed, personalized tip explaining how this activity benefits cardiovascular health, muscle strength, or mental well-being. Include suggestions on how to enhance their fitness routine or maintain consistency in their exercise habits. Use bold text for key points, and avoid bullet points or lists.
    """
    response = model.generate_content(prompt)
    return response.text.strip()

def get_mood_tip(mood, stress, energy):
    prompt = f"""
    You are a mental wellness coach offering personalized advice based on real-time inputs. The user has recorded their mental well-being using the app:
    
    **Mood:** {mood}/10  
    **Stress:** {stress}/10  
    **Energy:** {energy}/10  
    
    Provide an encouraging tip focused on improving mental well-being. Suggest ways to manage stress, elevate mood, and boost energy levels, such as mindfulness practices, light physical activities, or relaxation techniques. Make the tone supportive and motivating, keeping the response under 150 words. Use bold text for key points, and avoid bullet points or lists.
    """
    response = model.generate_content(prompt)
    return response.text.strip()

