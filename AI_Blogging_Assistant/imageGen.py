from huggingface_hub import InferenceClient
from apikey import huging_face_token

client = InferenceClient("black-forest-labs/FLUX.1-dev", token=huging_face_token)

# output is a PIL.Image object
image = client.text_to_image("Astronaut riding a horse")