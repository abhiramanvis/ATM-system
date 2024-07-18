# import the required libraries
import PySimpleGUI as sg


# method to log in screen
def login_screen():
  sg.theme('DarkTeal12') 
  # add the components inside the window
  layout = [  
    [sg.Text('ATM system',size=(15,2),font=('Arial',25),justification='center')],
    [sg.Text('Enter account number:',size=(20,2)), sg.Input(key='acc_number', size=(10, 2), font=('Arial', 16))],
    [sg.Text('Enter PIN:',size=(20,2)), sg.Input(key='pin',password_char="*", size=(10, 2), font=('Arial', 16))],
    [sg.Text('',size=(10,2)),sg.Button('Sign in'), sg.Button('Cancel') ]
  ]  

  # create the Window
  window = sg.Window('Login', layout)  

 # event loop to keep the GUI window active
  while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break           
  window.close()

login_screen()
# method to the main screen
def main_screen(acc_no,pin):
  sg.theme('DarkTeal12')   # add a touch of color
  # all the stuff inside your window.
  layout = [  [sg.Text('ATM system',size=(20,2),font=('Arial', 25),justification='center')],
              [sg.Button('Check Balance',size=(20,2)), sg.Button('Change PIN',size=(20,2)) ],
              [sg.Button('Withdraw Amount',size=(20,2)), sg.Button('Transfer Funds', size=(20,2))],
              [sg.Button('Deposit Amount',size=(20,2)), sg.Button('Transaction History', size=(20,2))],
              [sg.Text('',size=(15,2)), sg.Button('Logout', size=(10,2)) ]]

  # create the Window
  window = sg.Window('Main Screen', layout)
  # event Loop to process "events" and get the "values" of the inputs
  while True:
    event, values = window.read()
    balance = 0
    if event == sg.WIN_CLOSED: # if the user closes the window or clicks cancel
      break
    # check for logout
    if event == "Logout":
      # close the active window
      window.close()
      login_screen()  
# close the active window
  window.close()
