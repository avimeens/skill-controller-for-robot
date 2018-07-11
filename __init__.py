from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class ControllerForRobotSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder().require('ControllerForRobot'))
    def handle_controller_for_robot(self, message):
        self.speak_dialog('controller.for.robot')


def create_skill():
    return ControllerForRobotSkill()

