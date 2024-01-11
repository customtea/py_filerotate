# Python File Rotate

## Requrement
```
croniter
```


## Table of Contents

- [Python File Rotate](#python-file-rotate)
  - [Requrement](#requrement)
  - [Table of Contents](#table-of-contents)
  - [filerotate](#filerotate)
    - [FileRotate Objects](#filerotate-objects)
      - [\_\_init\_\_](#__init__)
      - [force\_rotate](#force_rotate)
      - [flush](#flush)
      - [write](#write)
      - [writelines](#writelines)
      - [writerow](#writerow)
      - [writerows](#writerows)

<a id="filerotate"></a>

## filerotate

<a id="filerotate.FileRotate"></a>

### FileRotate Objects

```python
class FileRotate()
```

Auto File Rotation

<a id="filerotate.FileRotate.__init__"></a>

#### \_\_init\_\_

```python
def __init__(savedir: str = ".",
             crontext: str = "0 * * * *",
             pathstring: str = "#YYYY##MM##DD#_#hh##mm##ss#.txt",
             *,
             csv_mode: bool = False,
             bin_mode: bool = False) -> None
```

init
```
Parameters
----------
savedir : str, optional
    Save Directory Path, by default "."
crontext : str, optional
    File Rotation Trigger with Cron String, by default "0 * * * *"
pathstring : str, optional
    Save FilePath String, by default "`YYYY`#`MM`#`DD_`#hh#`mm`#`ss.txt`"
    `YYYY`# : 4digit Year.
    `YY`# : 2digit Year.
    `DD`# : 2digit Month.
    `hh`# : 2digit Hour.
    `mm`# : 2digit Minute.
    `ss`# : 2digit Second.
csv_mode : bool, optional
    CSV Write mode, by default False
bin_mode : bool, optional
    Binary File Mode, by default False
```

<a id="filerotate.FileRotate.force_rotate"></a>

#### force\_rotate

```python
def force_rotate()
```

Force Rotation File

<a id="filerotate.FileRotate.flush"></a>

#### flush

```python
def flush()
```

flush

<a id="filerotate.FileRotate.write"></a>

#### write

```python
def write(*__s: str, flush=False)
```

write string
```
Parameters
----------
__s : str
    strings
flush : bool, optional
    File Write and Flush, by default False
```

<a id="filerotate.FileRotate.writelines"></a>

#### writelines

```python
def writelines(__lines: typing.Iterable[str], *, flush=False)
```

write iterable string

```
Parameters
----------
__lines : Iterable[str]
    strings
flush : bool, optional
    File Write and Flush, by default False
```

<a id="filerotate.FileRotate.writerow"></a>

#### writerow

```python
def writerow(row: typing.Iterable[typing.Any])
```

write csv

```
Parameters
----------
row : typing.Iterable[typing.Any]
    row

Notes
-----
This Method is CSV Mode ONLY
```

<a id="filerotate.FileRotate.writerows"></a>

#### writerows

```python
def writerows(rows: typing.Iterable[typing.Iterable[typing.Any]])
```

write csv rows

```
Parameters
----------
rows : typing.Iterable[Iterable[Any]]
    rows

Notes
-----
This Method is CSV Mode ONLY
```
