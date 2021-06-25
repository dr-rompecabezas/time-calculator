def add_time(start, duration, *day):
    # print(start, duration)
    new_time = ''

    # Start arg breakdown
    start_time = start.split()
    start_hhmm = start_time[0].split(':')
    start_hh = int(start_hhmm[0])
    start_mm = int(start_hhmm[1])
    meridian = [start_time[1]]
    if meridian[0] == 'AM':
        meridian.append('PM')
    elif meridian[0] == 'PM':
        meridian.append('AM')

    # Duration arg breakdown
    add_hhmm = duration.split(':')
    add_hh = int(add_hhmm[0])
    add_mm = int(add_hhmm[1])

    # Optional day arg
    week_day = ''
    if day:
        week_day = day[0].title()

    # Calculations
    start_minutes = (start_hh * 60) + start_mm
    add_minutes = (add_hh * 60) + add_mm
    days_count = int(add_minutes / 1440)
    result_minutes = start_minutes + add_minutes

    result_hh = int(result_minutes / 60)
    result_mm = result_minutes % 60

    # Output builder
    meridian_index = int(int(result_hh / 12) % 2)
    final_mm = str(result_mm)

    if len(final_mm) < 2:
        final_mm = '0' + final_mm

    while result_hh > 12:
        result_hh -= 12

    final_meridian = meridian[meridian_index]
    final_hh = str(result_hh)

    final_days = ''
    week_day_count = 0

    if meridian[0] == 'PM' and final_meridian == 'AM':
        if days_count < 1:
            final_days = final_days + '(next day)'
            week_day_count += 1
        elif days_count >= 1:
            final_days = final_days + f'({days_count + 1} days later)'
            week_day_count += days_count + 1
    elif meridian[0] == 'AM' and final_meridian == 'AM':
        if days_count == 1 or (days_count < 1 and add_minutes > 720):
            final_days = final_days + '(next day)'
            week_day_count += 1
        elif days_count > 1:
            final_days = final_days + f'({days_count} days later)'
            week_day_count += days_count
    elif meridian[0] == 'PM' and final_meridian == 'PM':
        if days_count == 1 or (days_count < 1 and add_minutes > 720):
            final_days = final_days + '(next day)'
            week_day_count += 1
        elif days_count > 1:
            final_days = final_days + f'({days_count} days later)'
            week_day_count += days_count
    elif meridian[0] == 'AM' and final_meridian == 'PM':
        if days_count < 1 and add_minutes > 720:
            final_days = final_days + '(next day)'
            week_day_count += 1
        elif days_count >= 1:
            final_days = final_days + f'({days_count + 1} days later)'
            week_day_count += days_count + 1

    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    if week_day:
        day_index = week.index(week_day)
        rotated_week = week[day_index:] + week[:day_index]
        week_day = rotated_week[week_day_count % 7]

    # Return constructor
    new_time = new_time + final_hh + ':' + final_mm + ' ' + final_meridian

    if week_day and final_days:
        new_time = new_time + ', ' + week_day + ' ' + final_days
    elif final_days:
        new_time = new_time + ' ' + final_days
    elif week_day:
        new_time = new_time + ', ' + week_day

    return new_time
