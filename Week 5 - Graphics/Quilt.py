from graphics import Canvas

PATCH_SIZE = 100
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 200

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Milestone 2: Drawing the first row (Top Row)
    draw_square_patch(canvas, 0, 0)
    draw_circle_patch(canvas, 100, 0)
    draw_square_patch(canvas, 200, 0)
    draw_circle_patch(canvas, 300, 0)
    
    # Milestone 2: Drawing the second row (Bottom Row)
    # Note that the patches swap positions here
    draw_circle_patch(canvas, 0, PATCH_SIZE)
    draw_square_patch(canvas, 100, PATCH_SIZE)
    draw_circle_patch(canvas, 200, PATCH_SIZE)
    draw_square_patch(canvas, 300, PATCH_SIZE)

# Milestone 1: Defining the Circle Patch
def draw_circle_patch(canvas, start_x, start_y):
    """
    Draws a salmon-colored circle that fills the 100x100 patch area.
    """
    # The circle fills the patch, so the diameter is PATCH_SIZE
    canvas.create_oval(
        start_x, 
        start_y, 
        start_x + PATCH_SIZE, 
        start_y + PATCH_SIZE, 
        'salmon'
    )

def draw_square_patch(canvas, start_x, start_y):
    # draws a purple frame at (start_x, start_y)
    # Outer purple square
    canvas.create_rectangle(
        start_x, 
        start_y, 
        start_x + PATCH_SIZE, 
        start_y + PATCH_SIZE, 
        'purple'
    )
    # Inner white square (to create the "frame" look)
    inset = 20
    canvas.create_rectangle(
        start_x + inset, 
        start_y + inset, 
        start_x + PATCH_SIZE - inset, 
        start_y + PATCH_SIZE - inset, 
        'white'
    )

if __name__ == '__main__':
    main()