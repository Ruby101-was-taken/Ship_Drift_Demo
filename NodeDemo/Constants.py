import Types

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 700

GRID_SIZE = 100
GRID_LINE_WIDTH = 2

CONNECTING_LINE_WIDTH = 5

TYPE_COLOURS = {
    Types.NodeTypes.GOAL : (255, 255, 0),
    Types.NodeTypes.ENEMIES : (255, 0, 0),
    Types.NodeTypes.CLEAN_UP: (0, 255, 255),
    Types.NodeTypes.SPEED_SAIL: (0, 0, 255),
    Types.NodeTypes.BARRIER : (0, 0, 255),
    Types.NodeTypes.FISHERS : (255, 255, 255),
    Types.NodeTypes.SHOP : (255, 0, 255)
}