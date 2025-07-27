#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from news_scrapper.crew import NewsScrapper

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs',
        'date': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    }

    inputs_array = [
        {
        'topic': 'AI agents',
        'date': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        },

        {
        'topic': 'Open AI',
        'date': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        },

        {
        'topic': 'husgging face',
        'date': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        },
    ]
    
    try:
        NewsScrapper().crew().kickoff_for_each(inputs=inputs_array)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

