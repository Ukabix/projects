# źródło: https://www.youtube.com/watch?v=8lhxIOAfDss

def move(f, t):
    print("Move disc from {} to {}!".format(f,t))


def moveVia(f, v, t):
    move(f, v)
    move(v, t)
# moveVia("A", "B", "C")


# def foo(x):
#     foo(x)
#
# foo(3) # RecursionError: maximum recursion depth exceeded


# # ABC - słupki 1<2<3<4 - talerze
# # start A 4321 B C
# def hanoi(n, f, v, t): # number, fromA, viaB, targetC
#     hanoi(n-1, f, t, v) # przemieszczamy 123 na B przy pomocy C
# # A 4 B321 C
#     move(f, t) # przemieszczamy duży dysk na C
# # A B321 C4
#     hanoi(n-1, v, f, t) # przemieszczamy 123 na C przy pomocy A
# # A B C4321
#
# hanoi(3, "A", "B", "C") # RecursionError: maximum recursion depth exceeded - liczy dla ujemnej liczy dysków

# ABC - słupki 1<2<3<4 - talerze
# start A 4321 B C
def hanoi(n, f, v, t): # number, fromA, viaB, targetC
    if n == 0:
        pass
    else:
        hanoi(n-1, f, t, v) # przemieszczamy 123 na B przy pomocy C
# A 4 B321 C
        move(f, t) # przemieszczamy duży dysk na C
# A B321 C4
        hanoi(n-1, v, f, t) # przemieszczamy 123 na C przy pomocy A
# A B C4321

hanoi(3, "A", "B", "C") # bez RecursionError: maximum recursion depth exceeded
