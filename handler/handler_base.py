from pyjoycon import JoyCon, get_R_id, get_L_id
import time

class JoyConHandler(object):
    def __init__(self) -> None:
        # only support two joycon this time.
        left_joycon_id = get_L_id()
        right_joycon_id = get_R_id()

        self.left_joycon = JoyCon(*left_joycon_id)
        self.right_joycon = JoyCon(*right_joycon_id)

        self.handller_exec = None
        self.hz = 10

        print(right_joycon_id, left_joycon_id)

    def register_handller_callback(self, func, hz = 10):
        self.handller_exec = func
        self.hz = hz

    def spin(self):
        while True:
            self.handller_exec(self.left_joycon,
                        self.right_joycon)
            time.sleep(1 / self.hz)
    # TODO
    def check_life(self):
        pass



# print(joycon_id)
# joycon = JoyCon(*joycon_id)




if __name__ == "__main__":
    obj = JoyConHandler()
