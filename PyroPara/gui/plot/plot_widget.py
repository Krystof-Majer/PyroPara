from PyroPara.gui.base import PlotWidget, TabStatus


class TgPlot(PlotWidget, TabStatus):
    X_LABEL = "T"
    Y_LABEL = "TG"
    X_UNIT = "K"
    Y_UNIT = "-"

    def __init__(self, index) -> None:
        super().__init__(index)

    @property
    def tab_label(self) -> str:
        return "TG"

    def plot(self, files: list) -> None:
        for file in files:
            x = file._df.temperature
            y = file._df.mass_filtered
            label = str(f"{file.beta} K")
            super().plot(x, y, clear=False, legend=True, label=label)
            super().set_ylim(0, 1.05)
        self.draw()

    def remove(self, files: list) -> None:
        for file in files:
            pass


class DtgPlot(PlotWidget, TabStatus):
    X_LABEL = "T"
    Y_LABEL = "DTG"
    X_UNIT = "K"
    Y_UNIT = "1/s"

    def __init__(self, index) -> None:
        super().__init__(index)
        self.set_axis_labels()

    @property
    def tab_label(self) -> str:
        return "DTG"

    def plot(self, files: list) -> None:
        for file in files:
            x = file._df.temperature
            y = file._df.mass_diff_filtered
            label = str(f"{file.beta} K")
            super().plot(x, y, clear=False, legend=True, label=label)
        super().set_axis_labels()
        self.draw()

    @property
    def label(self) -> str:
        return ""


class DdtgPlot(PlotWidget, TabStatus):
    X_LABEL = "T"
    Y_LABEL = "DDTG"
    X_UNIT = "K"
    Y_UNIT = "1/s²"

    def __init__(self, index) -> None:
        super().__init__(index)
        self.minima_lines = []

    @property
    def tab_label(self) -> str:
        return "DDTG"

    def plot(self, files: list) -> None:
        for file in files:
            x = file._df.temperature
            y = file._df.mass_diff2_filtered
            label = str(f"{file.beta} K")
            super().plot(x, y, clear=False, legend=True, label=label)
        super().set_axis_labels()
        self.draw()

    def plot_normalized(self, files: list) -> None:
        for file in files:
            x = file._df.temperature
            y = file._df.mass_diff2_normalized
            label = str(f"{file.beta} K")
            super().plot(x, y, clear=False, legend=True, label=label)
        super().set_axis_labels_normalized()
        self.draw()

    def plot_minima(self, files: list) -> None:
        color_list: list = super().colors
        self.minima_lines.clear()

        for i, file in enumerate(files):
            _max = super().ylim[1]
            points = file.local_minima
            x, y = zip(*points)
            self.minima_lines.append(
                super().plot_minima(x, _max, color=color_list[i])
            )

    def toggle_lines(self, enable: bool):
        for line in self.minima_lines:
            super().toggle_line(enable, line)


class DdtgPlotNormalized(PlotWidget, TabStatus):
    X_LABEL = "T"
    X_UNIT = "K"
    Y_UNIT_N = "0-1"
    Y_LABEL_N = "DDTG"

    def __init__(self, index) -> None:
        super().__init__(index)
        self.minima_lines = []

    @property
    def tab_label(self) -> str:
        return "Normalized"

    def plot(self, files: list) -> None:
        for file in files:
            x = file._df.temperature
            y = file._df.mass_diff2_normalized
            label = str(f"{file.beta} K")
            super().plot(x, y, clear=False, legend=True, label=label)
            super().set_ylim(0, 1)
        super().set_axis_labels_normalized()
        self.draw()

    def plot_minima(self, files: list) -> None:
        color_list: list = super().colors
        self.minima_lines.clear()

        for i, file in enumerate(files):
            _max = 1
            points = file.local_minima
            x, y = zip(*points)
            self.minima_lines.append(
                super().plot_minima(x, _max, color=color_list[i])
            )

    def toggle_lines(self, enable: bool):
        for line in self.minima_lines:
            super().toggle_line(enable, line)
