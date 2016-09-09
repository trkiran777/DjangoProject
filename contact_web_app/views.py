from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from models import Contact, Provider, User


def contacts_home(request):
    if 'username' in request.session.keys():
        username = request.session['username']
    else:
        username = ''
    return render(request, "contact_web_app/index.html", {'username': username})


def add_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
        password = request.POST['password']
        try:
            User.objects.get(email=email)
            message = 'User already exist!'
            return HttpResponse(message)
        except User.DoesNotExist:
            try:
                User.objects.get(phone_no=phone_no)
                message = 'User already exist!'
                return HttpResponse(message)
            except User.DoesNotExist:
                user = User(name=name, email=email, phone_no=phone_no, password=password)
                user.save()
                message = 'Registration is successful!'
                return HttpResponse(message)


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email, password=password)
            request.session['username'] = user.name
            request.session['user_id'] = user.email
            return HttpResponse("login success")
        except User.DoesNotExist:
            message = 'Invalid Email or Password!'
            return HttpResponse(message)


def logout(request):
    try:
        for session_key in request.session.keys():
            del request.session[session_key]
    except:
        pass
    return HttpResponseRedirect("/")


def add_contact_form(request):
    if 'username' in request.session.keys():
        username = request.session['username']
    else:
        username = ''
    return render(request, "contact_web_app/add_contact.html", {'username': username})


def add_contact(request):
    if request.method == 'POST':
        if 'user_id' in request.session.keys():
            user_id = request.session['user_id']
            name = request.POST['name']
            phone_no = request.POST['phone_no']
            email = request.POST['email']
            street = request.POST['street']
            city = request.POST['city']
            state = request.POST['state']
            pin_code = request.POST['pin_code']
            try:
                Contact.objects.get(phone_no=phone_no, user_id=user_id)
            except Contact.DoesNotExist:
                contact = Contact(user_id=user_id, name=name, phone_no=phone_no, email=email, street=street, city=city,
                                  state=state, pin_code=pin_code)
                contact.save()
                message = 'Contact successfully added!'
                return HttpResponse(message)
            else:
                message = 'Contact already exist!'
                return HttpResponse(message)
        else:
            return HttpResponse('login first!')


def modify_contact_form(request):
    username = request.session['username']
    name = request.POST['name']
    phone_no = request.POST['phone_no']
    email = request.POST['email']
    street = request.POST['street']
    city = request.POST['city']
    state = request.POST['state']
    pin_code = request.POST['pin_code']
    return render(request, "contact_web_app/modify_contact.html", {'name': name, 'phone_no': phone_no, 'email': email,
                                                                   'street': street, 'city': city, 'state': state,
                                                                   'pin_code': pin_code, 'username': username})


