# pydotthz changelog

All notable changes to the `pydotthz` package will be documented in this file.

# Unreleased

* ...

## 1.0.0 - 14.5.2025

### Added:

* `DotTHzFile` now allows accessing measurements directly: `file[measurement_name]`
* `DotTHzFile` now allows accessing datasets directly: `file[measurement_name][dataset_name]`
* Memory mapping is now fully supported. Datasets and Attributes are now wrapped for THz meta_data and datasets with
  keys according to `dsDescription` and `mdDescription`.
* Added more tests:
    * `test_dotthz_extend_existing_measurement_with_dataset()`
    * `test_dotthz_extend_existing_measurement_with_existing_meta_data_attribute()`
    * `test_dotthz_extend_existing_measurement_with_new_meta_data_attribute()`

### Deprecated:

* Usage of `file.get_measurements()` is replaced by `file.items()`
* Usage of `file.get_measurement(name)` is replaced by `file[name]`

### Breaking:

* `DotTHzMeasurement` has been removed, the data is now fully memory mapped and never copied into another data
  structure.
* `DotTHzMetaData` is only optional if you want to extract the meta-data. It now normally remains as attributes with
  memory mapping attached to the HDF5 file.
* Renamed `meta_data` to `metadata` for consistency with the rest of the codebase.

## 0.4.0 - ...

### Breaking:

* Changed import name from `dotthz` to `pydotthz` for consistency

### Added:

* Added a module level docstring outlining functionality
* Bug fix for empty user metadata

## 0.3.2 - ...

### Added:

* Updated websites in `pyproject.toml` after repo transfer

## 0.3.0 - 28.01.2025

### Added:

* Example to interface 2D THz images

## 0.2.0 - 5.12.2024

### Added:

* New structure for `DotthzFile`
* Bug fix in strings (thanks [@JasperWB](https://github.com/JasperWB))

