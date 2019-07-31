from functions.action_functions.exclude_all_campaigns_for_blacklisted_p_widgets import exclude_all_campaigns_for_blacklisted_p_widgets

# This is the script that checks for any mistakes in excluding all campaigns
# for blacklisted p widgets.

# it runs every morning on CRON and sends email reports

exclude_all_campaigns_for_blacklisted_p_widgets("oneeighty")
