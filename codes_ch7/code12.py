def run(self):
    with MyThread.lock:
        self.file.write(
            'This line was written by thread #{}\n'.format(self.i))
