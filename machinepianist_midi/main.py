from base64 import b64encode, b64decode
from time import sleep

import requests

for i in range(1, 717):
    try:
        with open(f"christianstudy_midi/temp/hymnary{i:03}.mid", "rb") as f:
            inbytes = b64encode(f.read())

        input = {"filename": "test", "generate_wav": 0, "midi": inbytes.decode()}
        res = requests.post(
            "http://machinepianist.com/cloudInference/performMidi", json=input
        )
        res.raise_for_status()
        outbytes = b64decode(res.json()["0"])

        with open(f"machinepianist_midi/temp/hymnary{i:03}.mid", "wb") as f:
            f.write(outbytes)

        sleep(10)
    except FileNotFoundError:
        print(f"Skip {i}")
    except Exception as e:
        print(f"Cannot transform hymnary {i}", e)
