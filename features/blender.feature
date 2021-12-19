Feature: Blender

Scenario Outline: Blender function
   Given I put <thing> in a blender,
   When I switch the blender on
   Then it should transform into <other thing>

 Examples: things
   | thing   | other thing   |
   | ice     | crushed ice   |
   | avocado | not guacamole |
