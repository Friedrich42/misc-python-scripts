from random import choice

ppl = ["Name1", "Name2"] * 100

while True:
    p1 = choice(ppl)
    p2 = choice(ppl)

    if not p1 == p2:
        print(p1, " => ", p2)
        break
