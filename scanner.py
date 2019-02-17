import os
import google
import io
import re

credential_path = "/Users/sanja/Desktop/hacknyu2019.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    #print(texts)

    str= ""
    coords = []
    for text in texts:
        str += text.description
        #print('\n"{}"'.format(text.description))
        print(text.description)
        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        #print('bounds: {}'.format(','.join(vertices)))
        try:
            if text.description.index('.') != -1:
                float(text.description)
                coords.append((text.bounding_poly.vertices[0].x,
                text.bounding_poly.vertices[0].y,
                text.bounding_poly.vertices[2].x,
                text.bounding_poly.vertices[2].y))
        except:
            pass
            #print('In except')

    floatNum = "([0-9]+\.[0-9]+[0-9])"
    prices = re.findall(floatNum, str)
    a = len(prices)
    prices = prices[:(a//2)]
    #print(prices)
    #print(coords)
