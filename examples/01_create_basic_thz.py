from pathlib import Path
import numpy as np
from pydotthz import DotthzFile, DotthzMetaData

if __name__ == "__main__":
    # Sample data
    time = np.linspace(0, 1, 100)
    data = np.random.rand(100)

    # save the file
    path1 = Path("test1.thz")
    with DotthzFile(path1, "w") as file:
        file.create_measurement("Measurement 1")

        # create metadata
        metadata = DotthzMetaData()
        metadata.user = "John Doe"
        metadata.version = "1.00"
        metadata.instrument = "Toptica TeraFlash Pro"
        metadata.mode = "THz-TDS/Transmission"

        file["Measurement 1"].set_metadata(metadata)

        # for thzVer 1.00, we need to transpose the array!
        file["Measurement 1"]["Sample"] = np.array([time, data]).T
