from graphics import Canvas

# The width of the canvas 
CANVAS_WIDTH = 450
# The height of the canvas 
CANVAS_HEIGHT = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # We draw a red rectangle for the top half of the flag.
    # Left_x starts at 0.
    # Top_y starts at 0.
    # Right_x goes to the full width (450).
    # Bottom_y goes to half the height (150).
    canvas.create_rectangle(
        0, 
        0, 
        CANVAS_WIDTH, 
        CANVAS_HEIGHT / 2, 
        'red'
    )

if __name__ == '__main__':
    main()