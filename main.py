from Grid import *


# Draw all the pixels gave in grid
def draw_points(win, grid):
    for pixel in grid:
        pixel.point.draw(win)


def bubble_sort(win, grid, txt):
    swap = 0
    n = len(grid.pixel_grid)

    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            no_swapped = True
            txt.setText("swap=%d" % swap)
            if grid.pixel_grid[j].value > grid.pixel_grid[j + 1].value:
                grid.pixel_grid[j], grid.pixel_grid[j + 1] = grid.pixel_grid[j + 1], grid.pixel_grid[j]
                swap += 1
                grid.pixel_grid[j].point.x = grid.pixel_grid[j].point.y = j
                grid.pixel_grid[j + 1].point.x = grid.pixel_grid[j + 1].point.y = j + 1

                already_sorted = False
                no_swapped = False

            if i == 0:
                grid.pixel_grid[j].point.undraw()
                if no_swapped:
                    grid.pixel_grid[j].point.x = grid.pixel_grid[j].point.y = j
                grid.pixel_grid[j].point.draw(win)

                if j == n - i - 2:
                    if no_swapped:
                        grid.pixel_grid[j + 1].point.x = grid.pixel_grid[j + 1].point.y = j + 1
                    grid.pixel_grid[j + 1].point.undraw()
                    grid.pixel_grid[j + 1].point.draw(win)
            else:
                if not no_swapped:
                    grid.pixel_grid[j].point.move(-1, -1)
                    grid.pixel_grid[j + 1].point.move(1, 1)

        if already_sorted:
            break


def main():
    # One of the 2 dimension of the window. (Window must be a square)
    square_size = int(input('Insert one dimension of the square: '))

    # Window settings
    win = GraphWin('Sorter', square_size, square_size)
    win.setBackground('black')

    # Text settings
    txt = Text(Point((square_size / 2) + (square_size / 4), 20), "swap=0")
    txt.setTextColor('white')
    txt.draw(win)
    txt_for_pause = Text(Point(square_size/2, square_size/2), 'Click on the screen to start')
    txt_for_pause.setTextColor('white')

    # Grid settings
    grid = Grid(square_size)
    grid.shuffle()

    # Draws all the point on the canvas
    draw_points(win, grid.pixel_grid)

    # Draws a text befor starting the sort
    txt_for_pause.draw(win)
    win.getMouse()
    txt_for_pause.undraw()

    # Starts the bubble sorting
    bubble_sort(win, grid, txt)

    # Wait for user input
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
