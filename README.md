# Datacamp Downloader (Enhanced Fork)
![Python](https://img.shields.io/badge/python-3.6%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

Major rewrite of code architecture, new features, and API & Chrome compatibility fixes

## Description

This is an enhanced fork of the original [Datacamp Downloader](https://github.com/TRoboto/datacamp-downloader) with significant improvements and new features.

For information about the original tool's features and basic usage, refer to the [original repository](https://github.com/TRoboto/datacamp-downloader).

## What's New in This Fork

### 1) Core Compatibility Fix (Already Merged in [PR #84](https://github.com/TRoboto/datacamp-downloader/pull/84))
Fixed compatibility issues with the current DataCamp API and modernized ChromeDriver setup. This fix was merged into the original repository in [Pull Request #84](https://github.com/TRoboto/datacamp-downloader/pull/84).

---

### 2) New Feature: Course Metadata Export
Added a new `export-courses` command that exports comprehensive metadata about your completed courses to CSV format. The exported data includes:

- **Basic Info**: `id`, `title`, `description`, `short_description`, `slug`
- **Course Details**: `programming_language`, `difficulty_level`, `xp`, `state`, `paid`
- **Time/Duration**: `time_needed_in_hours`, `duration_minutes`
- **Classification**: `topic_id`, `technology_id`, `content_area`, `type`
- **Media**: `link`, `image_url`, `last_updated_on`
- **Stats**: `nb_of_subscriptions`, `num_chapters`, `num_exercises`, `num_videos`, `datasets_count`
- **People**: `instructors_names`, `collaborators_names`
- **Relationships**: `tracks_titles`, `prerequisites_titles`

---

### 3) Enhanced Code Architecture
Improved the internal structure of the classes, functions, and commands of the codebase with:

- **Robust Course Class**: Enhanced `Course` class constructor that safely handles API response data with comprehensive error handling and fallback mechanisms
- **Better Data Parsing**: Improved parsing of nested objects (chapters, datasets, instructors, collaborators, tracks, prerequisites) with graceful error handling
- **Enhanced Error Management**: Added comprehensive error handling in course fetching with proper fallback strategies and user-friendly error messages
- **Flexible Field Handling**: Support for both legacy and current API field names with automatic fallback mechanisms
- **Data Validation**: Added validation for required fields and safe defaults for optional fields
- **Memory Management**: Better handling of large datasets and memory-efficient processing of course metadata

## Installation

**Recommended**: Install in an isolated virtual environment to avoid dependency conflicts:

### Windows
```cmd
python -m venv datacamp-env
datacamp-env\Scripts\activate
pip install git+https://github.com/Michael-Matta1/datacamp-downloader.git
```

### Linux/macOS
```bash
python -m venv datacamp-env
source datacamp-env/bin/activate
pip install git+https://github.com/Michael-Matta1/datacamp-downloader.git
```

Alternatively, install directly (not recommended):
```bash
pip install git+https://github.com/Michael-Matta1/datacamp-downloader.git
```

### Autocompletion

To enable command autocompletion:

```bash
datacamp --install-completion [bash|zsh|fish|powershell|pwsh]
```

Then restart your terminal.

## New Usage: Export Course Metadata

Export your completed course metadata to CSV:

```bash
datacamp export-courses
```

Options:
- `--output`: Specify output file (default: `completed_courses.csv`)
- `--refresh`: Refresh course data from API before exporting

Example:
```bash
datacamp export-courses --output my_courses.csv --refresh
```

The CSV file can be opened in Excel, Google Sheets, or any spreadsheet application for analysis and reporting.

## Documentation

Full command documentation is available in [docs.md](https://github.com/Michael-Matta1/datacamp-downloader/blob/master/docs.md)

## Disclaimer

This tool is for personal use only. Sharing DataCamp course content violates their Terms of Use. The developers are not responsible for any misuse of this tool.
