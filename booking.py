
class MR_booking:


    global bookings_list
    global number_of_available_rooms

    bookings_list = []
    number_of_available_rooms = 100

    def booking_func(employee_id,number_of_rooms,start_time,end_time,number_of_employees):
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

        bookings_list.append(booking_elements)

        return bookings_list
    
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

    

        
        
        
            


