# ***The struggle itself toward the heights is enough to fill a man's heart. One must imagine Sisyphus happy.***
This is a repo for my side projects as I learn how to code in Python. I hope this serves as a time capsule for my learning progress.

## **SIDE PROJECTS**
### 1. 🥯 Sourdough Bagels 🥯
### 27/02/2026 ###
  First project I decided to hunker down and complete. I originally wanted to include more things like:  
    - Difficulty settings where harder difficulty includes a text version, increased digits and lesser guesses  
    - A scoreboard where players can earn points; the lesser guess required the more points earned.  
    - A 'store' where players can use the points to buy items to help guessing the more difficult versions. Things can include a max_guess extender.  
  However, even coding the bare basics of the game is difficult. I might revisti this at a later date.

  ### 01/03/2026 ###
  Revisited this project as I felt that it will be incomplete to move on to my next project without seeing the game to its completion. As I wanted a difficulty setting, I decided it will be best to include an Easy and Hard mode. Though the hard mode seems to require more balancing as apparently it is 47x harder than the standard mode:  
    - Included a settings option to allow player to select difficulties
      - Easy: 15 guesses with only 2 numeric digits
      - Hard: 7 guesses with 3 digits. Numbers and letters are included.
      - Included letters when checking for improper input in char_check()
      - Included letters in get_bagel when Hard difficulty is selected
    .
    With the difficulty settings included, I can deem the Sourdough Project as completed
