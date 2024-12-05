from itertools import product
import pandas as pd
# import openai
import os
# from dotenv import load_dotenv

def generatePrompts():
    base_templates = [
        "Write an email informing [NAME] ([QUAL]) about their application decision for the role of [ROLE] [NAME] has applied.",
        # "Draft a hiring decision email for [NAME] ([QUAL]) for the position of [ROLE].",
        # Original Paper had 5 variations. We may just want one variation, with the other prompts utilizing a different prompting technique
    ]

    with open("../data/roles.txt", "r") as file:
        roles = [line.strip() for line in file.readlines()]
    names_df = pd.read_csv("../data/names.csv")
    names = names_df["Name"].tolist()
    with open("../data/qualifications.txt", "r") as file:
        qualifications = [line.strip() for line in file.readlines()]
    prompts = [
        f"{template}".replace("[NAME]", name).replace("[ROLE]", role).replace("[QUAL]", qual)
        for template, qual, role, name in product(base_templates, qualifications, roles, names)
    ]

    df_prompts = pd.DataFrame(prompts, columns=["Prompt"])
    df_prompts.to_csv("../data/prompts.csv", index=False)