from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django. contrib import messages,auth
from .models import Creater, Skill, Certificate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os


# Create your views here.

def home_of(request,username):
    user1 = request.user
    user_loggedin = True
    if user1.username == '':
        user_loggedin = False
        user1 = User.objects.get(username = 'Robot') 
    creater1 = Creater.objects.get(user_id = user1.username)
    user = User.objects.get(username = username)
    creater = Creater.objects.get(user_id = user.username)
    skills = Skill.objects.filter(skill_username = user.username)   
    certificates = Certificate.objects.filter(certificate_username = user.username)
    groups = []
    group = []
    sets = []
    set = []

    # Assuming skills and certificates are lists containing the respective items
    for skill in skills:
        group.append(skill)
        if len(group) == 3:
            groups.append(group.copy())
            group.clear()

    # Append the last group if it has less than 3 items
    if group:
        groups.append(group.copy())

    for certificate in certificates:
        set.append(certificate)
        if len(set) == 3:
            sets.append(set.copy())
            set.clear()

    # Append the last set if it has less than 3 items
    if set:
        sets.append(set.copy())
    context = {'sets': sets,'groups': groups, 'creater': creater, 'creater1': creater1, 'certificates': certificates,'user' : user,'user1': user1, 'user_loggedin': user_loggedin}
    return render(request, 'home_of.html', context)



def allskills_of(request,username):
    if request.method == 'GET':
        user1 = request.user
        user_loggedin = True
        if user1.username == '':
            user_loggedin = False
            user1 = User.objects.get(username = 'Robot') 
        creater1 = Creater.objects.get(user_id = user1.username)
        
        user = User.objects.get(username = username)
        creater = Creater.objects.get(user_id = user.username)
        skills = Skill.objects.filter(skill_username = user.username)   
        groups = []
        group = []
        for skill in skills:
            group.append(skill)
            if len(group) == 3:
                groups.append(group.copy())
                group.clear()
        if group:
            groups.append(group.copy())
        context = {'groups': groups, 'creater1': creater1,'user' : user,'user1': user1, 'user_loggedin': user_loggedin}
        return render(request, 'allskills_of.html', context)
    else:
        return redirect('home_of')
    


def certificates_of(request, username):
    if request.method == 'GET':
        user1 = request.user
        user_loggedin = True
        if user1.username == '':
            user_loggedin = False
            user1 = User.objects.get(username = 'Robot') 
        creater1 = Creater.objects.get(user_id = user1.username)
        user = User.objects.get(username = username)
        creater = Creater.objects.get(user_id = user.username) 
        certificates = Certificate.objects.filter(certificate_username = user.username)
        sets = []
        set = []
        for certificate in certificates:
            set.append(certificate)
            if len(set) == 3:
                sets.append(set.copy())
                set.clear()
        if set:
            sets.append(set.copy())
        context = {'sets': sets,'creater': creater, 'creater1': creater1,'user' : user,'user1': user1, 'user_loggedin': user_loggedin}
        
        return render(request, 'certificates_of.html', context)
    else:
        return redirect('home_of')



def skill_of(request,username):

    if request.method == 'POST':
        user1 = request.user
        user_loggedin = True
        if user1.username == '':
            user_loggedin = False
            user1 = User.objects.get(username = 'Robot') 
        creater1 = Creater.objects.get(user_id = user1.username)
        user = User.objects.get(username = username)
        creater = Creater.objects.get(user_id = user.username)

        skill_name = request.POST.get('skill_name')

        skills = Skill.objects.filter(skill_username = user.username)
        skill = get_object_or_404(skills, skill_name = skill_name)

        context = {
            'skill':skill,
            'user_loggedin': user_loggedin,
            'user1':user1,
            'user': user,
            'creater': creater,
            'creater1':creater1
        }
        return render(request,'skill_of.html', context)
    return render(request, 'home_of.html')


