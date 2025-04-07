import smtplib
import requests
from config import settings
from logger import get_logger

logger = get_logger("Alerts")


def send_email(subject: str, body: str):
    cfg = settings.alerts
    if not cfg.email:
        return
    # Simplified SMTP; configure as needed
    try:
        with smtplib.SMTP('localhost') as smtp:
            msg = f"Subject: {subject}\n\n{body}"
            smtp.sendmail('noreply@bot', cfg.email, msg)
        logger.info(f"Email sent to {cfg.email}")
    except Exception as e:
        logger.error(f"Email error: {e}")


def send_webhook(payload: dict):
    url = settings.alerts.webhook_url
    if not url:
        return
    try:
        resp = requests.post(url, json=payload, timeout=5)
        resp.raise_for_status()
        logger.info("Webhook delivered")
    except Exception as e:
        logger.error(f"Webhook error: {e}")

