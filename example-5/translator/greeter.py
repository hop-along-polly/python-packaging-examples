from translator.lang import en, es

def greet(name, lang):
  if lang.upper() == 'ES':
    return es.greet(name)
  else:
    return en.greet(name)
