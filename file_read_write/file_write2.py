ai_tools = ["ChatGPT", "AlphaGo", "Alexa", "Tesla Autopilot"]

with open("ai_tools.txt", "w") as file:
    for tool in ai_tools:
        file.write(tool + "\n")
print("AI tools written to ai_tools.txt")