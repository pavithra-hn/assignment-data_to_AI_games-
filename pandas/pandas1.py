# print("hello world")
import pandas as pd
db = {
    "player" : ["sonu" ,"pinky" ,"neha"],
    "games" :["ludo" ,"temple run " ,"8 ball pool"],
    "score": [85,90,75]
}

df = pd.DataFrame.from_dict(db)
print("game player names")
print(df)

average_score = df["score"].mean()
print(average_score)


# output :
#  game player names
#   player        games  score
# 0   sonu         ludo     85
# 1  pinky  temple run      90
# 2   neha  8 ball pool     75
# 83.33333333333333