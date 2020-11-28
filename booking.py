from datetime import datetime

TOTAL_ROOMS = 100

class MR_booking:


    global bookings_list
    global available_rooms
    global format

    bookings_list = []
    available_rooms = []

    format = '%b %d %Y %I:%M%p'


    def avalable_number_of_rooms(start_time,end_time):

        start_time = datetime.strptime(start_time,format)
        end_time = datetime.strptime(end_time,format)
        minimum_number = []
        if len(available_rooms) != 0:    
            for i in available_rooms:
                if (start_time >= i['start_time'] and start_time <= i['end_time']) or (end_time >= i['start_time'] and end_time <= i['end_time']):
                    minimum_number.append(i['balance_number_of_rooms'])
            if len(minimum_number) > 0:
                return min(minimum_number)
            else:
                return TOTAL_ROOMS
        else:
            return TOTAL_ROOMS

    def update_number_of_available_rooms(start_time,end_time,balance_number_of_rooms):
        if len(available_rooms) != 0:
            for i in available_rooms:
                if start_time >= i['start_time'] and end_time <= i['end_time']:
                    i['end_time'] = end_time
                    mid_time = {'start_time' : start_time , 'end_time' : end_time , 'balance_number_of_rooms' : balance_number_of_rooms }
                    last_time = {'start_time' : end_time , 'end_time' : i['end_time'] , 'balance_number_of_rooms' : i['balance_number_of_rooms'] }
                    available_rooms.append(mid_time)
                    available_rooms.append(last_time)
                    # add function for making unique entries
                    return True
                elif start_time < i['start_time'] and end_time > i['start_time'] and end_time <= i['end_time']:
                    first_time = {'start_time' : start_time , 'end_time' : i['start_time'] , 'balance_number_of_rooms' : balance_number_of_rooms }
                    pass
        else:
            room={}
            room['start_time'] = start_time
            room['end_time'] = end_time
            room['balance_number_of_rooms'] = balance_number_of_rooms
            available_rooms.append(room)


    def booking_func(employee_id,number_of_rooms,start_time,end_time,number_of_employees):
        
        fetch_available_rooms = avalable_number_of_rooms(start_time,end_time)

        if fetch_available_rooms >=number_of_rooms:
            if len(bookings_list) == 0:
                booking_id = 1
            else:
                booking_id = bookings_list[-1]['booking_id'] + 1
            
            booking_elements = {}
            booking_elements['booking_id'] = booking_id
            booking_elements['employee_id'] = employee_id
            booking_elements['number_of_rooms'] = number_of_rooms
            booking_elements['start_time'] = start_time
            booking_elements['end_time'] = end_time
            booking_elements['number_of_employees'] = number_of_employees
            booking_elements['balance_number_of_rooms'] = TOTAL_ROOMS-number_of_rooms

            bookings_list.append(booking_elements)


            return True
    
    def cancellation_func(booking_id):
        flag = False
        index = None
        for i in bookings_list:
            if i['booking_id'] == booking_id:
                flag = True
                index = i
                break
        if flag:
            bookings_list.pop(index)
        else:
            print('booking_id not found')
        return True
    







    

        
        
        
            


