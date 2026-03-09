import subprocess

class CommandRunner:

    def run_cmd(self):
        result = subprocess.run("echo 1>/tmp/1", shell=True, capture_output=True, text=True)
        return result.stdout
