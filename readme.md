#A Metal Gear Solid-style code name generator.#

To generate a name, simply run mgsv\_names.py with Python 2.6, 2.7 or 3.0+

Sometimes, this will generate an 'uncommon' or even a 'rare' code name.

To add new names, you can edit the adjectives.txt, animals.txt, uncommons.txt, or rares.txt files.
In these files, lines beginning with a '#' are ignored. A ',' separates column values if multiple are used.

Then, run load\_db.py. That script generates the names.db file that the mgsv\_names.py script uses.
