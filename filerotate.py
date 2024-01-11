from pathlib import Path
import datetime
from croniter import croniter
import csv
import typing

__author__ = 'customtea (https://github.com/customtea/)'
__version__ = '1.3.0'

class FileRotate():
    """Auto File Rotation
    """
    def __init__(self, 
    savedir: str = ".",
    crontext: str = "0 * * * *",
    pathstring:str = "#YYYY##MM##DD#_#hh##mm##ss#.txt",
    *,
    csv_mode: bool = False,
    bin_mode: bool = False,
    ) -> None:
        """init

        Parameters
        ----------
        savedir : str, optional
            Save Directory Path, by default "."
        crontext : str, optional
            File Rotation Trigger with Cron String, by default "0 * * * *"
        pathstring : str, optional
            Save FilePath String, by default "#YYYY##MM##DD#_#hh##mm##ss#.txt"
            #YYYY# : 4digit Year.
            #YY# : 2digit Year.
            #DD# : 2digit Month.
            #hh# : 2digit Hour.
            #mm# : 2digit Minute.
            #ss# : 2digit Second.
        csv_mode : bool, optional
            CSV Write mode, by default False
        bin_mode : bool, optional
            Binary File Mode, by default False
        """
        self.__save_dir = Path(savedir)
        self.__set_cron(crontext)
        self.__path_string = pathstring
        self.__current_filename = self.__gen_filepath()
        self.__is_csvmode = csv_mode
        self.__is_bin = bin_mode
        if self.__is_bin:
            self.__file_mode = "ab"
        else:
            self.__file_mode = "a"
        self.__open()
    
    def __set_cron(self, crontext: str):
        self.__crontext = crontext
        self.__cron = croniter(self.__crontext)
        self.__next_cron()

    def __next_cron(self):
        self.__dt_next = self.__cron.get_next(datetime.datetime, datetime.datetime.now())
    
    def __gen_filepath(self):
        p_name = self.__genpath_pathstring()
        return self.__save_dir / p_name
    
    def __genpath_pathstring(self):
        dt_current = datetime.datetime.now()
        tpath = self.__path_string
        YYYY = dt_current.strftime("%Y")
        YY = dt_current.strftime("%y")
        MM = dt_current.strftime("%m")
        DD = dt_current.strftime("%d")
        hh = dt_current.strftime("%H")
        mm = dt_current.strftime("%M")
        ss = dt_current.strftime("%S")
        tpath = tpath.replace("#DD#",DD).replace("#MM#",MM).replace("#YYYY#",YYYY).replace("#YY#",YY).replace("#hh#",hh).replace("#mm#",mm).replace("#ss#",ss)
        return Path(tpath)
    
    def __open(self):
        self.__current_filename.parent.mkdir(parents=True, exist_ok=True)
        self.__current_file = open(self.__current_filename, self.__file_mode, encoding="utf8", newline="")
        self.__current_filesize = self.__current_file.__sizeof__()
        if self.__is_csvmode:
            self.__current_csvwriter = csv.writer(self.__current_file)

    def __close(self):
        self.__current_file.close()
        self.__current_filename = ""
    
    def __nextopen(self):
        filepath = self.__gen_filepath()
        if self.__current_filename != filepath:
            self.__close()
            self.__current_filename = filepath
            self.__open()
    
    def __rotate_conditions(self) -> bool:
        dt_now = datetime.datetime.now()
        if dt_now >= self.__dt_next:
            return True
        return False
    
    
    def __rotate_check(self):
        if self.__rotate_conditions():
            self.__nextopen()
            self.__next_cron()
    
    def force_rotate(self):
        """Force Rotation File
        """
        self.__nextopen()
    
    def flush(self):
        """flush
        """
        self.__current_file.flush()
    
    def write(self, *__s: str, flush=False):
        """write string
        Parameters
        ----------
        __s : str
            strings
        flush : bool, optional
            File Write and Flush, by default False
        """
        self.__rotate_check()
        self.__current_file.write(*__s)
        if flush:
            self.__current_file.flush()

    def writelines(self, __lines: typing.Iterable[str], *, flush=False):
        """write iterable string

        Parameters
        ----------
        __lines : Iterable[str]
            strings
        flush : bool, optional
            File Write and Flush, by default False
        """
        self.__rotate_check()
        self.__current_file.writelines(__lines)
        if flush:
            self.__current_file.flush()
    
    def writerow(self, row: typing.Iterable[typing.Any]):
        """write csv

        Parameters
        ----------
        row : typing.Iterable[typing.Any]
            row
        
        Notes
        -----
        This Method is CSV Mode ONLY
        """ 
        self.__rotate_check()
        self.__current_csvwriter.writerow(row)

    def writerows(self, rows: typing.Iterable[typing.Iterable[typing.Any]]):
        """write csv rows

        Parameters
        ----------
        rows : typing.Iterable[Iterable[Any]]
            rows
        
        Notes
        -----
        This Method is CSV Mode ONLY
        """
        self.__rotate_check()
        self.__current_csvwriter.writerows(rows)
