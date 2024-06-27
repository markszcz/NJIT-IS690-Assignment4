from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
from datasets import load_dataset

load_dotenv(find_dotenv())

def img2text(url):
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

    text = image_to_text(
            url,  max_new_tokens=20)[0]['generated_text']
    return text


def getPlantCareInstructions(my_plant):
    ds = load_dataset("jibrand/Plant-dataset", split="train")
    my_plant_index = ds['Plant'].index(my_plant)
    return ds[my_plant_index]

print("Identifying the image: ")
print(img2text("rose.png"))
print()

print("Getting plant care information: ")
print(getPlantCareInstructions("Rose"))
