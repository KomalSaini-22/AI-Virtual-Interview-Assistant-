# utils/score.py

# def calculate_score(answer):
#     if len(answer) > 100:
#         return 10
#     elif len(answer) > 50:
#         return 8
#     elif len(answer) > 20:
#         return 6
#     else:
#         return 3

def calculate_score(answer):

    words = len(answer.split())

    if words >= 80:

        return 10

    elif words >= 50:

        return 8

    elif words >= 25:

        return 6

    else:

        return 4