from functools import partial
import os
import pygame
import pygame_menu
from pygame_menu.examples import create_example_window
from pygame_menu import sound
from typing import Tuple, Any, Optional, List
import k2
from k35 import play_k35_random
FPS = 60
WINDOW_SIZE = (1200, 800)

TYPE = ['RANDOM']
PLAYERS =['2P']
def on_button_click(value: str, text: Any = None) -> None:
    """
    Button event on menus.
    :param value: Button value
    :param text: Button text
    """
    if not text:
        print(f'Hello from {value}')
    else:
        print(f'Hello from {text} with {value}')


def paint_background(surface: 'pygame.Surface') -> None:
    """
    Paints a given surface with background color.
    :param surface: Pygame surface
    """
    bg = pygame.image.load("assets/pics/background.jpeg")
    bg = pygame.transform.scale(bg, (1200 ,800))
    surface.blit(bg,(0,00))
    

def change_type(value: Tuple[Any, int], type: str) -> None:
    """
    Change type of the simulation.

    :param value: Tuple containing the data of the selected object
    :param difficulty: Optional parameter passed as argument to add_selector
    """
    selected, index = value
    print(f'Selected type: "{selected}" ({type}) at index {index}')
    TYPE[0] = type

def change_players(value: Tuple[Any, int], type: str) -> None:
    """
    Change number of players for the simulation.

    :param value: Tuple containing the data of the selected object
    :param difficulty: Optional parameter passed as argument to add_selector
    """
    selected, index = value
    print(f'Selected type: "{selected}" ({type}) at index {index}')
    PLAYERS[0] = type

def play_k2(type: List, font: 'pygame.font.Font', test: bool = False) -> None:
    """
    k2 game function.

    :param difficulty: type of the game
    :param font: Pygame font
    :param test: Test method, if ``True`` only one loop is allowed
    """
    assert isinstance(type, list)
    type = TYPE[0]
    assert isinstance(type, str)

    # Define globals
    global main_menu
    global clock

    if type == 'RANDOM':
        f = font.render('Simulating random ', True, (255, 255, 255))
    elif type == 'BFS':
        f = font.render('Simulating bfs', True, (255, 255, 255))
    elif type == 'DFS':
        f = font.render('Simulating dfs', True, (255, 255, 255))
    else:
        raise ValueError(f'unknown type {type}')
    f_esc = font.render('Press ESC to open the menu', True, (255, 255, 255))
    


def make_long_menu() -> 'pygame_menu.Menu':
    """
    Create a long scrolling menu.
    :return: Menu
    """
    theme_menu = pygame_menu.themes.THEME_SOLARIZED.copy()
    theme_menu.scrollbar_cursor = pygame_menu.locals.CURSOR_HAND

    # Main menu, pauses execution of the application
    menu = pygame_menu.Menu(
        height=800,
        onclose=pygame_menu.events.EXIT,
        theme=theme_menu,
        title='Select Level',
        width=800
    )

    menu_k2 = pygame_menu.Menu(
        columns=1,
        height=800,
        onclose=pygame_menu.events.EXIT,
        rows=3,
        theme=pygame_menu.themes.THEME_DARK,
        title='Class K-2',
        width=800
    )
    # menu_k2 
    menu_k2.add.button('Start',  # When pressing return -> play(DIFFICULTY[0], font)
                         k2.play_k2_random,
                         TYPE,
                         pygame.font.Font(pygame_menu.font.FONT_FRANCHISE, 22))
    menu_k2.add.selector('Select Type of Simulation ',
                           [('Random', 'RANDOM'),
                            ('BREADTH FIRST SEARCH', 'BFS'),
                            ('DEPTH FIRST SEARCH', 'DFS')],
                           onchange=change_type,
                           selector_id='select_difficulty')
    #menu_k2.add.button('Another menu', play_submenu)
    menu_k2.add.button('Return to main menu', pygame_menu.events.BACK)

    menu_k35 = pygame_menu.Menu(
        height=800,
        onclose=pygame_menu.events.EXIT,
        theme=pygame_menu.themes.THEME_DARK,
        title='Class K-3 --> k-5',
        width=800
    )
    # menu_k2 
    menu_k35.add.button('Start',  # When pressing return -> play(DIFFICULTY[0], font)
                         play_k35_random,
                         PLAYERS,
                         TYPE,
                         pygame.font.Font(pygame_menu.font.FONT_FRANCHISE, 22))
    menu_k35.add.selector('Select number of players ',
                           [('2 Players', '2P'),
                            ('3 Players', '3P'),
                            ('4 Players', '4P')],
                           onchange=change_players,
                           selector_id='select_np')
    menu_k35.add.selector('Select level of Simulation ',
                           [('Random', 'RANDOM'),
                            ('BREADTH FIRST SEARCH', 'BFS'),
                            ('DEPTH FIRST SEARCH', 'DFS')],
                           onchange=change_type,
                           selector_id='select_difficulty')
    
    menu_k35.add.button('Return to main menu', pygame_menu.events.BACK)


    menu_k68 = pygame_menu.Menu(
        height=800,
        onclose=pygame_menu.events.EXIT,
        theme=pygame_menu.themes.THEME_DARK,
        title='Class k-6 --> k-8',
        width=800
    )
    # menu_k2 
    menu_k68.add.button('Start',  # When pressing return -> play(DIFFICULTY[0], font)
                         play_k35_random,
                         PLAYERS,
                         TYPE,
                         pygame.font.Font(pygame_menu.font.FONT_FRANCHISE, 22))
    menu_k68.add.selector('Select number of players ',
                           [('2 Players', '2P'),
                            ('3 Players', '3P'),
                            ('4 Players', '4P')],
                           onchange=change_players,
                           selector_id='select_np')
    menu_k68.add.selector('Select level of Simulation ',
                           [('Random', 'RANDOM'),
                            ('BREADTH FIRST SEARCH', 'BFS'),
                            ('DEPTH FIRST SEARCH', 'DFS')],
                           onchange=change_type,
                           selector_id='select_difficulty')
    menu_k68.add.button('Return to main menu', pygame_menu.events.BACK)

    menu.add.button('Class K-2', menu_k2)
    menu.add.button('Clas K-2 to K-5', menu_k35)
    menu.add.button('Class K-6 to K-8', menu_k68)
    menu.add.vertical_margin(20)  # Adds margin

    menu.add.button('Exit', pygame_menu.events.EXIT)

    return menu


def main(test: bool = False) -> None:
    """
    Main function.
    :param test: Indicate function is being tested
    """
    pygame.init()
    pygame.mixer.init()
    screen = create_example_window('Lost in the Woods', WINDOW_SIZE)
    music = pygame.mixer.music.load("assets/sound/bg_music.mp3")
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    menu = make_long_menu()

    # -------------------------------------------------------------------------
    # Main loop
    # -------------------------------------------------------------------------
    while True:

        # Tick
        clock.tick(FPS)

        # Paint background
        paint_background(screen)

        # Execute main from principal menu if is enabled
        menu.mainloop(
            surface=screen,
            bgfun=partial(paint_background, screen),
            disable_loop=test,
            fps_limit=FPS
        )
        engine = sound.Sound()
        engine.set_sound(sound.SOUND_TYPE_CLICK_MOUSE, 'click.mp3')
        engine.set_sound(sound.SOUND_TYPE_OPEN_MENU, 'open.mp3')

        menu = pygame_menu.Menu(...)
        menu.set_sound(engine, recursive=True)

        # Update surface
        pygame.display.flip()

        # At first loop returns
        if test:
            break


if __name__ == '__main__':
    main()