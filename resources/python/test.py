try:
  with open('https://K3nzo-m.github.io/resources/database.json', 'r+') as f:
    data = json.load(f)
    logins = data
    f.close
except:
  f = open('https://K3nzo-m.github.io/resources/database.json', 'w')
  logins = {}
  json.dump(logins, f)
  f.close
