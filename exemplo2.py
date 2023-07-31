from collections.abc import Callable, Iterable, Mapping
from threading import Thread
from typing import Any
import sys
#diagramas UML  = diagrama de classes


class ProcessadorImpressao(Thread):
    def __init__(self, numeroThread):
        Thread.__init__(self)
        self.numero = numeroThread
    def run(self):
        sys.stdout.write(str(self.numero))
        sys.stdout.flush()
for i in range(1, 11):
    Thread = ProcessadorImpressao(i)
    thread.start()

