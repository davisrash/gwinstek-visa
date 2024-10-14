import pyvisa


class GPD3303S:
    """Class to control the GW Instek GPD-3303S power supply"""

    def __init__(self, resource_name):
        self.rm = pyvisa.ResourceManager()
        self.instrument = self.rm.open_resource(resource_name)

    def set_voltage(self, channel, voltage):
        """Set the voltage for a specific channel"""
        self.instrument.write(f"VSET{channel}:{voltage:.2f}")

    def get_voltage(self, channel):
        """Read the set voltage for a specific channel"""
        return float(self.instrument.query(f"VOUT{channel}?").rstrip("V\r\n"))

    def set_output(self, state):
        """Enable or disable output for a specific channel"""
        state_value = "1" if state else "0"
        self.instrument.write(f"OUT{state_value}")

    def close(self):
        """Close the instrument connection"""
        self.instrument.close()


# Example usage:
# psu = GPD3303S("USB0::0x0483::0x7540::NI_VISA::INSTR")
# psu.set_voltage(1, 5.0)  # Set channel 1 to 5.0V
# psu.set_output(1, True)  # Enable output on channel 1
