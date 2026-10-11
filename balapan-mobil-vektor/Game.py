import pygame
import sys
import random
import time

pygame.init()
pygame.font.init()

# Screen dimensions
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balapan Mobil Vektor")
            
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 20, 60)
BLUE = (65, 105, 225)
GREEN = (50, 205, 50)
GRAY = (200, 200, 200)
YELLOW = (255, 215, 0)
DARK_GRAY = (50, 50, 50)

# Fonts
QUESTION_FONT = pygame.font.SysFont('Arial', 22)
ANSWER_FONT = pygame.font.SysFont('Arial', 22)
INSTR_FONT = pygame.font.SysFont('Arial', 18)
RESULT_FONT = pygame.font.SysFont('Arial', 28, bold=True)
WINNER_FONT = pygame.font.SysFont('Arial', 36, bold=True)
TITLE_FONT = pygame.font.SysFont('Arial', 48, bold=True)
INPUT_FONT = pygame.font.SysFont('Arial', 30)

# Car dimensions
CAR_WIDTH, CAR_HEIGHT = 240, 120

# Load car images
# MAKE SURE YOU HAVE car_red.png and car_blue.png in the same directory as this script.
car_red_image = pygame.image.load('car_red.png')
car_blue_image = pygame.image.load('car_blue.png')
car_red_image = pygame.transform.scale(car_red_image, (CAR_WIDTH, CAR_HEIGHT))
car_blue_image = pygame.transform.scale(car_blue_image, (CAR_WIDTH, CAR_HEIGHT))

# Starting positions
START_X = 50
PLAYER1_Y = HEIGHT // 3 - CAR_HEIGHT // 7.2
PLAYER2_Y = 2 * HEIGHT // 3 - CAR_HEIGHT // 1.2

# Speeds
BASE_SPEED = 7
SPEED_UP = 6
SPEED_DOWN = 2

# Keys for answer input
P1_KEYS = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]
P2_KEYS = [pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]

