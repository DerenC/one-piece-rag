import pandas as pd
import os

FILTERED_CHARACTERS = ("USE FOR TWO QCERS",
    "Man ",
    "Woman",
    "Voice ",
    "Some ",
    # "Narrator",
)

def delete_all_dialogue_file():
    folder = 'data/dialogue'

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path) # Deletes the file
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

def create_dialogue_file(episode, text_arr):
    if len(text_arr) == 0: return
    with open(f"data/dialogue/{episode}.txt", "w") as file:
        file.write("\n".join(text_arr) + "\n")


## START OF SCRIPT

delete_all_dialogue_file()

df = pd.read_csv("hf://datasets/mramazan/One-Piece-Transcripts-with-Character-Names-382-777/onepiece.csv")

df = df[["episode", "character", "text"]]

curr_episode = -1
curr_character = ""
curr_dialogue = []
curr_dialogue_arr = []

for row in df.itertuples():
    if any([row.character.startswith(ch) for ch in FILTERED_CHARACTERS]): # type: ignore
        continue

    # 1st iteration. Initialise
    if curr_episode == -1:
        curr_episode = row.episode
        curr_character = row.character
        curr_dialogue = [row.text]
        continue

    # Different episode
    if row.episode != curr_episode:
        create_dialogue_file(curr_episode, curr_dialogue_arr)
        curr_episode = row.episode
        curr_character = row.character
        curr_dialogue = [row.text]
        curr_dialogue_arr = []
    # Different character
    elif row.character != curr_character:
        dialogue_as_str = f"{curr_character}: {' '.join(curr_dialogue)}" # type: ignore
        curr_dialogue_arr.append(dialogue_as_str)

        curr_character = row.character
        curr_dialogue = [row.text]
    # Same episode; Same character
    else:
        curr_dialogue.append(row.text)

dialogue_as_str = f"{curr_character}: {' '.join(curr_dialogue)}" # type: ignore
curr_dialogue_arr.append(dialogue_as_str)
create_dialogue_file(curr_episode, curr_dialogue_arr)
