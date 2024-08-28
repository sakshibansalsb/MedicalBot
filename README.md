# HealthCheck Medical Bot

HealthCheck Medical Bot is an interactive chatbot designed to help users understand potential causes of their symptoms. It uses Google’s Gemini API integrated with Gradio for the chat interface.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Architecture](#architecture)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Contributing](#contributing)

## Project Overview

HealthCheck Medical Bot is built using a Large Language Model (LLM) integrated with Gradio for the chat interface. It assists users in identifying potential causes of their symptoms and encourages them to consult healthcare professionals for accurate diagnosis and treatment.

## Key Features

- Greet users and provide an introduction.
- Collect detailed descriptions of symptoms.
- Suggest potential causes based on the symptoms described.
- Provide a user-friendly chat interface with a background image.

## Architecture
![diagram-export-8-27-2024-1_56_55-PM]()

<div align="center">
  <img src="https://github.com/user-attachments/assets/b7f229c5-56d5-4ac2-ad13-25f800dc48ee" alt="ArchitectureDiagram" width="400" height="700">
</div>


The system is composed of the following components:

- **Chatbot Interface (Gradio)**: Provides the user interface for interacting with the chatbot.
- **Backend Processor**: Manages conversation context and prepares data for the LLM.
- **API Gateway**: Handles API requests and responses between the backend and the LLM.
- **Large Language Model (LLM)**: Processes user inputs and generates appropriate responses.

### Data Flow

1. **User Input → Chatbot Interface**: Users enter their messages describing symptoms.
2. **Chatbot Interface → Backend Processor**: Sends user input for context management.
3. **Backend Processor → API Gateway**: Prepares and forwards the request to the LLM.
4. **API Gateway → LLM**: LLM processes the request and generates a response.
5. **LLM → API Gateway**: Returns the response to the API Gateway.
6. **API Gateway → Backend Processor**: Forwards the LLM's response.
7. **Backend Processor → Chatbot Interface**: Sends the response to be displayed.
8. **Chatbot Interface → User**: Displays the response to the user.

## Setup Instructions

To set up and run HealthCheck Medical Bot locally, follow these instructions:

### Prerequisites

- Python 3.7 or later
- Pip (Python package installer)

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/healthcheck-medical-bot.git
    cd healthcheck-medical-bot
    ```

2. **Create and Activate a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**

    Create a `.env` file in the root directory with the following content:

    ```env
    API_KEY=your_actual_api_key_here
    ```

5. **Run the Application**

    ```bash
    python app.py
    ```

## Usage

- **Start the Chat**: Initiate interaction with the bot, which will greet you and ask about your symptoms.
- **Describe Symptoms**: Provide details about your symptoms, including their duration and severity.
- **Receive Information**: The bot will analyze your input and suggest potential causes.
- **Consult Professionals**: Always consult a healthcare professional for a precise diagnosis and treatment.

## Contributing

Contributions to HealthCheck Medical Bot are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push the branch to your fork (`git push origin feature-branch`).
5. Create a Pull Request from your fork to the main repository.
