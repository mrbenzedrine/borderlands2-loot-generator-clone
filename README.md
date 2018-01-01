# borderlands2-loot-generator-clone
Simplified clone of the procedural loot generator in Borderlands 2

## About
Borderlands 2 is an FPS-RPG hybrid game for Xbox 360/PS3/PC. One of its main features
is its loot based item system, where items / loot are procedurally generated. There are many variables
that determine an item's stats and characteristics and so this leads to a very large number of
different items if one takes into account all these variables. This project is an attempt to
mimic the procedural generation of items that is found in BL2.

Most of the information that was used to write this can be found in the [Borderlands wiki],
and also [this][Loot blog post] blog post by the creative and design director of BL2.

[Borderlands wiki]: http://borderlands.wikia.com/wiki/Borderlands_Wiki
[Loot blog post]: http://www.gearboxsoftware.com/2013/09/inside-the-box-the-borderlands-2-loot-system/

## Current state
In its current state this project has a basic foundation for generation of common rarity versions
of all the item types in BL2. It is however, lacking more features than it is providing; 
there is still Unique and Orange rarity / Legendary weapon generation, chest loot generation,
and perhaps most importantly, the mathematics behind the stats of all the items, to name a few, to
yet be implemented.

## Running
Simply using `python main.py` should do the trick.

## Tests
The built-in unittest module for Python has been used for unit testing in this project.

Note that all the following commands are for when the user is in the project root directory.
To run all tests use `python -m unittest discover`, to run all tests in a particular 
sub-directory of `tests` use `python -m unittest discover path_to_sub_directory`;
for example, to run all tests in the `tests/gear_tests/weapons_tests` sub-directory use 
`python -m unittest discover tests/gear_tests/weapon_tests`. Finally, to run a single test 
file use the command `python -m unittest path_to_test_file/test_file.py`.
