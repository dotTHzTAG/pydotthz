from pathlib import Path
import numpy as np
from pydotthz import DotthzFile, DotthzMetaData

if __name__ == "__main__":

    # read out an image file:
    image_path_1 = Path("../tests/test_files/test_image.thz")
    with DotthzFile(image_path_1, "r") as image_file:
        # read the first group/measurement
        key = list(image_file.keys())[0]
        print(image_file.get(key).metadata)
        datasets = image_file.get(key).datasets
        print(datasets.keys())

        # from the first dataset, extract the image,
        # for that it is essential to use the `np.array()` function to copy
        # the data, since we want to use it outside of the opened file context.
        # If we would not do this, then `time_trace` and `image` would only be
        # pointers to a closed file and thus empty.
        time_trace = np.array(datasets["time"])
        image = np.array(datasets["dataset"])

        # print image dimensions
        print(image.shape)

    # save an image file:
    image_path_2 = Path("../tests/test_files/test_image_2.thz")
    with DotthzFile(image_path_2, "w") as file:

        file.create_measurement("Image")

        # set metadata
        metadata = DotthzMetaData()
        metadata.user = "John Doe"
        metadata.email = "john.doe@unibe.ch"
        metadata.institution = "University of Bern"
        metadata.orcid = "ORCID"
        metadata.description = "some comment"
        metadata.date = "date"
        metadata.time = "time"
        metadata.version = "1.10"
        metadata.instrument = "Toptica TeraFlash Pro"
        metadata.mode = "THz-TDS/Transmission"

        # add more keys from your "info" dictionary ...
        # for (key, value) in info.items():
        #    metadata.add_field(key, value)

        file["Image"].set_metadata(metadata)

        # important: do not manipulate keys on the `dataset` field, otherwise
        # it won't be written to the file.
        file["Image"]["time"] = time_trace
        file["Image"]["dataset"] = image
