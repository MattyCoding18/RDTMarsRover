
class Plateau:
    """Storing the maximum X and Y Axis for the Plateau"""
    def __init__(self, max_x, max_y):
        self.max_x = max_x # Highest X Coordinate allowed
        self.max_y = max_y # Highest Y Coordinate allowed

    def rover_within_bounds(self, x, y):
        """Returns True if x and y are greater than 0
        and less than the maximum size of Plateau"""
        return 0 <= x <= self.max_x and 0 <= y <= self.max_y


class Rover:
    """The Mars rover can move and rotated based on commands"""
    directions = ["N", "E", "S", "W"] # Directions list, handling left+right turns

    def __init__(self, plateau, x, y, direction):
        """Ensures that the Rover always starts at (0,0) and faces North"""
        self.plateau = plateau # So the rover knows the boundaries
        self.x = x # The rovers current X position
        self.y = y # The rovers current Y position
        self.direction = direction # Current direction rover is facing

    def move(self):
        """Moves the Rover forward the way it's facing, and if it's in boundary"""
        if self.direction == "N" and self.plateau.rover_within_bounds(self.x, self.y + 1):
            self.y += 1 # Moving up so increase y
        elif self.direction == "E" and self.plateau.rover_within_bounds(self.x + 1, self.y):
            self.x += 1 # Moving right so increase X
        elif self.direction == "S" and self.plateau.rover_within_bounds(self.x, self.y - 1):
            self.y -= 1 # Moving down so decrease Y
        elif self.direction == "W" and self.plateau.rover_within_bounds(self.x - 1, self.y):
            self.x -= 1 # Moving left so decrease X

    def move_left(self):
        """Rover rotates 90 degrees to the left, goes through directions list index - 1"""
        index = self.directions.index(self.direction) # Find what index the current direction is at
        new_index = (index - 1 ) % len(self.directions) # Move -1 index left
        self.direction = self.directions[new_index] # Update to the new direction


    def move_right(self):
        """Rover rotates 90 degrees to the right, goes through directions list index + 1"""
        index = self.directions.index(self.direction) # Find what index the current direction is at
        new_index = (index + 1) % len(self.directions) # Move +1 index right
        self.direction = self.directions[new_index] # Update to the new direction


    def execute_instructions(self, commands):
        for letter in commands:
            if letter.upper() == "M": # Rover move forward
                self.move()
            elif letter.upper() == "L": # Rover turn left
                self.move_left()
            elif letter.upper() == "R": # Rover turn right
                self.move_right()

        print(self.get_position()) # Prints final position after instructions

    def get_position(self):
        """Returns the Rover's final position and its direction as a string"""
        return f"{self.x} {self.y} {self.direction}"


def main():
    """Handles user input and runs the Rover"""

    # Get the plateau size input from user (Eg: "5 5")
    max_x, max_y = map(int, input("Enter the plateau size (max_x max_y): ").split())
    plateau = Plateau(max_x, max_y) # Create the plateau grid

    # Ask for the number of robots
    num_rovers = int(input("Enter the number of rovers: "))
    rovers = [] # Stores all the rovers and their movements

    # Loops through each rover
    for i in range(num_rovers):
        # Get Rover's starting position input (Eg: 1 1 N)
        x, y, direction = input("Enter the rover's starting position (x y direction) : ").split()
        x, y = int(x), int(y) # Converts to int

        # Gets movement instructions from user (Eg: "MRLMLRMML")
        commands = input("Enter the movement commands (L, R, M): ")

        # Create the Rover object, append to list as tuple
        rover = Rover(plateau, x, y, direction)
        rovers.append((rover, commands))

    # Goes through each rover one by one stored in the list
    for rover, commands in rovers:
        rover.execute_instructions(commands) # Executes the movement commands

if __name__ == "__main__":
    main()

