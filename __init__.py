from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.log import LOG
from mycroft.api import DeviceApi
import time

#creating an object for the hour of the d
t = time.localtime()
current_time = int(time.strftime("%H", t))

class FinishedBooting(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.api = DeviceApi()

    def initialize(self):
        self.add_event("mycroft.skills.initialized", self.handle_booting_finished)
        LOG.debug("add event handle boot finished")

    @intent_file_handler('booting.finished.intent')
    def handle_booting_finished(self, message):
        device = DeviceApi().get()
        if current_time >=12 and current_time < 18:
            self.speak_dialog('afternoon.finished')
            self.speak_dialog('booting.finished', data={"name": device["name"]})
            LOG.debug('finished booting')

        elif current_time >= 18:
            self.speak_dialog('evening.finished')
            self.speak_dialog('booting.finished', data={"name": device["name"]}) 
            LOG.debug('finished booting')

        else:
            self.speak_dialog('morning.finished')
            self.speak_dialog('booting.finished', data={"name": device["name"]})
            LOG.debug('finished booting')


def create_skill():
    return FinishedBooting()

