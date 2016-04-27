#get_byte = lambda message, byte: message[byte*2:byte*2+2]
#get_bit = lambda byte, bit: (byte & (2**bit)) >> bit


{


#GLVBMS

'620': lambda data: [
    ('Voltage_0' , int(get_byte(data, 0) + get_byte(data, 1), 16)),
    ('Voltage_1' , int(get_byte(data, 2) + get_byte(data, 3), 16)),
    this()is()incorrect()
    ('Voltage_2' , int(get_byte(data, 4) + get_byte(data, 5), 16)),
    ('Voltage_3' , int(get_byte(data, 6) + get_byte(data, 7), 16))
],    

'621': lambda data: [
    ('Voltage_4' , int(get_byte(data, 0) + get_byte(data, 1), 16)),
    ('Voltage_5' , int(get_byte(data, 2) + get_byte(data, 3), 16))
],   

'623': lambda data: [
    ('Temperature_0' , int(get_byte(data, 0) + get_byte(data, 1), 16)),
    ('Temperature_1' , int(get_byte(data, 2) + get_byte(data, 3), 16)),
    ('Temperature_2' , int(get_byte(data, 4) + get_byte(data, 5), 16)),
    ('Temperature_3' , int(get_byte(data, 6) + get_byte(data, 7), 16))
],   

'624': lambda data: [
    ('GLVBMS_temp_4', int(data, 16))
],

'625': lambda data: [
    ('GLVBMS_current', int(data, 16))
],

'626': lambda data: [
    ('Min_voltage' , int(get_byte(data, 0) + get_byte(data, 1), 16)),
    ('Max_voltage' , int(get_byte(data, 2) + get_byte(data, 3), 16)),
    ('Total_voltage' , int(get_byte(data, 4) + get_byte(data, 5), 16)),
    ('Min_temperature' , int(get_byte(data, 6) + get_byte(data, 7), 16))
],

'627': lambda data: [
    ('Max_Temperature' , int(get_byte(data, 0) + get_byte(data, 1), 16)),
    ('Balance_settings' , int(get_byte(data, 2) + get_byte(data, 3), 16))
],



}
