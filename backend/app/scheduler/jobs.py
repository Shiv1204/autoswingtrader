from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def start_scheduler(job):
    scheduler.add_job(
        job,
        trigger="interval",
        hours=1,
        id="scanner_job",
        replace_existing=True
    )
    scheduler.start()
