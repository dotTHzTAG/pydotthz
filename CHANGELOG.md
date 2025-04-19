# pydotthz changelog

All notable changes to the `pydotthz` package will be documented in this file.

# Unreleased

* ...

## 1.0.0 - 19.4.2025

### Added:

* `DotTHzFile` now allows accessing measurements like a dictionary: `file[name]`
* When setting a measurement value either in `file[name]` or `file.measurements[name]` it is automatically written to
  the file on the disk.

### Deprecated:

* Usage of `file.get_measurements()` is replaced by `file.measurements`
* Usage of `file.get_measurement(name)` is replaced by `file[name]` or `file.measurements[name]`

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

