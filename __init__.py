from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class ControllerForRobotSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('robot.controller.intent')
    def handle_controller_for_robot(self, message):
        self.speak_dialog('controller.for.robot')

    @intent_file_handler('robot.move.intent')
    def handle_ppt_open(self, message):
        distance = message.data.get("distance")
        if distance is None:
            self.speak_dialog('robot.no.distance')
            return
        direction = message.data.get("direction")
        if direction is None:
            self.speak_dialgo('robot.no.direction')
            return
        resp = {'distance' : distance, 'direction' : direction}
        self.speak_dialog('robot.move', data=resp)


def create_skill():
    return ControllerForRobotSkill()

