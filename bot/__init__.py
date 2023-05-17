#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get("26861990"))

API_HASH = os.environ.get("0592761ae3a24dcf709d85ab87bc12b9")

BOT_TOKEN = os.environ.get("6296295298:AAG82Ph5DQjGVKwg4vSUyNyuLaW3YXL4A7E")

DB_URI = os.environ.get("mongodb+srv://jayvora:1850@cluster.t5ql7o3.mongodb.net/?retryWrites=true&w=majority")

USER_SESSION = os.environ.get("BQGZ4aYAb7SbzAcwkRxG_ICO_fcDZMR6BIO3vIKApsfqKWJT-2-_oaEVmxn1CXvx-hi9s14_ennY0WMclgKkTQaFT-aQqN4HSt5BdRQJ6B99Er0pmAR5iij29Axu0RGVP8Zf3YqX7_hHFxYKkPm0MwpEjGvRNQT8ZqQssm2mcMF1O2sM5CI3YA7JgkYuOJeDKtNiyOXr0Y_kKp-tQaiUYkFq-D1jrHoNzHS2oMBU77b10gFiZHIBDD0kd4x9-17HB4OG-33qjcMMUPbFv-dkpYDueIX8HerB0v2yb6OItXiXq7rAuJX_mj5-yGt_eOSq275A4iMUDH1DzeM4WAAaiB4QZAIXvwAAAAFnifBOAA")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
