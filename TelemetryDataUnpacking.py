{
#GLVBMS Current
'625': lambda data: [
    ('GLVBMS_current', int(data, 16)/1000)
],

'624': lambda data: [
    ('GLVBMS_temp_4', int(data, 16)/100)
],


}
