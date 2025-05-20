class Logger:
    def __init__(self):
        print("Logger initialized")

    def __del__(self):
        print("Logger deleted")

#Test
log = Logger()
del log