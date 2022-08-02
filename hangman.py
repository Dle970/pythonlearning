import random

HANGMANPICS = ['''



 +---+

 |   |

     |

     |

     |

     |

=========''', '''



 +---+

 |   |

 O   |

     |

     |

     |

=========''', '''



 +---+

 |   |

 O   |

 |   |

     |

     |

=========''', '''



 +---+

 |   |

 O   |

/|   |

     |

     |

  =========''', '''



 +---+

 |   |

 O   |

/|\  |

     |

     |

=========''', '''



 +---+

 |   |

 O   |

/|\  |

/    |

     |

=========''', '''



 +---+

 |   |

 O   |

/|\  |

/ \  |

     |

=========''']

words = 'ant badger bat bear deer dog random elephant'.split()

def get_random_word(any_word_list):
    return random.choice(any_word_list)

def display_board(hangman_pics, missed_letters, correct_letters, secret_word):
    print(hangman_pics[len(missed_letters)]) # assuming that you can only get 6 letters wrong?
    print()

    print("Missed Letters: ", end = " ")

    for letter in missed_letters:
        print(letter, end = " ")
    print()
    print()

print("Hangman")

missed_letters = ""
correct_letters = ""
secret_word = get_random_word(words)
game_is_done = False

while True:
    display_board(HANGMANPICS, missed_letters, correct_letters, secret_word)
    break