import os, base64, requests

API_KEY = os.getenv("README_API_KEY") or "rdme_xn8s9h9dcb4e2a4febc52b5a58b845a08a9c2cfb8c002d524550166287ad26e686527f"
VER     = os.getenv("README_VERSION", "latest")

s = requests.Session()
s.auth = (API_KEY, "")                      # Basic auth: username=API_KEY
# Không dùng header x-readme-version để thử
# Thử với API v2
# Thử với production API
url = "https://api.readme.com/v1.0/categories"

r = s.get(url, timeout=30)
print("Status:", r.status_code)
print("URL   :", url)
print("Hdrs  :", s.headers)
print("Body  :", r.text[:1000])
