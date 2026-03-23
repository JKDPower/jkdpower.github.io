<?php exit; ?>
[2023-11-01 18:38:20] WARNING: Form 4015 > dmen******@ya***.com is already subscribed to the selected list(s)
[2023-11-01 18:38:30] WARNING: Form 4015 > dmen******@ya***.com is already subscribed to the selected list(s)
[2024-03-09 00:51:15] WARNING: Form 4015 > ruaw******@em********.com is already subscribed to the selected list(s)
[2024-10-11 13:21:24] ERROR: Form 4015 > Mailchimp API error: 400 Bad Request. Invalid Resource. crac*******@gm***.com has signed up to a lot of lists very recently; we're not allowing more signups for now

Request: 
POST https://us10.api.mailchimp.com/3.0/lists/2cf7937a5e/members

{"status":"pending","email_address":"crac*******@gm***.com","interests":{},"merge_fields":{},"email_type":"html","ip_signup":"217.148.143.198","tags":[]}

Response: 
400 Bad Request
{"type":"https://mailchimp.com/developer/marketing/docs/errors/","title":"Invalid Resource","status":400,"detail":"crac*******@gm***.com has signed up to a lot of lists very recently; we're not allowing more signups for now","instance":"43694b47-fd1a-8b15-97dc-0adc76eafc7f"}
[2025-06-17 22:56:12] WARNING: Form 4015 > dona*************@gm***.com is already subscribed to the selected list(s)
[2025-08-17 14:14:27] ERROR: Form 4015 > Mailchimp API error: 400 Bad Request. Member Exists. dtig*******@gm***.com is already a list member. Use PUT to insert or update list members.

Request: 
POST https://us10.api.mailchimp.com/3.0/lists/2cf7937a5e/members

{"status":"pending","email_address":"dtig*******@gm***.com","interests":{},"merge_fields":{},"email_type":"html","ip_signup":"76.37.8.141","tags":[]}

Response: 
400 Bad Request
{"title":"Member Exists","status":400,"detail":"dtig*******@gm***.com is already a list member. Use PUT to insert or update list members.","instance":"a1536a31-862f-7f76-b94e-aa77e57d0432"}
