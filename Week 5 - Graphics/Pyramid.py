from graphics import Canvas

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 300

# Constants for brick dimensions and base size
BRICK_WIDTH = 30
BRICK_HEIGHT = 12
BRICKS_IN_BASE = 14

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Outer loop: counts which row we are on (from 0 to BRICKS_IN_BASE - 1)
    for row in range(BRICKS_IN_BASE):
        
        # Number of bricks in the current row decreases as row index increases
        bricks_in_row = BRICKS_IN_BASE - row
        
        # Calculate the starting X for this row to keep it centered
        # We find the center of the canvas and subtract half the width of the row
        row_width = bricks_in_row * BRICK_WIDTH
        start_x = (CANVAS_WIDTH - row_width) / 2
        
        # Calculate the Y position (moving UP from the bottom)
        start_y = CANVAS_HEIGHT - (BRICK_HEIGHT * (row + 1))
        
        # Inner loop: draw each brick in the current row
        for i in range(bricks_in_row):
            x = start_x + (i * BRICK_WIDTH)
            y = start_y
            
            canvas.create_rectangle(
                x, 
                y, 
                x + BRICK_WIDTH, 
                y + BRICK_HEIGHT, 
                "yellow", 
                "black"
            )

if __name__ == '__main__':
    main()