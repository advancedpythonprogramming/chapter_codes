class Browser:

    def __init__(self, current_url='http://www.google.com'):
        self.__urls_stack = []
        self.__current_url = current_url

    def __load_url(self, url):
        self.__current_url = url
        print('loading url: {0}'.format(url))

    def go(self, url):
        self.__urls_stack.append(self.__current_url)
        print('go ->', end=' ')
        self.__load_url(url)

    def back(self):
        last_url = self.__urls_stack.pop()
        print('back->', end=' ')
        self.__load_url(last_url)

    def show_current_url(self):
        print('Current URL: {0}'.format(self.__current_url))


if __name__ == '__main__':
    chrome = Browser()
    chrome.go('http://www.uc.cl')
    chrome.go('http://www.uc.cl/en/courses')
    chrome.go('http://www.uc.cl/es/doctorado')

    chrome.show_current_url()
    chrome.back()
    chrome.show_current_url()
