#get_byte = lambda message, byte: message[byte*2:byte*2+2]
#get_bit = lambda byte, bit: (byte & (2**bit)) >> bit


{


#GLVBMS

'620': lambda data: [
    ('Voltage_0' , int(get_byte(data, 0) + get_byte(data, 1), 16)),
    ('Voltage_1' , int(get_byte(data, 2) + get_byte(data, 3), 16)),
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

#R16 mechanical data 1
'290': lambda data: [
    ('R16[1] current speed' 	, int(get_byte(data, 0) + get_byte(data, 1), 16) / 100),
    ('R16[1] speed setpoint' 	, int(get_byte(data, 2) + get_byte(data, 3), 16) / 100),
    ('R16[1] torque setpoint' 	, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100)
],

#R16 mechanical data 2
'294': lambda data: [
    ('R16[2] current speed' 	, int(get_byte(data, 0) + get_byte(data, 1), 16) / 100),
    ('R16[2] speed setpoint' 	, int(get_byte(data, 2) + get_byte(data, 3), 16) / 100),
    ('R16[2] torque setpoint' 	, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100)
],

#R16 mechanical data 3
'298': lambda data: [
    ('R16[3] current speed' 	, int(get_byte(data, 0) + get_byte(data, 1), 16) / 100),
    ('R16[3] speed setpoint' 	, int(get_byte(data, 2) + get_byte(data, 3), 16) / 100),
    ('R16[3] torque setpoint' 	, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100)
],

#R16 mechanical data 4
'29C': lambda data: [
    ('R16[4] current speed' 	, int(get_byte(data, 0) + get_byte(data, 1), 16) / 100),
    ('R16[4] speed setpoint' 	, int(get_byte(data, 2) + get_byte(data, 3), 16) / 100),
    ('R16[4] torque setpoint' 	, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100)
],

#R16 temp data
'291': lambda data: [
    ('R16[1] temp 1' 			, int(get_byte(data, 0) + get_byte(data, 1), 16) / 100),
    ('R16[1] temp 2' 			, int(get_byte(data, 2) + get_byte(data, 3), 16) / 100),
    ('R16[1] temp 3' 			, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100),
    ('R16[1] Motor temp' 				, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100)
],
	
#R16 temp data		
'295': lambda data: [		
    ('R16[2] temp 1' 			, int(get_byte(data, 0) + get_byte(data, 1), 16) / 100),
    ('R16[2] temp 2' 			, int(get_byte(data, 2) + get_byte(data, 3), 16) / 100),
    ('R16[2] temp 3' 			, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100),
    ('R16[2] Motor temp' 				, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100)
],
	
#R16 temp data		
'299': lambda data: [		
    ('R16[3] temp 1' 			, int(get_byte(data, 0) + get_byte(data, 1), 16) / 100),
    ('R16[3] temp 2' 			, int(get_byte(data, 2) + get_byte(data, 3), 16) / 100),
    ('R16[3] temp 3' 			, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100),
    ('R16[3] Motor temp' 				, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100)
],

#R16 temp data
'29D': lambda data: [
    ('R16[4] temp 1' 			, int(get_byte(data, 0) + get_byte(data, 1), 16) / 100),
    ('R16[4] temp 2' 			, int(get_byte(data, 2) + get_byte(data, 3), 16) / 100),
    ('R16[4] temp 3' 			, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100),
    ('R16[4] Motor temp' 				, int(get_byte(data, 4) + get_byte(data, 5), 16) / 100)
],

#R16 Electrical data
'292': lambda data: [
    ('R16[1] torque current' 	, int(get_byte(data, 0) + get_byte(data, 1), 16)) / 100),
    ('R16[1] direct current' 	, int(get_byte(data, 2) + get_byte(data, 3), 16)) / 100),
    ('R16[1] DC current' 		, int(get_byte(data, 4) + get_byte(data, 5), 16)) / 100),
    ('R16[1] DC voltage' 		, int(get_byte(data, 6) + get_byte(data, 7), 16)) / 100)
],

#R16 Electrical data
'296': lambda data: [
    ('R16[2] torque current' 	, int(get_byte(data, 0) + get_byte(data, 1), 16)) / 100),
    ('R16[2] direct current' 	, int(get_byte(data, 2) + get_byte(data, 3), 16)) / 100),
    ('R16[2] DC current' 		, int(get_byte(data, 4) + get_byte(data, 5), 16)) / 100),
    ('R16[2] DC voltage' 		, int(get_byte(data, 6) + get_byte(data, 7), 16)) / 100)
],

#R16 Electrical data
'29A': lambda data: [
    ('R16[3] torque current' 	, int(get_byte(data, 0) + get_byte(data, 1), 16)) / 100),
    ('R16[3] direct current' 	, int(get_byte(data, 2) + get_byte(data, 3), 16)) / 100),
    ('R16[3] DC current' 		, int(get_byte(data, 4) + get_byte(data, 5), 16)) / 100),
    ('R16[3] DC voltage' 		, int(get_byte(data, 6) + get_byte(data, 7), 16)) / 100)
],

#R16 Electrical data
'29E': lambda data: [
    ('R16[4] torque current' 	, int(get_byte(data, 0) + get_byte(data, 1), 16)) / 100),
    ('R16[4] direct current' 	, int(get_byte(data, 2) + get_byte(data, 3), 16)) / 100),
    ('R16[4] DC current' 		, int(get_byte(data, 4) + get_byte(data, 5), 16)) / 100),
    ('R16[4] DC voltage' 		, int(get_byte(data, 6) + get_byte(data, 7), 16)) / 100)
],

#R16 Status data
'293': lambda data: [
    ('R16[1] status bit_{0}'.format(i) 		, int(self.endian_invert(data), 32) & (2**i) != 0) for i in range(32),
    ('R16[1] accumulated status {0}'.format(i), int(self.endian_invert(data), 32) & (2**i) != 0) for i in range(32, 64)
]

#R16 Status data
'297': lambda data: [
    ('R16[2] status bit_{0}'.format(i) 		, int(self.endian_invert(data), 32) & (2**i) != 0) for i in range(32),
    ('R16[2] accumulated status {0}'.format(i), int(self.endian_invert(data), 32) & (2**i) != 0) for i in range(32, 64)
]


#R16 Status data
'29B': lambda data: [
    ('R16[3] status bit_{0}'.format(i) 		, int(self.endian_invert(data), 32) & (2**i) != 0) for i in range(32),
    ('R16[3] accumulated status {0}'.format(i), int(self.endian_invert(data), 32) & (2**i) != 0) for i in range(32, 64)
]

#R16 Status data
'29F': lambda data: [
    ('R16[4] status bit_{0}'.format(i) 		, int(self.endian_invert(data), 32) & (2**i) != 0) for i in range(32),
    ('R16[4] accumulated status {0}'.format(i), int(self.endian_invert(data), 32) & (2**i) != 0) for i in range(32, 64)
]

}
