from flask import Flask,render_template,request
#from Student import Student,Friend
from DB import DBHandler
from controller import controller
from contact import contact

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/form')
def displayform():
    return render_template('create_contact.html')

@app.route('/createContact',methods=["GET","POST"])
def createContact():
    if request.method == "POST":
        name = request.form["name"]
        mobileno = request.form["mobileno"]
        city = request.form["city"]
        prof = request.form["profession"]
        user_contact = contact(name,mobileno,city,prof)
        controller_obj=controller()
        status = controller_obj.insertContact(user_contact)
        if status:
            return render_template("create_contact.html",msg='Contact Created Successfully!!')
        else:
            return render_template("create_contact.html",msg='ERROR!! In Account Creation')
    else:
        return render_template('create_contact.html')

@app.route('/showcontacts')
def showContacts():
    controller_obj = controller()
    contact_list = controller_obj.showContact()
    if contact_list is not None:
        return render_template('contacts.html',data=contact_list)
    else:
        return render_template('contacts.html',msg='NO contacts to show!!')

@app.route('/search')
def search():
    return render_template('contact.html')

@app.route('/getContact',methods=["GET","POST"])
def getContact():
    if request.method == "POST":
        name = request.form["name"]
        controller_obj = controller()
        contact = controller_obj.getContactByName(name)
    #contact_list = [{'name':contact.name,'mobileno':contact.mobileno,'city':contact.city,'profession':contact.profession}]
        if contact is not None:
            return render_template('search.html', data = contact)
        else:
            return render_template('search.html', msg='NO contacts to show!!')
    else:
        return render_template('contact.html')



if __name__ == '__main__':
    app.run()
