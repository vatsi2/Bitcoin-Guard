def verify_hardware_wallet(device):
    expected_vendor_ids = [0x2c97, 0x534c]  # Ledger, Trezor
    if device.idVendor not in expected_vendor_ids:
        raise SecurityError("Untrusted device")
    if not device.firmware_signed:
        raise SecurityError("Invalid firmware signature")
