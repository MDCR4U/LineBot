import requests
import csv
import os
import time

APP_ID = 'your_app_id'
APP_SECRET = 'your_app_secret'
USER_ACCESS_TOKEN = 'EAAAAUaZA8jlABACA25PeMyGJBHWrj1g5Rr88PDbzw7rLvjXZBApBgomzUeP2RQrZBu0uJJzx2rCs9dRkVqVIOI3jJJibWXb7pyw71IqKXzlg2dwZCvhD345U0OBtKYf3E8P6IXKc3zhIlud0G4XyLd8hQvRiFGU3fe8ZCK2EbyC5d7TnbqOvNmsRDghTukGUZD"'
USER_ID = '100004867093723'

icnt = 0
ocnt = 0

def get_user_email(user_id, access_token):
    url = f"https://graph.facebook.com/{user_id}?fields=email&access_token={access_token}"
    #print(url)
    response = requests.get(url)
    #print(response)
    data = response.json()

    if 'email' in data:
        return data['email']
    else:
        return("----------")
    #    raise Exception(f"Email not found for user with ID: {user_id}")

def xmain():
    USER_ID= '100013429277544' #input("user id ")
#    a = 'y'
#    if USER_ID[0:1] == 'X' :
#       a= 'n'#
#
    #USER_ID= input("user id ")
    
    try:    
            email = get_user_email(USER_ID, USER_ACCESS_TOKEN)
            print(f"Email: {email}")
    except Exception as e:
            print(e)
           
def check_facebook_token_validity(access_token):
    url = f"https://graph.facebook.com/me?access_token={USER_ACCESS_TOKEN}"
    response = requests.get(url)

    if response.status_code == 200:
        return True
    else:
        return False

def read_and_write_csv(input_filename, output_filename):
    wicnt = 0
    wocnt = 0
    if os.path.exists(output_filename):
        mode = 'a'  # append mode
    else:
        mode = 'w'  # write mode

    with open(input_filename, 'r', newline='', encoding='utf-8') as input_file, open(output_filename, mode, newline='', encoding='utf-8') as output_file:
        reader = csv.reader(input_file)
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)

        if mode == 'w':
            # Write the header if the output file is being created for the first time
            writer.writerow(['Column 1', 'Column 2'])

        for row in reader:
                wicnt = wicnt + 1
                wsUSER_ID = row[0]
                url = f"https://graph.facebook.com/me?access_token={USER_ACCESS_TOKEN}"
                response = requests.get(url)

                if response.status_code != 200:
                    print("token invalid")    
                    return False
                
                wsemail = get_user_email(wsUSER_ID, USER_ACCESS_TOKEN)
                if wsemail[0:1] != '-' :
                    print(wsUSER_ID  + "--" + wsemail)
                    wocnt = wocnt + 1
            #writer.writerow([row[0], row[1]])
                writer.writerow([wsUSER_ID, wsemail])
                print(str(wicnt) + " - " + str(wocnt))
                time.sleep(5)
def check_facebook_token_validity(access_token):
    url = f"https://graph.facebook.com/me?access_token={access_token}"
    response = requests.get(url)

    if response.status_code == 200:
        return True
    else:
        return False
def main():
    input_filename = 'uid.csv' #'textcsv.csv'   #input("Enter the input CSV filename: ")
    output_filename = input_filename.split('.')[0] + "_o.csv"
    read_and_write_csv(input_filename, output_filename)
    print(f"Data has been written to {output_filename}")

    #is_valid = check_facebook_token_validity(USER_ACCESS_TOKEN )
    #if is_valid:
    #    print("Facebook access token is valid.")
    #else:
    #    print("Facebook access token is not valid.")
    #    return 

if __name__ == "__main__":
    main()
