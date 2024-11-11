import json
import urllib
import tarfile
import requests

with open("packages.json") as f:
    data = json.load(f)

package_name = input("Enter the package name: ")

found = False
for package in data.get("packages", []):
    if package.get("name") == package_name:
        if "https" in package.get("url"):
            security = "secured / https"
        else:
            security="http"
        print(f"Downloading from {package_name}: {package.get('url')} |", security)
        urllib.request.urlretrieve(package.get("url"), package_name + ".tar.xz")
        print("Package retrieval successful.")
        tarfile_path = package_name + ".tar.xz"
        with tarfile.open(tarfile_path, 'r:xz') as tar:
            tar.extractall(path="packages")
        found = True
        break

if not found:
    print(f"Package named '{package_name}' not found.")
