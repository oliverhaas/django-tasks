from django.dispatch import Signal

task_enqueued = Signal()
task_starting = Signal()
task_finished = Signal()
