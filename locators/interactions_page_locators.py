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
