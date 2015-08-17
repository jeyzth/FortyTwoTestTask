from django.utils.timezone import now


from hello.models import MyRequest


class SaveRequest(object):
    def process_request(self, request):
        d = {}
        rh = request.method
        if request.method == 'GET':
            d = request.GET.dict()

        if request.method == 'POST':
            d = request.POST.dict()

        s = str(d)
        z = request.path
        try:
            i = z.index('requests10')
            if i >= 0:
                return None

        except:
            i = 0

        try:
            i = z.index('chknewreq')
            if i >= 0:
                return None

        except:
            i = 0

            new_req = MyRequest(
                query_dt=now(),
                remote_ip=request.META["REMOTE_ADDR"],
                remote_host=str(request.path),
                query_string=rh+"="+s
            )
            new_req.save()
            return None