def modify_contact(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        name = request.POST['name']
        phone_no = request.POST['phone_no']
        email = request.POST['email']
        street = request.POST['street']
        city = request.POST['city']
        state = request.POST['state']
        pin_code = request.POST['pin_code']
        try:
            contact = Contact.objects.get(phone_no=phone_no, user_id=user_id)
            contact.name = name
            contact.email = email
            contact.street = street
            contact.city = city
            contact.state = state
            contact.pin_code = pin_code
            contact.save()
            message = 'Contact successfully modified!'
            return HttpResponse(message)
        except Contact.DoesNotExist:
            message = 'There is no contact with this phone number!'
            return HttpResponse(message)


def delete_contact_form(request):
    if 'username' in request.session.keys():
        username = request.session['username']
    else:
        username = ''
    return render(request, "contact_web_app/delete_contact.html", {'username': username})


def delete_contact(request):
    if request.method == 'POST':
        if 'user_id' in request.session.keys():
            user_id = request.session['user_id']
            phone_no = request.POST['phone_no']
            try:
                contact = Contact.objects.get(phone_no=phone_no, user_id=user_id)
                contact.delete()
                message = 'Contact deleted successfully!'
                return HttpResponse(message)
            except Contact.DoesNotExist:
                message = 'There is no contact with this phone number!'
                return HttpResponse(message)
        else:
            return HttpResponse('login first!')


def get_contact_form(request):
    if 'username' in request.session.keys():
        username = request.session['username']
    else:
        username = ''
    message = ''
    return render(request, "contact_web_app/get_contact.html", {'username': username, 'message': message})


def get_contact(request):
    if request.method == 'POST':
        phone_no = request.POST['phone_no']
        try:
            if 'username' in request.session.keys():
                username = request.session['username']
                user_id = request.session['user_id']
                contact = Contact.objects.get(phone_no=phone_no, user_id=user_id)
            else:
                username = ''
                contact = Contact.objects.get(phone_no=phone_no)
            return render(request, "contact_web_app/view_contact.html", {'contact': contact, 'username': username})
        except Contact.DoesNotExist:
            if 'username' in request.session.keys():
                username = request.session['username']
            else:
                username = ''
            message = 'There is no contact with this phone number!'
            return render(request, "contact_web_app/get_contact.html", {'message': message, 'username': username})

def get_provider_form(request):
    if 'username' in request.session.keys():
        username = request.session['username']
    else:
        username = ''
    return render(request, "contact_web_app/get_provider.html", {'username': username})


def get_provider(request):
    if request.method == 'POST':
        phone_no = request.POST['phone_no']
        providers = Provider.objects.all()
        for provider in providers:
            if phone_no[0:4] in provider.series_list:
                return HttpResponse(provider.provider_name)
        return HttpResponse('Other')


def get_contacts_by_provider_form(request):
    if 'username' in request.session.keys():
        username = request.session['username']
    else:
        username = ''
    return render(request, "contact_web_app/get_contacts_by_provider.html", {'username': username})


def get_contacts_by_provider(request):
    if request.method == 'POST':
        provider_name = request.POST['provider']
        provider = Provider.objects.get(provider_name=provider_name)
        li = []
        if 'user_id' in request.session.keys():
            user_id = request.session['user_id']
            contacts = Contact.objects.filter(user_id=user_id)
        else:
            contacts = Contact.objects.all()
        for contact in contacts:
            if contact.phone_no[0:4] in provider.series_list:
                li.append(contact)
        if li:
            if 'username' in request.session.keys():
                username = request.session['username']
            else:
                username = ''
            return render(request, "contact_web_app/view_contacts.html", {'contacts': li, 'username': username})
        else:
            if 'username' in request.session.keys():
                username = request.session['username']
            else:
                username = ''
            message = 'There are no contacts with this provider!'
            return render(request, "contact_web_app/view_contacts.html", {'message': message, 'username': username})


def get_contacts_by_field_form(request):
    if 'username' in request.session.keys():
        username = request.session['username']
    else:
        username = ''
    return render(request, "contact_web_app/get_contacts_by_field.html", {'username': username})


def get_contacts_by_field(request):
    if request.method == 'POST':
        if 'user_id' in request.session.keys():
            user_id = request.session['user_id']
        else:
            user_id = ''
        string = request.POST['string']
        field = request.POST['field']
        if field == 'name' and user_id:
            subset = Contact.objects.filter(name__contains=string, user_id=user_id)
        elif field == 'name' and user_id == '':
            subset = Contact.objects.filter(name__contains=string)
        elif field == 'phone_no' and user_id:
            subset = Contact.objects.filter(phone_no__contains=string, user_id=user_id)
        elif field == 'phone_no' and user_id == '':
            subset = Contact.objects.filter(phone_no__contains=string)
        elif field == 'email' and user_id:
            subset = Contact.objects.filter(email__contains=string, user_id=user_id)
        elif field == 'email' and user_id == '':
            subset = Contact.objects.filter(email__contains=string)
        elif field == 'street' and user_id:
            subset = Contact.objects.filter(street__contains=string, user_id=user_id)
        elif field == 'street' and user_id == '':
            subset = Contact.objects.filter(street__contains=string)
        elif field == 'city' and user_id:
            subset = Contact.objects.filter(city__contains=string, user_id=user_id)
        elif field == 'city' and user_id == '':
            subset = Contact.objects.filter(city__contains=string)
        elif field == 'state' and user_id:
            subset = Contact.objects.filter(state__contains=string, user_id=user_id)
        elif field == 'state' and user_id == '':
            subset = Contact.objects.filter(state__contains=string)
        elif field == 'pin_code' and user_id:
            subset = Contact.objects.filter(pin_code__contains=string, user_id=user_id)
        else:
            subset = Contact.objects.filter(pin_code__contains=string)
        if subset:
            if 'username' in request.session.keys():
                username = request.session['username']
            else:
                username = ''
            return render(request, 'contact_web_app/view_contacts.html', {'contacts': subset, 'username': username})
        else:
            if 'username' in request.session.keys():
                username = request.session['username']
            else:
                username = ''
            message = 'There are no matching contacts!'
            return render(request, "contact_web_app/view_contacts.html", {'message': message, 'username': username})
