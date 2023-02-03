import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 600
HEIGHT = 600

def show_menu():
    menu_font = pygame.font.Font(None, 48)
    play_text = menu_font.render("Play", True, (255, 255, 255))
    insert_text = menu_font.render("Insert word", True, (255, 255, 255))
    quit_text = menu_font.render("Quit", True, (255, 255, 255))
    window.blit(play_text, [WIDTH//2-50, HEIGHT//2])
    window.blit(insert_text, [WIDTH//2-100, HEIGHT//2+50])
    window.blit(quit_text, [WIDTH//2-50, HEIGHT//2+100])
    pygame.display.update()

    running_menu = True
    while running_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_menu = False
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                if WIDTH//2-50 < x < WIDTH//2+50 and HEIGHT//2 < y < HEIGHT//2+50:
                    play_game()
                    running_menu = False
                elif WIDTH//2-100 < x < WIDTH//2+100 and HEIGHT//2+50 < y < HEIGHT//2+100:
                    insert_word()
                    running_menu = False
                elif WIDTH//2-50 < x < WIDTH//2+50 and HEIGHT//2+100 < y < HEIGHT//2+150:
                    pygame.quit()
                    running_menu = False


def play_game():
    global words
    word = random.choice(words)

def insert_word():
    word = input("Enter a word: ")
    with open("mots.txt", "a") as f:
        f.write(word + "\n")
        show_menu()

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.Font(None, 32)

with open("mots.txt", "r") as f:
    words = f.readlines()

words = [word.strip() for word in words]

word = random.choice(words)

incorrect_guesses = 0
correct_guesses = 0
guessed_letters = []

show_menu()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            letter = chr(event.key)
            
            if letter not in guessed_letters:
                guessed_letters.append(letter)
                
                if letter in word:
                    correct_guesses += 1
                else:
                    incorrect_guesses += 1
                    
                if correct_guesses == len(word) or incorrect_guesses == 7:
                    running = False
                    
    display_word = ""
    for char in word:
        if char in guessed_letters:
            display_word += char + " "
        else:
            display_word += "_ "
    text = font.render(display_word, True, BLACK)
    window.blit(text, [100, 100])
    
    if incorrect_guesses >= 1:
        hangman_image = pygame.image.load("hangman_0.png")
        window.blit(hangman_image, (200, HEIGHT-250))
    if incorrect_guesses >= 2:
        hangman_image = pygame.image.load("hangman_1.png")
        window.blit(hangman_image, (200, HEIGHT-250))
    if incorrect_guesses >= 3:
        hangman_image = pygame.image.load("hangman_2.png")
        window.blit(hangman_image, (200, HEIGHT-250))
    if incorrect_guesses >= 4:
        hangman_image = pygame.image.load("hangman_3.png")
        window.blit(hangman_image, (200, HEIGHT-250))
    if incorrect_guesses >= 5:
        hangman_image = pygame.image.load("hangman_4.png")
        window.blit(hangman_image, (200, HEIGHT-250))
    if incorrect_guesses >= 6:
        hangman_image = pygame.image.load("hangman_5.png")
        window.blit(hangman_image, (200, HEIGHT-250))
    if incorrect_guesses >= 7:
        hangman_image = pygame.image.load("hangman_6.png")
        window.blit(hangman_image, (200, HEIGHT-250))

    pygame.display.update()
    
    window.fill(WHITE)
    
if incorrect_guesses == 7:
    result_text = "Perdu! Le mot était " + word
elif correct_guesses == len(word):
    result_text = "Félicitation Le mot était " + word
else:
    result_text = "Merci d'avoir joué !"
result = font.render(result_text, True, BLACK)
window.blit(result, [200, 200])

pygame.display.update()

pygame.time.wait(3000)

pygame.quit()