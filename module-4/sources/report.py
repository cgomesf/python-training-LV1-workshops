class Page:
    def __init__(self, text):
        self.text = text

class Report:
    def __init__(self,filename):
        self.filename = filename
        self.page_num = 0
        self.page_list = []

    @classmethod
    def with_valid_extension(self,filename):
        correct_extension = ["pdf","txt"]
        if filename.split(".")[-1] in correct_extension:
            return self
        else:
            return None

    def add_page(self,page):
        self.page_list.append(page)
        self.page_num = self.page_num + 1

    def number_of_pages(self):
        return self.page_num

    def pages(self):
        return self.page_list

def main():
    page_1 = Page("First page")
    page_2 = Page("Second page")
    page_3 = Page("Third page")
    assert Report.with_valid_extension("test.invalid") is None
    assert Report.with_valid_extension("test.pdf") is not None
    assert Report.with_valid_extension("test.txt") is not None

    report = Report("valid_document.pdf")
    assert report.number_of_pages() == 0

    report.add_page(page_1)
    report.add_page(page_2)
    report.add_page(page_3)

    assert report.number_of_pages() == 3
    for page in report.pages():
      assert isinstance(page, Page)

    print("OK !")


if __name__ == "__main__":
    main()
