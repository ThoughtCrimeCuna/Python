import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen and grid settings
screen_width, screen_height = 1400, 800
menu_width = 5 * 50  # Width of menu area (5 columns)
grid_width = (screen_width - menu_width) // 50  # Adjust grid width to exclude menu area
screen = pygame.display.set_mode((screen_width, screen_height))
background_color = (30, 30, 30)
grid_color = (50, 50, 50)
token_color = "hotpink"
selected_token_color = "aliceblue"
direction_line_color = (255, 255, 255)
menu_color = (70, 70, 70)
button_color = (100, 100, 200)
button_text_color = (255, 255, 255)
turn_number = 1


# Font settings
font = pygame.font.SysFont(None, 24)

# Grid cell size
grid_size = 50  # Size of each grid cell

# Add multiple tokens with starting positions, directions, and names
tokens = [
    #{'position': (2, 3), 'selected': False, 'direction': 'down', 'name': 'scout', 'ap': 3, 'max_ap': 3},
    
]


# Function to check if a position is already occupied
def is_position_occupied(position):
    return any(token['position'] == position for token in tokens)

# Generate spear_men in the first column without overlapping
for i in (1,3,5,7,9,11,13,15):
    position = (0, i)
    if not is_position_occupied(position):
        tokens.append({'position': position, 'selected': False, 'direction': 'up', 'name': 'spear_man', 'ap': 5, 'max_ap': 5,'hp': 5, 'max_hp': 5})


# Generate houses in the first column, also ensuring no overlap
for i in (0,2,4,6,8,10,12,14,16):
    position = (random.randint(1,5)+random.randint(0,3), i)
    if not is_position_occupied(position):
        tokens.append({'position': position, 'selected': False, 'direction': 'down', 'name': 'house', 'ap': 0, 'max_ap': 0,'hp': 5, 'max_hp': 5})

# Generate rocks at random positions, ensuring no overlap
for _ in range(50):
    while True:
        x = random.randint(1,10) + random.randint(1,6)  # Choose range based on grid width you want rocks in
        y = random.randint(0, 16)
        position = (x, y)
        if not is_position_occupied(position):
            tokens.append({'position': position, 'selected': False, 'direction': 'right', 'name': 'rock', 'ap': 0, 'max_ap': 0,'hp': 50, 'max_hp': 50})
            break


# Button settings
button_end_turn = pygame.Rect(screen_width - menu_width + 10, screen_height - 60, menu_width - 20, 50)

# Function to draw the grid
def draw_grid():
    for x in range(0, screen_width - menu_width, grid_size):
        for y in range(0, screen_height, grid_size):
            rect = pygame.Rect(x, y, grid_size, grid_size)
            pygame.draw.rect(screen, grid_color, rect, 1)

