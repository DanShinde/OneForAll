from apscheduler.schedulers.background import BackgroundScheduler
import logging
from .views import entry

logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler(timezone='Asia/Kolkata')

def start():
    scheduler.start()
    logger.info("Scheduler started")

def stop():
    scheduler.shutdown()
    logger.info("Scheduler stopped")

def schedule_entry():
    scheduler.add_job(entry, 'cron', hour=18, minute=1)  # Schedule the entry function to run every day at 06:01am

schedule_entry()  # Schedule the entry function when the module is loaded
