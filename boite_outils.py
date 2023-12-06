import torch

def get_model(model_path):
    model = torch.load(model_path)

    return model

def get_genre_musical():
    return "Blues"
