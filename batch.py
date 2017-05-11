from datetime import datetime, timedelta
import calendar
import event_export
import settings

def add_months(sourcedate,months):
    month = sourcedate.month - 1 + months
    year = int(sourcedate.year + month / 12 )
    month = month % 12 + 1
    day = min(sourcedate.day,calendar.monthrange(year,month)[1])
    return datetime(year,month,day)

if __name__ == '__main__':
    from_date = datetime.strptime(raw_input("From Date: "), "%Y-%m-%d")
    to_date = datetime.strptime(raw_input("To Date: "), "%Y-%m-%d")

    while True:
        end_date = add_months(from_date,1)
        if to_date < end_date : end_date = to_date
	api_secret = settings.mixpanel['api_secret']
	output_file = "mixpanel_{}_{}_{}.json".format(settings.mixpanel['project'], from_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"))
        event_export.mixpanel(from_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"), output_file, api_secret)
        if to_date == end_date:
            break
        from_date = end_date