# Questions for different difficulties
questions_easy = [
    {
        'question': 'Vektor A = 2i + 4j dan vektor B = 4i + 8j. Perbandingan panjang A : B adalah',
        'choices': ['1:2', '2:1', '1:1 ', '1:4'],
        'answer': 0
    },
    {
        'question': 'Jika vektor P = 3i - 4j dan vektor Q = 6i - 8j, maka vektor P dan Q...?',
        'choices': ['Tegak Lurus', 'Berlawanan Arah', 'Searah ', 'Tak Sebanding'],
        'answer': 2
    },
    {
        'question': 'Panjang vektor A = 5 satuan dan panjang vektor B = 10 satuan. Perbandingan panjang A : B adalah...',
        'choices': ['5:10', '1:2', '2:1', '10:5'],
        'answer': 1
    },
    {
        'question': 'Jika vektor A = a(2i + j) dan vektor B = 6i + 3j, maka nilai a agar A dan B searah adalah...',
        'choices': ['2', '3', '1', '0'],
        'answer': 1
    },
    {
        'question': 'Diberikan vektor A = i + j dan B = 2i + 2j. Vektor A dan B merupakan...',
        'choices': ['Vektor Ortogonal', 'Vektor Searah', 'Vektor Berlawanan Arah', 'Vektor Sembarang'],
        'answer': 1
    },
    {
        'question': 'Jika vektor A = 5i dan vektor B = 3i, maka perbandingan panjang A : B adalah..',
        'choices': ['5:3', '3:5', '1:1', '2:1'],
        'answer': 0
    },
    {
        'question': 'Panjang vektor u = √10 dan panjang vektor v = √40. Maka perbandingan u : v adalah...',
        'choices': ['1:4', '1:√2', '√10:√40', '1:2'],
        'answer': 3
    },
    {
        'question': 'Vektor A = -2i + 4j dan B = -4i + 8j. Maka vektor A dan B adalah...',
        'choices': ['Searah', 'Berlawanan Arah', 'Tegak Lurus', 'Tidak Sebanding'],
        'answer': 0
    },
    {
        'question': 'Jika dua vektor A dan B saling searah dan |A| = 7, |B| = 21, maka perbandingan A : B adalah...',
        'choices': ['1:2', '1:3', '2:1', '3:1'],
        'answer': 1
    },
    {
        'question': 'Vektor A = 3i + 4j dan vektor B = 6i + 8j. Panjang A dan B berturut-turut adalah...',
        'choices': ['5 dan 10', '6 dan 12', '7 dan 14', '9 dan 18'],
        'answer': 1
    },
    {
        'question': 'Vektor A = 2i + 4j dan B = 1i + 2j. Maka A dan B...',
        'choices': ['Tidak Sebanding', 'Searah', 'Berlawanan Arah', 'Tegak Lurus'],
        'answer': 1
    },
    {
        'question': 'Diketahui vektor A = 3i + 4j. Panjang vektor A adalah...',
        'choices': ['5', '6', '7', '25'],
        'answer': 0
    },
    {
        'question': 'Jika A = i + j dan B = -i - j, maka arah A dan B adalah...',
        'choices': ['Searah', 'Tegak Lurus', 'Berlawanan Arah', 'Sama Panjang, tapi beda arah'],
        'answer': 2
    },
    {
        'question': 'Vektor A = 5i - j dan B = 10i - 2j. Perbandingan A : B adalah...',
        'choices': ['1:1', '2:1', '1:2', 'Tidak Sebanding'],
        'answer': 2
    },
    {
        'question': 'Jika A = 4i + 3j, maka panjang A adalah...',
        'choices': ['7', '5', 'gatau', '4'],
        'answer': 1
    },
    {
        'question': 'Vektor A = i + 2j dan B = 2i + 4j. Maka A dan B...',
        'choices': ['Tidak Sebanding', 'Searah', 'Berlawanan', 'Tegak Lurus'],
        'answer': 1
    },
    {
        'question': 'Jika vektor A = -3i - 3j dan B = 3i + 3j, maka hubungan A dan B adalah...',
        'choices': ['Searah', 'Berlawanan Arah', 'Tegak Lurus', 'Tidak Sebanding'],
        'answer': 1
    },
    {
        'question': 'Vektor A = i dan B = j. Maka hubungan arah A dan B adalah...',
        'choices': ['Searah', 'Tegak Lurus', 'Berlawanan Arah', 'Tidak Diketahui'],
        'answer': 1
    },
    {
        'question': 'Vektor A = 6i dan B = -6i. Maka A dan B...',
        'choices': ['Searah', ' Berlawanan arah', 'Tidak sebanding', 'Tegak lurus'],
        'answer': 1
    },
    {
        'question': 'Jika A = 2i + 0j dan B = 4i + 0j, maka perbandingan A : B adalah...',
        'choices': ['1:2', '2:1', '1:1', '4:2'],
        'answer':0
   },
]

