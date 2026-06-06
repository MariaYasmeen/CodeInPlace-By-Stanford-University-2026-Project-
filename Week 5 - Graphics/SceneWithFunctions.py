from graphics import Canvas

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Draw background elements
    draw_sun(canvas, 50, 50, "orange")
    
    # Call the cloud function with different positions and colors
    draw_cloud(canvas, 100, 80, "pink")
    draw_cloud(canvas, 220, 50, "salmon")
    draw_cloud(canvas, 350, 90, "purple")
    
    # Call the tree function in different locations and colors
    draw_tree(canvas, 80, 220, "green")
    draw_tree(canvas, 150, 230, "red")
    draw_tree(canvas, 350, 230, "orange")

def draw_tree(canvas, x, y, leaf_color):
    """
    Draws a tree at (x, y). 
    The leaf_color parameter controls the circle color.
    """
    # Draw trunk
    trunk_width = 20
    canvas.create_rectangle(x - 10, y, x + 10, y + 60, "brown")
    
    # Draw leaves (the circle)
    radius = 35
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, leaf_color)

def draw_cloud(canvas, x, y, color):
    """
    Draws a cloud made of three overlapping circles.
    """
    radius = 30
    # Left part of cloud
    canvas.create_oval(x, y, x + radius * 2, y + radius * 2, color)
    # Right part
    canvas.create_oval(x + 40, y, x + 40 + radius * 2, y + radius * 2, color)
    # Top part
    canvas.create_oval(x + 20, y - 25, x + 20 + radius * 2, y + radius * 2 - 25, color)

def draw_sun(canvas, x, y, color):
    """
    Draws a simple sun with a glow.
    """
    # Outer glow
    canvas.create_oval(x - 10, y - 10, x + 50, y + 50, "yellow")
    # Inner sun
    canvas.create_oval(x, y, x + 40, y + 40, color)

if __name__ == "__main__":
    main()