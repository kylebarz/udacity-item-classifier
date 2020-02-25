from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile


download_url = 'https://productid.azurewebsites.net/static/model_download/checkpoint-19.zip'
with urlopen(download_url) as zipresp:
    with ZipFile(BytesIO(zipresp.read())) as zfile:
        zfile.extractall('model/')
print('Model Download Complete')