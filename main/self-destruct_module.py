def wipe_device_on_intrusion(detect_count=3):
    intrusion_attempts = 0
    while True:
        if detect_intrusion():
            intrusion_attempts +=1
            if intrusion_attempts >= detect_count:
                os.system("rm -rf /secure_storage/*")
                return
