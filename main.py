from Grid import *


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
            # time.sleep(0.01)
            if grid.pixel_grid[j].value > grid.pixel_grid[j + 1].value:
                grid.pixel_grid[j], grid.pixel_grid[j + 1] = grid.pixel_grid[j + 1], grid.pixel_grid[j]
                swap += 1
                grid.pixel_grid[j].point.x, grid.pixel_grid[j].point.y = j, j
                grid.pixel_grid[j + 1].point.x, grid.pixel_grid[j + 1].point.y = j + 1, j + 1

                already_sorted = False
                no_swapped = False

            if i == 0:
                grid.pixel_grid[j].point.undraw()
                if no_swapped:
                    grid.pixel_grid[j].point.x, grid.pixel_grid[j].point.y = j, j
                grid.pixel_grid[j].point.draw(win)

                if j == n - i - 2:
                    if no_swapped:
                        grid.pixel_grid[j + 1].point.x, grid.pixel_grid[j + 1].point.y = j + 1, j + 1
                    grid.pixel_grid[j + 1].point.undraw()
                    grid.pixel_grid[j + 1].point.draw(win)
            else:
                if not no_swapped:
                    grid.pixel_grid[j].point.move(-1, -1)
                    grid.pixel_grid[j + 1].point.move(1, 1)

        if already_sorted:
            break


def main():
    # Window settings
    win = GraphWin('Sorter', 500, 500)
    win.setBackground('black')

    # Text settings
    txt = Text(Point((500 / 2) + (500 / 4), 20), "swap=0")
    txt.setTextColor('white')
    txt.draw(win)

    grid = Grid(500)
    grid.shuffle()

    # Draws all the point on the canvas
    draw_points(win, grid.pixel_grid)

    # Starts the bubble sorting
    bubble_sort(win, grid, txt)
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
