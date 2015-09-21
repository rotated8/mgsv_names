import random, os

global adjectives, animals, rares

with open(os.path.join(os.path.dirname(__file__), 'adjectives.txt')) as f:
    adjectives = f.readlines()

with open(os.path.join(os.path.dirname(__file__), 'animals.txt')) as f:
    animals = f.readlines()

with open(os.path.join(os.path.dirname(__file__), 'rares.txt')) as f:
    rares = f.readlines()

uncommons = {
        # Adjectives:
        'master': 'miller',
        'raging': 'bull',
        'hidden': 'dragon',
        'humming': 'bird',
        'spicy': 'sandworm',
        # Animals:
        'ocelot': 'revolver',
        'lion': 'snooping',
        'tiger': 'crouching',
        'hippo': 'hungry',
        'falcon': 'punching',
}

def generate_name():
    adj = random.choice(adjectives).strip()
    anim = random.choice(animals).strip()

    r = random.random()
    if r < 0.001 or r >= 0.999:
        return random.choice(rares).strip()
    elif r < 0.3 and adj in uncommons:
        return ' '.join((adj, uncommons[adj]))
    elif r >= 0.7 and anim in uncommons:
        return ' '.join((uncommons[anim], anim))

    return ' '.join((adj, anim))

if __name__ == '__main__':
    print(generate_name())
