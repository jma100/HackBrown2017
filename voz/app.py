from luis_sdk import LUISClient

def process_res(res):
    '''
    A function that processes the luis_response object and prints info from it.
    :param res: A LUISResponse object containing the response data.
    :return: None
    '''
    print(u'---------------------------------------------')
    print(u'LUIS Response: ')
    print(u'Query: ' + res.get_query())
    print(u'Top Scoring Intent: ' + res.get_top_intent().get_name())
    if res.get_dialog() is not None:
        if res.get_dialog().get_prompt() is None:
            print(u'Dialog Prompt: None')
        else:
            print(u'Dialog Prompt: ' + res.get_dialog().get_prompt())
        if res.get_dialog().get_parameter_name() is None:
            print(u'Dialog Parameter: None')
        else:
            print('Dialog Parameter Name: ' + res.get_dialog().get_parameter_name())
        print(u'Dialog Status: ' + res.get_dialog().get_status())
    print(u'Entities:')
    for entity in res.get_entities():
        print(u'"%s":' % entity.get_name())
        print(u'Type: %s, Score: %s' % (entity.get_type(), entity.get_score()))
    #youtube commands
    if res.get_top_intent().get_name() == 'OpenYoutube':    print(u'python -m webbrowser -t "http://www.youtube.com"')
    if res.get_top_intent().get_name() == 'CloseYoutube':   print(u'command')
    if res.get_top_intent().get_name() == 'SearchVideo':    print(u'command')
    if res.get_top_intent().get_name() == 'PauseVideo':     print(u'command')
    if res.get_top_intent().get_name() == 'PlayVideo':      print(u'command')
    #Powerpoint commands
    if res.get_top_intent().get_name() == 'OpenPowerpoint': print(u'command')
    if res.get_top_intent().get_name() == 'ClosePowerpoint':print(u'command')
    if res.get_top_intent().get_name() == 'AdvanceSlide':   print(u'command')
    if res.get_top_intent().get_name() == 'GoBackASlide':   print(u'command')

try:
    APPID = '9af1cccd-54af-484f-bf53-1ad33f7f3575'
    APPKEY = '0f8646a177804853bc5d2c8d4d2a07cf'
    TEXT = raw_input(u'Please input the text to predict:\n')
    CLIENT = LUISClient(APPID, APPKEY, True)
    res = CLIENT.predict(TEXT)
    while res.get_dialog() is not None and not res.get_dialog().is_finished():
        TEXT = raw_input(u'%s\n'%res.get_dialog().get_prompt())
        res = CLIENT.reply(TEXT, res)
    process_res(res)
except Exception, exc:
    print(exc)
