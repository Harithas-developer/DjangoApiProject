from django.core.management.base import BaseCommand


import  os
os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'newproject.settings')

import  django
django.setup()
from  firstapp.models import  Name , AcitvityPeriod
from faker import Faker
fakegen = Faker()



class Command(BaseCommand):
    help = "Populates the data in the DB"


    def handle(self,N=10, **options):
        for num in range(N):
            help = "populating database with dummy data"
            full_name = fakegen.name
            date = [{"start_time": fakegen.month_name()+" "+ fakegen.day_of_month() +" " + fakegen.year()+ " " +  fakegen.time() + " "+fakegen.am_pm(), "end_time": fakegen.month_name()+" "+ fakegen.day_of_month() +" " + fakegen.year()+ " " +  fakegen.time() + " "+fakegen.am_pm()},
                    {" start_time":fakegen.month_name()+" "+ fakegen.day_of_month() +" " + fakegen.year()+ " " +  fakegen.time() + " "+fakegen.am_pm(), "end_time":fakegen.day_of_month() +" " + fakegen.year()+ " " +  fakegen.time() + " "+fakegen.am_pm()},
                    {" start_time":fakegen.month_name()+" "+ fakegen.day_of_month() +" " + fakegen.year()+ " " +  fakegen.time() + " "+fakegen.am_pm(), "end_time": fakegen.month_name()+" "+ fakegen.day_of_month() +" " + fakegen.year()+ " " +  fakegen.time() + " "+fakegen.am_pm()}]
            name_obj = Name.objects.get_or_create(name=full_name)[0]
            activity_obj = AcitvityPeriod.objects.get_or_create(name=name_obj, data=date)[0]
            num+=1





if __name__ == '__main__':
    print("data is populating")
    Command.handle()
    print("population complete.")



