# Copyright (c) 2017 Ultimaker B.V.
# Cura is released under the terms of the LGPLv3 or higher.

from cura.PrinterOutput.PrinterOutputController import PrinterOutputController

MYPY = False
if MYPY:
    from cura.PrinterOutput.PrintJobOutputModel import PrintJobOutputModel
    from cura.PrinterOutput.PrinterOutputModel import PrinterOutputModel


class ClusterUM3PrinterOutputController(PrinterOutputController):
    def __init__(self, output_device):
        super().__init__(output_device)
        self.can_pre_heat_bed = False
        self.can_pre_heat_extruders = False
        self.can_control_manually = False

    def setJobState(self, job: "PrintJobOutputModel", state: str):
        data = "{\"action\": \"%s\"}" % state
        self._output_device.put("print_jobs/%s/action" % job.key, data, onFinished=None)