questions_medium = [
    {
        'question': 'Vektor A = 2i + 2j dan B = -2i - 2j. Maka hubungan antara A dan B adalah...',
        'choices': ['Searah', 'Tegak lurus', 'Berlawanan arah', 'Tidak sebanding'],
        'answer': 2
    },
    {
        'question': 'Jika A = 3i - 4j dan B = -6i + 8j, maka perbandingan panjang A : B adalah...',
        'choices': ['1:2', '2:1', '1:√2', '1:1'],
        'answer': 0
    },
    {
        'question': 'Vektor A = 3i + 4j, dan vektor B = 4i - 3j. Maka A dan B...',
        'choices': ['Searah', 'Tegak Lurus', 'Berlawanan Arah', 'Tak Sebanding'],
        'answer': 1
    },
    {
        'question': 'Diketahui vektor A = ai + 3j dan B = 4i + 6j. Jika A dan B searah, maka nilai a adalah...',
        'choices': ['3', '4', '2', '1'],
        'answer': 2
    },
    {
        'question': 'Vektor A = i - 2j + k dan vektor B = 2i - 4j + 2k. Perbandingan panjang A : B adalah...',
        'choices': ['1:√2', '1:2', '√3:√12', '1:1'],
        'answer': 1
    },
    {
        'question': 'Vektor A = 2i - 3j, dan B = -4i + 6j. Sudut antara A dan B adalah...',
        'choices': ['0°', '45°', '90°', '180°'],
        'answer': 3
    },
    {
        'question': 'Jika panjang vektor A = √29 dan vektor B = 2A, maka panjang B adalah...',
        'choices': ['√29', '2√29', '4√29', '29'],
        'answer': 1
    },
    {
        'question': 'Diberikan vektor A = 5i + 12j dan vektor B = ki + (12k)j. Agar A dan B searah, maka nilai k adalah...',
        'choices': ['5', '12', '1', 'Tidak ada'],
        'answer': 2
    },
    {
        'question': ' Vektor A = -3i + 4j dan B = 6i - 8j. Maka A dan B memiliki arah...',
        'choices': ['Sama', 'Berlawanan', 'Tegak Lurus', 'Tidak bisa ditentukan'],
        'answer': 1
    },
    {
        'question': 'Jika A dan B adalah vektor dengan |A| = 5 dan |B| = 10, dan sudut antara A dan B adalah 60°, maka besar vektor resultan A + B adalah...',
        'choices': ['5√33', '10', '√75', '√125'],
        'answer': 3
    },   
    {
        'question': 'Diketahui vektor A = 2i + 3j + k dan B = i - 2j + 4k. Tentukan A·B (dot product) dan perbandingan A : B berdasarkan panjangnya.',
        'choices': ['1:2', '2:1', '1:1', 'Tidak sebanding'],
        'answer': 0
    },
    {
        'question': 'Vektor A = 4i + 3j - k dan B = -2i + j + 3k. Tentukan nilai perbandingan panjang A : B dan apakah arah keduanya searah atau berlawanan.',
        'choices': ['2:3,searah', '3:2,berlawanan arah', '1:1,searah', '1:1,berlawanan arah'],
        'answer': 1
    },
    {
        'question': 'Diketahui panjang A = 5 dan panjang B = 7, dan sudut antara keduanya adalah 120°. Tentukan besar A + B menggunakan hukum kosinus.',
        'choices': ['5', '8', '10', '12'],
        'answer': 2
    },
    {
        'question': ' Vektor A = 3i + 4j + k dan B = 6i - 8j + 2k. Tentukan besar vektor A - B dan perbandingan panjang A : B.',
        'choices': ['√10,1:2', '√14,1:1', '√14,2:1', '√10,1:1'],
        'answer': 2
    },
    {
        'question': 'Jika vektor A = 3i - 2j + 4k dan B = -i + 3j + 2k, tentukan nilai A x B (cross product) dan perbandingan arah A : B.',
        'choices': ['2k,searah', '-2k,berlawanan arah', '2k,tidak sebanding', '-2k,tegak lurus'],
        'answer': 3                                                     
    },

]

questions_hard = [
    {
        'question': 'Diberikan vektor A = ai + bj dan B = 6i - 2j. Jika A dan B tegak lurus, dan panjang A = √(a² + b²) = 5, tentukan nilai a : b.',
        'choices': [' 1:2', '2:1', '3:4', '1:3'],
        'answer': 1
    },
    {
        'question': 'Diketahui A = i + 2j + 3k dan B = 2i + 4j + 6k. Tentukan perbandingan A : B dan hubungan arah keduanya.',
        'choices': ['1:√2,sembarang', '1:2,tegak lurus', '1:2,searah', '1:1,berlawanan arah'],
        'answer': 2
    },
    {
        'question': 'Jika vektor A dan B memiliki panjang masing-masing 10 dan 5, dan sudut di antara keduanya adalah 120°, maka perbandingan besar A + B dan A - B adalah...',
        'choices': [' 1 : √3', ' √3 : √7 ', '1 : 2', '2 : 1'],
        'answer': 1
    },
    {
        'question': 'Vektor A dan B berada di bidang dan diketahui |A| = |B| = a, sudut antara A dan B adalah θ. Berapa perbandingan panjang dari A + B dan A - B?',
        'choices': ['cos(θ/2) : sin(θ/2)', 'sin(θ/2) : cos(θ/2)', 'tan(θ/2) : 1', '1 : tan(θ/2)'],
        'answer': 0
    },
    {
        'question': 'Diketahui vektor A = xi + yj dan B = yi - xj. Jika panjang A dan B sama, maka perbandingan x : y adalah...',
        'choices': ['1 : √3', '1 : 1', '2 : 1', '√2 : 1'],
        'answer': 1
    },
    {
        'question': 'Jika A dan B adalah dua vektor dengan panjang yang sama dan A + B tegak lurus A - B, maka sudut antara A dan B adalah...',
        'choices': [' 45°', ' 60°', '90°', '120°'],
        'answer': 2
    },
    {
        'question': 'Diberikan vektor A = ai + bj + ck dan B = bi + cj + ak. Jika A dan B searah, tentukan hubungan a, b, dan c.',
        'choices': ['a = b = c', 'a = b = -c', 'a² = b² = c²', 'a = c, b = c'],
        'answer': 2
    },
    {
        'question': 'Jika A = 3i + 4j dan B = pi + qj, dan diketahui sudut antara A dan B adalah 60°, serta panjang B = 5, maka nilai p dan q memenuhi...',
        'choices': ['3p + 4q = 12.5', '3p + 4q = 10', ' 3p + 4q = 7.5', '3p + 4q = 5'],
        'answer': 0
    },
    {
        'question': 'Diketahui A = ai + aj dan B = bi - bj. Jika A dan B tegak lurus, maka nilai perbandingan a : b adalah...',
        'choices': [' 1 : 0', '1 : -1', '-1 : 1', '1 : 1'],
        'answer': 3
    },
    {
        'question': 'Vektor A = 2i + 3j - k dan B = -4i - 6j + 2k. Maka perbandingan A : B adalah...',
        'choices': ['1 : -2', '-1 : 2', '1 : 2', 'A dan B tidak sebanding'],
        'answer': 0
    },
    
]

