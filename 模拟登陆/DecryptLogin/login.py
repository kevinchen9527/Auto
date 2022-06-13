from pip import main
from DecryptLogin import login
lg = login.Login()
infos_resp, session = lg.twitter(username='', password='')
