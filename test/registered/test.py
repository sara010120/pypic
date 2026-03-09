import subprocess

subprocess.run("ls -al", shell=True)
subprocess.run("echo 1 >/tmp/1", shell=True)

register_cuda_ci(stage-a-test-1,suite="stage-a-test-1")
