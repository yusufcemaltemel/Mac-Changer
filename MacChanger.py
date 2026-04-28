import subprocess
import optparse
import re

class MacChanger:
    help_message_m = "Change your MAC address less than a second"
    help_message_i = "MyMacChanger started"

    @staticmethod
    def create_option():
        parse_object = optparse.OptionParser()
        parse_object.add_option("-i", "--interface", dest="interface", help=MacChanger.help_message_i)
        parse_object.add_option("-m", "--mac", dest="mac_address", help=MacChanger.help_message_m)
        option_tuple = parse_object.parse_args()
        (user_inputs, arguments) = option_tuple
        return option_tuple

    def get_input(self):
        user_interface = self.create_option()[0].interface
        user_mac = self.create_option()[0].mac_address
        input_list = [user_interface,user_mac]
        return input_list

    def change_mac(self):
        subprocess.call(["ifconfig",self.get_input()[0],"down"])
        subprocess.call(["ifconfig",self.get_input()[0],"hw","ether",self.get_input()[1]])
        subprocess.call(["ifconfig", self.get_input()[0], "up"])

    def __str__(self):
        return "MacChanger is being started..."

    def is_mac_match(self):
        ifconfig = subprocess.check_output(["ifconfig",self.get_input()[0]])
        new_mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))

        if new_mac_address.group(0) == self.get_input()[1]:
            return "Mac address has been changed successfully!"
        else:
            return "Mac address hasn't been changed"

if __name__ == "__main__":
    changer = MacChanger()
    changer.change_mac()
    print(changer.is_mac_match())