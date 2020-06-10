import os
from configparser import RawConfigParser, NoOptionError
import logging

logger = logging.getLogger("filter")


class ConfigTool(object):
    section = ""
    config = None
    default_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.ini")

    def __init__(self, file_path=None):
        if file_path is None:
            file_path = self.default_file_path
        self.config = RawConfigParser()
        self.config.read(file_path)
        self.file_path = file_path

    def set_section(self, section):
        self.section = section

    def get(self, key):
        if self.section:
            try:
                return self.config.get(self.section, key)
            except NoOptionError:
                message_info = [self.section, str(key), "ConfigTool.error", "no_key"]
                logger.error("|".join(message_info))
                return None

    def get_section_all(self, section):

        return self.config.items(section)

