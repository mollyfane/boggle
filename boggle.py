# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 21:54:35 2018

@author: Molly
"""

"""
 Show how to put a timer on the screen.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
 
import pygame
import find_letters

# Define some colors
BLACK = (0, 0, 155)
WHITE = (255, 253, 230)
RED = (255,40,40)

pygame.init()
 
# Set the width and height of the screen
size = [530, 540]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Molly's Boggle Extravaganza")
 
# Loop until the user clicks the close button.
game_done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
font = pygame.font.Font(None, 25)
dice_font = pygame.font.Font(None, 125)
done_font = pygame.font.Font(None, 45)

frame_count = 0
frame_rate = 60
start_time = 180
start = False
change_flag = False
done = False
hide_letters = True
shuffled_dice = find_letters.boggle()

# -------- Main Program Loop -----------
while not game_done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            game_done = True  # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                start = True
                change_flag = True
                done = False
                hide_letters = False
            if event.key == pygame.K_p:
                if(start == True and done == False):
                    start = False
                    change_flag = False
                    hide_letters = True
                elif(start == False and done == False):
                    start = True
                    change_flag = False
                    hide_letters = False
                    
    # Set the screen background
    screen.fill(BLACK)
 
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

    text = font.render('New Game: press N', True, WHITE)
    screen.blit(text, [300,5])
    text = font.render('Pause: press P', True, WHITE)
    screen.blit(text, [300,20])
    for i in range(5):
        for j in range(5):
            pygame.draw.rect(screen, WHITE, (20+99*i,40+99*j,94,94), 0)
            if(hide_letters == False):
                the_letter = shuffled_dice[i,j]
                letter = dice_font.render(the_letter, True, BLACK)
                if the_letter == 'I':
                    screen.blit(letter, [55+99*i, 50+99*j])
                elif the_letter == 'T':
                    screen.blit(letter, [40+99*i, 50+99*j])
                elif the_letter == 'W':
                    screen.blit(letter, [27+99*i, 50+99*j])
                else: screen.blit(letter, [35+99*i, 50+99*j])
                
    if(done == True):
        text = done_font.render('DONE', True, RED)
        for i in range(5):
            for j in range(5):
                screen.blit(text, [20+99*i,110+99*j,94,94])

    if(start == True):
        if(change_flag == True):
            frame_count = 0
            shuffled_dice = find_letters.boggle()
            change_flag = False

        # --- Timer going up ---
        # Calculate total seconds
        total_seconds = frame_count // frame_rate
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
        text = font.render(output_string, True, WHITE)
        screen.blit(text, [20, 5])
        
        # --- Timer going down ---
        # Calculate total seconds
        total_seconds = start_time - (frame_count // frame_rate)
        if total_seconds <= 0:
            total_seconds = 0
            done = True
            start = False
            change_flag = True
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
        text = font.render(output_string, True, WHITE)
        screen.blit(text, [20, 20])  

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    frame_count += 1
 
    # Limit frames per second
    clock.tick(frame_rate)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()