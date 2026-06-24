import gradio as gr
import json

with open("outputs/persona.json") as f:
    persona = json.load(f)

def chatbot(query):
    q = query.lower()

    if "habit" in q:
        return "\n".join(persona["habits"][:5])

    elif "personality" in q or "trait" in q:
        return "\n".join(persona["personality_traits"][:5])

    elif "communicate" in q or "talk" in q:
        return "\n".join(persona["communication_style"])

    elif "fact" in q:
        return "\n".join(persona["personal_facts"][:5])

    return "Information unavailable."

demo = gr.Interface(
    fn=chatbot,
    inputs="text",
    outputs="text",
    title="Adaptive Persona Chatbot"
)

demo.launch()