# lichess 

## Table Of Contents
- [Purpose](#purpose)
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [How To Use](#how-to-use)

## Purpose
Purpose of this tool is to provide assistance in preparation for a chess game.

## Introduction
This project uses ```lichess``` and ```python-lichess``` python libraries to communicate with 
lichess API and obtain user infromation, such as user rating, games played, it's moves and so on.\
\
Main functionality is to get a certain number of user's games, and count how many lost and won games are there.
Then, output the openings which user has lost the most games to, and also which openings user plays most oftenly.\
\
This information can be used to prepare for the game with this player.

## Prerequisites
Install ```lichess``` and ```python-lichess``` python libraries:  
```
python3 -m pip install lichess pyhton-lichess
```

## How To Use
- Run main script:
```
python3 main.py
```
- input information: user's lichess nickname
- input information: desired time control
- input information: amount of games to count in analysis
- view results