# Function to draw tokens with directional line and AP count
def draw_tokens():
    for token in tokens:
        color = selected_token_color if token['selected'] else token_color
        x, y = token['position']
        center_x = x * grid_size + grid_size // 2
        center_y = y * grid_size + grid_size // 2

        # Draw token based on its name
        if token['name'] == 'spear_man':
            points = [
                (center_x, center_y - grid_size // 3), 
                (center_x - grid_size // 6, center_y + grid_size // 3),
                (center_x + grid_size // 6, center_y + grid_size // 3)
            ]
            pygame.draw.polygon(screen, color, points)
            pygame.draw.circle(screen, color, (center_x, center_y - grid_size // 3), 5)

            if token['direction'] == 'up':
                line_start = (center_x + grid_size // 6, center_y)
                line_end = (center_x + grid_size // 6, center_y - grid_size // 2)
            elif token['direction'] == 'down':
                line_start = (center_x - grid_size // 6, center_y)
                line_end = (center_x - grid_size // 6, center_y + grid_size // 2)
            elif token['direction'] == 'left':
                line_start = (center_x, center_y - grid_size // 6)
                line_end = (center_x - grid_size // 2, center_y - grid_size // 6)
            elif token['direction'] == 'right':
                line_start = (center_x, center_y + grid_size // 6)
                line_end = (center_x + grid_size // 2, center_y + grid_size // 6)
            pygame.draw.line(screen, direction_line_color, line_start, line_end, 2)

        elif token['name'] == 'goblin':
            sword_width = grid_size // 6
            sword_height = grid_size // 2
            pygame.draw.rect(screen, "green", (center_x - sword_width // 2, center_y - sword_height // 2, sword_width, sword_height))

        elif token['name'] == 'rock':
            pygame.draw.rect(screen, 'grey33', (center_x - grid_size // 3, center_y - grid_size // 3, grid_size // 1.5, grid_size // 1.5))
            pygame.draw.rect(screen, 'grey50', (center_x - grid_size // 4, center_y - grid_size // 4, grid_size // 2, grid_size // 2))

        elif token['name'] == 'house':
            # Draw a house with a rectangular base and triangular roof
            # Base of the house
            base_width = grid_size // 2
            base_height = grid_size // 3
            base_x = center_x - base_width // 2
            base_y = center_y - base_height // 4

            pygame.draw.rect(screen, "grey40", (base_x, base_y, base_width, base_height))

            # Roof of the house (triangle)
            roof_points = [
                (center_x, center_y - base_height),  # Top of the triangle
                (base_x-5, base_y),                         # Bottom-left of the triangle
                (base_x+5 + base_width, base_y)             # Bottom-right of the triangle
            ]
            pygame.draw.polygon(screen, "brown", roof_points)


        # Draw AP value in top left corner of tokens square
        if token['ap'] > 0:
            ap_text = font.render(str(token['ap']), True, "white")
            screen.blit(ap_text, (x * grid_size + 5, y * grid_size + 5))
        # Draw HP value in the bottom left corner of the token's square
        if token['hp'] == token['max_hp']:
            #hp_text = font.render(str(token['hp'])+"/"+str(token['max_hp']), True, "white")
            #screen.blit(hp_text, (x * grid_size + 5, y * grid_size + grid_size - 20))
            pass
        elif 0 < token['hp'] < token['max_hp']:
            hp_text = font.render(str(token['hp'])+"/"+str(token['max_hp']), True, "yellow")
            screen.blit(hp_text, (x * grid_size + 5, y * grid_size + grid_size - 20))
        elif token['hp'] <= 0:
            tokens.remove(token)
            

# Function to draw menu and buttons
def draw_menu():
    # Draw the menu background
    pygame.draw.rect(screen, menu_color, (screen_width - menu_width, 0, menu_width, screen_height))
    turn_print = font.render("Turn: " + str(turn_number), True, "white")
    screen.blit(turn_print, (screen_width - menu_width + 5, 5, menu_width, screen_height))
    # Draw the "End Turn" button
    pygame.draw.rect(screen, button_color, button_end_turn)
    button_text = font.render("End Turn", True, button_text_color)
    screen.blit(button_text, (button_end_turn.x + 15, button_end_turn.y + 15))

# Function to reset AP for all tokens
def reset_action_points():
    for token in tokens:
        token['ap'] = max(0,(token['max_ap']))

# Function to select a token based on mouse click
def select_token(mouse_pos):
    grid_x, grid_y = mouse_pos[0] // grid_size, mouse_pos[1] // grid_size
    if mouse_pos[0] < screen_width - menu_width:  # Ensure clicks outside the grid don't select
        for token in tokens:
            if token['position'] == (grid_x, grid_y):
                token['selected'] = True
            else:
                token['selected'] = False

# Function to check if a position is occupied
def is_position_occupied(x, y):
    for token in tokens:
        if token['position'] == (x, y):
            return True
    return False

# Function to move the selected token and update its direction
def move_selected_token(direction):
    for token in tokens:
        if token['selected'] and token['ap'] > 0:
            x, y = token['position']
            new_position = {
                'up': (x, y - 1),
                'down': (x, y + 1),
                'left': (x - 1, y),
                'right': (x + 1, y)
            }.get(direction, (x, y))

            token['direction'] = direction

            new_x, new_y = new_position
            if (0 <= new_x < grid_width and 0 <= new_y < screen_height // grid_size and 
                not is_position_occupied(new_x, new_y)):
                token['position'] = new_position
                token['ap'] -= 1  # Decrement action points by 1
            elif is_position_occupied(new_x, new_y):
                for target in tokens:
                    if target["position"] == (new_x, new_y) and target["name"] == 'goblin':
                        target["hp"] -= 1
                        token['ap'] -= 1


selected_token_index = 0  # Starts at the first token

# Function to select the next token with AP
def select_next_token_with_ap():
    global selected_token_index
    
    # Start looking from the next token
    start_index = (selected_token_index + 1) % len(tokens)
    
    # Find the next token with AP > 0
    for i in range(len(tokens)):
        index = (start_index + i) % len(tokens)
        if tokens[index]['ap'] > 0:
            # Deselect the current token and select the new one
            tokens[selected_token_index]['selected'] = False
            tokens[index]['selected'] = True
            selected_token_index = index
            break


def deselect_current_token():
    for token in tokens:
        if token['selected']:
            token['selected'] = False
            break

# Function to handle attack logic based on direction
def foe_attack(direction, x, y, damage):
    # Determine the attack position based on the direction
    attack_position = {
        "left": (x - 1, y),
        "right": (x + 1, y),
        "up": (x, y - 1),
        "down": (x, y + 1)
    }[direction]

    # Check each token to see if it occupies the attack position
    for target in tokens:
        if target['position'] == attack_position:
            target["hp"] -= damage
            break  # Stop after hitting the first target


# Function to move foes and initiate attacks as needed
def foes_move(direction):
    global screen_width, screen_height, menu_width, grid_width, grid_size
    for token in tokens:
        if token['name'] == "goblin":
            x, y = token['position']
            new_position = {
                "left": (x - 1, y),
                "right": (x + 1, y),
                "up": (x, y - 1),
                "down": (x, y + 1)
            }[direction]

            # Move goblin if the new position is unoccupied
            if not is_position_occupied(*new_position):
                new_x, new_y = new_position
                if (0 <= new_x < grid_width and 0 <= new_y < screen_height // grid_size):
                    token['position'] = new_position
                else:
                    token['position'] = token['position']
                token['direction'] = direction
            else:
                # Target in front: attack or decide a different path
                for target in tokens:
                    if target['position'] == new_position:
                        if target["name"] in ("rock","goblin"):
                            confused = ["down", "up", "left", "right"]
                            confused.remove(direction)
                            choice = random.choice(confused)
                            bypass_position = {
                                "down": (x, y + 1),
                                "up": (x, y - 1),
                                "left": (x - 1, y),
                                "right": (x + 1, y)
                            }[choice]
                            new_x, new_y = bypass_position
                            if not is_position_occupied(*bypass_position):
                                if (0 <= new_x < grid_width and 0 <= new_y < screen_height // grid_size):
                                    token['position'] = bypass_position
                                    token['direction'] = choice
                            else:
                                if target["name"] == "goblin":
                                    break
                                else:
                                    foe_attack(direction, x, y, 1)

                        elif target["name"] == "spear_man":
                            if target['direction'] == "right":
                                token["hp"] -= 1  # Spearman attacks the goblin
                            else:
                                foe_attack(direction, x, y, 1)  # Goblin attacks spear man

                        else:
                            foe_attack(direction,x,y,1)
                        break  # Stop checking other tokens once an action is taken

    # Update the screen with each move
    screen.fill(background_color)
    draw_grid()
    draw_tokens()
    draw_menu()
    pygame.display.flip()
    pygame.time.wait(50)

                            
                            

    


# Main game loop
running = True
while running:
    screen.fill(background_color)
    draw_grid()
    draw_tokens()
    draw_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button_end_turn.collidepoint(mouse_pos):
                turn_number += 1
                for i in range(0,5):
                    foes_move("left")
                for i in range(0,16):
                    position = (22, random.randint(0,15))
                    if not is_position_occupied(position[0],position[1]):
                        tokens.append({'position': position, 'selected': False, 'direction': 'up', 'name': 'goblin', 'ap': 0, 'max_ap': 0,'hp': 3, 'max_hp': 3})
                reset_action_points()  # Reset AP when "End Turn" button is clicked
            else:
                select_token(mouse_pos)
        
        elif event.type == pygame.KEYDOWN:
            shift_pressed = pygame.key.get_mods() & pygame.KMOD_SHIFT
            if event.key == pygame.K_UP:
                if shift_pressed:
                    for token in tokens:
                        if token['selected'] and token['ap'] > 0:
                            token['direction'] = 'up'
                else:
                    move_selected_token('up')
            elif event.key == pygame.K_DOWN:
                if shift_pressed:
                    for token in tokens:
                        if token['selected'] and token['ap'] > 0:
                            token['direction'] = 'down'
                else:
                    move_selected_token('down')
            elif event.key == pygame.K_LEFT:
                if shift_pressed:
                    for token in tokens:
                        if token['selected'] and token['ap'] > 0:
                            token['direction'] = 'left'
                else:
                    move_selected_token('left')
            elif event.key == pygame.K_RIGHT:
                if shift_pressed:
                    for token in tokens:
                        if token['selected'] and token['ap'] > 0:
                            token['direction'] = 'right'
                else:
                    move_selected_token('right')
            
                 
            elif event.key == pygame.K_RETURN:
                deselect_current_token()
                select_next_token_with_ap()  # Cycle to the next token with AP
                

    pygame.display.flip()