def certificate_of(request,username):
    if request.method == 'POST':
        user1 = request.user
        user_loggedin = True
        if user1.username == '':
            user_loggedin = False
            user1 = User.objects.get(username = 'Robot') 
        creater1 = Creater.objects.get(user_id = user1.username)
        user = User.objects.get(username = username)
        creater = Creater.objects.get(user_id = user.username)
        certificate_name = request.POST.get('certificate_name')

        certificates = Certificate.objects.filter(certificate_username = user.username)
        certificate = get_object_or_404(certificates, certificate_name = certificate_name)

        context = {'certificate':certificate,'creater': creater, 'creater1': creater1,'user' : user,'user1': user1, 'user_loggedin': user_loggedin}
        
        return render(request, 'certificate_of.html', context)


def home(request):    
    user = request.user
    user_loggedin = True
    if user.username == '':
        user_loggedin = False     
        user = User.objects.get(username = 'Robot')
    creater = Creater.objects.get(user_id = user.username)
    skills = Skill.objects.filter(skill_username = user.username)   
    certificates = Certificate.objects.filter(certificate_username = user.username)
    groups = []
    group = []
    sets = []
    set = []

    # Assuming skills and certificates are lists containing the respective items
    for skill in skills:
        group.append(skill)
        if len(group) == 3:
            groups.append(group.copy())
            group.clear()

    # Append the last group if it has less than 3 items
    if group:
        groups.append(group.copy())

    for certificate in certificates:
        set.append(certificate)
        if len(set) == 3:
            sets.append(set.copy())
            set.clear()

    # Append the last set if it has less than 3 items
    if set:
        sets.append(set.copy())

    # Assuming creater is defined somewhere in your code
    context = {'skills':skills,'sets': sets,'groups': groups,'creater': creater,'user' : user, 'user_loggedin' : user_loggedin}

    return render(request, 'home.html', context)



def allskills(request):
    user = request.user
    user_loggedin = True
    if user.username == '':
        user_loggedin = False     
        user = User.objects.get(username = 'Robot')
    creater = Creater.objects.get(user_id = user.username)
    skills = Skill.objects.filter(skill_username = user.username)
    group =[]
    groups = []
    for skill in skills:
        group.append(skill)
        print(skill)
        if len(group) == 3:
            groups.append(group.copy())
            group.clear()
    if group:
        groups.append(group)
    context = {'groups':groups,'users' : user,'creater': creater , 'user_loggedin' : user_loggedin}
    return render(request, 'allskills.html', context)



def certificates(request):
    user = request.user
    user_loggedin = True
    if user.username == '':
        user_loggedin = False     
        user = User.objects.get(username = 'Robot')
    creater = Creater.objects.get(user_id = user.username)
    certificates = Certificate.objects.filter(certificate_username = user.username)
    sets = []
    set = []

    for certificate in certificates:
        set.append(certificate)
        if len(set) == 3:
            sets.append(set.copy())
            set.clear()

    if set:
        sets.append(set.copy())
    context = {'sets': sets,'creater': creater,'user' : user, 'user_loggedin' : user_loggedin}

    return render(request, 'certificates.html', context)



def skill(request):
    user = request.user
    user_loggedin = True
    if user.username == '':
        user_loggedin = False     
        user = User.objects.get(username = 'Robot')
    skill_name = request.POST.get('skill_name')  # Use get() method to avoid KeyError

    skills = Skill.objects.filter(skill_username = user.username)
    skill = get_object_or_404(skills, skill_name = skill_name)

    context = {
        'skill':skill,
        'user_loggedin':user_loggedin,
        'user':user,

    }
    return render(request, 'skill.html', context)



def certificate(request):
    user = request.user
    user_loggedin = True
    if user.username == '':
        user_loggedin = False     
        user = User.objects.get(username = 'Robot')
    creater = Creater.objects.get(user_id = user.username)
    certificate_name = request.POST.get('certificate_name')

    certificates = Certificate.objects.filter(certificate_username = user.username)
    certificate = get_object_or_404(certificates, certificate_name = certificate_name)

    context = {'certificate':certificate,'creater': creater,'user' : user, 'user_loggedin' : user_loggedin}
    return render(request, 'certificate.html', context)



def logout(request,username = None):
    auth.logout(request)
    return redirect('home')


