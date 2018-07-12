from mycroft import MycroftSkill, intent_file_handler


class ControllerForRobotSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('robot.controller.intent')
    def handle_controller_for_robot(self, message):
        self.speak_dialog('controller.for.robot')

    @intent_file_handler('robot.move.intent')
    def handle_robot_move(self, message):
        distance = message.data.get("distance")
        if distance is None:
            self.speak_dialog('robot.no.distance')
            return
        direction = message.data.get("direction")
        if direction is None:
            self.speak_dialog('robot.no.direction')
            return
        unit = message.data.get("unit")
        if unit is None:
            self.speak_dialog('robot.no.unit')
            return
        resp = {'distance' : distance, 'direction' : direction, 'unit' : unit}
        self.speak_dialog('robot.move', data=resp)

    @intent_file_handler('robot.stop.intent')
    def handle_robot_stop(self, message):
        self.speak_dialog('robot.stop')

def create_skill():
    return ControllerForRobotSkill()

