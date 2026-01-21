AI = [
    { "name":"chatgpt","type_of_AI":"generative AI", "use_case":"text generation"},
    { "name":"Gemini","type_of_AI":"Image generation", "use_case":"image and video generation"},
    { "name":"claude","type_of_AI":"coding platform", "use_case":"code generation"},
    { "name":"Alexa","type_of_AI":"conversational AI", "use_case":"voice assistant"}
]
for llms in AI :
    print(llms["name"],llms["type_of_AI"],llms["use_case"],sep=", ")


# output:
# data_to_AI_games, Datatoaigamersrani
# Subway Surfers, SYBO Games
# Angry Birds, Rovio Entertainment