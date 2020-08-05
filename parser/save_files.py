import os
import urllib3
from MSFO_links import get_MSFO_links
from threading import Thread

class DownloadThread(Thread):
    """
    Загрузка файлов csv
    """

    def __init__(self, url, name):
        """Инициализация потока"""
        Thread.__init__(self)
        self.name = name
        self.url = url

    def run(self):
        """Запуск потока"""
        handle = urllib3.urlopen(self.url)
        fname = os.path.basename(self.url)

        with open(fname, "wb") as f_handler:
            while True:
                chunk = handle.read(1024)
                if not chunk:
                    break
                f_handler.write(chunk)

        msg = "%s закончил загрузку %s!" % (self.name, self.url)
        print(msg)


def main(urls):
    """
    Run the program
    """
    for item, url in enumerate(urls):
        name = "Поток %s" % (item+1)
        thread = DownloadThread(url, name)
        thread.start()

if __name__ == "__main__":
    urls = get_MSFO_links()

    main(urls)
    