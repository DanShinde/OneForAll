from apscheduler.schedulers.background import BackgroundScheduler
import logging
from . import views

logger = logging.getLogger(__name__)

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(views.entry, 'cron', hour=14, minute=21)
    scheduler.start()

#scheduler = BackgroundScheduler(timezone='Asia/Kolkata')

# def start():
#     scheduler.start()
#     logger.info("Scheduler started")

# def stop():
#     scheduler.shutdown()
#     logger.info("Scheduler stopped")

# def schedule_entry():
#     scheduler.add_job(entry, 'cron', hour=13, minute=45)  # Schedule the entry function to run every day at 06:01am

# schedule_entry()  # Schedule the entry function when the module is loaded
