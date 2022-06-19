from handler.handler_base import JoyConHandler



class Master(object):
    def __init__(self) -> None:
        self.handler = JoyConHandler()
        self.callback_connect()

    def handler_callback(self, left_status, right_status):
        print(left_status["gyro"], right_status['gyro'], end="\n")

    def callback_connect(self):
        self.handler.register_handller_callback(self.handler_callback, 10)

    def run(self):
        self.handler.spin()



if __name__ == "__main__":
    obj = Master()
    obj.run()