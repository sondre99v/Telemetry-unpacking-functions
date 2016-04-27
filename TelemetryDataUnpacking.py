{

'620': lambda data: [
    ('Voltage_0' , int(self.get_byte(data, 0) + self.get_byte(data, 1), 16)),
    ('Voltage_1' , int(self.get_byte(data, 2) + self.get_byte(data, 3), 16)),
    ('Voltage_2' , int(self.get_byte(data, 4) + self.get_byte(data, 5), 16)),
    ('Voltage_3' , int(self.get_byte(data, 6) + self.get_byte(data, 7), 16))
],    

'621': lambda data: [
    ('Voltage_4' , int(self.get_byte(data, 0) + self.get_byte(data, 1), 16)),
    ('Voltage_5' , int(self.get_byte(data, 2) + self.get_byte(data, 3), 16))
],   

'623': lambda data: [
    ('Temperature_0' , int(self.get_byte(data, 0) + self.get_byte(data, 1), 16)),
    ('Temperature_1' , int(self.get_byte(data, 2) + self.get_byte(data, 3), 16)),
    ('Temperature_2' , int(self.get_byte(data, 4) + self.get_byte(data, 5), 16)),
    ('Temperature_3' , int(self.get_byte(data, 6) + self.get_byte(data, 7), 16))
],   

'624': lambda data: [
    ('GLVBMS_temp_4', int(data, 16)/100)
],

'625': lambda data: [
    ('GLVBMS_current', int(data, 16)/1000)
],




}
