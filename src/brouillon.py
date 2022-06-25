try:
        ser = ser = serial.Serial('/dev/ttyACM0', 115200)
        time.sleep(2)
    except SerialException:
        print("device is currently used")
        sys.exit(1)