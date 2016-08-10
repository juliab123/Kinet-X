V = ["a", "i", "e", "o", "u"]
def piglatin (AB):
    if AB[0] in V:
        return AB + "way"
    else:
        if AB[1] in V:
            return AB[1:]+ AB[:1] +"ay"
        else:
            return AB[2:]+ AB[:2] + "ay"

print piglatin("cream")
        
