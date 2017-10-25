import requests, hashlib, json, os

#Twilio
from twilio.rest import Client
ACCOUNT_SID = 'TWILIO_SID'
AUTH_TOKEN  = 'TWILIO_TOKEN'
CLIENT = Client(ACCOUNT_SID, AUTH_TOKEN)
PHONE_TO = '+YOUR_PHONE_NUMBER'
PHONE_FROM = '+YOUR_TWILIO_NUMBER'

#Pages to check
SITES = {
    'BorzoiRescue': 'http://www.nbrf.org/category/available'
}

def main():
    updated_content = {}

    #Get existing content hashes in file
    base_path = ''
    #Append mode will create a new file if one does not exist
    content_file = open(os.path.join(base_path, 'webpage_update_hashes.txt'), 'a+')
    content_file.seek(0)
    content_hashes = content_file.read()
    content_file.close()

    #If file is empty, add temporary hash to dictionary
    if content_hashes == '':
        new_file_content = {}
        for ea in SITES:
            new_file_content[ea] = ''
        prev_content = json.loads(json.dumps(new_file_content))
    #Or load existing hashes to dictionary
    else:
        prev_content = json.loads(content_hashes)

    for ea in SITES:

        if ea not in prev_content:
            prev_content[ea] = ''
        #Get current page content and hash it
        res = requests.get(SITES[ea], verify=False) #Will not verify SSL certs
        new_hash = hashlib.md5(res.text.encode('utf-8')).hexdigest()

        #Assign hash to updated content dictionary
        updated_content[ea] = new_hash

        #If content has updated, send text
        if new_hash != prev_content[ea]:
            #Send text message
            CLIENT.messages.create(
                to=PHONE_TO,
                from_=PHONE_FROM,
                body='There are changes on the ' + str(ea) + ' page! ' + SITES[ea])

    #If any content has updated, write new hashes to file
    if prev_content != updated_content:
        write_content = open(os.path.join(base_path, 'webpage_update_hashes.txt'), 'w')
        write_content.write(json.dumps(updated_content))
        write_content.close()
    else:
        CLIENT.messages.create(
            to=PHONE_TO,
            from_=PHONE_FROM,
            body='No changes on the pages today.')

if __name__ == '__main__':
    main()
