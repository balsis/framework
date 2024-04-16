class SortablePageLocators:
    TAB_LIST = ("xpath", "//a[@id='demo-tab-list']")
    LIST_ITEM = (
    "xpath", "//div[@class='vertical-list-container mt-4']/div[@class='list-group-item list-group-item-action']")
    TAB_GRID = ("xpath", "//a[@id='demo-tab-grid']")
    GRID_ITEM = ("xpath", "//div[@class='create-grid']/div[@class='list-group-item list-group-item-action']")


class SelectablePageLocators:
    TAB_LIST = ("xpath", "//a[@id='demo-tab-list']")
    LIST_ITEM = ("xpath", "//li[@class='mt-2 list-group-item list-group-item-action']")
    LIST_ITEM_ACTIVE = ("xpath", "//li[@class='mt-2 list-group-item active list-group-item-action']")
    TAB_GRID = ("xpath", "//a[@id='demo-tab-grid']")
    GRID_ITEM = ("xpath", "//li[@class='list-group-item list-group-item-action']")
    GRID_ITEM_ACTIVE = ("xpath", "//li[@class='list-group-item active list-group-item-action']")


class ResizablePageLocators:
    RESIZABLE_BOX_HANDLE = ("xpath", "//div[@id='resizableBoxWithRestriction']/span")
    RESIZABLE_BOX = ("xpath", "//div[@id='resizableBoxWithRestriction']")
    RESIZABLE_HANDLE = ("xpath", "//div[@id='resizable']/span")
    RESIZABLE = ("xpath", "//div[@id='resizable']")

class DroppablePageLocators:
    # Simple
    SIMPLE_TAB = ("xpath", "//a[@id='droppableExample-tab-simple']")
    DRAG_ME_SIMPLE = ("xpath", "//div[@id='draggable']")
    DROP_HERE_SIMPLE = ("xpath", "//div[@id='simpleDropContainer']/div[@id='droppable']")

    # Accept
    ACCEPT_TAB = ("xpath", "//a[@id='droppableExample-tab-accept']")
    ACCEPTABLE = ("xpath", "//div[@id='acceptable']")
    NOT_ACCEPTABLE = ("xpath", "//div[@id='notAcceptable']")
    DROP_HERE_ACCEPT = ("xpath", "//div[@id='acceptDropContainer']/div[@id='droppable']")

    # Prevent Propogation
    PREVENT_TAB = ("xpath", "//a[@id='droppableExample-tab-preventPropogation']")
    NOT_GREEDY_DROP_BOX_TEXT = ("xpath", '//div[@id="notGreedyDropBox"]/p')
    NOT_GREEDY_INNER_BOX = ("xpath", "//div[@id='notGreedyInnerDropBox']")
    GREEDY_DROP_BOX_TEXT = ("xpath", "//div[@id='greedyDropBox']/p")
    GREEDY_INNER_BOX = ("xpath", "//div[@id='greedyDropBoxInner']")
    DRAG_ME_PREVENT = ("xpath", "//div[@id='dragBox']")

    # Revert Draggable
    REVERT_TAB = ("xpath", "//a[@id='droppableExample-tab-revertable']")
    WILL_REVERT = ("xpath", "//div[@id='revertable']")
    NOT_REVERT = ("xpath", "//div[@id='notRevertable']")
    DROP_HERE_REVERT = ("xpath", "//div[@id='revertableDropContainer']/div[@id='droppable']")

class DraggablePageLocators:
    # Simple
    SIMPLE_TAB = ("xpath", "//a[@id='draggableExample-tab-simple']")
    DRAG_ME = ("xpath", "//div[@id='draggableExample-tabpane-simple']/div[@id='dragBox']")
    # Axis Restricted
    AXIS_TAB = ("xpath", "//a[@id='draggableExample-tab-axisRestriction']")
    ONLY_X = ("xpath", "//div[@id='restrictedX']")
    ONLY_Y = ("xpath", "//div[@id='restrictedY']")