def get_questions(difficulty):
    if difficulty == 'easy':
        return questions_easy.copy()
    elif difficulty == 'medium':
        return questions_medium.copy()
    elif difficulty == 'hard':
        return questions_hard.copy()

def draw_car(x, y, image):
    screen.blit(image, (x, y))

def draw_track():
    # Load the background image
    background_image = pygame.image.load('jalan.png')  # Update with your image path
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Scale the image to fit
    # Draw the background image
    screen.blit(background_image, (0, 0))  
    lane_y1 = HEIGHT // 2
    lane_y2 = 2 * HEIGHT // 2
    # Define the position for the finish line
    finish_x = WIDTH
    # Draw the finish line
    for i in range(WIDTH // 20):
        color = BLACK if i % 2 == 0 else WHITE
        pygame.draw.rect(screen, color, (900, i * 15, 20, 15))
        # Draw long rectangles at the top and bottom
        pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, 190))  # Top rectangle
        pygame.draw.rect(screen, BLACK, (0, HEIGHT - 170, WIDTH, 200))  # Bottom rectangle
        pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, 180))  # Top rectangle
        pygame.draw.rect(screen, WHITE, (0, HEIGHT - 160, WIDTH, 200))  # Bottom rectangle
    return finish_x
    
def draw_question(qdata):
    question = qdata['question']
    choices = qdata['choices']
    question_surface = QUESTION_FONT.render(question, True, BLACK)
    # Define maximum line width
    max_line_width = 850
    # Function to wrap text into multiple lines
    def wrap_text(text, font, max_width):
        lines = []
        current_line = ''
        for word in text.split(' '):
            test_line = f"{current_line} {word}".strip()
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)
        
        return lines
    for i, line in enumerate(wrap_text(question, QUESTION_FONT, max_line_width)):
        screen.blit(QUESTION_FONT.render(line, True, BLACK), (10, 10 + i * 25))

    for i, choice in enumerate(choices):
        choice_text = f"{chr(65 + i)}. {choice}"
        screen.blit(ANSWER_FONT.render(choice_text, True, BLACK), (20, -20 + (i + len(choices)) * 25))
    instr1 = "Player 1: Pencet 1-4 buat jawab"
    instr2 = "Player 2: Pencet 6-9 buat jawab"
    screen.blit(INSTR_FONT.render(instr1, True, RED), (WIDTH - 330, 550))
    screen.blit(INSTR_FONT.render(instr2, True, BLUE), (WIDTH - 330, 570))

