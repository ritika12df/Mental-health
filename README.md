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

## Required Dependencies
Python 3.8+

Taipy GUI (taipy-gui)

Google Generative AI (google-generativeai)

SQLite3

# Note
You should have your Gemini Api key ready to use this application which you have to put in main.py and backend.py file

## Setup Instructions

# Clone the Repository
First, clone the repository from GitHub:
```bash
https://github.com/ritika12df/Mental-health
```
## Install Dependencies
```bash
pip install taipy google-generativeai
```
## Start the application:
```bash
taipy run main.py
```
### View the Application
Once both the frontend and backend are running, you can view the AI-powered Real-Time Health & Wellness Monitor in your browser by navigating to http://localhost:5000.

### twitter Handles
  
 - @Sdfg44257235