def login(request, username = None):
    if request.method == 'POST':
        username = request.POST['login_username']
        password = request.POST['login_password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect(home)
        else:
            messages.info(request, "Invalid Credentials!!!")
            return redirect('login')
    else:
        return render(request, 'login.html')
    

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fullname = request.POST['fullname']
        first_name,last_name = fullname.split(' ')
        profilepic = request.FILES.get('image')
        email = request.POST['email']
        date_of_birth = request.POST['date_of_birth']
        short_discription = request.POST['short_discription']
        detailed_discription = request.POST['detailed_discription']
        address = request.POST['address']
        linkedin = request.POST['linkedin']
        instagram = request.POST['instagram']
        facebook = request.POST['facebook']
        contact_no = request.POST['contact_no']
        password = request.POST['password']
        password2 = request.POST['password2']


        l = [' ','!','@','#','$','%','^','&','*','(',')','<','>',',','.','?','/',';',':','[',']','{','}','\\','|','"',"'",'`','~']
        for e in l:
            if e in username:
                messages.info(request,"Invalid Username !!!")
                return redirect('register')
        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request,"Email Already in use !!!")
                return redirect('register')
            elif User.objects.filter(username = username).exists():
                messages.info(request,"Username Already in use !!!")
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username= username,
                    email= email,
                    password= password,
                    first_name = first_name,
                    last_name = last_name,
                )
                if profilepic:
                    fs = FileSystemStorage(location=settings.MEDIA_ROOT)
                    filename = f"{username}.{profilepic.name.split('.')[-1]}"
                    profilepic.name = fs.save(filename, profilepic)
                creater = Creater(
                    user_id = username, 
                    image = profilepic,
                    full_name = fullname, 
                    discription = short_discription,
                    detailed_discription = detailed_discription ,                        
                    date_of_birth  = date_of_birth,
                    address = address,                                  
                    linkedin =linkedin  ,                                 
                    instagram = instagram,                                 
                    facebook = facebook,                               
                    contact_no = contact_no,
                )
                creater.save()
                user.save()
                user = auth.authenticate(username = username, password = password)
                auth.login(request, user)
                return redirect('profile')
        else:
            messages.info(request,'Password Not The Same')
            return redirect('register')
    else:
        return render(request,'register.html')
    
@login_required
def profile(request,username = None):
    user = request.user
    creater = Creater.objects.get(user_id = user.username)    
    skills = Skill.objects.filter(skill_username = user.username)     
    certificates = Certificate.objects.filter(certificate_username = user.username)
    groups = []
    group = []
    sets = []
    set = []

    for skill in skills:
        group.append(skill)
        if len(group) == 3:
            groups.append(group.copy())
            group.clear()

    if group:
        groups.append(group.copy())

    for certificate in certificates:
        set.append(certificate)
        if len(set) == 3:
            sets.append(set.copy())
            set.clear()

    if set:
        sets.append(set.copy())

    context = {'sets': sets[:-1], 'last_certificates': sets[-1] if sets else [], 'groups': groups[:-1], 'creater': creater, 'last_skills': groups[-1] if groups else []}

    return render(request, 'profile.html', context)
    

@login_required
def addskill(request,username = None):
    if request.method == 'POST':
        user = request.user
        skill_name = request.POST['skill_name']
        short_discription = request.POST['short_discription']
        detailed_discription = request.POST['detailed_discription']
        point1 = request.POST['point1']
        point2 = request.POST['point2']
        point3 = request.POST['point3']
        point4 = request.POST['point4']
        point5 = request.POST['point5']
        new_skill = Skill(skill_username = user.username,skill_name= skill_name, skill_discription= short_discription, detailed_discription= detailed_discription, point1 = point1, point2 = point2, point3 = point3, point4 = point4, point5 = point5)
        new_skill.save()
        return redirect('profile')

    else:
        if  request.user != None:     
            return render(request,'addskill.html')
        else:
            pass

