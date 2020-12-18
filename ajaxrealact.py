def verify_unbind(request):
    user_id = int(request.GET.get('user_id')) if request.GET.get('user_id') else 0
    print "user_id", user_id
    try:
        Broker.objects.filter(user_id=int(user_id)).update(verify_status=0, card_status=0)
        # Broker.objects.filter(user_id=0).update(verify_status=0, card_status=0)
    except Broker.DoesNotExist:
        error = copy.copy(settings.ERROR['NOT_EXIST_ERR'])
        error['msg'] = u"经纪人不存在"
        return JSONResponse(error=error)

    new_broker = Broker.objects.get(user_id=int(user_id))
    res = {"status": True, "verify_status":int(new_broker.verify_status), "card_status": new_broker.card_status}
    print "ressssssssssssss", res
    return HttpResponse(json.dumps(res))