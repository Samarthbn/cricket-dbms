

from io import BytesIO

from django.shortcuts import redirect, render, HttpResponse

from CRICKET_APP.models import *
import hashlib
from django.template.loader import get_template
from xhtml2pdf import pisa


# Create your views here.


def index(request):
    return render(request, 'index.html')


def captaindetails(request):
    return render(request, 'captaindetails.html')


def matchdetails(request):
    return render(request, 'matchdetails.html')


def teamdetails(request):
    return render(request, 'teamdetails.html')


def umpiredata(request):
    return render(request, 'umpiredata.html')


def teamin(request):
    st = team.objects.all()

    istr = '''

    <table class="table table-bordered " style="height: 50%; border-style:double; border-width:10px; margin-left:3cm; padding-bottom:2cm;">
    <thead class="table ">
    <tr>

    <th style="font-size: 23px; font-weight:bolder; font-family:times roman;margin-left:1cm;color:#731a1a;">TEAM NAME</th>

    <th style="font-size: 23px; font-weight:bolder; font-family:times roman;margin-left:1cm;color:#731a1a;">TEAM RANK</th>

    <th style="font-size: 25px; font-family:times roman;color:#731a1a;padding-left:1xcm">NO OF WINS</th>
    <th style="font-size: 25px; font-family:times roman;color:#731a1a;padding-left:1cm">NO OF LOSES</th>

    <th style="font-size: 25px; font-family:times roman;margin-left:cm;padding-left:2cm;color:#731a1a;">NO OF BATSMEN</th>
    <th style="font-size: 25px; font-family:times roman;;margin-left:0cm;padding-left:2cm;color:#731a1a;">NO OF BOWLERS</th>
    

    <br>
    </tr>
    </td>

    </thead>


        '''

    for bn in st:
        istr += "<tr><td>" + str(bn.team_name)+"</td><td>"+str(bn.team_rank) + \
            "</td><td>"+str(bn.no_of_wins) + "</td><td>" + \
                str(bn.no_of_loses)+"</td><td>" + str(bn.no_of_batsmen) + \
            "</td><td>" + str(bn.no_of_bowlers)

    return HttpResponse(istr)


def deletematch(request):
    return render(request, 'deletematch.html')


def login(request):
    return render(request, 'login.html')


def search(request):
    return render(request, 'search.html')


def signup(request):
    return render(request, 'signup.html')


def matchdata(request):
    return render(request, 'matchesdata.html')


def userlogin(request):
    return render(request, 'userlogin.html')


def teamsearch(request):
    return render(request, 'teamsearch.html')


def matchsearch(request):
    return render(request, 'matchsearch.html')


def playersearch(request):
    return render(request, 'playersearch.html')


def dashboar(request):
    return render(request, 'dashboard1.html')


def playerdata(request):
    return render(request, 'playerdata.html')


