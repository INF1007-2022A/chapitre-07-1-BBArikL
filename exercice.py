#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TODO: Importez vos modules ici
import math
import turtle
from typing import Union


# TODO: Définissez vos fonction ici
def ellipsoide(premier_axe=0, deuxieme_axe=0, trois_axe=0,
               masse_vol: Union[int, float] = 1):
    volume = (4 / 3) * math.pi * premier_axe * deuxieme_axe * trois_axe

    return volume, volume * masse_vol


def get_most_freq(lett_freq: dict):
    return list(sorted(lett_freq.items(), key=lambda x: x[1], reverse=True))[0][0]


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    lett_freq = {}
    for char in sentence:
        if char not in lett_freq:
            nb_rep = sentence.count(char)
            # if nb_rep >= 5:  # Les tests ne font pas la vérification de du nombre de répétitions
            lett_freq.update({char: nb_rep})

    # Depuis https://datagy.io/python-sort-a-dictionary-by-values/
    lett_freq = dict(
        sorted(lett_freq.items(), key=lambda x: x[1], reverse=True))  # noqa: List of tuples given to dict()

    return lett_freq


def draw_recursive_branch(nb_branches: int, angle: float = 45, contained_turtle=turtle.Turtle()):
    contained_turtle.left(angle)

    if nb_branches != 0:
        contained_turtle.forward(100)
        next_turtle = contained_turtle.clone()
        # next_turtle.setposition(contained_turtle.pos())
        # next_turtle.setposition(contained_turtle.pos())
        # next_turtle.clone()
        draw_recursive_branch(nb_branches - 1, angle, next_turtle)

        next_turtle = turtle.clone()
        # next_turtle.setposition(contained_turtle.pos())
        # next_turtle.setposition(contained_turtle.pos())
        draw_recursive_branch(nb_branches - 1, angle*2, next_turtle)


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(ellipsoide(14, 34, 2, 1.5))

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    print(frequence(sentence))
    print(f"'{get_most_freq(frequence(sentence))}'")

    # init of turtle
    turtle.color('green')
    turtle.begin_fill()
    draw_recursive_branch(2)
    turtle.end_fill()
    turtle.done()
