from mycroft import MycroftSkill, intent_file_handler


class FinishedBooting(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('booting.finished.intent')
    def handle_booting_finished(self, message):
        self.speak_dialog('booting.finished')


def create_skill():
    return FinishedBooting()

