"""
Handler to retrieve the usage
"""

import json
from os.path import splitext, basename

import psutil
from notebook.base.handlers import IPythonHandler


class ResourceUsageHandler(IPythonHandler):

    def get(self):
        kernel = self.get_argument('kernel', '')
        nb_processes = self.get_notebook_processes()
        resource_data = {'cpu': None, 'mem': None}
        for process in nb_processes:
            kernel_name = self.get_kernel_name(process)
            if kernel_name == kernel:
                resource_data = {
                    'cpu': process.cpu_percent(),
                    'mem': process.memory_info().rss,
                    'total_mem': psutil.virtual_memory().total
                }
        self.write(json.dumps(resource_data))

    def get_kernel_name(self, process):
        """
        gets the kernel id from a process
        """
        for arg in process.cmdline():
            if arg.endswith('.json') and '/kernel-' in arg:
                return splitext(basename(arg).replace('kernel-', ''))[0]

    def get_notebook_processes(self):
        def filter_notebook_process(process):
            """
            Is the process an IPython notebook process
            """
            if 'python' in process.name().lower():
                for arg in process.cmdline():
                    if arg.endswith('.json') and '/kernel-' in arg:
                        return True
        return list(filter(filter_notebook_process, psutil.process_iter()))
