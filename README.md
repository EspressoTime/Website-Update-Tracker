# Website-Update-Tracker

Hash webpages and send text messages via the Twilio API to alert you of changes.

# Getting Started

Replace the following variables:

* `ACCOUNT_SID` - Your Twilio Account SID
* `AUTH_TOKEN` - Your Twilio Auth Token
* `PHONE_TO` - Your receiving phone number with country code (e.g. +15558675309)
* `PHONE_FROM` - Your Twilio number with country code (e.g. +15558675309)
* `SITES` - Add your sites to the dictionary with `'SiteTitle': 'SiteURL'` 

Run with `python3 website_update_tracker.py`.