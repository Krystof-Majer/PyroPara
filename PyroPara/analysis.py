import glob
from typing import List

from PyroPara.filter import FILTERS, Filter
from PyroPara.stafile import STAfile
from PyroPara.utils import get_beta


class Analysis:
    def __init__(self) -> None:
        self.sta_files: List[STAfile] = []

    def __len__(self) -> int:
        return len(self.sta_files)

    def load_all_files(self, directory: str):
        """Loads all files from given directory.
        Assigns default filters

        Args:
            directory (str): Directory path

        Raises:
            Exception: Default filter failed to load
        """

        self.sta_files.clear()

        files = glob.glob(f"{directory}/PYRO**.txt")

        for path in files:

            # Retrieves heating rate (beta)
            beta = get_beta(path)

            default_filter = FILTERS.get(beta)

            if default_filter is None:
                raise Exception("Default filter failed to load")

            # STAfile class initialization and loading
            file = STAfile(path=path, beta=beta, filter=default_filter)
            file.load()

            self.sta_files.append(file)

    def check_filter_parameters(self):
        pass

    def load_file(self, path: str, filter: Filter = None):
        """Loads single file from directory and assigns given filter.

        Args:
            path (str): File path
            filter (Filter, optional): Filter:class to assign.
                yDefaults to None.
        """
        beta = get_beta(path)
        if filter is None:
            default_filter = FILTERS.get(beta)
        file = STAfile(path=path, beta=beta, filter=default_filter)
        file.load()

        self.sta_files.append(file)

    def run(self):
        """Runs process method for all stafiles:STAfile in self.sta_files"""
        for file in self.sta_files:
            file.process()
            file.calculate_local_minima()
