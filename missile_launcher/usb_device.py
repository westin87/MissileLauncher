import platform

import usb


class USBDevice:
    def __init__(self):
        self.device = usb.core.find(idVendor=0x2123, idProduct=0x1010)

        if self.device is None:
            self.device = usb.core.find(idVendor=0x0a81, idProduct=0x0701)

            if self.device is None:
                raise ValueError('Missile device not found')
            else:
                self.device_type = "Original"
        else:
            self.device_type = "Thunder"

        # On Linux we need to detach usb HID first
        if "Linux" == platform.system():
            try:
                self.device.detach_kernel_driver(0)
            except Exception:
                pass  # already unregistered

        self.device.set_configuration()

    def send_command(self, cmd):
        if "Thunder" == self.device_type:
            self.device.ctrl_transfer(0x21, 0x09, 0, 0, [0x02, cmd, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        elif "Original" == self.device_type:
            self.device.ctrl_transfer(0x21, 0x09, 0x0200, 0, [cmd])

    def led(self, cmd):
        if "Thunder" == self.device_type:
            self.device.ctrl_transfer(0x21, 0x09, 0, 0, [0x03, cmd, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        elif "Original" == self.device_type:
            print("There is no LED on this device")