from PIL import Image, ImageDraw
import monocular
import json
import imghdr

monocular.initialize({
    'client_id':'94254abb64b66d55bf51745c78db1f41',
    'client_secret':'0028439b9feab3196745c23ddd69f54a5dcfd68a'
})

invalid = True
while invalid:
    try:
        # Get the path from user input
        path = raw_input('Enter image path:')
        # Validate Image
        if imghdr.what(path) in valid_types:
            invalid = False
        else:
            print('Image must be png, jpg or bmp format')
    except IOError:
        print('File does not exist.')

response = monocular.face_detection({'landmarks':True, 'image':path})

img = Image.open(path)
draw = ImageDraw.Draw(img)

for box in response:
    draw.rectangle([(box['left'], box['top']), (box['right'], box['bottom'])], outline='#00ff00');

    i = 0;
    for landmark in box['landmarks']:
        # Draw large point
        draw.point([landmark[0]+1, landmark[1]], fill='#00ffff')
        draw.point([landmark[0]-1, landmark[1]], fill='#00ffff')
        draw.point([landmark[0], landmark[1]+1], fill='#00ffff')
        draw.point([landmark[0], landmark[1]-1], fill='#00ffff')
        draw.point([landmark[0], landmark[1]], fill='#00ff00')
        i = i + 1