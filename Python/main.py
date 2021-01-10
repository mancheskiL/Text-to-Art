import pygame
import json
import random
from tqdm import tqdm

random.seed(1)

# TODO: initialize by loading desired files
print('Importing word map')
word_map = ''
with open('../source/words_dictionary.json') as f:
    word_map = json.load(f)

print('Initializing word map')
for key, value in word_map.items():
    word_map[key] = None

print('Importing source text')
with open('../source/text.txt') as f:
    text_file = f.read()


# set each word to a unique hexadecimal value
print('Setting hex values')
used_hexes = []

for key, value in tqdm(word_map.items()):
    make_hex = True
    while make_hex:
        random_num = random.randint(0, 16777215)
        hex_number = str(hex(random_num))
        hex_number = '#' + hex_number[2:]
        if(hex_number not in used_hexes):
            word_map[key] = hex_number
            used_hexes.append(hex_number)
            make_hex = False

# remove any numeric values from text (i.e. 1, 12, etc)
print('Cleaning text of numbers')
text_list = text_file.split()
no_num_text = []
for i, item in enumerate(text_list):
    try:
        int(item)
    except:
        no_num_text.append(item)

# remove any symbols from text (i.e. $, %, &, etc)
print('Cleaning text of special symbols')
symbols = ['.', ',', '$', '%', '&', ':', ';', '(', ')', '!', '/']
cleaned_text_list = []
for item in no_num_text:
    if ('.' or ',' or '$' or '%' or '&' or ':' or ';' or '(' or ')' or '!' or '/') not in item: 
        cleaned_text_list.append(item)

# make all words lowercase
lowercase_list = []
for item in cleaned_text_list:
    lowercase_list.append(item.lower())


# Initialize game
pygame.init()

# Set display size in pixels
screen = pygame.display.set_mode([500, 500])

# Activate Run Loop
running = True

square_width = 10
square_height = 10

while running:
    sq_Rect = pygame.Rect((0, 0), (10, 10))

    # TODO: build screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    for item in lowercase_list:
        color_code = word_map.get(item, '#ffffff')
        color = pygame.Color(color_code)
        # square = pygame.draw.rect(screen, (255, 100, 50), sq_Rect)
        square = pygame.draw.rect(screen, color, sq_Rect)
        sq_Rect = sq_Rect.move(square_width, 0)

    pygame.display.flip()
pygame.quit()