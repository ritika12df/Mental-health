## AI-Powered Real-Time Health & Wellness Monitor

This project is a real-time health & wellness tracker built using Python, Taipy GUI, and Gemini AI for generating personalized tips. The application allows users to log hydration intake, physical activities, and mood metrics, providing AI-driven tips and daily summaries.

## Features

# Hydration Tracker

- Log water intake in milliliters.

- View progress towards a hydration goal.

- Receive AI-generated hydration tips based on intake.

# Physical Activity Logger

- Log activity type and duration.

- Automatically estimate calories burned using Gemini AI.

- Receive personalized activity tips.

# Mental Well-Being Check-In

- Record mood, stress, and energy levels (1-10 scale).

- Receive supportive tips for improving mental well-being.

# Daily Summary

- Display a summary of hydration, calories burned, and mood status.

## How It Works

# AI Tip Generation

The app uses Gemini AI to generate personalized tips for hydration, activity, and mood, ensuring relevant and supportive feedback for the user.

# Data Storage

Logged data is stored in a local SQLite database (wellness.db) with tables for hydration, activity, and mood.

## Dependencies
Python 3.8+

Taipy GUI (taipy-gui)

Google Generative AI (google-generativeai)

SQLite3

## Setup Instructions

# Clone the Repository

bash
Copy code
git clone <repository_url>
cd <repository_folder>
Install Dependencies

bash
Copy code
pip install taipy-gui google-generativeai
Set Up Database
Create the wellness.db database with the following schema:

sql
Copy code
CREATE TABLE hydration (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    intake INTEGER
);

CREATE TABLE activity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    activity_type TEXT,
    duration INTEGER,
    calories INTEGER
);

CREATE TABLE mood (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    mood INTEGER,
    stress INTEGER,
    energy INTEGER
);
Run the Application

bash
Copy code
python main.py
Usage
Enter hydration, activity, or mood data in the respective fields.
Click the "Log" button to save data and view AI-generated tips.
Review the daily summary at the bottom of the interface.
Customization
Modify hydration goals or AI prompts by editing the variables and prompt templates in main.py.
Update the UI by changing the HTML and CSS in the layout variable.
License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it.

