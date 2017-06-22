import npyscreen

from vent.helpers.meta import Services


class ServicesForm(npyscreen.FormBaseNew):
    """ Services form for the Vent CLI """
    def quit(self, *args, **kwargs):
        """ Overridden to switch back to MAIN form """
        self.parentApp.switchForm('MAIN')

    def create(self):
        """ Override method for creating FormBaseNew form """
        self.add_handlers({"^T": self.quit, "^Q": self.quit})
        services = Services()
        if services:
            for service in services:
                value = ""
                for val in service[1]:
                    value += val+", "
                title_text = self.add(npyscreen.TitleFixedText,
                                      name=service[0],
                                      value=value[:-2])
