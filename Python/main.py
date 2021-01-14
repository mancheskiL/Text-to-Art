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

print('Importing source text')
with open('../source/text.txt', 'r', encoding='utf-8') as f:
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
    if ('.' or ',' or '$' or '%' or '&' or ':' or ';' or '(' or ')' or '!' or '/' or '-' or '_') not in item: 
        cleaned_text_list.append(item)

# make all words lowercase
lowercase_list = []
for item in cleaned_text_list:
    lowercase_list.append(item.lower())

# initialize by loading desired files
print('Importing word map')
with open('../source/words_dictionary.json', 'r', encoding='utf-8') as f:
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
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            hex_code = '#%02x%02x%02x' % (r, g, b)
            if(hex_code not in used_hexes):
                word_map[key] = hex_code
                used_hexes.append(hex_code)
                make_hex = False
        
    print('Updating length records')
    with open('../source/map_length.txt', 'w') as f:
        f.write(str(len(word_map)))

# calculate nearest perfect square, add placeholder to fill
root, final_list = makePerfectSquareList(lowercase_list)

# Initialize game
pygame.init()

# Set display size in pixels
# screen = pygame.display.set_mode([500, 500])
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height], pygame.RESIZABLE)

# Activate Run Loop
running = True

# square_width = 10
# square_height = 10
square_width = screen_width / root
square_height = screen_height / root

while running:
    word_index = 0

    # build screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            old_screen = screen
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            screen.blit(old_screen, (0, 0))
            del old_screen

    screen.fill((255, 255, 255))

    # creates grid of cells (i.e. makes large square, from smaller squares
    # movement on y-axis
    for i in range(root):
        y_cord = i*square_height
        #movement on x-axis
        for j in range(root):
            x_cord = j*square_width
            # get color hex code, set default code if word hasn't been discovered yet
            color_code = word_map.setdefault(final_list[word_index], '#000000')
            color = pygame.Color(color_code)
            # draw square with given coordinates and dimensions
            square = pygame.draw.rect(screen, color, pygame.Rect((x_cord, y_cord), (square_width, square_height)))

            # increase index, which is used to call each word from the source text array
            word_index += 1

    pygame.display.flip()
pygame.quit()

# Save word_map to file for cache use later
print('Artwork closing, updated word map')
with open('../source/words_dictionary.json', 'w') as f:
    json.dump(word_map, f)