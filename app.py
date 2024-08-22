import google.generativeai as genai
import gradio as gr


api_key = "AIzaSyBizxFLIQSrfhGMOoRb-0N2iA0lVOV-NUU"
genai.configure(api_key=api_key)

# Define the generative model instance
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize the conversation history (empty list)
chat = model.start_chat(history=[])

# Define function, which helps to execute any prompt
def get_llm_response(message):
    response = chat.send_message(message)
    return response.text

# Define the basic information about the medical bot
base_info = """
Welcome to HealthCheck Bot. I'm here to help you understand what might be causing your symptoms. 
You can describe what you're experiencing, and I'll provide some potential causes or diseases that might match your description.
Remember, this is just a guide—please consult a healthcare professional for accurate diagnosis and treatment.
"""

# Define a starting prompt for the medical bot
starting_prompt = """
Let's get started by understanding your symptoms. 
Please describe how you're feeling, including any specific symptoms, duration, and severity. 
For example, you might say "I have a sore throat, a mild fever, and have been feeling fatigued for the past 3 days."
"""

# Define function to create the initial welcome message
def create_welcome_message():
    """
    Generates the initial welcome message with instructions for users.

    Returns:
        str: The welcome message string.
    """
    return f"""
    {base_info}
    {starting_prompt}
    """

# Define greeting message
greeting_message = "Hello! Welcome to HealthCheck Bot. \n 🤖 I'm here to help you figure out what might be causing your symptoms. \n How can I assist you today?"

# Define communication function
def bot(message, history):
    # If this is the first interaction, send the greeting message
    if not history:
        response = greeting_message
    else:
        # Otherwise, use the conversation history and symptoms provided
        prompt = create_welcome_message() + f"\nUser: {message}"
        response = get_llm_response(prompt)
    
    # Update history with the user message and the response
    if not history:
        history.append([greeting_message, "bot"])  # Add greeting to history
    history.append([message, "user"])
    history.append([response, "bot"])
    
    return response

# Create Gradio instance
demo = gr.ChatInterface(
    fn=bot, 
    examples=[
        "I have a sore throat and a mild fever.",
        "I've been feeling nauseous and have a headache.",
        "I have a cough and shortness of breath.",
        "I'm experiencing fatigue and muscle aches."
    ], 
    title="HealthCheck Medical Bot"
)

# Launch Gradio chatbot
demo.launch(debug=True, share=True)
