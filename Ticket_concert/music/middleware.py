from django.utils.deprecation import MiddlewareMixin
from oauth2_provider.models import AccessToken, Application
from django.shortcuts import redirect, reverse
from django.contrib.auth import logout, authenticate
from datetime import datetime, timedelta
from oauthlib.common import generate_token
from django.contrib.auth.models import User
class CheckTokenMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)
        user = request.user
        # Code to be executed for each request/response after
        # the view is called.
        if hasattr(request.resolver_match,'url_name'):
            if request.resolver_match.url_name == 'login' or request.resolver_match.url_name == 'signin':
                print('========== THIS IS URL LOGIN ===========')
                if request.method == 'POST' and user.is_authenticated:
                    print('========== AUTH SUCCESS ===========')
                    user_id = User.objects.get(username=request.POST['username'])
                    is_have_token = AccessToken.objects.filter(user=user_id.id).exists()
                    if is_have_token:
                        AccessToken.objects.filter(user=request.user.id).delete()
                        AccessToken.objects.create(user=user_id,token=generate_token(),
                                                    application=Application.objects.get(user=user_id),
                                                    expires=datetime.now() + timedelta(hours=1),
                                                    scope='read write')
                        print('========= Create Token ===========')
                    else:
                        AccessToken.objects.create(user=user_id,token=generate_token(),
                                                    application=Application.objects.get(user=user_id),
                                                    expires=datetime.now() + timedelta(hours=1),
                                                    scope='read write')
                        print('========= Create Token ===========')

            else:
                if user is not None and user.is_authenticated:
                    #tok_hr = request.session.get('tok_hr')
                    #tok_min = request.session.get('tok_min')
                    #if tok_hr or tok_min is not None:
                    #    now = datetime.now()
                    #    if datetime(now.year,now.month,now.day,tok_hr,tok_min) > now:
                    #        logout(request)
                    #        return redirect(reverse('signin') + '?next=' + reverse(request.resolver_match.url_name))
                    token = AccessToken.objects.filter(user=user.id)
                    if token[0].is_expired():
                        logout(request)
                        print('======= TOKEN EXPIRES AT' + request.META['PATH_INFO'])
                        return redirect(reverse('signin') + '?next=' + reverse(request.resolver_match.url_name))
                    else:
                        token.update(expires = datetime.now() + timedelta(hours=1))
                        request.session['tok_hr'] = token[0].expires.hour
                        request.session['tok_min'] = token[0].expires.minute
                        print('UPDATED TOKEN IN COMMON REQUEST')
        return response







    def handler_token(self,request):
        user = request.user
        def update_token(token):
            exp = token.objects.only('expires').filter(user=user.id)
            exp.expires = datetime.now() + timedelta(seconds=3600)
            request.session['tok_exp_hr'] = exp.expires.hour
            request.session['tok_exp_min'] = exp.expires.minute
        if user is not None and user.is_authenticated:
            exp_minute_sess = request.session.get('tok_exp_min')
            exp_hour_sess = request.session.get('tok_exp_hr')
            is_tok_exp_sess = request.session.get('is_tok_exp')
            
            if exp_minute_sess is not None:
                if is_tok_exp_sess is not None:
                    print('IS EXPIRES SESS ====== >>>>>' + is_tok_exp_sess)
                    if is_tok_exp_sess:
                        logout(request)
                        return redirect('home')
            else:
                token_expires = AccessToken.objects.only('expires').filter(user=user.id)
                if token_expires[0].is_expired:
                    request.session['is_tok_exp'] = True
            #    else:
            #        #===== Update Token To DataBase ========
            #        token_expires.expires = datetime.now() + timedelta(seconds=30)
            #        print('======= Update Token To Database =======')

            #        #============ Update Token To Session ==============
            #        request.session['tok_exp_hr'] = token_expires.expires.hour
            #        request.session['tok_exp_min'] = token_expires.expires.minute
            #        print('============ Update Token To Session ==============')