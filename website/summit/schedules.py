from .summittest import SummitDataEntry
import logging
from . models import SummitData
from django.forms.models import model_to_dict

logger = logging.getLogger(__name__)


def entry():
    myData = SummitData.objects.all()
    for data in myData:
        dataDict = model_to_dict(data)
        Entry = SummitDataEntry(data_dict=dataDict)
        print(dataDict)
        Entry.login()
        logger.info("Login Successful Entry")
        Entry.submit_data()
        logger.info("Submit data Successful Entry")
        Entry.submitForApproval()