import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

supported_brands = ['aldo', 'rakuten', 'bestbuy', 'lyft', 'uber', 'domino', 'newegg', 'expedia', 'booking.com',
                    'hotwire', 'nike', 'moviepass', 'cinemark', 'sinemia']


def detect_brand(image_uri):
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = image_uri

    response = client.label_detection(image=image)
    labels = response.label_annotations
    for label in labels:
        for word in label.description.split(' '):
            if word in supported_brands:
                return word

    # default to Nike
    return 'Nike'
