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

        # create meta-data
        metadata = DotthzMetaData()
        metadata.user = "John Doe"
        metadata.version = "1.00"
        metadata.instrument = "Toptica TeraFlash Pro"
        metadata.mode = "THz-TDS/Transmission"

        file["Measurement 1"].set_metadata(metadata)

        # for thzVer 1.00, we need to transpose the array!
        file["Measurement 1"]["Sample"] = np.array([time, data]).T

    del file  # optional, not required as the file is already closed

    # create and save a second file
    path2 = Path("test2.thz")
    with DotthzFile(path2, "w") as file:
        file["Measurement 1"]["Sample"] = np.array([time, data]).T
    del file  # optional, not required as the file is already closed

    # open the first file again in append mode and the second in read mode
    with DotthzFile(path1, "a") as file1, DotthzFile(path2) as file2:
        for name, measurement in file2.items():
            file1[name] = measurement.group
    del file1  # optional, not required as the file is already closed

    with DotthzFile(path1, "r") as file1:
        # read the first measurement
        key = list(file1.keys())[0]
        print(file1.get(key).metadata)
        print(file1.get(key).datasets)

        # for that it is essential to use the `np.array()` function to copy
        # the data, since we want to use it outside of the opened file context.
        # If we would not do this, then `time_trace` and `pulse_trace` would only be
        # pointers to a closed file and thus empty.

        time = np.array(file1.get(key).datasets["Sample"])[:, 0]
        pulse_trace = np.array(file1.get(key).datasets["Sample"])[:, 1]
