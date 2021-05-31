# -*- coding: utf-8 -*-
"""
Created on Fri May 28 16:30:48 2021

@author: 91860
"""
def game():
    import random
    play=print("do you want to play random 8? Y or N")
    play=input()
    future={"1":"be careful","2":"things will be fine","3":"be watchful","4":"You are the best"}
    play="y"
    while play=="y":
        rand_num=random.randint(1,4)
        convert=str(rand_num)
        print("("+convert+")-"+future[convert])
        print("do you want to play again? y or n")
        answer=input()
        if answer=="n":
            print("thanks for playing")
            break
            
        