def starting_screen():
    # First select difficulty
    difficulties = ['Easy', 'Medium', 'Hard']
    selected = 1  # Start with Medium selected
    selecting = True

    while selecting:
        screen.fill(DARK_GRAY)
        title_surf = TITLE_FONT.render("Balapan Mobil Vektor", True, YELLOW)
        screen.blit(title_surf, (WIDTH // 2 - title_surf.get_width() // 2, 30))

        instr_surf = INSTR_FONT.render("Pilih Tingkat Kesulitan (Gunakan tombol panah Kiri/Kanan, Enter untuk konfirmasi)", True, WHITE)
        screen.blit(instr_surf, (WIDTH // 2 - instr_surf.get_width() // 2, 100))

        # Draw difficulty options
        total_width = 0
        diff_surfs = []
        spacing = 50
        for diff in difficulties:
            surf = WINNER_FONT.render(diff, True, WHITE)
            diff_surfs.append(surf)
            total_width += surf.get_width() + spacing
        total_width -= spacing  # remove last spacing

        start_x = WIDTH // 2 - total_width // 2
        for i, surf in enumerate(diff_surfs):
            x = start_x + sum(s.get_width() + spacing for s in diff_surfs[:i])
            color = GREEN if i == selected else WHITE
            outline_rect = pygame.Rect(x - 10, 150, surf.get_width() + 20, surf.get_height() + 10)
            pygame.draw.rect(screen, DARK_GRAY if i == selected else GRAY, outline_rect)
            pygame.draw.rect(screen, color, outline_rect, 2 if i == selected else 1)
            screen.blit(surf, (x, 160))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected = (selected - 1) % len(difficulties)
                elif event.key == pygame.K_RIGHT:
                    selected = (selected + 1) % len(difficulties)
                elif event.key == pygame.K_RETURN:
                    selecting = False

    # After difficulty selected, get the names
    input_boxes = {'Player 1': '', 'Player 2': ''}
    active_box = 'Player 1'
    waiting_for_start = True

    while waiting_for_start:
        screen.fill(DARK_GRAY)
        title_surf = TITLE_FONT.render("Balapan Mobil Vektor", True, YELLOW)
        screen.blit(title_surf, (WIDTH // 2 - title_surf.get_width() // 2, 30))

        # Show selected difficulty
        diff_text = f"Difficulty: {difficulties[selected]}"
        diff_surf = INSTR_FONT.render(diff_text, True, WHITE)
        screen.blit(diff_surf, (WIDTH // 2 - diff_surf.get_width() // 2, 90))

        instr_surf = INSTR_FONT.render(
            "Ketik nama pemain dan tekan Enter untuk memulai", True, WHITE
        )
        screen.blit(instr_surf, (WIDTH // 2 - instr_surf.get_width() // 2, 120))

        y_start = 160
        for idx, (label, name) in enumerate(input_boxes.items()):
            label_surf = INSTR_FONT.render(f"{label} Name:", True, RED if label == 'Player 1' else BLUE)
            screen.blit(label_surf, (WIDTH // 2 - 150, y_start + idx * 70))
            rect = pygame.Rect(WIDTH // 2 - 20, y_start + idx * 70 - 5, 300, 40)
            pygame.draw.rect(screen, WHITE if active_box == label else GRAY, rect, 0)
            pygame.draw.rect(screen, BLACK, rect, 2)

            # Render the name inside the box
            text_surf = INPUT_FONT.render(name, True, BLACK)
            screen.blit(text_surf, (rect.x + 5, rect.y + 5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    # Toggle active box
                    active_box = 'Player 2' if active_box == 'Player 1' else 'Player 1'
                elif event.key == pygame.K_BACKSPACE:
                    input_boxes[active_box] = input_boxes[active_box][:-1]
                elif event.key == pygame.K_RETURN:
                    # Start game if both names given
                    if input_boxes['Player 1'].strip() and input_boxes['Player 2'].strip():
                        return input_boxes['Player 1'].strip(), input_boxes['Player 2'].strip(), difficulties[selected].lower()
                else:
                    # Limit name length
                    if len(input_boxes[active_box]) < 15:
                        if event.unicode.isprintable():
                            input_boxes[active_box] += event.unicode

        pygame.display.flip()
        pygame.time.Clock().tick(30)

def countdown():
    count_font = WINNER_FONT
    for count in range(3, 0, -1):
        screen.fill(GRAY)
        count_surf = count_font.render(str(count), True, YELLOW)
        screen.blit(count_surf, (WIDTH // 2 - count_surf.get_width() // 2, HEIGHT // 2 - count_surf.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(1000)
    # Show "Go!"
    screen.fill(GRAY)
    go_surf = count_font.render("Go!", True, GREEN)
    screen.blit(go_surf, (WIDTH // 2 - go_surf.get_width() // 2, HEIGHT // 2 - go_surf.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(1000)


def main():
    # Start screen: get player names and difficulty
    player1_name, player2_name, difficulty = starting_screen()

    questions = get_questions(difficulty)
    random.shuffle(questions)

    clock = pygame.time.Clock()
    run = True

    p1_x = START_X
    p2_x = START_X

    p1_speed = BASE_SPEED
    p2_speed = BASE_SPEED

    p1_laps = 0
    p2_laps = 0
    TOTAL_LAPS = 10

    q_index = 0

    waiting_for_answer = True
    answer_submitted = False
    first_answerer = None
    first_answer_correct = False

    feedback_time = 0
    feedback_duration = 2
    feedback_message = ""
    feedback_color = BLACK

    finish_x = draw_track()
    winner = None

    countdown()

    while run:
        clock.tick(30)
        screen.fill(GRAY)
        finish_x = draw_track()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and waiting_for_answer:
                if event.key in P1_KEYS and not answer_submitted:
                    answer_index = P1_KEYS.index(event.key)
                    first_answerer = 1
                    if answer_index == questions[q_index]['answer']:
                        first_answer_correct = True
                        p1_speed = BASE_SPEED + SPEED_UP
                        feedback_message = f"{player1_name} Benar! Speed diboost"
                        feedback_color = GREEN
                    else:
                        first_answer_correct = False
                        p1_speed = max(0, BASE_SPEED - SPEED_DOWN)
                        feedback_message = f"{player1_name} Salah! Speed dikurangi"
                        feedback_color = RED
                    answer_submitted = True
                    feedback_time = time.time()

                elif event.key in P2_KEYS and not answer_submitted:
                    answer_index = P2_KEYS.index(event.key)
                    first_answerer = 2
                    if answer_index == questions[q_index]['answer']:
                        first_answer_correct = True
                        p2_speed = BASE_SPEED + SPEED_UP
                        feedback_message = f"{player2_name} Benar! Speed diboost"
                        feedback_color = GREEN
                    else:
                        first_answer_correct = False
                        p2_speed = max(0, BASE_SPEED - SPEED_DOWN)
                        feedback_message = f"{player2_name} Salah! Speed dikurangi"
                        feedback_color = RED
                    answer_submitted = True
                    feedback_time = time.time()

        p1_x += p1_speed
        p2_x += p2_speed

        if winner is None:
            if p1_x + CAR_WIDTH >= finish_x:
                p1_laps += 1
                p1_x = START_X
            if p2_x + CAR_WIDTH >= finish_x:
                p2_laps += 1
                p2_x = START_X
            if p1_laps >= TOTAL_LAPS:
                winner = 1
            elif p2_laps >= TOTAL_LAPS:
                winner = 2

        # Draw cars using images
        draw_car(p1_x, PLAYER1_Y, car_red_image)
        draw_car(p2_x, PLAYER2_Y, car_blue_image)

        # Display player names and laps
        p1_lap_text = INSTR_FONT.render(f"{player1_name}: Laps {p1_laps}/{TOTAL_LAPS}", True, RED)
        p2_lap_text = INSTR_FONT.render(f"{player2_name}: Laps {p2_laps}/{TOTAL_LAPS}", True, BLUE)
        screen.blit(p1_lap_text, (20, HEIGHT - 60))
        screen.blit(p2_lap_text, (20, HEIGHT - 30))

        if waiting_for_answer and q_index < len(questions):
            draw_question(questions[q_index])

        if answer_submitted:
            time_passed = time.time() - feedback_time
            feedback_surf = RESULT_FONT.render(feedback_message, True, feedback_color)
            screen.blit(feedback_surf, (WIDTH // 2 - feedback_surf.get_width() // 2, HEIGHT // 2 - 40))
            if time_passed > feedback_duration:
                q_index += 1
                answer_submitted = False
                waiting_for_answer = True
                first_answerer = None
                first_answer_correct = False
                p1_speed = BASE_SPEED
                p2_speed = BASE_SPEED
                if q_index >= len(questions):
                    waiting_for_answer = False

        if winner is not None:
            waiting_for_answer = False
            winner_name = player1_name if winner == 1 else player2_name
            winner_text = f"{winner_name} MENANG!"

            winner_surf = WINNER_FONT.render(winner_text, True, YELLOW)
            screen.blit(winner_surf, (WIDTH // 2 - winner_surf.get_width() // 2, HEIGHT // 2 + 20))

            instr_restart = "Tekan R untuk Memulai Ulang atau Q untuk Keluar"
            instr_surf = INSTR_FONT.render(instr_restart, True, BLACK)
            screen.blit(instr_surf, (WIDTH // 2 - instr_surf.get_width() // 2, HEIGHT // 2 + 70))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                # Restart everything including names and difficulty prompt
                main()
                return
            if keys[pygame.K_q]:
                run = False
                pygame.quit()
                sys.exit()

        pygame.display.flip()

if __name__ == "__main__":
    main()

