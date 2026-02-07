# Arcscaff

A lightweight scaffolding tool that creates a consistent folder structure for GIS / geospatial projects (e.g., `data/`, `scripts/`, `automation/`, etc.) so you can start working immediately instead of hand-building directories every time. It will also detect types of data in the data directory and will process to ingest it automatically into the project.

It can also **detect whether an ArcGIS Pro project file (`.aprx`) exists** in the target workspace (useful for recognizing/validating an ArcGIS Pro project context before scaffolding or automation steps).

## Features

- Creates a standard project layout in seconds
- Detects presence of an **ArcGIS Pro `.aprx`** file in the project/workspace
- Safe to run multiple times (won’t fail if folders already exist)
- Customizable structure via config (optional)
- Works on macOS, Linux, and Windows

## Example Structure

```text
my-project/
  data/
    raw/
    processed/
  scripts/
  automation/
  outputs/
  docs/
  logs/
  config/
