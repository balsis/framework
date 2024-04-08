from pages.interactions_page import SortablePage, SelectablePage


class TestSortablePage:
    def test_sortable(self, driver):
        sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
        sortable_page.open()
        list_before, list_after = sortable_page.change_list()
        grid_before, grid_after = sortable_page.change_grid()
        assert list_before != list_after, 'the order of the list has not been changed'
        assert grid_before != grid_after, 'the order of the grid has not been changed'


class TestSelectablePage:
    def test_selectable(self, driver):
        selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
        selectable_page.open()


