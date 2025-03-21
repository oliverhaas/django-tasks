from django.dispatch import Signal

task_enqueued = Signal()
task_started = Signal()
task_finished = Signal()