@login_required
def addcertificate(request,username = None):
    if request.method == 'POST':
        user = request.user
        certificate_image = request.FILES.get('certificate_image')
        if 'certificate_image' in request.FILES:
            certificate = Certificate(
                certificate_username = user.username,
                certificate_name = request.POST['certificate_name'],
                short_discription = request.POST['short_discription'],
                detailed_discription = request.POST['detailed_discription'],
            )
            if certificate_image:
                fs = FileSystemStorage(location=settings.MEDIA_ROOT)
                filename = f"{user.username}_certificate_{certificate.id}.{certificate_image.name.split('.')[-1]}"
                certificate_image.name = fs.save(filename, certificate_image)
        
            
            certificate.certificate_image = certificate_image
            certificate.save()
            return redirect('profile')  # Redirect to profile page after successful upload
        else:
            error_message = "Please upload a certificate image."
            return render(request, 'addcertificate.html', {'error_message': error_message})
    else:
        return render(request, 'addcertificate.html')

@login_required
def delete_skill(request,username = None):
    if request.method == 'POST':
        user = request.user
        skill_name = request.POST.get('skill_name')

        skills = Skill.objects.filter(skill_username=user.username)
        skill = get_object_or_404(skills, skill_name=skill_name)
        skill.delete()

        return redirect('profile')
    return redirect('profile')

@login_required
def saveskill(request,username = None):
    if request.method == 'POST':
        user = request.user 
        skill_name = request.POST['skill_name_og']
        skills = Skill.objects.filter(skill_username=user.username)
        skill = get_object_or_404(skills, skill_name=skill_name)
        skill.delete()

        skill_name = request.POST['skill_name']
        short_discription = request.POST['short_discription']
        detailed_discription = request.POST['detailed_discription']
        point1 = request.POST['point1']
        point2 = request.POST['point2']
        point3 = request.POST['point3']
        point4 = request.POST['point4']
        point5 = request.POST['point5']
        new_skill = Skill(
            skill_username = user.username,
            skill_name= skill_name,
            skill_discription= short_discription,
            detailed_discription= detailed_discription,
            point1 = point1,
            point2 = point2,
            point3 = point3,
            point4 = point4,
            point5 = point5
        )
        new_skill.save()
        return redirect('profile')

@login_required
def editskill(request,username = None):
    user = request.user
    if user.username == '' or user == None:
        user = User.objects.get(username='Robot')

    skill_name = request.POST.get('skill_name')

    skills = Skill.objects.filter(skill_username = user.username)
    skill = get_object_or_404(skills, skill_name = skill_name)

    context = {
        'skill_username': user,
        'skill_name': skill_name,
        'short_discription': skill.skill_discription,
        'detailed_discription': skill.detailed_discription,
        'point1': skill.point1,
        'point2': skill.point2,
        'point3': skill.point3,
        'point4': skill.point4,
        'point5': skill.point5,
        'highlighted': skill.highlighted,
    }
    # return render(request, 'skill.html', context)
    return render(request, 'editskill.html', context)

@login_required
def editcertificate(request,username = None):
    user = request.user
    if user.username == '' or user == None:
        user = User.objects.get(username='Robot')

    certificate_name = request.POST.get('certificate_name') 

    certificates = Certificate.objects.filter(certificate_username = user.username)
    certificate = get_object_or_404(certificates, certificate_name = certificate_name)

    context = {
        'certificate_name': certificate.certificate_name,
        'certificate_image': certificate.certificate_image,
        'short_discription': certificate.short_discription,
        'detailed_discription': certificate.detailed_discription,
    }
    return render(request, 'editcertificate.html', context)

@login_required
def savecertificate(request,username = None):
    if request.method == 'POST':
        user = request.user
        certificate_name = request.POST['certificate_name_og']
        
        certificates = Certificate.objects.filter(certificate_username=user.username)
        certificate = get_object_or_404(certificates, certificate_name=certificate_name)
        certificate_image = request.FILES.get('certificate_image',certificate.certificate_image)
        if certificate_image:
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            filename = f"{user.username}_certificate_{certificate.id}.{certificate_image.name.split('.')[-1]}"
            certificate_image.name = fs.save(filename, certificate_image)
        
        if certificate.certificate_image:
            fs.delete(certificate.certificate_image.name)
        new_certificate = Certificate(
                certificate_username = user.username,
                certificate_name = request.POST.get('certificate_name',certificate.certificate_name),
                certificate_image = certificate_image,
                short_discription = request.POST.get('short_discription',certificate.short_discription),
                detailed_discription = request.POST.get('detailed_discription',certificate.detailed_discription),
            )
        certificate.delete()
        new_certificate.save()
        return redirect('profile')