def report1(request):

    teams = team.objects.all()
    template = 'report1.html'
    context = {'teams': teams}
    pdf = render_to_pdf(template, context)

    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "report%s.pdf" % ("team")
        content = "inline; filename='%s'" % (filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response


def alo(request):
    usn = request.GET.get('users')
    passw = request.GET.get('passs')
    z = usign.objects.filter(username=usn, password=passw)
    print(usn, passw)

    if(z):
        response = render(request, 'dashboard.html')
        return response
    else:
        return render(request, 'login.html')


def lo(request):
    usn = request.GET.get('users')
    passw = request.GET.get('passs')
    passw = hashlib.md5(passw.encode('utf-8')).hexdigest()
    z = sign.objects.filter(username=usn, password=passw)

    print(usn, passw)
    if(z):
        response = render(request, 'dashboard1.html')
        return response
    else:
        return render(request, 'userlogin.html')


def sg(request):
    names = request.GET.get('fname')
    use = request.GET.get('usern')
    passw = request.GET.get('passwd')
    passw = hashlib.md5(passw.encode('utf-8')).hexdigest()
    print(names, use, passw)
    sig = sign(fullname=names, username=use, password=passw)
    sig.save()
    return render(request, 'userlogin.html')


def data(request):
    return render(request, 'data.html')


def datam(request):
    tid = request.GET.get('sa')
    tr = request.GET.get('sb')
    tn = request.GET.get('sc')
    nw = request.GET.get('sd')
    nl = request.GET.get('se')
    nb = request.GET.get('sf')
    nbs = request.GET.get('sg')
    ump = request.GET.get('ump')

    print(tid, tr, tn, nw, nl, nb, nbs, ump)
    u = matches(match_id=tid, match_date=tr, team_1_name=tn,
                team_2_name=nw, winner=nl, loser=nb, venue=nbs, umpire_name=ump)

    u.save()

    a = matches.objects.filter(match_id=tid)
    b = umpire.objects.filter(umpire_name=ump)

    a.first().umpired_by.add(b.first())

    return render(request, 'dashboard.html')


def dataf(request):
    tid = request.GET.get('sa')
    tr = request.GET.get('sb')
    tn = request.GET.get('sc')
    nw = request.GET.get('sd')
    nl = request.GET.get('se')
    nb = request.GET.get('sf')
    nbs = request.GET.get('sg')
    bl = request.GET.get('ll')
    nz = request.GET.get('sl')

    print(tid, tr, tn, nw, nl, nb, nbs, bl, nz)
    u = team(team_id=tid, team_rank=tr, team_name=tn, no_of_wins=nw,
             no_of_loses=nl, no_of_bowlers=nb, no_of_batsmen=nbs, player_name=bl, match_date=nz)

    u.save()
    a = team.objects.filter(team_id=tid)
    b = player.objects.filter(player_name=bl)

    a.first().has.add(b.first())

    a = team.objects.filter(team_id=tid)
    b = matches.objects.filter(match_date=nz)

    a.first().plays.add(b.first())

    return render(request, 'dashboard.html')


def delt(request):
    tname = request.GET.get('dl')
    try:
        c = team.objects.filter(team_name=tname)
        print(tname)
        c.delete()

        d = player.objects.filter(team_id=tname)
        d.delete()

        print("order deleted")
        print("Record deleted successfully!")

        return render(request)
    except:
        return redirect(deletematch)


def dashboard(request):
    return render(request, 'dashboard.html')


def matchin(request):
    st = matches.objects.all()

    istr = '''

    <table class="table table-bordered " style="height: 50%; border-style:double; border-width:10px; margin-left:3cm; padding-bottom:2cm;">
    <thead class="table ">
    <tr>

    <th style="font-size: 23px; font-weight:bolder; font-family:times roman;margin-left:1cm;color:#731a1a;">TEAM 1 NAME</th>

    <th style="font-size: 23px; font-weight:bolder; font-family:times roman;margin-left:1cm;color:#731a1a;">TEAM 2 NAME</th>

    <th style="font-size: 25px; font-family:times roman;text-align:end;color:#731a1a;padding-left:1xcm">WINNER</th>
    <th style="font-size: 25px; font-family:times roman;text-align:end;color:#731a1a;padding-left:1cm">LOSER</th>

    <th style="font-size: 25px; font-family:times roman;text-align:end;margin-left:cm;padding-left:2cm;color:#731a1a;">VENUE</th>
    <th style="font-size: 25px; font-family:times roman;text-align:;margin-left:0cm;padding-left:2cm;color:#731a1a;">MATCH DATE</th>

    <br>
    </tr>
    </td>

    </thead>


    '''

    for bn in st:
        istr += "<tr><td>" + str(bn.team_1_name)+"</td><td>"+str(bn.team_2_name) + \
            "</td><td>"+bn.winner + "</td><td>" + \
                str(bn.loser)+"</td><td>" + bn.venue + \
            "</td><td>" + str(bn.match_date)

    return HttpResponse(istr)


def datac(request):
    tid = request.GET.get('sa')
    tr = request.GET.get('sb')
    tn = request.GET.get('sc')

    print(tid, tr, tn)
    u = captain(captain_id=tid, captain_name=tr, team_name=tn)

    u.save()
    
    a = captain.objects.filter(captain_id=tid)
    b = team.objects.filter(team_name=tn)
    print(a,b)
    a.first().leads.add(b.first())

    return render(request, 'dashboard.html')


def searchm(request):
    sa = request.GET.get('searin')
    te = matches.objects.filter(match_date=sa)

    istr = '''
     <h2  style="margin-left: 13cm;padding-bottom:1.5cm; color:red;font-size:1.5cm;font-family:roman;font-weight:bolder;">Matched Items</h2>
    <table class="table thead-dark" style="width: %; border-style:; border-width:10px; margin-left:2cm; padding-bottom:2cm;">
    <thead>
    <tr>
    <th class="" style="font-size: 23px; font-weight:bolder; font-family:times roman;padding-right:1cm;color:#731a1a; ">MATCH DATE</th>
    <th style="font-size: 25px; font-family:times roman; padding-right:2cm;color:#731a1a;">TEAM 1 NAME</th>
    <th style="font-size: 25px; font-family:times roman;padding-right:2cm;color:#731a1a;">TEAM 2 NAME</th>
    <th style="font-size: 25px; font-family:times roman;padding-right:2cm;color:#731a1a;">WINNER</th>
    <th style="font-size: 25px; font-family:times roman;padding-right:2cm;color:#731a1a;">LOSER</th>
    <th style="font-size: 25px; font-family:times roman;padding-right:2cm;color:#731a1a;">VENUE</th>
    <br>
    </tr>
    </thead>

    '''
    for t in te:
        istr += "<tr><td>" + str(t.match_date) + "</td><td>"+t.team_1_name+"</td><td>"+str(t.team_2_name)+"</td><td>"+str(
            t.winner)+"</td><td>"+str(t.loser)+"</td><td>"+str(t.venue)

    return HttpResponse(istr)


def searchs(request):
    sa = request.GET.get('searin')
    te = team.objects.filter(team_name=sa)

    istr = '''
     <h2  style="margin-left: 13cm;padding-bottom:1.5cm; color:red;font-size:1.5cm;font-family:roman;font-weight:bolder;">Matched Items</h2>
    <table class="table thead-dark" style="width: %; border-style:; border-width:10px; margin-left:2cm; padding-bottom:2cm;">
    <thead>
    <tr>
    <th class="" style="font-size: 23px; font-weight:bolder; font-family:times roman;padding-right:1cm;color:#731a1a; ">Team ID</th>
    <th style="font-size: 25px; font-family:times roman; padding-right:2cm;color:#731a1a;">Team Name</th>
    <th style="font-size: 25px; font-family:times roman;padding-right:2cm;color:#731a1a;">Team Rank</th>
    <th style="font-size: 25px; font-family:times roman;padding-right:2cm;color:#731a1a;">No of wins</th>
    <th style="font-size: 25px; font-family:times roman;padding-right:2cm;color:#731a1a;">No of loses</th>
    <th style="font-size: 25px; font-family:times roman;padding-right:2cm;color:#731a1a;">No of bowlers</th>
    <th style="font-size: 25px; font-family:times roman;padding-right:2cm;color:#731a1a;">No of batsmen</th>
    <br>
    </tr>
    </thead>

    '''
    for t in te:
        istr += "<tr><td>" + t.team_id + "</td><td>"+t.team_name+"</td><td>"+str(t.team_rank)+"</td><td>"+str(
            t.no_of_wins)+"</td><td>"+str(t.no_of_loses)+"</td><td>"+str(t.no_of_bowlers)+"</td><td>"+str(t.no_of_batsmen)+"</td><td>"

    return HttpResponse(istr)


def searchp(request):
    sa = request.GET.get('searin')
    te = player.objects.filter(player_name=sa)

    istr = '''
     <h2  style="margin-left: 13cm;padding-bottom:1.5cm; color:red;font-size:1.5cm;font-family:roman;font-weight:bolder;">Matched Items</h2>
    <table class="table thead-dark" style="width: %; border-style:; border-width:10px; margin-left:-0.2cm; padding-bottom:2cm;">
    <thead>
    <tr>
    <th class="" style="font-size: 15px; font-weight:bolder; font-family:times roman;padding-right:1cm;color:#731a1a; ">PLAYER NAME</th>
    
    <th style="font-size: 15px; font-family:times roman;padding-right:1cm;color:#731a1a;">BATTING AVERAGE</th>

    <th style="font-size: 15px; font-family:times roman;padding-right:1cm;color:#731a1a;">NO OF TOTAL RUN</th>

    <th style="font-size: 15px; font-family:times roman;padding-right:1cm;color:#731a1a;">NO OF WICKETS</th>
    <th style="font-size: 15px; font-family:times roman;padding-right:1cm;color:#731a1a;">TYPE OF BOWLER</th>
    <th style="font-size: 15px; font-family:times roman;padding-right:1cm;color:#731a1a;">ECONOMY</th>




    <br>
    </tr>
    </thead>

    '''
    for t in te:
        istr += "<tr><td>" + str(t.player_name) + "</td><td>"+str(t.batting_average)+"</td><td>"+str(t.no_of_totalruns)+"</td><td>"+str(
            t.no_of_wickets)+"</td><td>"+str(t.type_of_bowler)+"</td><td>"+str(t.economy)

    return HttpResponse(istr)


def report(request):

    matchs = matches.objects.all()
    template = 'report.html'
    context = {'matchs': matchs}
    pdf = render_to_pdf(template, context)

    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "report%s.pdf" % ("mat")
        content = "inline; filename='%s'" % (filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(
        BytesIO(html.encode("ISO-8859-1")), result)

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def datap(request):
    tid = request.GET.get('sa')
    tr = request.GET.get('sb')
    tn = request.GET.get('sc')
    nw = request.GET.get('sd')
    nl = request.GET.get('se')
    nb = request.GET.get('sf')
    nbs = request.GET.get('sg')

    print(tid, tr, tn, nw, nl, nb, nbs)
    u = player(player_id=tid, player_name=tr, batting_average=tn, no_of_totalruns=nw,
               no_of_wickets=nl, type_of_bowler=nb, economy=nbs)

    u.save()
    return render(request, 'dashboard.html')



def datau(request):
    tid = request.GET.get('sa')
    tr = request.GET.get('sb')
    tn = request.GET.get('sc')
    nw = request.GET.get('sd')
   

    print(tid, tr, tn, nw)
    u = umpire(umpire_id=tid, umpire_name=tr, no_of_matches=tn,country=nw)

    u.save()

    return render(request, 'dashboard.html')