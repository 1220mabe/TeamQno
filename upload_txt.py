import os
import requests
from traceback import print_exc
from urllib.parse import urljoin

# credential
wp_base_url_ = "https://teamqno.work/wp/"
user_ = "qno"
pass_ = "3gBL 0aGm cKDt sHnB GC3v xPMO"
 
def upload_image(file_path):
    # check local file path
    if not os.path.isfile(file_path):
        raise Exception("invalid file path: {}".format(file_path))
    # build header
    file_name = os.path.basename(file_path)
    headers_ = {
        "Content-Disposition": 'attachment; filename="{}"'.format(file_name),
        "Content-Type": "application/octet-stream"}
    # read local picture file
    with open(file_path, 'rb') as f:
        txt_data = f.read()
    # send POST request
    res = requests.post(urljoin(wp_base_url_, "wp-json/wp/v2/media/"),
                        data=txt_data,
                        #headers=headers_,
                        auth=(user_, pass_))
    print(repr(res))

upload_image(r"E:\TeamQno\Decks\Standard-Challenge-2020-07-05 _Tia93_ (122st Place).txt")