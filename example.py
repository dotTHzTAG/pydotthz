from pathlib import Path
import numpy as np

from dotthz import DotthzFile, DotthzMeasurement, DotthzMetaData

if __name__ == "__main__":

    # Create a new .thz file
    file = DotthzFile().new()

    # Sample data
    time = np.linspace(0, 1, 100)  # your time array
    data = np.random.rand(100)  # example 3D data array

    measurement = DotthzMeasurement()
    # for thzVer 1.00, we need to transpose the array!
    datasets = {"Sample": np.array([time, data]).T}
    measurement.datasets = datasets

    # set meta_data
    meta_data = DotthzMetaData()
    meta_data.user = "John Doe"
    meta_data.version = "1.00"
    meta_data.instrument = "Toptica TeraFlash Pro"
    meta_data.mode = "THz-TDS/Transmission"

    measurement.meta_data = meta_data

    file.groups["Measurement"] = measurement

    # save the file
    path1 = Path("test1.thz")
    path2 = Path("test2.thz")
    file.save(path1)
    file.save(path2)
    del file

    # open the file again
    file = DotthzFile.from_file(path1)

    # add more measurements from a file
    file.add_from_file(path2)

    # read the first group (measurement)
    key = list(file.groups.keys())[0]
    print(file.groups.get(key).meta_data)
    print(file.groups.get(key).datasets)
