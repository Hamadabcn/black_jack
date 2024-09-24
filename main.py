import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
BUTTON_COLOR = (0, 0, 128)
BUTTON_HOVER_COLOR = (0, 100, 255)
FONT = pygame.font.SysFont('comic sans', 25)
LARGE_FONT = pygame.font.SysFont('comic sans', 48)
SMALL_FONT = pygame.font.SysFont('comic sans', 20)
LARGE_SYMBOL_FONT = pygame.font.SysFont('Arial', 90)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('BlackJack')


# Card class representing a single playing card
class Card:
    def __init__(self, rank, value, suit_symbol):
        self.rank = rank
        self.value = value
        self.suit_symbol = suit_symbol

    def __repr__(self):
        return f"{self.rank}{self.suit_symbol}"


# Button class
class Button:
    def __init__(self, text, x, y, width, height, action=None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = BUTTON_COLOR
        self.action = action

    def draw(self, screen):
        # Change color on hover
        if self.is_hovered():
            self.color = BUTTON_HOVER_COLOR
        else:
            self.color = BUTTON_COLOR

        pygame.draw.rect(screen, self.color, self.rect)
        text_surf = FONT.render(self.text, True, WHITE)
        screen.blit(text_surf, (self.rect.x + (self.rect.width - text_surf.get_width()) // 2,
                                self.rect.y + (self.rect.height - text_surf.get_height()) // 2))

    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.is_hovered():
            if self.action:
                self.action()


# Initialize deck
def init_deck():
    suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    suit_symbols = {'Hearts': '♥', 'Diamonds': '♦', 'Spades': '♠', 'Clubs': '♣'}
    cards = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
             '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

    deck = []
    for suit in suits:
        for card, value in cards.items():
            deck.append(Card(card, value, suit_symbols[suit]))
    random.shuffle(deck)
    return deck


# Show cards on the screen
def show_cards(screen, cards, x, y):
    for i, card in enumerate(cards):
        card_x = x + i * (80 + 10)
        card_y = y
        pygame.draw.rect(screen, WHITE, (card_x, card_y, 80, 130))
        pygame.draw.rect(screen, BLACK, (card_x, card_y, 80, 130), 2)

        # Render the rank on the left side
        card_text = SMALL_FONT.render(f'{card.rank}', True, BLACK)
        screen.blit(card_text, (card_x + 5, card_y + 5))  # Adjust position for left alignment

        # Render the symbol in the center
        symbol_text = LARGE_SYMBOL_FONT.render(card.suit_symbol, True, BLACK)
        screen.blit(symbol_text, (card_x + (80 - symbol_text.get_width()) // 2,
                                  card_y + (130 - symbol_text.get_height()) // 2 - 10))  # Center the symbol


# Show dealer's first card hidden
def show_dealer_cards(screen, dealer_cards, hide_first_card=False):
    for i, card in enumerate(dealer_cards):
        card_x = 100 + i * (80 + 10)  # X position for each card
        card_y = 100  # Y position for the cards

        # Draw card rectangle
        pygame.draw.rect(screen, WHITE, (card_x, card_y, 80, 120))
        pygame.draw.rect(screen, BLACK, (card_x, card_y, 80, 120), 2)

        if i == 0 and hide_first_card:
            # Hide the first card
            pygame.draw.rect(screen, BLACK, (card_x, card_y, 80, 120))
            pygame.draw.line(screen, WHITE, (card_x, card_y), (card_x + 80, card_y + 120), 2)
            pygame.draw.line(screen, WHITE, (card_x + 80, card_y), (card_x, card_y + 120), 2)
        else:
            # Render the rank on the left side
            card_text = SMALL_FONT.render(f'{card.rank}', True, BLACK)
            screen.blit(card_text, (card_x + 5, card_y + 5))  # Adjust position for left alignment

            # Render the symbol in the center of the card
            symbol_text = LARGE_SYMBOL_FONT.render(card.suit_symbol, True, BLACK)
            symbol_text_x = card_x + (80 - symbol_text.get_width()) // 2
            symbol_text_y = card_y + (130 - symbol_text.get_height()) // 2 - 10  # Center vertically
            screen.blit(symbol_text, (symbol_text_x, symbol_text_y))


# Show scores
def show_scores(player_score, dealer_score, hide_dealer=True):
    player_text = FONT.render(f'Player Score: {player_score}', True, WHITE)
    screen.blit(player_text, (100, 400))
    if hide_dealer:
        dealer_text = FONT.render(f'Dealer Score: ?', True, WHITE)
    else:
        dealer_text = FONT.render(f'Dealer Score: {dealer_score}', True, WHITE)
    screen.blit(dealer_text, (100, 50))


# Show instructions
def show_instructions():
    running = True
    while running:
        screen.fill(GREEN)
        title = LARGE_FONT.render('BlackJack Instructions', True, WHITE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))

        instructions = [
            "1. Your goal is to reach a hand value of 21 without going over.",
            "2. Cards 2-10 are worth their face value.",
            "3. Face cards (J, Q, K) are worth 10, and Aces can be worth 1 or 11.",
            "4. Click 'Hit' to draw another card, or 'Stand' to stop drawing.",
            "5. The dealer must draw until they reach a value of 17 or more.",
            "6. If you exceed 21, you 'Bust' and lose the game.",
            "7. Whoever has the closest hand value to 21 without busting wins!"
        ]

        for i, line in enumerate(instructions):
            instruction_text = SMALL_FONT.render(line, True, WHITE)
            screen.blit(instruction_text, (50, 150 + i * 30))

        back_button = Button('Back', WIDTH // 2 - 50, HEIGHT - 100, 100, 50, main_menu)
        back_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            back_button.handle_event(event)

        if back_button.is_hovered():
            back_button.color = BUTTON_HOVER_COLOR
        else:
            back_button.color = BUTTON_COLOR

        pygame.display.update()


# Main menu function
def main_menu():
    play_button = Button('Play', WIDTH // 2 - 50, HEIGHT // 2 - 25, 100, 50, play_blackjack)
    instructions_button = Button('Instructions', WIDTH // 2 - 75, HEIGHT // 2 + 50, 150, 50, show_instructions)
    quit_button = Button('Quit', WIDTH // 2 - 50, HEIGHT // 2 + 125, 100, 50, sys.exit)

    while True:
        screen.fill(GREEN)
        title = LARGE_FONT.render('Welcome to the BlackJack Game!', True, BLACK)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))
        play_button.draw(screen)
        instructions_button.draw(screen)
        quit_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            play_button.handle_event(event)
            instructions_button.handle_event(event)
            quit_button.handle_event(event)

        if play_button.is_hovered():
            play_button.color = BUTTON_HOVER_COLOR
        else:
            play_button.color = BUTTON_COLOR

        if instructions_button.is_hovered():
            instructions_button.color = BUTTON_HOVER_COLOR
        else:
            instructions_button.color = BUTTON_COLOR

        if quit_button.is_hovered():
            quit_button.color = BUTTON_HOVER_COLOR
        else:
            quit_button.color = BUTTON_COLOR

        pygame.display.flip()


# Calculate score with ace adjustment
def calculate_score(hand):
    score = sum(card.value for card in hand)
    aces = sum(1 for card in hand if card.rank == 'A')
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score


# Blackjack game logic
def play_blackjack():
    deck = init_deck()
    player_hand = []
    dealer_hand = []

    player_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    dealer_hand.append(deck.pop())

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    hit_button = Button('Hit', WIDTH // 2 + 140, HEIGHT - 150, 100, 50, None)
    stand_button = Button('Stand', WIDTH // 2 + 250, HEIGHT - 150, 100, 50, None)
    play_again_button = Button('Play Again', WIDTH // 2 + 150, HEIGHT - 100, 200, 50, play_blackjack)
    back_to_menu_button = Button('Main Menu', WIDTH // 2 + 150, HEIGHT - 160, 200, 50, main_menu)

    game_over = False
    result_text = ""

    # Define hit and stand functions
    def hit():
        nonlocal player_score
        player_hand.append(deck.pop())
        player_score = calculate_score(player_hand)
        if player_score > 21:
            nonlocal game_over, result_text
            game_over = True
            result_text = "Bust! You lose!"

    def stand():
        nonlocal dealer_score, game_over, result_text
        while dealer_score < 17:
            dealer_hand.append(deck.pop())
            dealer_score = calculate_score(dealer_hand)
        game_over = True
        if dealer_score > 21:
            result_text = "Dealer busts! You win!"
        elif player_score > dealer_score:
            result_text = "You win!"
        elif player_score < dealer_score:
            result_text = "You lose!"
        else:
            result_text = "It's a tie!"

    # Assign button actions
    hit_button.action = hit
    stand_button.action = stand

    while True:
        screen.fill(GREEN)
        show_dealer_cards(screen, dealer_hand, hide_first_card=not game_over)
        show_cards(screen, player_hand, 100, 450)

        # Change here to hide the dealer's score during gameplay
        show_scores(player_score, dealer_score, hide_dealer=not game_over)

        if game_over:
            result_surface = LARGE_FONT.render(result_text, True, WHITE)
            screen.blit(result_surface, (WIDTH // 2 - result_surface.get_width() // 2, HEIGHT // 2))

            # Reveal the dealer's score at the end of the game
            show_scores(player_score, dealer_score, hide_dealer=False)

            play_again_button.draw(screen)
            back_to_menu_button.draw(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                play_again_button.handle_event(event)
                back_to_menu_button.handle_event(event)

        else:
            hit_button.draw(screen)
            stand_button.draw(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                hit_button.handle_event(event)
                stand_button.handle_event(event)

        pygame.display.update()


# Start the game
main_menu()
pygame.quit()
