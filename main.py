import asyncio
from scheduler import Scheduler
from logger import get_logger

logger = get_logger("Main")


def main():
    sched = Scheduler()
    try:
        logger.info("Starting scheduler...")
        asyncio.run(sched.start())
    except KeyboardInterrupt:
        logger.info("Shutting down...")
    finally:
        asyncio.run(sched.ex_mgr.close())


if __name__ == "__main__":
    main()
