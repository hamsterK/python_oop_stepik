class Pagination:
    def __init__(self, data, page_size):
        self.data = data
        self.page_size = page_size
        self.current_page = 1
        self.total_pages = (len(data) + page_size - 1) // page_size  # Определение общего количества страниц

    def get_visible_items(self):
        start_idx = (self.current_page - 1) * self.page_size
        end_idx = start_idx + self.page_size
        return self.data[start_idx:end_idx]

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
        return self

    def next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
        return self

    def first_page(self):
        self.current_page = 1
        return self

    def last_page(self):
        self.current_page = self.total_pages
        return self

    def go_to_page(self, page_num):
        if page_num < 1:
            self.current_page = 1
        elif page_num > self.total_pages:
            self.current_page = self.total_pages
        else:
            self.current_page = page_num
        return self



alphabet = list('abcdefghijklmnopqrstuvwxyz')

pagination = Pagination(alphabet, 4)
print(pagination.get_visible_items())
print(pagination.total_pages)
print(pagination.current_page)
