# Inference
# this is the inference code that you can use after you have trained your model
# Unhide code below and change prj_path to your repo or local path (e.g. my_dreambooth_project)



from diffusers import DiffusionPipeline, StableDiffusionXLImg2ImgPipeline
import torch

prj_path = "username/repo_name"
prj_path = "C:/Users/sanju/Desktop/projects/explore/Dreambooth/sanjay-dreambooth-project/sanjay-dreambooth-project"
model = "stabilityai/stable-diffusion-xl-base-1.0"
pipe = DiffusionPipeline.from_pretrained(
    model,
)
pipe.to("cpu")
pipe.load_lora_weights(prj_path, weight_name="pytorch_lora_weights.safetensors")

refiner = StableDiffusionXLImg2ImgPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-refiner-1.0",
)
refiner.to("cpu")

prompt = "Executive photo of Sanjay (male) for linkedln profile"

seed = 42
generator = torch.Generator("cpu").manual_seed(seed)
image = pipe(prompt=prompt, generator=generator).images[0]
image = refiner(prompt=prompt, generator=generator, image=image).images[0]
image.save(f"generated_image.png")