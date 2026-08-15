# DayTrip Planner — Installation Guide

## Prerequisites

- Python 3.14.6
- Google Agent Development Kit (ADK) 2.7.0
- Google Gemini API access

## Installation

Install Google ADK:

```bash
pip3 install google-adk

python3 -c "from google import genai; print('SDK OK')"


Configuration

Configure the required Gemini API credentials according to the Google ADK environment setup.

Run the Agent

Start the DayTrip Planner using the Google ADK runtime.

Testing

Run:
python3 test_agent.py
