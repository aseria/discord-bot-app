import yaml

stream = open('setting.yml', 'r')
setting = yaml.load(stream, Loader=yaml.FullLoader)
