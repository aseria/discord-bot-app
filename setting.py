import yaml

stream = open('setting-sample.yml', 'r')
setting = yaml.load(stream, Loader=yaml.FullLoader)
