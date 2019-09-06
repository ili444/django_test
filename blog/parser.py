import re
import time
from datetime import datetime
from .models import Post
from django.http import Http404, HttpResponse
from urllib.request import urlopen, URLError
from threading import Thread
from queue import Queue

class ParserThread(Thread):

    def __init__(self, queue, shift):
        """Инициализация потока"""
        Thread.__init__(self)
        self.queue = queue
        self.shift = shift

    def run(self):
        """Запуск потока"""
        while True:
            # Получаем url из очереди
            url = self.queue.get()
            data = Post.objects.filter(url=url).values()[0]
            time.sleep(self.shift)
            try:
                date = parse_url(url)
                update_db(date)
            except URLError:
                parsed = {'success': False, 'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                data.update(parsed)
            # Отправляем сигнал о том, что задача завершена
            self.queue.task_done()



#Запускаем парсер
def start(request):
        data = Post.objects.all().order_by('timeshift').values()
        # генерируем словарь
        timeshifts = {d['timeshift']: [a['url'] for a in data if a['timeshift'] == d['timeshift']] for d in data}
        # создаем потоки и очередь
        date = parse(timeshifts)
        return date


def parse(timeshifts):

    queue = Queue()


    for shift in sorted(timeshifts):
        for url in timeshifts[shift]:
            t = ParserThread(queue, shift)
            t.setDaemon(True)
            t.start()
            queue.put(url)

    queue.join()
    return 'ok'



def parse_url(url):
        html = str(urlopen(str(url)).read().decode('utf-8'))
        title = re.findall(r'<title>(.*?)</title>', html)
        h1 = re.findall(r'<h1>(.*?)</h1>', html)
        encode = re.findall(r'<meta.*charset=(.*?)>', html)
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        parse_result = {
                'url': str(url),
                'title': title[0],
                'h1': h1[0] if len(h1) > 0 else None,
                'encode': encode[0].replace('"', '') if len(encode) > 0 else None,
                'time': str(time),
                'success': True,
            }
        return parse_result

# обновляем url
def update_db(data):
    Post.objects.filter(url=data['url']).update(title=data['title'],
                                                h1=data['h1'],
                                                encode=data['encode'],
                                                success=data['success'],
                                                time=data['time'])

