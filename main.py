import configparser

configs = configparser.ConfigParser()
configs.read('~/test-config-files/clients.cfg')
client = configs['SANDBOX']
print(client['username'])