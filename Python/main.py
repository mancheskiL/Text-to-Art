import pygame
import json
import random
from tqdm import tqdm
import math

def makePerfectSquareList(text_list):
    value = None
    output_list = text_list
    sr = math.sqrt(len(text_list))

    if (sr - math.floor(sr)) != 0:
        # add 1 to whatever number is left of decimal after sqrt function
        # gives the next possible perfect square value
        value = math.floor(sr) + 1

        # add placeholders to list to make perfect square
        perfect_square = value * value
        for _ in range(perfect_square - len(text_list)):
            output_list.append('luman')
    else:
        value = sr
        output_list = text_list
    
    return [value, output_list]

random.seed(1)

# TODO: initialize by loading desired files
print('Importing word map')
with open('../source/words_dictionary.json', 'r') as f:
     word_map = json.load(f)

print('Reading previous word map length')
with open('../source/map_length.txt', 'r') as f:
     previous_word_map_len = f.read()

if len(word_map) > int(previous_word_map_len):
    print('Initializing word map')
    for key, value in word_map.items():
        word_map[key] = None
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
        
    print('Updating length records')
    with open('../source/map_length.txt', 'w') as f:
        f.write(str(len(word_map)))

print('Importing source text')
with open('../source/text.txt') as f:
    text_file = f.read()
# remove any numeric values from text (i.e. 1, 12, etc)
print('Cleaning text of numbers')
text_list = text_file.split()
no_num_text = []
for item in text_list:
    try:
        int(item)
    except:
        no_num_text.append(item)

# remove any symbols from text (i.e. $, %, &, etc)
print('Cleaning text of special symbols')
# symbols = ['.', ',', '$', '%', '&', ':', ';', '(', ')', '!', '/']
cleaned_text_list = []
for item in no_num_text:
    if ('.' or ',' or '$' or '%' or '&' or ':' or ';' or '(' or ')' or '!' or '/') not in item: 
        cleaned_text_list.append(item)

# make all words lowercase
lowercase_list = []
for item in cleaned_text_list:
    lowercase_list.append(item.lower())


# calculate nearest perfect square, add placeholder to fill
root, final_list = makePerfectSquareList(lowercase_list)

# create our square grid based on the given root value
grid = []
for _ in range(root):
    grid.append([])

for cell in grid:
    for _ in range(root):
        cell.append([])

# Initialize game
pygame.init()

# Set display size in pixels
screen = pygame.display.set_mode([500, 500])

# Activate Run Loop
running = True

square_width = 10
square_height = 10

# while running:
#     sq_Rect = pygame.Rect((0, 0), (10, 10))

#     # TODO: build screen
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill((255, 255, 255))

#     for item in final_list:
#         color_code = word_map.setdefault(item, '#000000')
#         color = pygame.Color(color_code)
#         square = pygame.draw.rect(screen, color, sq_Rect)
#         sq_Rect = sq_Rect.move(square_width, 0)

#     pygame.display.flip()
# pygame.quit()

while running:
    sq_Rect = pygame.Rect((0, 0), (10, 10))
    word_index = 0

    # TODO: build screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    for i in range(root):
        # y_rect = sq_Rect.move(0, i*10)
        y_cord = i*10
        for j in range(root):
            # x_rect = sq_Rect.move(j*10, 0)
            x_cord = j*10
            color_code = word_map.setdefault(final_list[word_index], '#000000')
            color = pygame.Color(color_code)
            square = pygame.draw.rect(screen, color, pygame.Rect((x_cord, y_cord), (10, 10)))

            word_index += 1

    pygame.display.flip()
pygame.quit()

# Save word_map to file for cache use later
print('Artwork closing, updated word map')
with open('../source/words_dictionary.json', 'w') as f:
    json.dump(word_map, f)