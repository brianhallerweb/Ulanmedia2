from config.config import *
from config.mgid_token import mgid_token
from functions.action_functions.check_all_mgid_ads import check_all_mgid_ads

# This is the script that checks all mgid ads and gives this email report

# subject: 500 ads: 450 active, 50 paused, 0 rejected.

# body:
# 450 out of 500 ads in all campaigns are active.
# 50 out of 500 ads in all campaigns are paused.
# 0 out of 500 ads in all campaigns are rejected.

# it runs every morning on CRON

check_all_mgid_ads(mgid_token)
