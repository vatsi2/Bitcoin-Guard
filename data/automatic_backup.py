import schedule

schedule.every().day.at("23:00").do(
    encrypt_and_backup,
    path='/vaults/primary',
    destination='/secure/usb'
)
