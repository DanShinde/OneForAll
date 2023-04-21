from .summittest import SummitDataEntry
import logging
from . models import SummitData
from django.forms.models import model_to_dict
from datetime import date 

logger = logging.getLogger(__name__)


def entry():
    today = date.today().strftime("%A")
    myData = SummitData.objects.all()
    for data in myData:
        dataDict = model_to_dict(data)
        print(dataDict)
        if today in dataDict['weekdays']:
            Entry = SummitDataEntry(data_dict=dataDict)
            Entry.login()
            Entry.submit_data()
            Entry.submitForApproval()