@login_required
def deletecertificate(request,username = None):

    if request.method == 'POST':
        user = request.user
        certificate_name = request.POST['certificate_name']
        certificates = Certificate.objects.filter(certificate_username=user.username)
        certificate = get_object_or_404(certificates, certificate_name=certificate_name)
        certificate.delete()
    return redirect('profile')

@login_required
def editprofile(request,username = None):
    user = request.user
    if user.username == '':    
        user = User.objects.get(username = 'Robot')
    creater = Creater.objects.get(user_id = user.username)
    context = { 'creater': creater, 'users' : user}
    return render(request, 'editprofile.html', context)
   
@login_required
def saveprofile(request,username = None):
    if request.method == 'POST':
        user = request.user
        creater = get_object_or_404(Creater, user_id=user.username)
        first_name =  request.POST.get('firstname',user.first_name)
        last_name = request.POST.get('lastname',user.last_name)
        fullname = first_name + " " + last_name
        profilepic = request.FILES.get('image',creater.image)
        email = request.POST.get('email',user.email)
        date_of_birth = request.POST.get('date_of_birth',creater.date_of_birth)
        short_discription = request.POST.get('short_discription',creater.discription)
        detailed_discription = request.POST.get('detailed_discription',creater.detailed_discription)
        address = request.POST.get('address',creater.address)
        linkedin = request.POST.get('linkedin',creater.linkedin)
        instagram = request.POST.get('instagram',creater.instagram)
        facebook = request.POST.get('facebook',creater.facebook)
        contact_no = request.POST.get('contact_no',creater.contact_no)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        if profilepic:
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            filename = f"{username}.{profilepic.name.split('.')[-1]}"
            profilepic.name = fs.save(filename, profilepic)
        existing_pic = os.path.join(settings.MEDIA_ROOT, f"{user.username}.*")
        if os.path.exists(existing_pic):
            os.remove(existing_pic)
        creater.image = profilepic
        creater.full_name = fullname
        creater.discription = short_discription
        creater.detailed_discription = detailed_discription                        
        creater.date_of_birth  = date_of_birth
        creater.address = address                      
        creater.linkedin =linkedin                                 
        creater.instagram = instagram                                 
        creater.facebook = facebook                              
        creater.contact_no = contact_no
        creater.save()
                
        return redirect('profile')

@login_required
def changepassword(request,username = None):
    if request.method == 'POST':
        user = request.user
        creater = get_object_or_404(Creater, user_id=user.username)
        old_password = request.POST.get('old_password')
        if user.check_password(old_password):
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
            if password == password2:
                user.set_password(password)
                user.save()
                messages.success(request, 'Password changed successfully!!!.')
                return redirect('/profile')
            else:
                messages.error(request, 'Passwords do not match !!!.')
        else:
            messages.error(request, 'Invalid old password !!!.')
    else:
        user = request.user
        creater = Creater.objects.get(user_id = user.username)
        context = { 'creater': creater, 'users' : user}
        return render(request, 'changepassword.html', context)        

@login_required
def changeusername(request,username = None):
    if request.method == 'POST':
        user = request.user
        creater = get_object_or_404(Creater, user_id=user.username)
        new_userid = request.POST.get('new_userid',user.password)
        password = password = request.POST.get('password',user.password)
        
        l = [' ','!','@','#','$','%','^','&','*','(',')','<','>',',','.','?','/',';',':','[',']','{','}','\\','|','"',"'",'`','~']
        for e in l:
            if e in new_userid:
                messages.info(request,"Invalid Username !!!")
                return redirect('changeusername')
        
        
        if(password == user.password):
            user.save()
            user = auth.authenticate(username = user.username, password = password)
            auth.login(request, user)
            return redirect('profile')
        else:
            messages.info(request,"Invalid password !!!")
            return redirect('changeusername')
    else:
        user = request.user
        creater = Creater.objects.get(user_id = user.username)
        context = { 'creater': creater, 'users' : user}
        return render(request, 'changeusername.html', context)

