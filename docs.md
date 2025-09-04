# `datacamp`

**Usage**:

```console
$ datacamp [OPTIONS] COMMAND [ARGS]...
```

**Options**:

- `--version`: Show version.
- `--install-completion`: Install completion for the current shell.
- `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
- `--help`: Show this message and exit.

**Commands**:

- `courses`: List your completed courses.
- `download`: Download courses/tracks given their ids.
- `export-courses`: Export completed courses metadata to a CSV file.
- `login`: Log in to Datacamp using your username and password.
- `reset`: Restart the session.
- `set-token`: Log in to Datacamp using your token.
- `tracks`: List your completed tracks.

## `datacamp login`

Log in to Datacamp using your username and password.

**Usage**:

```console
$ datacamp login [OPTIONS]
```

**Options**:

- `-u, --username TEXT`: [required]
- `-p, --password TEXT`: [required]
- `--help`: Show this message and exit.

## `datacamp set-token`

Log in to Datacamp using your token.

**Usage**:

```console
$ datacamp set-token [OPTIONS] TOKEN
```

**Arguments**:

- `TOKEN`: [required]

**Options**:

- `--help`: Show this message and exit.

## `datacamp courses`

List your completed courses.

**Usage**:

```console
$ datacamp courses [OPTIONS]
```

**Options**:

- `-r, --refresh`: Refresh completed courses. [default: False]
- `--help`: Show this message and exit.

## `datacamp tracks`

List your completed tracks.

**Usage**:

```console
$ datacamp tracks [OPTIONS]
```

**Options**:

- `-r, --refresh`: Refresh completed tracks. [default: False]
- `--help`: Show this message and exit.

## `datacamp download`

Download courses/tracks given their ids.

Example: `datacamp download id1 id2 id3`

To download all your completed courses run:
`datacamp download all`

To download all your completed tracks run:
`datacamp download all-t`

**Usage**:

```console
$ datacamp download [OPTIONS] IDS...
```

**Arguments**:

- `IDS...`: IDs for courses/tracks to download or `all` to download all your completed courses, `all-t` to download all your completed tracks. [required]

**Options**:

- `-p, --path DIRECTORY`: Path to the download directory. [default: `current_directory/Datacamp`]
- `--slides / --no-slides`: Download slides. [default: True]
- `--datasets / --no-datasets`: Download datasets. [default: True]
- `--videos / --no-videos`: Download videos. [default: True]
- `--exercises / --no-exercises`: Download exercises. [default: True]
- `-st, --subtitles [en|zh|fr|de|it|ja|ko|pt|ru|es]`: Choose subtitles to download. [default: en]
- `--audios / --no-audios`: Download audio files. [default: False]
- `--scripts, --transcript / --no-scripts, --no-transcript`: Download scripts or transcripts. [default: True]
- `--python-file / --no-python-file`: Download your own solution as a python file if available. [default: True]
- `--no-warnings`: Disable warnings. [default: True]
- `-w, --overwrite`: Overwrite files if exist. [default: False]
- `--help`: Show this message and exit.

## `datacamp export-courses`

Export completed courses metadata to a CSV file.

**Usage**:

```console
$ datacamp export-courses [OPTIONS]
```

**Options**:

- `--output TEXT`: Output CSV file. [default: completed_courses.csv]
- `--refresh`: Refresh data from API. [default: False]
- `--help`: Show this message and exit.

**Description**:

This command exports comprehensive metadata about your completed courses to a CSV file. The exported data includes:

**Core Course Information:**
- Course ID, title, description, and short description
- Slug, programming language, and difficulty level
- XP points, state, and payment status
- Time requirements and duration

**Content Statistics:**
- Number of chapters, exercises, and videos
- Dataset count and availability
- Content area and course type

**People and Relationships:**
- Instructor and collaborator names
- Associated track titles
- Course prerequisites

**Technical Metadata:**
- Topic and technology IDs
- Last updated dates
- Image URLs and marketing information
- SEO details and subscription counts

**Example Usage:**

```console
# Export to default file (completed_courses.csv)
$ datacamp export-courses

# Export to custom file with fresh data
$ datacamp export-courses --output my_courses.csv --refresh

# Export using cached data to specific location
$ datacamp export-courses --output /path/to/courses_backup.csv
```

The CSV file can be opened in Excel, Google Sheets, or any other spreadsheet application for analysis, filtering, and reporting of your completed DataCamp courses.

## `datacamp reset`

Restart the session.

**Usage**:

```console
$ datacamp reset [OPTIONS]
```

**Options**:

- `--help`: Show this message and exit.