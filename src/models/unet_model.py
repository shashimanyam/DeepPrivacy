from src.models.discriminator import Discriminator, DeepDiscriminator
from src.models.generator import Generator
from src.utils import wrap_models


def init_model(pose_size, start_channel_dim, image_channels, discriminator_model):
    if discriminator_model == "deep":
        d = DeepDiscriminator
    else:
        assert discriminator_model == "normal"
        d = Discriminator

    discriminator = d(image_channels,
                      start_channel_dim,
                      pose_size)
    generator = Generator(pose_size, start_channel_dim, image_channels)
    discriminator, generator = wrap_models([discriminator, generator])
    return discriminator, generator
