import file_watch
import os
import pytest
import subprocess
import time

def test_settings():
    """ Tests settings """
    os.environ['REMOTE_REDIS_HOST'] = "localhost"
    os.environ['REMOTE_REDIS_PORT'] = "6379"
    import settings

def test_file_queue():
    """ Tests simulation of new file """
    os.system('docker run -d alpine:3.5 /bin/sh -c "echo core hello world;"')
    os.system('docker run -d alpine:3.5 /bin/sh -c "echo core hello world;"')
    os.system('docker run -d alpine:3.5 /bin/sh -c "echo core hello world;"')
    time.sleep(5)
    file_watch.file_queue("/tmp")
    file_watch.file_queue("/dev/null")
    file_watch.file_queue("/dev/null", base_dir=os.getcwd()+"/")

def test_template_queue():
    """ Tests simulation of new/modified template """
    os.environ['HOSTNAME'] = "test"
    os.system('docker run -d alpine:3.5 /bin/sh -c "echo core hello world;"')
    os.system('docker run --name core-template-queue1 -d alpine:3.5 /bin/sh -c "while true; do echo core hello world; sleep 1; done"')
    os.system('docker run --name active-template-queue1 -d alpine:3.5 /bin/sh -c "while true; do echo core hello world; sleep 1; done"')
    os.system('docker run --name passive-template-queue1 -d alpine:3.5 /bin/sh -c "while true; do echo core hello world; sleep 1; done"')
    os.system('docker run --name visualization-template-queue1 -d alpine:3.5 /bin/sh -c "while true; do echo core hello world; sleep 1; done"')
    file_watch.template_queue("/dev/null")
    file_watch.template_queue("/modes.template")
    file_watch.template_queue("/core.template")
    file_watch.template_queue("/collectors.template")
    file_watch.template_queue("/visualization.template")

    os.environ['HOSTNAME'] = subprocess.check_output('docker run --name core-template-queue2 -d alpine:3.5 /bin/sh -c "while true; do echo core hello world; sleep 1; done"', shell=True)[:4]
    file_watch.template_queue("/core.template")
    os.environ['HOSTNAME'] = subprocess.check_output('docker run --name active-template-queue2 -d alpine:3.5 /bin/sh -c "while true; do echo core hello world; sleep 1; done"', shell=True)[:4]
    file_watch.template_queue("/collectors.template")
    os.environ['HOSTNAME'] = subprocess.check_output('docker run --name passive-template-queue2 -d alpine:3.5 /bin/sh -c "while true; do echo core hello world; sleep 1; done"', shell=True)[:4]
    file_watch.template_queue("/collectors.template")
    os.environ['HOSTNAME'] = subprocess.check_output('docker run --name visualization-template-queue2 -d alpine:3.5 /bin/sh -c "while true; do echo core hello world; sleep 1; done"', shell=True)[:4]
    file_watch.template_queue("/visualization.template")
